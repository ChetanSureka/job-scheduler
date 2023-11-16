# Generated by Django 4.2.7 on 2023-11-08 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.basemodel')),
                ('connection_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('connection_type', models.TextField()),
                ('connection_details', models.TextField()),
            ],
            options={
                'db_table': 'connections',
            },
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='KafkaTopics',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.basemodel')),
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('broker_url', models.TextField()),
            ],
            options={
                'db_table': 'kafka_topics',
            },
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='RestApis',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.basemodel')),
                ('api_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('base_url', models.TextField()),
                ('api_key', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rest_apis',
            },
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='SparkJobs',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.basemodel')),
                ('spark_job_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('spark_details', models.TextField()),
            ],
            options={
                'db_table': 'spark_jobs',
            },
            bases=('api.basemodel',),
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={},
        ),
        migrations.AlterModelOptions(
            name='steps',
            options={},
        ),
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='is_restartable',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='scheduled_time',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='steps',
            name='dependencies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.jobs'),
        ),
        migrations.AlterField(
            model_name='steps',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='steps',
            name='operation_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='operation_type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='steps',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='status',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='steps',
            name='step_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='jobs',
            table='jobs',
        ),
        migrations.AlterModelTable(
            name='steps',
            table='steps',
        ),
        migrations.CreateModel(
            name='StepLogs',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.basemodel')),
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_timestamp', models.TextField()),
                ('log_message', models.TextField(blank=True, null=True)),
                ('log_level', models.TextField()),
                ('step_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.steps')),
            ],
            options={
                'db_table': 'step_logs',
            },
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='JobLogs',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.basemodel')),
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_timestamp', models.TextField()),
                ('log_message', models.TextField(blank=True, null=True)),
                ('log_level', models.TextField()),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.jobs')),
            ],
            options={
                'db_table': 'job_logs',
            },
            bases=('api.basemodel',),
        ),
    ]