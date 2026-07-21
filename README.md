# 🛡 CyberShield Analytics
## Enterprise Security Operations Center (SOC) Platform
CyberShield Analytics is an enterprise-style Security Operations Center (SOC) platform developed using Python, MySQL, and Streamlit.The platform monitors system logs and simulated network traffic, identifies malicious activities using a rule-based detection engine, calculates dynamic risk scores, stores threat intelligence in a MySQL database

### Project Overview
CyberShield Analytics is an enterprise-style Security Operations Center (SOC) platform developed using Python, MySQL, and Streamlit.
The platform continuously monitors system logs and simulated network traffic, identifies malicious activities using a rule-based detection engine, calculates dynamic risk scores, stores threat intelligence in a MySQL database, and visualizes incidents through an interactive SOC dashboard.

This project demonstrates practical cybersecurity analytics, automation, database management, dashboard development, authentication, and incident management within a single application.


### 🎯 Business Problem

Organizations receive thousands of security events every day from servers, applications, firewalls, and network devices. Manually reviewing these logs is time-consuming and often results in delayed responses to cyber threats.

Security teams require an automated platform that can:

Monitor incoming logs continuously
Detect suspicious activities automatically
Prioritize threats based on risk
Alert analysts quickly
Track incidents until resolution
Visualize security metrics through dashboards

CyberShield Analytics addresses these challenges by providing a simplified yet enterprise-inspired Security Operations Center (SOC) workflow.
Project Objectives

The primary objectives of this project are:

Build a real-time cybersecurity monitoring platform
Detect common cyber attacks automatically
Calculate dynamic risk scores
Store security events in a centralized database
Provide interactive SOC dashboards
Implement user authentication with role-based access
Manage incidents from detection to resolution
Demonstrate enterprise software architecture for portfolio purposes

Key Features
✅ Real-Time Log Monitoring

Automatically monitors system log files using Python Watchdog and processes new log entries without manual intervention.

Example:
192.168.1.100, FAILED
Brute Force Attack Detected

| Threat                     | Detection Pattern |
| -------------------------- | ----------------- |
| Brute Force                | FAILED            |
| SQL Injection              | UNION SELECT      |
| Cross Site Scripting (XSS) | `<script>`        |
| Port Scan                  | Nmap              |
| SSH Attack                 | Port 22           |
| FTP Attack                 | Port 21           |
| Telnet Attack              | Port 23           |
| SMB Attack                 | Port 445          |
| RDP Attack                 | Port 3389         |
| SQL Server Attack          | Port 1433         |


✅ Dynamic Risk Scoring

Instead of assigning a fixed risk level, CyberShield calculates a dynamic risk score using:
| Parameter         | Value |
| ----------------- | ----- |
| Severity          | 5     |
| Asset Criticality | 10    |
| Frequency         | 6     |
Risk Score = 5 × 10 × 6 = 300
This enables analysts to prioritize high-risk incidents.

✅ Network Traffic Monitoring

The platform simulates enterprise network monitoring by processing network events containing:

Source IP
Destination IP
Protocol
Port
Action (ALLOW / DENY)

Example:
Source: 192.168.1.15
Destination: 10.0.0.10
Protocol: TCP
Port: 3389
Action: DENY

Threat Detected:
Remote Desktop Protocol (RDP) Attack

✅ IP Intelligence

Each detected threat can be enriched with additional information including:

Country
City
ISP
Organization
Risk Score

This allows analysts to identify suspicious geographic locations and external attackers.

✅ Incident Management

Every critical threat generates an incident that can be tracked through its lifecycle.

Incident statuses include:
OPEN
↓

INVESTIGATING
↓

RESOLVED

✅ Interactive SOC Dashboard

The Streamlit dashboard provides security analysts with real-time insights.

Key Performance Indicators (KPIs):

Total Alerts
Critical Threats
Average Risk Score
Unique Attackers
Countries Detected

Visualizations include:

Threat Distribution
Top Attackers
Risk Analysis
Live Incident Logs

✅ Role-Based Authentication

The application supports secure login using hashed passwords (bcrypt).

User Roles:
| Role        | Permissions                             |
| ----------- | --------------------------------------- |
| Admin       | Full access, user management, incidents |
| SOC Analyst | Investigate and update incidents        |
| Viewer      | Read-only dashboard access              |


🛠 Technology Stack
| Category             | Technology             |
| -------------------- | ---------------------- |
| Programming Language | Python 3.12            |
| Dashboard            | Streamlit              |
| Database             | MySQL                  |
| Data Processing      | Pandas                 |
| Visualization        | Plotly                 |
| File Monitoring      | Watchdog               |
| Authentication       | bcrypt                 |
| Database Connector   | mysql-connector-python |
| Version Control      | Git & GitHub           |


## Login Page

![Login Page](screenshots/login_page.png)

## Dashboard

![Dashboard](screenshots/dashboard_home.png)

## Threat Logs

![Threat Logs](screenshots/threat_logs.png)


### Enterprise Architecture
                    System Logs
                         │
                         ▼
              Watchdog File Monitor
                         │
                         ▼
              Threat Detection Engine
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
 Risk Score Engine                Incident Manager
         │                               │
         └───────────────┬───────────────┘
                         ▼
                 MySQL Database
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
 Streamlit SOC Dashboard          Alert Engine
                         │
                         ▼
                    SOC Analyst


