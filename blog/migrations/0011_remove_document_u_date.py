# Generated by Django 2.1.2 on 2018-11-20 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181120_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='u_date',
        ),
    ]