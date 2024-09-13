# Jira-app

## Description

This application interacts with the Jira API to fetch and display project information. It uses command-line arguments to trigger different functionalities.

## Requirements

- Python 3.x
- `requests` library
- `tabulate` library
- `python-dotenv` library

You can install the required libraries using:

```sh
pip install requests tabulate python-dotenv
```


## Installation

To install the application, navigate to the directory containing the [`setup.py`](vscode-file://vscode-app/c:/Users/Charana%20S%20V/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) file and run:


**``pip install .``**

This will install the application and make the `jira` command available.

## Usage

To use the application, you can now use the `jira` command:

**jira** **--get-projects**

### Arguments

* `-gpa` or `--get-projects`: Fetches and displays the list of projects from Jira.

**jira** **--get-projects**

This will output a table of projects with their names and keys.

* `-gp` or `--project-details <project_key>`: Fetches and displays details of a specific project.

**jira** **--project-details** **PROJECT_KEY**

* `-cp` or `--create-project --key <key> --name <name> --project_type_key <project_type_key> --leadid <lead_account_id>`: Creates a new project in Jira.
  ```
  jira --create-project --key KEY --name NAME --project_type_key PROJECT_TYPE_KEY --leadid LEAD_ACCOUNT_ID
  ```

## Environment Variables

Ensure you have a [`.env`](vscode-file://vscode-app/c:/Users/Charana%20S%20V/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) file in the root directory 

**JIRA_API_TOKEN="your_jira_api_token_here"**

**This update includes instructions for installing t**he application using `pip install .` and using the** `jira` command for various functionalities, all f**ormatted in Markdown.
