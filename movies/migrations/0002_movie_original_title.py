# Generated by Django 2.2.7 on 2019-11-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='original_title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]