### Project Structure
CyberShield-Analytics/
│
├── app.py
├── login.py
├── monitor.py
├── detector.py
├── database.py
├── config.py
├── network_monitor.py
├── traffic_generator.py
├── incident_manager.py
├── server_access.log
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── login.png
│   ├── dashboard.png
│   ├── incidents.png
│   └── threat_detection.png
│
└── sql/
    ├── database.sql
    └── sample_data.sql



Database Design

CyberShield Analytics uses MySQL as the backend database to securely store security events, user information, and incident records. The database is designed to simulate a Security Information and Event Management (SIEM) platform where all detected threats are centrally stored for analysis and investigation.

The project contains three primary tables:

ThreatLogs – Stores detected security events.
Users – Manages authentication and role-based access.
Incidents – Tracks the lifecycle of security incidents.

📋 ThreatLogs Table

The ThreatLogs table is the core of the application. Every detected threat is inserted into this table.
| Column            | Data Type    | Description               |
| ----------------- | ------------ | ------------------------- |
| id                | INT          | Primary Key               |
| source_ip         | VARCHAR(50)  | Source IP Address         |
| event_type        | VARCHAR(100) | Attack Type               |
| severity_level    | INT          | Threat Severity (1–5)     |
| asset_criticality | INT          | Asset Importance          |
| description       | TEXT         | Original Log/Event        |
| frequency         | INT          | Number of occurrences     |
| risk_score        | INT          | Calculated Risk Score     |
| country           | VARCHAR(50)  | IP Country                |
| city              | VARCHAR(50)  | IP City                   |
| isp               | VARCHAR(100) | Internet Service Provider |
| organization      | VARCHAR(100) | Organization Name         |
| created_at        | TIMESTAMP    | Detection Time            |


👥 Users Table

The Users table manages authentication and authorization.
| Column   | Description              |
| -------- | ------------------------ |
| user_id  | Primary Key              |
| username | Login Username           |
| password | Encrypted using bcrypt   |
| role     | Admin / Analyst / Viewer |


🚨 Incidents Table

Every critical threat creates an incident.
| Column        | Description                     |
| ------------- | ------------------------------- |
| incident_id   | Primary Key                     |
| threat_id     | Related Threat                  |
| source_ip     | Attacker IP                     |
| attack_type   | Attack Name                     |
| severity      | Severity Level                  |
| risk_score    | Calculated Risk                 |
| status        | OPEN / INVESTIGATING / RESOLVED |
| assigned_to   | Analyst Name                    |
| created_time  | Incident Creation Time          |
| resolved_time | Resolution Time                 |


Authentication Workflow

CyberShield uses bcrypt for secure password hashing and role-based access control (RBAC).

Login Process
User Opens Login Page
          │
          ▼
Enter Username & Password
          │
          ▼
Retrieve User from Database
          │
          ▼
Verify Password (bcrypt)
          │
          ▼
Authentication Successful?
     ┌───────────────┐
     │               │
    Yes             No
     │               │
     ▼               ▼
Dashboard      Error Message



<p>
  <img src="Streamlit_Dashboards/dashboard_2.png" width="700"/>
</p>


## How to Run the System

### 1. Set Up the Database
- Open your MySQL Workbench.
- Create a cyber_security_db database
- Run the provided cyber_security_db.sql to create the tables & storing for data

### 3. Install Dependencies
```python
pip install streamlit mysql-connector-python plotly pandas
```

### 4. Run the Detector
Open a terminal and start the background script that monitors the logs:
Start the Log Monitor
```python
python monitor.py
```

Start the Network Monitor (or Simulator)
```
python network_monitor.py
```

### Launch the Dashboard
Open a second terminal and run the UI:
```python
streamlit run ap.py
```

Open in Browser
```
http://localhost:8501
```
Project Outcomes

The project successfully demonstrates:

Automated threat detection using Python.
Real-time log monitoring.
Simulated network traffic monitoring.
Dynamic risk scoring.
MySQL database integration.
Interactive SOC dashboard using Streamlit.
Role-based authentication (Admin, Analyst, Viewer).
Incident creation and tracking.
Cybersecurity data visualization.


Future Enhancements
Although the project meets its objectives, several enhancements could make it even closer to a production SOC platform.
Machine Learning Integration
Network anomaly detection.
Insider threat detection.
Behavioral analysis.

External Threat Intelligence
Integrate public threat intelligence APIs such as:
AbuseIPDB
VirusTotal


Live Packet Capture
Replace simulated network traffic with real packet capture using Scapy or similar tools.

Notification System
Support:
Email alerts
Slack notifications


Conclusion

CyberShield Analytics demonstrates how modern Security Operations Centers can automate the collection, analysis, and visualization of cybersecurity events. By combining Python, MySQL, and Streamlit, the project provides a realistic simulation of SOC workflows, including log monitoring, threat detection, risk assessment, incident management, and dashboard reporting.

While the current implementation focuses on rule-based detection and simulated network traffic, the modular architecture allows future expansion with machine learning, real packet capture, and external threat intelligence feeds. This makes CyberShield Analytics a strong portfolio project that highlights software engineering, data analytics, and cybersecurity concepts in a practical, end-to-end application.

Author
Prajakta Bhondave
Aspiring Data Analyst | Python | SQL | Power BI | Streamlit | Cybersecurity Analytics
Connect with Me
GitHub: https://github.com/prajakta-89
LinkedIn: (Add your LinkedIn profile URL here.)
