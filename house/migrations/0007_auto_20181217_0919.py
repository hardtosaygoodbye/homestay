# Generated by Django 2.1.4 on 2018-12-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_auto_20181217_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]