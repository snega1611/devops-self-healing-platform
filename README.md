# AI-Powered Kubernetes Incident Response System

## Overview

This project automates Kubernetes incident detection, root cause analysis (RCA), and reporting using Grafana, n8n, Python, and Google Gemini.

When a Kubernetes incident occurs (for example, ImagePullBackOff, CrashLoopBackOff, Pending Pods, or Container Creation failures), Grafana triggers an alert. The workflow automatically collects live Kubernetes evidence, analyzes the incident using AI, and generates a detailed incident report with remediation recommendations.

---

## Problem Statement

Troubleshooting Kubernetes incidents often requires engineers to manually inspect:

* Pod status
* Events
* Deployment configurations
* Logs
* Resource utilization

This process can be time-consuming during production incidents.

This project reduces investigation time by automatically gathering evidence and generating an AI-powered root cause analysis report.

---

🔧 What I implemented
☸️ Kubernetes Setup & Deployments
Set up Minikube cluster
Created and managed:
Deployments
ReplicaSets
Services
Performed rolling updates and debugging using kubectl
🌐 Networking & Ingress
Exposed applications using Kubernetes Service (ClusterIP/NodePort)
Configured and tested Ingress controller for routing traffic
Verified external access using ngrok tunnel for webhook testing
💾 Storage & Volumes
Implemented Persistent Volume (PV) and Persistent Volume Claim (PVC)
Mounted shared storage inside pods
Tested data persistence across pod restarts
⚙️ Resource Management
Defined CPU and Memory requests/limits
Tested resource sharing behavior between pods
Configured Horizontal Pod Autoscaler (HPA) based on CPU usage
Observed scaling behavior under load
❤️ Health & Reliability
Implemented:
Liveness probe
Readiness probe
Simulated failures like:
ImagePullBackOff
CrashLoopBackOff
Probe failures
Debugged using:
kubectl logs
kubectl describe
kubectl get events
📊 Observability & Alerting
Integrated Grafana alert rules
Monitored:
Pod failures
CPU usage anomalies
Deployment health
Triggered alerts via webhooks to n8n workflow
🔁 Automation Flow (DevOps + AI)
Alerts triggered n8n workflow
Collected cluster diagnostics (pods, events, logs)
Sent data to AI agent for root cause analysis
Generated incident report automatically

## Architecture

# AI-Powered Kubernetes Incident Analyzer

```text
+-------------------+
| Kubernetes Cluster|
| (Pods, Deployments|
|  HPA, Services)   |
+---------+---------+
          |
          | Pod Failure
          | ImagePullBackOff
          | CrashLoopBackOff
          v
+-------------------+
| Grafana Alerting  |
| Alert Rules       |
+---------+---------+
          |
          | Webhook
          v
+-------------------+
| n8n Workflow      |
+---------+---------+
          |
          | Collect Data
          |
          +--------------------+
          |                    |
          v                    v
+----------------+    +----------------+
| kubectl get    |    | kubectl describe|
| pods/events    |    | logs/deployment |
+----------------+    +----------------+
          |
          | Consolidated Incident Data
          v
+-------------------+
| AI Analysis Agent |
| (Gemini/OpenAI)   |
+---------+---------+
          |
          | Root Cause Analysis
          | Impact Assessment
          | Recommended Fix
          v
+-------------------+
| Incident Report   |
| - Root Cause      |
| - Evidence        |
| - Impact          |
| - Fix             |
+---------+---------+
          |
          v
+-------------------+
| Email / Slack /   |
| Teams / Jira      |
+-------------------+
```

---

## Technology Stack

* Kubernetes
* Minikube
* Grafana
* n8n
* Python
* Flask
* Google Gemini
* Docker
* Kubernetes Metrics Server

---

## Features

### Incident Detection

Monitors and detects:

* ImagePullBackOff
* CrashLoopBackOff
* Error
* Pending Pods
* ContainerCreating Failures

### Automated Evidence Collection

The Python service automatically gathers:

* Pod status
* Kubernetes events
* Pod descriptions
* Deployment YAML
* Pod logs
* Resource utilization metrics

### AI-Powered Root Cause Analysis

Gemini analyzes collected evidence and provides:

* Incident summary
* Root cause
* Supporting evidence
* Business impact
* Recommended remediation
* Secondary findings
* Confidence level

### Automated Reporting

Incident reports are automatically delivered through email.

---

## Workflow

### Step 1: Kubernetes Failure Occurs

Example:

```text
self-healing-app-xxxx   0/1   ImagePullBackOff
```

---

### Step 2: Grafana Detects Failure

Grafana alert rule enters the Firing state.

---

### Step 3: n8n Workflow Triggered

The Grafana webhook triggers the n8n workflow.

---

### Step 4: Kubernetes Evidence Collection

The Flask API collects:

```bash
kubectl get pods
kubectl get events
kubectl describe pod
kubectl logs
kubectl get deployment -o yaml
kubectl top pods
```

---

### Step 5: AI Analysis

Gemini analyzes the evidence and generates an RCA report.

Example:

```text
Primary Root Cause:
Deployment references invalid image tag:
sne16/self-healing-app:notexists

Evidence:
- ImagePullBackOff detected
- Manifest not found
- Deployment rollout timed out

Impact:
Application running with reduced availability

Recommended Fix:
Update deployment with a valid image tag
```

---

### Step 6: Incident Report Delivery

The generated RCA report is automatically sent through email.

---

## Screenshots

### Normal Monitoring State

![Alert Normal](images/Alert-Normal.png)

### Pod Failure

![ImagePullBackOff](images/ImagePullBackoff.png)

### Grafana Alert Fired

![Status Fired](images/Status-Firing.png)

### n8n Workflow

![n8n Workflow](images/n8n-workflow.png)

### Flask API Response

![Flask API Response](images/FlaskAPIResponse.png)

### Email Incident Report

![Email Response](images/Email-response.png)

---

## Sample Incident

### Incident

ImagePullBackOff caused by an invalid image tag.

### Root Cause

```text
sne16/self-healing-app:notexists
```

### Evidence

```text
Failed to pull image:
manifest unknown

Reason:
ImagePullBackOff
```

### Impact

* Deployment rollout blocked
* One replica unavailable
* Reduced application availability

### Fix

```bash
kubectl set image deployment/self-healing-app \
self-healing-app=sne16/self-healing-app:latest \
-n devops-platform
```

