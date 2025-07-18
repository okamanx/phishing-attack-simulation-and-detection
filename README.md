# Phishing Attack Simulation and Detection Project

## Overview
This project simulates phishing attacks to test user awareness and implements detection mechanisms for email and website phishing. It is intended for educational and security awareness purposes only.

## Objectives
- Simulate phishing attacks (emails, fake websites) to test user awareness.
- Implement detection mechanisms (email filtering, fake website detection).

## Components
- **phishing_simulation/**: Tools to simulate phishing emails and fake websites.
- **detection/**: Scripts to detect phishing emails and websites.

## Tools Used
- Python 3.x
- Flask (for fake website)
- smtplib, email (for email simulation)
- scikit-learn (for ML-based detection)
- Requests (for URL analysis)

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd project_codec2
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### 1. Email Phishing Detection
Detect if an email is a phishing attempt using ML and heuristics.
```bash
python -m detection.email_filter
```
- Paste the email content and (optionally) sender when prompted.
- The script will output whether the email is likely phishing, a confidence score, and feature details.

### 2. Website Phishing Detection
Detect if a website URL is a phishing site using ML and rule-based features.
```bash
python -m detection.website_detector
```
- Enter the website URL when prompted.
- The script will output whether the site is likely phishing, a confidence score, and feature details.

### 3. Phishing Email Simulator
Send a simulated phishing email (for awareness testing).
```bash
python -m phishing_simulation.email_simulator
```
- Enter SMTP credentials, recipient, subject, and phishing link when prompted.
- The script will send a realistic Instagram-style phishing email to the recipient.

### 4. Phishing Website Simulator
Run a fake phishing website (Instagram-style login page) for awareness testing.
```bash
python -m phishing_simulation.website_simulator
```
- Opens a Flask web server (default: http://127.0.0.1:5000/).
- Captures submitted credentials (for simulation only).

## Disclaimer
This project is for educational and awareness testing purposes only. Do not use for unauthorized phishing or malicious activity. 
