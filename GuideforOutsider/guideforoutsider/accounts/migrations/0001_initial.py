# Generated by Django 2.1.1 on 2019-11-18 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='', max_length=20)),
                ('nickname', models.CharField(blank=True, default='', max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('student_number', models.IntegerField(default=20153686)),
                ('department', models.CharField(blank=True, default='', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
