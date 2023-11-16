from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Jobs(BaseModel):
    job_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    status = models.TextField()
    is_restartable = models.BooleanField()
    scheduled_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Jobs'
        db_table = 'jobs'


class Steps(BaseModel):
    step_id = models.AutoField(primary_key=True)
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
        verbose_name_plural = 'Steps'
        db_table = 'steps'


class JobLogs(BaseModel):
    log_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    log_timestamp = models.TextField()
    log_message = models.TextField(blank=True, null=True)
    log_level = models.TextField()

    class Meta:
        verbose_name_plural = 'Job Logs'
        db_table = 'job_logs'


class StepLogs(BaseModel):
    log_id = models.AutoField(primary_key=True)
    step_id = models.ForeignKey(Steps, on_delete=models.DO_NOTHING)
    log_timestamp = models.TextField()
    log_message = models.TextField(blank=True, null=True)
    log_level = models.TextField()

    class Meta:
        verbose_name_plural = "Step Logs"
        db_table = 'step_logs'


class Connections(BaseModel):
    connection_id = models.AutoField(primary_key=True)
    name = models.TextField()
    connection_type = models.TextField()
    connection_details = models.TextField()

    class Meta:
        verbose_name_plural = "Connections"
        db_table = 'connections'


class RestApis(BaseModel):
    api_id = models.AutoField(primary_key=True)
    name = models.TextField()
    base_url = models.TextField()
    api_key = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Rest Apis"
        db_table = 'rest_apis'


class KafkaTopics(BaseModel):
    topic_id = models.AutoField(primary_key=True)
    name = models.TextField()
    broker_url = models.TextField()

    class Meta:
        verbose_name_plural = "Kafka Topics"
        db_table = 'kafka_topics'



class SparkJobs(BaseModel):
    spark_job_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    spark_details = models.TextField()

    class Meta:
        verbose_name_plural = "Spark Jobs"
        db_table = 'spark_jobs'

