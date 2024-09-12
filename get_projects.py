import argparse
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

def main():
    parser = argparse.ArgumentParser(description="Jira Projects CLI")
    parser.add_argument('-gp', '--get-projects', action='store_true', help='Get Jira projects')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    elif args.get_projects:
        get_projects()

if __name__ == "__main__":
    main()
