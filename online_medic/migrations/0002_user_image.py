# Generated by Django 3.2.5 on 2024-02-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_medic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(default=False, max_length=1000),
        ),
    ]
