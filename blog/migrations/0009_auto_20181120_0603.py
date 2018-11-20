# Generated by Django 2.1.2 on 2018-11-20 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_document_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.CharField(choices=[('Statitics', 'Statitics'), ('Probabilty', 'Probabilty'), ('Algebra', 'Relational Algebra'), ('Geometry', 'Geometry')], default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='fname',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='document',
            name='u_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
