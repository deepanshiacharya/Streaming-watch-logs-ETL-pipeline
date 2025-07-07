# Streaming Platform Watch Logs ETL Pipeline

A complete end-to-end ETL pipeline project that simulates and processes watch logs for a video streaming service. Built using **Apache Airflow**, **PostgreSQL**, **Docker**, and visualized using **Apache Superset**.

---

## Project Overview

This project demonstrates a production-like ETL architecture for handling user activity data from a streaming platform. It covers:

-  Generating synthetic watch log data
-  Extracting and transforming logs using Python and Pandas
-  Loading processed data into PostgreSQL
-  Orchestrating the pipeline with Apache Airflow
-  Creating dashboards in Apache Superset for analytics

---

##  Tech Stack

| Tool              | Purpose                                |
|-------------------|----------------------------------------|
| Python & Pyspark  | Data generation and transformation     |
| PostgreSQL        | Data warehouse                         |
| Apache Airflow    | Workflow orchestration                 |
| Apache Superset   | Data visualization & BI dashboarding   |
| Docker            | Containerization of entire setup       |

---

##  Schema and Data

The project simulates a **watch logs dataset** with the following columns:

| Column              | Description                                      |
|---------------------|--------------------------------------------------|
| `user_id`           | ID of the user                                   |
| `content_id`        | ID of the content/movie/show watched             |
| `genre`             | Genre of the content                             |
| `device`            | Device used to stream (Mobile, TV, etc.)         |
| `country`           | Country of the user                              |
| `watch_start`       | Timestamp when viewing started                   |
| `watch_duration_min`| Duration of watch session (in minutes)           |
| `load_timestamp`    | Timestamp when the record was inserted to DB     |

---





