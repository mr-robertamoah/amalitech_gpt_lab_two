# System Resource Monitor

This Python module monitors system resource usage including CPU, RAM, and disk space. It sends an email alert if any of the monitored metrics exceed predefined thresholds.

## Features

- Monitors CPU usage, RAM usage, and disk free space.
- Sends email alerts when thresholds are exceeded.
- Configurable via environment variables for email settings.

## Usage

1. Set the required environment variables:

```bash
export FROM_EMAIL="your-email@gmail.com"
export TO_EMAIL="recipient-email@example.com"
export GMAIL_APP_PASSWORD="your-gmail-app-password"
```

On Windows Command Prompt, use:

```cmd
set FROM_EMAIL=your-email@gmail.com
set TO_EMAIL=recipient-email@example.com
set GMAIL_APP_PASSWORD=your-gmail-app-password
```

2. Run the monitor script:

```bash
python monitor.py
```

## System Thresholds

The following thresholds are set in the script:

- CPU usage threshold: 2%
- RAM usage threshold: 10%
- Disk free space threshold: 50% (alerts if free space is below this)

You can modify these thresholds by editing the constants in the `monitor.py` file:

```python
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50
```

## Environment Variables

The script requires the following environment variables to be set for sending email alerts:

- `FROM_EMAIL`: The email address from which alerts will be sent.
- `TO_EMAIL`: The recipient email address for alerts.
- `GMAIL_APP_PASSWORD`: The Gmail app password for the sender email account. (Use an app-specific password if 2FA is enabled.)

## Notes

- The script uses Gmail's SMTP server (`smtp.gmail.com`) on port 587 with TLS.
- Ensure that the Gmail account used for sending emails has "App Passwords" enabled if two-factor authentication is active.
- The script prints a message if all system metrics are within normal limits.

## Example

```bash
export FROM_EMAIL="sender@gmail.com"
export TO_EMAIL="admin@example.com"
export GMAIL_APP_PASSWORD="abcd-efgh-ijkl-mnop"
python monitor.py
```

## License

This project is provided as-is without any warranty.
