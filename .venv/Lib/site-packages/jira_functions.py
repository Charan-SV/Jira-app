# jira_functions.py
import requests
import json
from requests.auth import HTTPBasicAuth
from tabulate import tabulate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_projects():
    url = "https://charan-s-v.atlassian.net/rest/api/3/project/search"
    auth = HTTPBasicAuth("charanv@devtools.in", os.getenv("JIRA_API_TOKEN")) 
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, auth=auth, headers=headers)
    projects = json.loads(response.text).get('values', [])
    
    # Prepare the data for tabulate
    table_data = [["Name", "Key"]]
    for project in projects:
        table_data.append([project.get('name'), project.get('key')])
    
    # Print the table
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

def get_project_details(project_key):
    url = f"https://charan-s-v.atlassian.net/rest/api/3/project/{project_key}"
    auth = HTTPBasicAuth("charanv@devtools.in", os.getenv("JIRA_API_TOKEN")) 
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, auth=auth, headers=headers)
    project = json.loads(response.text)
    
    # Prepare the data for tabulate
    table_data = [
        ["Field", "Value"],
        ["Name", project.get('name')],
        ["Key", project.get('key')],
        ["Project Type", project.get('projectTypeKey')],
        ["Lead", project.get('lead', {}).get('displayName')],
        ["Roles", ", ".join([role for role in project.get('roles', {}).keys()])],
        ["Issue Types", ", ".join([issue_type.get('name') for issue_type in project.get('issueTypes', [])])],
        ["Components", ", ".join([component.get('name') for component in project.get('components', [])])],
        ["Versions", ", ".join([version.get('name') for version in project.get('versions', [])])],
    ]
    
    # Print the table
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))