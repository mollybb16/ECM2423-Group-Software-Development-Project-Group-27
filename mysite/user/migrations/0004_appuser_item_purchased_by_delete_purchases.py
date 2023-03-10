# Generated by Django 4.1.5 on 2023-02-26 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0003_alter_purchases_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('base_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='purchased_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Purchases',
        ),
    ]
