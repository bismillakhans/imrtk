# Generated by Django 2.1.2 on 2018-10-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.CharField(choices=[('alp', 'Alappuzha'), ('ekm', 'Ernakulam'), ('idk', 'Idukki'), ('knr', 'Kannur'), ('ksr', 'Kasaragod'), ('kol', 'Kollam'), ('ktm', 'Kottayam'), ('koz', 'Kozhikode'), ('mpm', 'Malappuram'), ('pkd', 'Palakkad'), ('ptm', 'Pathanamthitta'), ('tvm', 'Thiruvananthapuram'), ('tcr', 'Thrissur'), ('wnd', 'Wayanad')], max_length=15)),
                ('phone', models.CharField(max_length=10)),
                ('organisation', models.CharField(max_length=250, verbose_name='Organization / Institution')),
                ('address', models.TextField()),
                ('is_spoc', models.BooleanField(default=False, verbose_name='Is point of contact')),
                ('joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
