# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=False)


class Jobs(BaseModel):
    job_id = models.AutoField(primary_key=True, blank=True, null=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    status = models.TextField()
    is_restartable = models.BooleanField()
    scheduled_time = models.TextField()

    class Meta:
        db_table = 'jobs'


class Steps(BaseModel):
    step_id = models.AutoField(primary_key=True, blank=True, null=True)
    job_id = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    status = models.TextField()
    operation_type = models.TextField()
    operation_details = models.TextField(blank=True, null=True)
    dependencies = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    
    
    class Meta:
        db_table = 'steps'


class JobLogs(BaseModel):
    log_id = models.AutoField(primary_key=True, blank=True, null=True)
    job_id = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    log_timestamp = models.TextField()
    log_message = models.TextField(blank=True, null=True)
    log_level = models.TextField()

    class Meta:
        db_table = 'job_logs'


class StepLogs(BaseModel):
    log_id = models.AutoField(primary_key=True, blank=True, null=True)
    step_id = models.ForeignKey(Steps, on_delete=models.DO_NOTHING)
    log_timestamp = models.TextField()
    log_message = models.TextField(blank=True, null=True)
    log_level = models.TextField()

    class Meta:
        db_table = 'step_logs'


class Connections(BaseModel):
    connection_id = models.AutoField(primary_key=True, blank=True, null=True)
    name = models.TextField()
    connection_type = models.TextField()
    connection_details = models.TextField()

    class Meta:
        db_table = 'connections'


class RestApis(BaseModel):
    api_id = models.AutoField(primary_key=True, blank=True, null=True)
    name = models.TextField()
    base_url = models.TextField()
    api_key = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rest_apis'


class KafkaTopics(BaseModel):
    topic_id = models.AutoField(primary_key=True, blank=True, null=True)
    name = models.TextField()
    broker_url = models.TextField()

    class Meta:
        db_table = 'kafka_topics'



class SparkJobs(BaseModel):
    spark_job_id = models.AutoField(primary_key=True, blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    spark_details = models.TextField()

    class Meta:
        db_table = 'spark_jobs'


