# Generated by Django 3.2.8 on 2021-11-14 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('confessapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confession',
            name='dateofpublish',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]