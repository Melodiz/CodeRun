import re

def add_problem_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regular expression to match problem entries
    pattern = r'(\* \[)([^]]*?)(\]\(https://coderun\.yandex\.ru/problem/.*?/\) \[.*?\] - \[Solution\]\((?:Easy|Medium|Hard|autumn_intern_23)/(\d+)_.*?\))'
    
    def replace_match(match):
        prefix = match.group(1)
        title = match.group(2)
        suffix = match.group(3)
        problem_number = match.group(4)
        
        # Check if the title already starts with the number
        if not re.match(r'^\d+\.\s', title):
            new_title = f"{problem_number}. {title}"
            return f"{prefix}{new_title}{suffix}"
        return match.group(0)
    
    # Replace all matches
    updated_content = re.sub(pattern, replace_match, content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Problem numbers added to titles in {file_path}")

def fix_folder_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content into sections
    ml_section = re.search(r'# ML Problem List.*?(?=---)', content, re.DOTALL)
    algo_section = re.search(r'# Problem List Algorithms.*?(?=---)', content, re.DOTALL)
    intern_section = re.search(r'# Problem List - autumn_intern_23.*?(?=$|\Z)', content, re.DOTALL)
    
    if ml_section:
        ml_content = ml_section.group(0)
        # Fix paths in ML section: Easy/ -> ML/Easy/
        updated_ml_content = re.sub(
            r'(\[Solution\]\()(Easy|Medium|Hard)/', 
            r'\1ML/\2/', 
            ml_content
        )
        content = content.replace(ml_content, updated_ml_content)
    
    if algo_section:
        algo_content = algo_section.group(0)
        # Fix paths in Algorithms section: Easy/ -> Algorithms/Easy/
        updated_algo_content = re.sub(
            r'(\[Solution\]\()(Easy|Medium)/', 
            r'\1Algorithms/\2/', 
            algo_content
        )
        content = content.replace(algo_content, updated_algo_content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Folder paths fixed in {file_path}")

if __name__ == "__main__":
    readme_path = "README.md"  # Path to your README.md file
    fix_folder_paths(readme_path)
    # add_problem_numbers(readme_path)