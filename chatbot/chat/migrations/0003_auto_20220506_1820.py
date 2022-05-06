# Generated by Django 3.2.9 on 2022-05-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_details_d_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FILES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhaar', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('voterid', models.CharField(max_length=100)),
                ('drlics', models.CharField(max_length=100)),
                ('rcard', models.CharField(max_length=100)),
                ('sslc', models.CharField(max_length=100)),
                ('plustwo', models.CharField(max_length=100)),
                ('fsslc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'FILES',
            },
        ),
        migrations.CreateModel(
            name='PROFILE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhaarNO', models.CharField(max_length=20)),
                ('PanNO', models.CharField(max_length=20)),
                ('voterNO', models.CharField(max_length=20)),
                ('driveNO', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('focc', models.CharField(max_length=20)),
                ('mocc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'PROFILE',
            },
        ),
        migrations.RemoveField(
            model_name='details',
            name='Address',
        ),
        migrations.AddField(
            model_name='details',
            name='password',
            field=models.CharField(default='null', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='username',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]