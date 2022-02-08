# Generated by Django 3.0.14 on 2022-02-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('SNo', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=150)),
                ('Timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
