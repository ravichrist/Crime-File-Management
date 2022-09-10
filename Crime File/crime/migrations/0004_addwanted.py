# Generated by Django 2.1.5 on 2019-04-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0003_addmissing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addwanted',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('cmp1', models.TextField(max_length=500)),
                ('height', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='missing/')),
                ('case1', models.TextField(max_length=500)),
                ('type1', models.CharField(max_length=500)),
            ],
        ),
    ]
