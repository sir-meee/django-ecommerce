# Generated by Django 2.2 on 2019-09-24 14:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190924_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='laptop', editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
    ]