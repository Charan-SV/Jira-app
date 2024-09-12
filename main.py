# main.py
import argparse
from jira_functions import get_projects

def main():
    parser = argparse.ArgumentParser(description="Jira Projects CLI")
    parser.add_argument('-gpa', '--get_all_projects', action='store_true', help='Get Jira projects')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    elif args.get_all_projects:
        get_projects()

if __name__ == "__main__":
    main()
