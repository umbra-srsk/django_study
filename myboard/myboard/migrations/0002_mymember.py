# Generated by Django 4.0.5 on 2022-06-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('mypassword', models.CharField(max_length=100)),
                ('myemail', models.CharField(max_length=100)),
            ],
        ),
    ]
