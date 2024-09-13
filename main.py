import argparse
from jira_functions import get_projects, get_project_details, create_project

def main():
    parser = argparse.ArgumentParser(description="Jira Projects CLI")
    parser.add_argument('-gpa', '--get_all_projects', action='store_true', help='Get all Jira projects')
    parser.add_argument('-gp', '--get_project', type=str, help='Get details of a Jira project by key')
    
    # Group for creating a project
    create_group = parser.add_argument_group('create_project', 'Arguments for creating a new project')
    create_group.add_argument('--cp', action='store_true', help='Create a new Jira project')
    create_group.add_argument('--key', type=str, help='Key for the new project')
    create_group.add_argument('--name', type=str, help='Name of the new project')
    create_group.add_argument('--project-type-key', type=str, help='Project type key for the new project')
    create_group.add_argument('--leadid', type=str, help='Lead account ID for the new project')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    elif args.get_all_projects:
        get_projects()
    elif args.get_project:
        get_project_details(args.get_project)
    elif args.cp:
        if args.key and args.name and args.project_type_key and args.leadid:
            create_project(args.key, args.name, args.project_type_key, args.leadid)
        else:
            print("Missing arguments for creating a project. Please provide --key, --name, --project-type-key, and --leadid.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()