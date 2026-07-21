# 🛡 CyberShield Analytics
## Enterprise Security Operations Center (SOC) Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-green)
![License](https://img.shields.io/badge/License-MIT-success)

CyberShield Analytics is an enterprise-style **Security Operations Center (SOC)** platform built using **Python, Streamlit, and MySQL**.

The platform continuously monitors system logs and simulated network traffic, detects cyber threats using a rule-based detection engine, calculates dynamic risk scores, manages incidents, and provides an interactive dashboard for security analysts.

---

# 📑 Table of Contents

- Project Overview
- Business Problem
- Objectives
- Key Features
- Technology Stack
- System Architecture
- Dashboard Preview
- Project Structure
- Database Design
- Authentication Workflow
- Installation
- Running the Project
- Project Outcomes
- Future Enhancements
- Author

---

# 📖 Project Overview

Organizations generate thousands of security logs every day from servers, applications, firewalls, and network devices.

CyberShield Analytics automates the Security Operations Center (SOC) workflow by monitoring logs in real time, detecting cyber attacks, calculating risk scores, storing incidents in MySQL, and visualizing security metrics through a Streamlit dashboard.

This project demonstrates practical implementation of:

- Cybersecurity Analytics
- Log Monitoring
- Threat Detection
- Incident Management
- Risk Assessment
- Database Management
- Dashboard Development
- Role-Based Authentication

---

# 🎯 Business Problem

Security analysts spend countless hours manually reviewing logs.

Manual monitoring often causes:

- Delayed threat detection
- Missed security incidents
- Slow incident response
- Difficulty prioritizing critical attacks

CyberShield Analytics automates these tasks by:

- Monitoring logs continuously
- Detecting suspicious activities
- Calculating risk scores
- Creating security incidents
- Visualizing security events
- Supporting analyst investigation

---

# 🎯 Project Objectives

- Build a real-time SOC monitoring platform
- Detect common cyber attacks automatically
- Calculate dynamic risk scores
- Store threats in a centralized MySQL database
- Create interactive dashboards
- Implement secure login with role-based access
- Manage incidents through their lifecycle
- Demonstrate enterprise SOC architecture

---

# 🚀 Key Features

## ✅ Real-Time Log Monitoring

The platform continuously monitors log files using Python Watchdog.

Example log:

```text
192.168.1.100, FAILED
```

Detection:

```text
Brute Force Attack Detected
```

---

## 🔍 Supported Threat Detection

| Threat | Detection Pattern |
|---------|------------------|
| Brute Force | FAILED |
| SQL Injection | UNION SELECT |
| Cross-Site Scripting (XSS) | `<script>` |
| Port Scan | Nmap |
| SSH Attack | Port 22 |
| FTP Attack | Port 21 |
| Telnet Attack | Port 23 |
| SMB Attack | Port 445 |
| RDP Attack | Port 3389 |
| SQL Server Attack | Port 1433 |

---

## ⚠ Dynamic Risk Scoring

CyberShield calculates risk dynamically using:

Risk Score = Severity × Asset Criticality × Frequency

Example:

| Parameter | Value |
|-----------|------:|
| Severity | 5 |
| Asset Criticality | 10 |
| Frequency | 6 |

Risk Score = **300**

Higher scores indicate higher priority incidents.

---

## 🌐 Network Traffic Monitoring

The platform simulates enterprise network traffic.

Example:

```text
Source IP : 192.168.1.15
Destination : 10.0.0.10
Protocol : TCP
Port : 3389
Action : DENY
```

Detected Threat

```text
Remote Desktop Protocol (RDP) Attack
```

---

## 🌍 IP Intelligence

Each detected IP is enriched with:

- Country
- City
- ISP
- Organization
- Risk Score

---

## 🚨 Incident Management

Critical threats automatically generate incidents.

Incident Workflow

```text
OPEN
   ↓
INVESTIGATING
   ↓
RESOLVED
```

---

## 📊 Interactive SOC Dashboard

The dashboard provides:

- Total Alerts
- Critical Threats
- Average Risk Score
- Unique Attackers
- Countries Detected

### Dashboard Visualizations

- Threat Distribution
- Top Attackers
- Risk Analysis
- Incident Timeline
- Live Threat Logs

---

## 🔐 Role-Based Authentication

Passwords are securely hashed using bcrypt.

| Role | Permissions |
|------|-------------|
| Admin | Full Access |
| SOC Analyst | Investigate Incidents |
| Viewer | Read-only Dashboard |

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.12 |
| Dashboard | Streamlit |
| Database | MySQL |
| Data Processing | Pandas |
| Visualization | Plotly |
| Authentication | bcrypt |
| Log Monitoring | Watchdog |
| Database Connector | mysql-connector-python |
| Version Control | Git & GitHub |

---

# 🏗 Enterprise Architecture

```text
               System Logs
                    │
                    ▼
        Watchdog File Monitor
                    │
                    ▼
       Threat Detection Engine
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
Risk Score Engine        Incident Manager
       │                         │
       └────────────┬────────────┘
                    ▼
             MySQL Database
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
 Streamlit Dashboard      Alert Engine
                    │
                    ▼
               SOC Analyst
```

---

# 📸 Dashboard Preview

## Login

```markdown
![Login](screenshots/login.png)
```

---

## Dashboard

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

## Threat Logs

```markdown
![Threat Logs](screenshots/threat_logs.png)
```

---

## Incidents

```markdown
![Incidents](screenshots/incidents.png)
```

---

# 📂 Project Structure

```text
CyberShield-Analytics/
│
├── app.py
├── login.py
├── monitor.py
├── detector.py
├── network_monitor.py
├── traffic_generator.py
├── incident_manager.py
├── database.py
├── config.py
├── requirements.txt
├── README.md
│
├── screenshots/
│
├── sql/
│   ├── database.sql
│   └── sample_data.sql
│
└── server_access.log
```

---

# 🗄 Database Design

The application contains three primary tables.

## ThreatLogs

Stores all detected security events.

| Column | Description |
|---------|-------------|
| id | Primary Key |
| source_ip | Source IP |
| event_type | Attack Type |
| severity_level | Severity |
| asset_criticality | Asset Importance |
| description | Original Log |
| frequency | Occurrence Count |
| risk_score | Calculated Score |
| country | Country |
| city | City |
| isp | Internet Provider |
| organization | Organization |
| created_at | Detection Time |

---

## Users

Stores authentication information.

| Column | Description |
|---------|-------------|
| user_id | Primary Key |
| username | Login Username |
| password | bcrypt Password |
| role | User Role |

---

## Incidents

Tracks incident lifecycle.

| Column | Description |
|---------|-------------|
| incident_id | Primary Key |
| threat_id | Related Threat |
| source_ip | Attacker |
| attack_type | Attack |
| severity | Severity |
| risk_score | Score |
| status | OPEN / INVESTIGATING / RESOLVED |
| assigned_to | Analyst |
| created_time | Created |
| resolved_time | Resolved |

---

# 🔐 Authentication Workflow

```text
User Login
     │
     ▼
Enter Credentials
     │
     ▼
Fetch User from MySQL
     │
     ▼
Verify Password (bcrypt)
     │
     ▼
Authentication Successful?
      │
 ┌────┴────┐
 ▼         ▼
Dashboard  Login Failed
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/prajakta-89/CyberShield-Analytics.git
```

```bash
cd CyberShield-Analytics
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Database

Create the database:

```sql
CREATE DATABASE cyber_security_db;
```

Run:

```
sql/database.sql
```

---

# ▶ Running the Project

### Start Log Monitor

```bash
python monitor.py
```

### Start Network Monitor

```bash
python network_monitor.py
```

### Launch Dashboard

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 📈 Project Outcomes

CyberShield Analytics successfully demonstrates:

- Automated Threat Detection
- Real-Time Log Monitoring
- Network Traffic Monitoring
- Dynamic Risk Scoring
- Incident Management
- MySQL Integration
- Interactive Dashboards
- Role-Based Authentication
- Cybersecurity Analytics

---

# 🚀 Future Enhancements

- Machine Learning Threat Detection
- Behavioral Analytics
- Insider Threat Detection
- VirusTotal Integration
- AbuseIPDB Integration
- Email Alerts
- Slack Notifications
- Real Packet Capture (Scapy)
- SIEM Integration

---

# 👩‍💻 Author

## Prajakta Bhondave

**Aspiring Data Analyst | Python | SQL | Power BI | Streamlit | Cybersecurity Analytics**

### Connect with Me

- **GitHub:** https://github.com/prajakta-89
- **LinkedIn:** https://www.linkedin.com/in/prajakta-bhondave-773b092a6

---

## ⭐ If you found this project useful, please consider giving it a star.
