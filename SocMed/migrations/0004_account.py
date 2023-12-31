# Generated by Django 4.2.3 on 2023-07-27 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SocMed', '0003_post_shares'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Followers', models.IntegerField(default=0)),
                ('Following', models.IntegerField(default=0)),
                ('dp', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('posts', models.ManyToManyField(to='SocMed.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
