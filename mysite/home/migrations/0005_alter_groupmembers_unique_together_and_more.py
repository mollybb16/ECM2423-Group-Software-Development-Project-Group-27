# Generated by Django 4.1.5 on 2023-02-26 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_groupmembers_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmembers',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='groupmembers',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='groupmembers',
            name='user_id',
        ),
    ]
