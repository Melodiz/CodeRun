import argparse
from check_utils import check_topic_id, validate_html_content
from fetch_parse import get_html_content, extract_problem_data
from other_utils import create_solution_files, update_global_readme, update_local_readme
import os
import sys


def main():
    # parse command-line arguments
    arg_parser = argparse.ArgumentParser(description='Add a new CodeRun problem to the repository')
    arg_parser.add_argument('topic_folder', help='Target folder (e.g., ML/Easy)')
    arg_parser.add_argument('problem_id', help='Problem ID from CodeRun (e.g., book-shelf)')

    args = arg_parser.parse_args()
    check_topic_id(args.topic_folder) # will terminate the program if the folder does not exist

    html_content = get_html_content(args.problem_id)
    validate_html_content(html_content) # will terminate the program if the HTML content is empty

    print(f"OK: fetched HTML content for problem {args.problem_id}")
    problem_data = extract_problem_data(html_content, args.problem_id)

    # create a corresponding Folder with description and solution template file
    create_solution_files(args.problem_id, args.topic_folder, problem_data)


    # Update main README.md
    main_readme_path = os.path.join(os.getcwd(), "README.md") 
    update_global_readme(main_readme_path, args.problem_id, args.topic_folder, problem_data)
    
    # Update local readme.md
    local_readme_path = os.path.join(os.getcwd(), args.topic_folder.split('/')[0], "readme.md")
    update_local_readme(local_readme_path, args.problem_id, args.topic_folder, problem_data)

    # Clean the title for the commit message
    title_with_num = f"{problem_data['title_num']}. {args.problem_id}"
    clean_title = title_with_num.replace('_', ' ').replace('-', ' ')
    print("\n Git command shortcut:")
    print(f"git add . && git commit -m \"CodeRun: {clean_title}\" && git push origin main")

    return 0

if __name__ == "__main__":
    sys.exit(main())



