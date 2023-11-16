from django.contrib import admin
from .models import *


admin.site.register(Jobs)
admin.site.register(Steps)
admin.site.register(JobLogs)
admin.site.register(StepLogs)
admin.site.register(Connections)
admin.site.register(RestApis)
admin.site.register(KafkaTopics)
admin.site.register(SparkJobs)