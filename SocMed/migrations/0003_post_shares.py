# Generated by Django 4.2.3 on 2023-07-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocMed', '0002_comment_post_likes_alter_post_by_alter_post_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]