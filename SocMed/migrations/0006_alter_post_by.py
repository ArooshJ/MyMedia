# Generated by Django 4.2.3 on 2023-07-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocMed', '0005_remove_account_posts_alter_post_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='by',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
