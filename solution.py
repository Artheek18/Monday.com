import requests
import json
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

# Replace with your Monday.com API key
MONDAY_API_KEY = ''
BOARD_ID = ''

# Replace with your SendGrid API key
SENDGRID_API_KEY = ''
# The GraphQL endpoint for Monday.com
MONDAY_URL = 'https://api.monday.com/v2'

# GraphQL query to fetch items from the board
query = """
{
  boards(ids: %s) {
    items_page(limit: 500) {
      items {
        id
        name
        column_values {
          column {
            title
          }
          text
        }
      }
    }
  }
}
""" % BOARD_ID

# Headers for Monday.com request
monday_headers = {
    "Authorization": f"Bearer {MONDAY_API_KEY}",
    "Content-Type": "application/json"
}

def fetch_board_data():
    response = requests.post(MONDAY_URL, json={'query': query}, headers=monday_headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data with status code {response.status_code}")
        print(response.json())
        return None

def send_email(to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email("your_verified_sendgrid_email@example.com")  # Replace with your verified sender email
    to_email_obj = To(to_email)  # Create To object
    content = Content("text/plain", content)
    mail = Mail(from_email, to_email_obj, subject, content)
    try:
        response = sg.send(mail)
        print(f"Email sent to {to_email} with status code {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")

def process_board_data(data):
    if data:
        items = data.get('data', {}).get('boards', [{}])[0].get('items_page', {}).get('items', [])
        for item in items:
            email = None
            email_content = None
            for column in item.get('column_values', []):
                if column.get('column', {}).get('title') == 'Email':
                    email = column.get('text')
                elif column.get('column', {}).get('title') == 'Email Content':
                    email_content = column.get('text')
            
            if email and email_content:
                send_email(email, "Your Subject Here", email_content)
            else:
                print(f"Missing email or content for item {item.get('id')}")

if __name__ == "__main__":
    board_data = fetch_board_data()
    process_board_data(board_data)

"""
# railway.toml

[deploy]
  # Define the schedule for the deployment
  schedule = "0 */4 * * 1-5" # This schedules the script to run every 4 hours Monday through Friday

# If you need to specify any environment variables for your deployment
[env]
  MONDAY_API_KEY = "your_monday_api_key_here"
  SENDGRID_API_KEY = "your_sendgrid_api_key_here"
  BOARD_ID = "your_board_id_here"

# Additional configuration options can be added as needed
"""







