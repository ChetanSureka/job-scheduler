# Generated by Django 4.2.7 on 2023-11-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_connections_options_alter_joblogs_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='scheduled_time',
            field=models.DateTimeField(),
        ),
    ]
