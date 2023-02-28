# Generated by Django 4.1.5 on 2023-02-26 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_appuser_item_purchased_by_delete_purchases'),
        ('home', '0005_alter_groupmembers_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(related_name='group_members', to='user.appuser'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.appuser'),
        ),
        migrations.DeleteModel(
            name='GroupMembers',
        ),
    ]
