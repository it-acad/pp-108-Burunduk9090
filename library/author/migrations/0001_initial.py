# Generated by Django 4.1 on 2025-01-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(blank=True, max_length=20)),
                ('surname', models.CharField(blank=True, max_length=20)),
                ('patronymic', models.CharField(blank=True, max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('books', models.ManyToManyField(related_name='authors', to='book.book')),
            ],
        ),
    ]
