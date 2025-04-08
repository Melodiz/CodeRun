import os
import sys
import re
import argparse
from parser import get_problem_info

def extract_problem_num(title, html_content=None):
    """
    Extract problem number from the title or HTML content
    
    Args:
        title (str): Problem title
        html_content (str): HTML content of the problem page
        
    Returns:
        str: Problem number (e.g., '404', '123')
    """
    # Try to find a number at the beginning of the title
    match = re.search(r'^(\d+)\.', title)
    if match:
        return match.group(1)
    
    # If HTML content is provided, try to find the number in the HTML
    if html_content:
        # Look for patterns like "101. Поиск цикла" where "Поиск цикла" is the title
        clean_title = re.escape(title.strip())
        pattern = r'(\d+)\.\s*' + clean_title
        match = re.search(pattern, html_content)
        if match:
            return match.group(1)
    
    # If not found, generate a random number (for testing purposes)
    import random
    print("Failed to extract problem number. Generating random number for testing... 100-999...")
    return str(random.randint(100, 999))

def create_problem_folder(problem_id, topic_folder):
    """
    Create a new problem folder with description and solution files
    
    Args:
        problem_id (str): Problem ID from CodeRun (e.g., 'book-shelf')
        topic_folder (str): Target folder (e.g., 'ML/Easy')
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Fetch problem info from CodeRun
    print(f"Fetching problem info for {problem_id}...")
    info = get_problem_info(problem_id)
    
    if "Error" in info['title']:
        print(f"Error: Could not fetch problem info for {problem_id}")
        return False
    
    # Extract problem number from title and HTML content
    problem_num = extract_problem_num(info['title'], info.get('html_content', ''))
    
    # Create folder name: problem_num_problem_id
    folder_name = f"{problem_num}_{problem_id.replace('-', '_')}"
    folder_path = os.path.join(topic_folder, folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
    
    # Create description.md file
    desc_path = os.path.join(folder_path, "description.md")
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(f"# {info['title']}\n\n")
        f.write(f"Problem ID: {problem_id}\n\n")
        f.write(f"URL: {info['url']}\n\n")
        if info['tags']:
            f.write(f"Tags: {', '.join(info['tags'])}\n\n")
        f.write(info['description'])
    
    print(f"Created description file: {desc_path}")
    
    # Create empty solution file
    solution_path = os.path.join(folder_path, "solution.py")
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(f"# Solution for {info['url']}\n\n")
        f.write("def solution():\n")
        f.write("    # Your solution here\n")
        f.write("    pass\n\n")
        f.write("if __name__ == \"__main__\":\n")
        f.write("    solution()\n")
    
    print(f"Created solution file: {solution_path}")
    
    # Update README.md
    update_readme(info, problem_id, topic_folder, folder_name)
    
    return True
def update_readme(info, problem_id, topic_folder, folder_name):
    """
    Update the main README.md file with the new problem
    
    Args:
        info (dict): Problem information
        problem_id (str): Problem ID
        topic_folder (str): Target folder
        folder_name (str): Created folder name
    """
    # Update main README.md
    main_readme_path = os.path.join(os.getcwd(), "README.md")
    update_specific_readme(main_readme_path, info, problem_id, topic_folder, folder_name)
    
    # Update local readme.md
    topic_parts = topic_folder.split('/')
    main_category = topic_parts[0]  # 'ML', 'Algorithms', etc.
    local_readme_path = os.path.join(os.getcwd(), main_category, "readme.md")
    
    if os.path.exists(local_readme_path):
        update_specific_readme(local_readme_path, info, problem_id, topic_folder, folder_name, is_local=True)
    else:
        print(f"Warning: Local readme.md not found at {local_readme_path}")

def update_specific_readme(readme_path, info, problem_id, topic_folder, folder_name, is_local=False):
    """
    Update a specific README.md file with the new problem
    
    Args:
        readme_path (str): Path to the README.md file
        info (dict): Problem information
        problem_id (str): Problem ID
        topic_folder (str): Target folder
        folder_name (str): Created folder name
        is_local (bool): Whether this is a local readme (affects path in entry)
    """
    if not os.path.exists(readme_path):
        print(f"Warning: README file not found at {readme_path}")
        return
    
    # Read the current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine which section to update based on topic_folder
    topic_parts = topic_folder.split('/')
    main_category = topic_parts[0]  # 'ML', 'Algorithms', etc.
    difficulty = topic_parts[1] if len(topic_parts) > 1 else ""  # 'Easy', 'Medium', etc.
    
    # Find the appropriate section in the README
    section_marker = f"## {difficulty} <a name=\"{main_category.lower()}-{difficulty.lower()}\"></a>"
    
    # For local readme, the section marker might be different
    if is_local:
        section_marker = f"## {difficulty}"
    
    if section_marker not in content:
        print(f"Warning: Section {section_marker} not found in {readme_path}")
        return
    
    # Extract problem number from folder name
    problem_num = folder_name.split('_')[0]
    
    # Create the new entry line with problem number in the title
    # Check if the title already starts with the problem number
    if re.match(r'^\d+\.', info['title']):
        title_with_num = info['title']
    else:
        title_with_num = f"{problem_num}. {info['title']}"
    
    tags_str = f" [{', '.join(info['tags'])}]" if info['tags'] else ""
    
    # Adjust the solution path based on whether this is a local readme
    if is_local:
        # For local readme, use relative path from the category folder
        solution_path = f"{difficulty}/{folder_name}"
    else:
        # For main readme, use the full path
        solution_path = f"{topic_folder}/{folder_name}"
    
    new_entry = f"* [{title_with_num}]({info['url']}){tags_str} - [Solution]({solution_path})\n"
    
    # Find the position to insert the new entry
    section_pos = content.find(section_marker)
    next_section_pos = content.find("##", section_pos + len(section_marker))
    
    if next_section_pos == -1:
        # If this is the last section, find the next major section
        next_section_pos = content.find("# ", section_pos + len(section_marker))
    
    if next_section_pos == -1:
        # If still not found, append to the end
        insert_pos = len(content)
    else:
        # Insert before the next section
        insert_pos = next_section_pos
    
    # Find the last entry in the current section
    section_content = content[section_pos:insert_pos]
    last_entry_pos = section_content.rfind("* [")
    
    if last_entry_pos == -1:
        # No entries yet, add after the section marker
        new_content = content[:section_pos + len(section_marker)] + "\n\n" + new_entry + content[section_pos + len(section_marker):]
    else:
        # Add after the last entry
        absolute_pos = section_pos + last_entry_pos
        line_end = content.find("\n", absolute_pos)
        if line_end == -1:
            line_end = len(content)
        
        new_content = content[:line_end + 1] + new_entry + content[line_end + 1:]
    
    # Write the updated content back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    readme_type = "local" if is_local else "main"
    print(f"Updated {readme_type} README with new problem entry: {title_with_num}")
def main():
    """
    Main function to parse command line arguments and create a new problem
    """
    parser = argparse.ArgumentParser(description='Add a new CodeRun problem to the repository')
    parser.add_argument('topic_folder', help='Target folder (e.g., ML/Easy)')
    parser.add_argument('problem_id', help='Problem ID from CodeRun (e.g., book-shelf)')
    
    args = parser.parse_args()
    
    # Validate topic_folder
    if not os.path.exists(args.topic_folder):
        print(f"Error: Topic folder '{args.topic_folder}' does not exist")
        return 1
    
    # Create the problem folder and files
    success = create_problem_folder(args.problem_id, args.topic_folder)
    
    if success:
        print(f"Successfully added problem {args.problem_id} to {args.topic_folder}")
        return 0
    else:
        print(f"Failed to add problem {args.problem_id}")
        return 1

if __name__ == "__main__":
    sys.exit(main())