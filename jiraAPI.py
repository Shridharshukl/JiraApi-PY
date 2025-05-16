import requests
from requests.auth import HTTPBasicAuth
import json

# Use environment variables for credentials
Email = "your_email"
ApiToken = "your_api_token"
baseurl = "your_baseurl.atlassian.net"

url = f"https://{baseurl}/rest/api/2/issue"
auth = HTTPBasicAuth(Email, ApiToken)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

projectID = "SCRUM"
issueID = 10005 #bug ID

def create_issue(d, i, c):
    payload = {
        "fields": {
            "project": {
                "key": projectID
            },
            "issuetype": {
                "id": issueID
            },
            "summary": i + "  issueNo: " + str(c),
            "description": d
        }
    }

    response = requests.post(
        url,
        headers=headers,
        auth=auth,
        json=payload
    )

    r = json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": "))
    print("<<<<<<<<======= succees ======>>>>>>>>")
    return r

if __name__ == "__main__":
   print(create_issue("desc", "title", 1))
