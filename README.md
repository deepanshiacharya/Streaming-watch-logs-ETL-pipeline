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

Viewer analytics dashboard:
![viewer-analytics-devices-genres-time-2025-07-12T16-06-01 359Z](https://github.com/user-attachments/assets/71d4425a-d3ee-4cd5-ab70-6d7abd07d7a8)

**Insights** :
Total Users:
→ 20,000 users have engaged with the platform.

Geographic Reach:
→ Content was watched in 6 different countries, indicating early international traction.

Total Watch Time:
→ 1.81 million minutes watched — reflects strong user engagement.

Daily Active Users (DAU):
→ Stable usage observed over the month (approx. 150–180 daily users).
→ No significant dips — indicates consistent platform reliability.

Device Usage by Country:
→ TV usage is dominant in the USA and UK.
→ Mobile is widely used in India and Germany.
→ Suggests optimizing experience by device and region.

Most Watched Genres:
→ Drama, Action, Comedy, Romance, Thriller, and Documentary are all equally popular.
→ Personalization can be implemented as all genres have high viewership.

Time of Engagement (Heatmap):
→ Peak watch hours are 7 PM to 10 PM.
→ Highest engagement on weekends (especially Saturday & Sunday).
→ Ideal for scheduling content drops or system performance scaling.

Points to consider:
Focus marketing efforts on weekend evenings.
Ensure responsive design across TV, mobile, and tablets.
Use watch-time patterns for personalized recommendations.




