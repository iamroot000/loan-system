# Generated by Django 4.1.7 on 2023-04-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanager', '0012_alter_staff_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='total_profit',
            field=models.IntegerField(default=0),
        ),
    ]
