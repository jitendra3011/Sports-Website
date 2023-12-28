# Generated by Django 4.1.7 on 2023-04-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='col',
        ),
        migrations.AddField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='first_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
