# Generated by Django 4.2.3 on 2023-08-02 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocMed', '0008_alter_comment_by_alter_reply_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='Following',
        ),
        migrations.AddField(
            model_name='comment',
            name='AccountsLiked',
            field=models.ManyToManyField(blank=True, null=True, related_name='likedComments', to='SocMed.account'),
        ),
        migrations.AddField(
            model_name='post',
            name='AccountsLiked',
            field=models.ManyToManyField(blank=True, null=True, related_name='likedPosts', to='SocMed.account'),
        ),
        migrations.AddField(
            model_name='reply',
            name='AccountsLiked',
            field=models.ManyToManyField(blank=True, null=True, to='SocMed.account'),
        ),
        migrations.RemoveField(
            model_name='account',
            name='Followers',
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reply',
            name='by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likedReplies', to='SocMed.account'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='account',
            name='Followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='Following', to='SocMed.account'),
        ),
    ]
