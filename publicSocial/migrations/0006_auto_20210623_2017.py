# Generated by Django 3.1.7 on 2021-06-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicSocial', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/css/steph.jpg', null=True, upload_to=''),
        ),
    ]
