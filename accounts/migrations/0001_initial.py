# Generated by Django 4.1 on 2022-08-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('password', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_verified', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('shop', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]