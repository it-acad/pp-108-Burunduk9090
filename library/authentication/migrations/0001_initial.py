# Generated by Django 4.1 on 2025-01-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(default=None, max_length=20)),
                ('last_name', models.CharField(default=None, max_length=20)),
                ('middle_name', models.CharField(default=None, max_length=20)),
                ('email', models.CharField(default=None, max_length=100, unique=True)),
                ('password', models.CharField(default=None, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.IntegerField(choices=[(0, 'visitor'), (1, 'librarian')], default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
