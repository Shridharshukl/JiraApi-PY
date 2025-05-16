# 🚀 JIRA ISSUE CREATOR VIA GITHUB WEBHOOK

This project provides a lightweight Flask-based API that listens for GitHub webhook events  
(specifically issue comments) and **automatically creates corresponding Jira issues** using  
the Jira REST API.

---

## ✨ FEATURES

- 📥 Listens to GitHub webhook payloads via a Flask endpoint.
- 📝 Detects `/JIRA` command in issue comments to trigger Jira issue creation.
- 🔍 Extracts key data (title, author, comment, etc.) from the GitHub event.
- 🧩 Modular structure with `jira_api.py` handling all Jira API interactions.

---

## 📁 PROJECT STRUCTURE

```
cd Flask_APP
app.py     # Flask app to receive GitHub webhooks
jiraAPI.py           # Jira integration logic using REST API
```

---

## ⚙️ SETUP INSTRUCTIONS

1. **Clone the Repository:**
   ```sh
   git clone [Link](https://github.com/Shridharshukl/JiraApi-PY.git)
   cd jiraApi-PY
   ```

2. **Install Dependencies** *(recommended: virtual environment)*:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install flask requests
   ```

3. **Configure Jira Credentials:**

   Open `jira_api.py` and update the following:
   ```python
   Email = "your_email"
   ApiToken = "your_api_token"
   baseurl = "your-domain.atlassian.net"
   ```

   ⚠️ **IMPORTANT:**  
   Do **NOT** hardcode credentials in production.  
   Use environment variables or a secrets manager instead.

---

## ▶️ USAGE

1. **Run the Flask API:**
   ```sh
   python3 app.py
   ```
   The API will start on: [http://0.0.0.0:5000](http://0.0.0.0:5000)

2. **Set Up GitHub Webhook:**
   - Go to your GitHub repository → ⚙️ **Settings** → **Webhooks**
   - Click **Add webhook** and set:
     - **Payload URL:** `http://your-server-ip:5000/jira`
     - **Content type:** `application/json`
     - **Events:** Issue comments (or custom)

3. **Trigger Jira Issue Creation:**
   - Post a comment on a GitHub issue starting with `/JIRA` (case-insensitive)

   **Example:**
   ```
   /JIRA This bug must be fixed immediately.
   ```

   The Flask API will parse the comment and send a request to Jira to create a new issue.

---

## 📝 EXAMPLE

**GitHub Comment:**
```
/JIRA This is a bug that needs to be fixed ASAP.
```

**Created Jira Issue:**
- **Summary:** GitHub issue title + comment count
- **Description:** Includes GitHub username, comment content, timestamp, issue URL

---

## 🔒 SECURITY NOTES

- ❌ **Do NOT hardcode sensitive information in production.**
- 🔑 Use environment variables or secret vaults.
- 🛡️ Protect the `/jira` endpoint using token validation or IP whitelisting.
- 🧹 Always sanitize incoming data to avoid injection attacks.

---

## 📜 LICENSE

This project is licensed under the **MIT License**.

---

## 👤 AUTHOR

**Shridhar Shukla**  
GitHub: [Shridharshukl](https://github.com/Shridharshukl)

---

## 🤝 CONTRIBUTING

Contributions are welcome!  
Please open an issue to discuss improvements or bugs before submitting a pull request.

---
