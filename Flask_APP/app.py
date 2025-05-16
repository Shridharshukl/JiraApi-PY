from flask import Flask, request
import jiraAPI as jira 

app = Flask(__name__)

@app.route('/jira', methods=['POST'])
def hello_world():
    m = request.get_json()
    issue_title = m["issue"]["title"]
    comment_no = str(m["issue"]["comments"])
    user = m["comment"]["user"]["login"]
    create_date = m["comment"]["created_at"]
    url = m["issue"]["html_url"]
    mt = m["comment"]["body"].split(" ")

    # Check if the first word is "/JIRA"    
    if not mt or mt[0].upper() != "/JIRA": # Check if the first word is "/JIRA"
        print("<<<<<<<<======= CLOSED => Not a JIRA command ======>>>>>>>>")
        return ""
    else:
        mess = mt[1:] # Exclude the first word
        comment = " ".join(mess) # Join the rest of the words
        description = (
            f"Issue created from GitHub webhook\n"
            f"User: {user}\n"
            f"Created at: {create_date}\n"
            f"Comment: {comment}\n"
            f"Reactions URL: {url}\n"
        )
        return jira.create_issue(description, issue_title, comment_no)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)