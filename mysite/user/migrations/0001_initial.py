# Generated by Django 4.1.5 on 2023-02-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('hash_password', models.CharField(max_length=64)),
                ('points', models.IntegerField()),
            ],
        ),
    ]