# Generated by Django 3.1.7 on 2021-04-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('semester', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
