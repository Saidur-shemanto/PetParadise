# Generated by Django 4.2 on 2023-05-08 00:58

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
            name='rescuePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('rescue_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('create_date', models.DateTimeField(null=True)),
                ('animalName', models.CharField(max_length=30)),
                ('requester_contact', models.CharField(max_length=30, null=True)),
                ('rescue_location', models.TextField()),
                ('animal_condition', models.CharField(max_length=3)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rescuereq_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='rescueApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
