import argparse
import requests
from requests.auth import HTTPBasicAuth
import json
from tabulate import tabulate

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
        auth = HTTPBasicAuth("charanv@devtools.in", "ATATT3xFfGF06Ta38Jx42fFHq2keq2fXYoa-iykLbW5c3FeYTSFNeKdXs5yOSeq5DqUJOVCI-TqCSCh5qmImor3xefctHQGqUo06-fVHm2FrV5h3_wish_PiptldbJw9zwAyR5P_Ep0mQRQeK8ix7awjf7v_Y1EHoibWEz3NIFV5L7tvJL0KU_I=F2B549A4")
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
        
        # Prepare the data for tabulate
        table_data = [["Name", "Key"]]
        for project in projects:
            table_data.append([project.get('name'), project.get('key')])
        
        # Print the table
        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    else:
        # Print the default message
        print('[DEFAULT]: DEFAULT')
