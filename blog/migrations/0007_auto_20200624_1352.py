# Generated by Django 3.0.7 on 2020-06-24 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'publish', 'ordering': ('-publish',)},
        ),
    ]
