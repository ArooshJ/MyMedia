# Generated by Django 4.2.3 on 2023-08-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocMed', '0009_remove_account_following_comment_accountsliked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='link',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='postfiles/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postimgs/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='dps/'),
        ),
    ]
