# Splunk Alert Configuration

## Alert Name:
Brute Force Detection

## Condition:
Triggered when failed login attempts exceed threshold

## Query Used:
(index=botsv3 EventCode=4625 | stats count by Account_Name | where count > 10)

## Actions:
- Trigger Python script (block_ip.py)
- Send alert notification

## Purpose:
Automate response to brute force attacks (SOAR)
