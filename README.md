# Jira-app

## Description
This application interacts with the Jira API to fetch and display project information. It uses command-line arguments to trigger different functionalities.

## Requirements
- Python 3.x
- `requests` library
- `tabulate` library

You can install the required libraries using:
```sh
pip install requests tabulate
```

Usage
To use the application, navigate to the directory containing get_projects.py and run the following command:

```sh
python get_projects.py --get-projects
```
Arguments
-gp or --get-projects: Fetches and displays the list of projects from Jira.
```sh
python get_projects.py --get-projects
```
This will output a table of projects with their names and keys.
