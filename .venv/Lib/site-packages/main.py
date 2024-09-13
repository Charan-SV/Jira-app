# main.py
import argparse
from jira_functions import get_projects, get_project_details

def main():
    parser = argparse.ArgumentParser(description="Jira Projects CLI")
    parser.add_argument('-gpa', '--get_all_projects', action='store_true', help='Get all Jira projects')
    parser.add_argument('-gp', '--get_project', type=str, help='Get details of a Jira project by key')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    elif args.get_all_projects:
        get_projects()
    elif args.get_project:
        get_project_details(args.get_project)

if __name__ == "__main__":
    main()
