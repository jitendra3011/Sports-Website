from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
# from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .forms import UpdateProfileForm
from django.views import generic
from theblog.models import Profile
# from.forms import SignUpForm
# Create your views here.

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'edit_profile_page'
    fields = ['bio', 'profile_pic', 'fb_url', 'instagram_url']
    success_url = reverse_lazy('blog')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
       # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request, user)
            return redirect("/")
        
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
            
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching...')
            return redirect('register')
        return redirect('/')
    else: 
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        current_password = request.POST.get('current_password', '')
        if user.check_password(current_password):
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            if username != user.username and User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
            else:
                user.username = username
                email = request.POST.get('email', '')
                if email != user.email and User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already taken')
                else:
                    user.email = email
                new_password = request.POST.get('password1', '')
                confirm_password = request.POST.get('password2', '')
                if new_password and new_password == confirm_password:
                    user.set_password(new_password)
                user.save()
                messages.success(request, 'Your profile has been updated')
                return redirect('/')
        else:
            messages.error(request, 'Invalid current password')

    # Pre-populate form fields with user's existing information
    initial_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'username': user.username,
    }
    form = UpdateProfileForm(initial=initial_data)

    return render(request, 'edit_profile.html', {'form': form})
