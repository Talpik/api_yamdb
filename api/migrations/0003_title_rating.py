# Generated by Django 3.0.5 on 2020-10-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_title_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
