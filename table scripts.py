import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect("orchestration.db")
cursor = conn.cursor()

# Create tables for jobs, steps, job logs, step logs, connections, REST APIs, Kafka topics, and Spark jobs
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS jobs (
        job_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        is_restartable BOOLEAN NOT NULL,
        scheduled_time TIMESTAMP NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS steps (
        step_id INTEGER PRIMARY KEY,
        job_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        operation_type TEXT NOT NULL,
        operation_details TEXT,
        dependencies TEXT,
        start_time TIMESTAMP,
        end_time TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS job_logs (
        log_id INTEGER PRIMARY KEY,
        job_id INTEGER NOT NULL,
        log_timestamp TIMESTAMP NOT NULL,
        log_message TEXT,
        log_level TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS step_logs (
        log_id INTEGER PRIMARY KEY,
        step_id INTEGER NOT NULL,
        log_timestamp TIMESTAMP NOT NULL,
        log_message TEXT,
        log_level TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS connections (
        connection_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        connection_type TEXT NOT NULL,
        connection_details TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS rest_apis (
        api_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        base_url TEXT NOT NULL,
        api_key TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS kafka_topics (
        topic_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        broker_url TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS spark_jobs (
        spark_job_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        spark_details TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );
''')

# Sample functions to create a job and step
def create_job(name, description, scheduled_time, is_restartable):
    cursor.execute('''
        INSERT INTO jobs (name, description, status, is_restartable, scheduled_time)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, description, 'scheduled', is_restartable, scheduled_time))
    conn.commit()

def create_step(job_id, name, description, operation_type, operation_details, dependencies):
    dependencies = str(dependencies)
    cursor.execute('''
        INSERT INTO steps (job_id, name, description, status, operation_type, operation_details, dependencies)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (job_id, name, description, 'pending', operation_type, operation_details, dependencies))
    conn.commit()

# Sample code to create a job and its steps
job_scheduled_time = datetime(2023, 11, 1, 8, 0)  # Example scheduled time
create_job("Sample Job", "This is a test job.", job_scheduled_time, True)

job_id = cursor.lastrowid  # Get the ID of the created job

# Create steps for the job
create_step(job_id, "REST API Step", "Consume data from REST API", "REST_API", "API details here", [0])
create_step(job_id, "Kafka Step", "Publish data to Kafka topic", "Kafka", "Kafka details here", [1])
create_step(job_id, "Spark Step", "Run a Spark job", "Spark", "Spark details here", [2])

# Sample code to log a step
def log_step(step_id, log_timestamp, log_message, log_level):
    cursor.execute('''
        INSERT INTO step_logs (step_id, log_timestamp, log_message, log_level)
        VALUES (?, ?, ?, ?)
    ''', (step_id, log_timestamp, log_message, log_level))
    conn.commit()

log_timestamp = datetime.now()
log_step(1, log_timestamp, "REST API Step started", "INFO")

# Close the database connection
conn.close()
