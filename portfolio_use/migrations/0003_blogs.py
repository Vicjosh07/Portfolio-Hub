# Generated by Django 5.1.4 on 2024-12-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_use', '0002_contact_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
