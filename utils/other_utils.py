import os
from check_utils import validate_problem_folder, validate_global_readme, validate_local_readme


def create_solution_files(problem_id, topic_folder, problem_data):
    folder_name = f"{problem_data['title_num']}_{problem_id.replace('-', '_').replace(' ', '_')}"
    folder_path = os.path.join(topic_folder, folder_name)
    validate_problem_folder(folder_path)
    os.makedirs(folder_path)

    # Create description file
    with open(os.path.join(folder_path, "readme.md"), 'w', encoding='utf-8') as f:
        f.write(problem_data['description_text'])
    # Create empty solution file
    solution_path = os.path.join(folder_path, "solution.py")
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(f"# Solution for {problem_data['problem_link']}\n")
        f.write(f"# Other solutions: https://github.com/Melodiz/CodeRun\n\n")
        f.write("def main():\n")
        f.write("    pass\n\n")
        f.write("if __name__ == \"__main__\":\n")
        f.write("    main()\n")
    print(f"OK: created problem folder with files")


def update_global_readme(readme_path, problem_id, topic_folder, problem_data):
    validate_global_readme(readme_path)

    # Read the current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    main_category = topic_folder.split('/')[0]  # 'ML', 'Algorithms', etc.
    # 'Easy', 'Medium', etc.
    difficulty = topic_folder.split(
        '/')[1] if len(topic_folder.split('/')) > 1 else ""

    # Find the appropriate section in the README
    section_marker = f"## {difficulty} <a name=\"{main_category.lower()}-{difficulty.lower()}\"></a>"
    if section_marker not in content:
        print(f"ERROR: section {section_marker} not found in {readme_path}")
        print("Global README.md wasn't updated.")
        return

    title_with_num = f"{problem_data['title_num']}. {problem_data['title']}"
    tags_str = f" [{', '.join(problem_data['tags'])}]" if \
        (problem_data['tags'] and len(problem_data['tags']) > 0) else ""

    folder_name = f"{problem_data['title_num']}_{problem_id.replace('-', '_').replace(' ', '_')}"
    solution_path = f"{topic_folder}/{folder_name}"

    new_entry = f"* [{title_with_num}]({problem_data['problem_link']}){tags_str} - [Solution]({solution_path})\n"

    # Find the position to insert the new entry
    section_pos = content.find(section_marker)
    next_section_pos = content.find("##", section_pos + len(section_marker))

    if next_section_pos == -1:
        # If this is the last section, find the next major section
        next_section_pos = content.find(
            "# ", section_pos + len(section_marker))

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
        new_content = content[:section_pos + len(section_marker)] + \
            "\n\n" + new_entry + content[section_pos + len(section_marker):]
    else:
        # Add after the last entry
        absolute_pos = section_pos + last_entry_pos
        line_end = content.find("\n", absolute_pos)
        if line_end == -1:
            line_end = len(content)

        new_content = content[:line_end + 1] + \
            new_entry + content[line_end + 1:]
        # Write the updated content back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"OK: updated global readme.md with new problem entry")
    return new_entry


def update_local_readme(readme_path, problem_id, topic_folder, problem_data):
    validate_local_readme(readme_path)

    # Read the current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    main_category = topic_folder.split('/')[0]  # 'ML', 'Algorithms', etc.
    # 'Easy', 'Medium', etc.
    difficulty = topic_folder.split(
        '/')[1] if len(topic_folder.split('/')) > 1 else ""

    # Find the appropriate section in the README
    section_marker = f"## {difficulty}"
    if section_marker not in content:
        print(f"ERROR: section {section_marker} not found in {readme_path}")
        print("Local README.md wasn't updated.")
        return

    title_with_num = f"{problem_data['title_num']}. {problem_data['title']}"
    tags_str = f" [{', '.join(problem_data['tags'])}]" if problem_data['tags'] \
        and len(problem_data['tags']) > 0 else ""

    folder_name = f"{problem_data['title_num']}_{problem_id.replace('-', '_').replace(' ', '_')}"
    solution_path = f"{topic_folder}/{folder_name}"

    new_entry = f"* [{title_with_num}]({problem_data['problem_link']}){tags_str} - [Solution]({solution_path})\n"

    # Find the position to insert the new entry
    section_pos = content.find(section_marker)
    next_section_pos = content.find("##", section_pos + len(section_marker))

    if next_section_pos == -1:
        # If this is the last section, find the next major section
        next_section_pos = content.find(
            "# ", section_pos + len(section_marker))

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
        new_content = content[:section_pos + len(section_marker)] + \
            "\n\n" + new_entry + content[section_pos + len(section_marker):]
    else:
        # Add after the last entry
        absolute_pos = section_pos + last_entry_pos
        line_end = content.find("\n", absolute_pos)
        if line_end == -1:
            line_end = len(content)

        new_content = content[:line_end + 1] + \
            new_entry + content[line_end + 1:]
        # Write the updated content back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"OK: updated local readme.md with new problem entry")
    return new_entry
