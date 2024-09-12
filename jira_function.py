# jira_functions.py
import requests
from requests.auth import HTTPBasicAuth
import json
from tabulate import tabulate

def get_projects():
    url = "https://charan-s-v.atlassian.net/rest/api/3/project/search"
    auth = HTTPBasicAuth("charanv@devtools.in", "Token")
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
