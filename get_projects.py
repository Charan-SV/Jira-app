import argparse
import requests
from requests.auth import HTTPBasicAuth
import json

# Create the argument parser
parser = argparse.ArgumentParser(
    prog='Jira app',
    description='''#This is going to be our desc...''',
    epilog='copyright (c) 2020 Devtotls Jira app'
)

# Add the --get-projects argument as a flag
parser.add_argument('-gp', '--get-projects', action='store_true', help='this is the help of this add_argument')

# Parse the arguments
args = parser.parse_args()

# Check if no arguments are provided
if not any(vars(args).values()):
    parser.print_help()
else:
    # Check if the --get-projects flag is set
    if args.get_projects:
        # Define the URL and authentication
        url = "https://charan-s-v.atlassian.net/rest/api/3/project/search"
        auth = HTTPBasicAuth("charanv@devtools.in", "ATATT3xFfGF0bISEkv0NaZgJZ6w3uDw1mHjD9rb6BHYqxMIpqs1RcF1OAY7f7L_cxNOOvda2-A9Rb-SFGdWSyV6RKRp8Oksv_AJQSc7NXR3SWetMOzgdJrwPAw6oIzUj-jltLQ9mY4PpKWZN9lMrid7pEqRhM-89kVYFkqKhElwF5mYL8FTfaOc=48B9B27A")
        headers = {
            "Accept": "application/json"
        }
        
        # Make the GET request
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )
        
        # Parse the JSON response
        projects = json.loads(response.text).get('values', [])
        
        # Print the project names
        for project in projects:
            print(project.get('name'))
    else:
        # Print the default message
        print('[DEFAULT]: DEFAULT')
