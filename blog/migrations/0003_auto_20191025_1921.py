# Generated by Django 2.2.6 on 2019-10-25 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
