# Generated by Django 4.2.7 on 2023-11-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app1', '0003_alter_imagemodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
