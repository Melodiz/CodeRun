import os
import sys
def check_topic_id(topic_id):
    # Validate topic_folder
    if not os.path.exists(topic_id):
        print(f"ERROR: Topic folder '{topic_id}' does not exist")
        sys.exit(1)

def validate_html_content(html_content):
    if not html_content: 
        print('ERROR: Empty HTML content was provided to validate_html_content')
        sys.exit(1)

def validate_problem_folder(problem_folder):
    if os.path.exists(problem_folder):
        print(f"ERROR: Problem folder '{problem_folder}' already exists")
        sys.exit(1)

def validate_global_readme(readme_path):
    if not os.path.exists(readme_path):
        print(f"ERROR: Global README.md file does not exist at {readme_path}")
        sys.exit(1)

def validate_local_readme(readme_path):
    if not os.path.exists(readme_path):
        print(f"ERROR: Local README.md file does not exist at {readme_path}")
        sys.exit(1)