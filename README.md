# Automated Email Sender using Monday.com and SendGrid
This project automates sending emails by integrating Monday.com and SendGrid. It retrieves email addresses and corresponding content from a specified Monday.com board and sends personalized emails using the SendGrid API. The script can be scheduled to run every 4 hours from Monday to Friday using Railway CI/CD.

# Features
* Data Retrieval: Extracts email addresses and content from a Monday.com board.
* Email Sending: Uses the SendGrid API to send personalized emails.
* Scheduling: Configurable to run on a schedule with Railway CI/CD.

# Configuration
* Monday.com API Key: Update MONDAY_API_KEY in the script.
* Board ID: Update BOARD_ID with your Monday.com board ID.
* SendGrid API Key: Update SENDGRID_API_KEY in the script.
* Verified Sender Email: Replace "your_verified_sendgrid_email@example.com" with your verified SendGrid sender email.

# Deployment
Includes a railway.toml configuration for deployment and scheduling on Railway CI/CD.
