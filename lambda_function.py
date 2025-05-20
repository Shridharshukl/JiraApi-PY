import json
import requests  # Make sure requests module is zipped & uploaded as layer
from requests.auth import HTTPBasicAuth
import os
import boto3 

# Initialize SSM client
ssm = boto3.client('ssm')

# Function to get the API token from SSM Parameter Store
def get_api_token():
    response = ssm.get_parameter(
        Name='/jira/apiToken',
        WithDecryption=True
    )
    return response['Parameter']['Value']

# Load other configuration from environment variables
Email = os.environ['EMAIL']
ApiToken = get_api_token()
baseurl = os.environ['baseurl']
projectID = "SCRUM"
issueID = 10005

auth = HTTPBasicAuth(Email, ApiToken)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def create_issue(d, i, c):
    payload = {
        "fields": {
            "project": {"key": projectID},
            "issuetype": {"id": issueID},
            "summary": i + "  issueNo: " + str(c),
            "description": d
        }
    }

    response = requests.post(
        f"https://{baseurl}/rest/api/2/issue",
        headers=headers,
        auth=auth,
        json=payload
    )

    if response.status_code == 201:
        print("<<<<<<======= success ======>>>>>>>>")
    else:
        print("<<<<<<======= failed ======>>>>>>>>")
        print(response.text)

    return json.dumps(response.json(), indent=2)

def lambda_handler(event, context):
    m = event
    issue_title = m["issue"]["title"]
    comment_no = str(m["issue"]["comments"])
    user = m["comment"]["user"]["login"]
    create_date = m["comment"]["created_at"]
    url = m["issue"]["html_url"]
    mt = m["comment"]["body"].split(" ")

    if not mt or mt[0].upper() != "/JIRA":
        print("<<<<<<======= Not a JIRA command ======>>>>>>>>")
        return {'statusCode': 200, 'body': json.dumps("Not a JIRA command")}

    comment = " ".join(mt[1:])
    description = (
        f"Issue created from GitHub webhook\n"
        f"User: {user}\n"
        f"Created at: {create_date}\n"
        f"Comment: {comment}\n"
        f"Reactions URL: {url}\n"
    )

    response = create_issue(description, issue_title, comment_no)

    return {
        'statusCode': 200,
        'body': response
    }
