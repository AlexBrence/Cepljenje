# Generated by Django 2.2.12 on 2021-05-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emso', models.CharField(max_length=13)),
                ('nameInitial', models.CharField(max_length=1)),
                ('surnameInitial', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=100)),
                ('signupDate', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Oseba',
        ),
    ]