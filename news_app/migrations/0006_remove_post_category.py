# Generated by Django 3.2.16 on 2023-01-25 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
