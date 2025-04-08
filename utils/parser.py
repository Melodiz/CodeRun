import os
import requests
from bs4 import BeautifulSoup
import json
import time
import re

def is_russian_text(text):
    """
    Check if text contains Russian characters
    
    Args:
        text (str): Text to check
        
    Returns:
        bool: True if text contains Russian characters, False otherwise
    """
    # Russian Unicode range: 0x0400-0x04FF
    return bool(re.search('[\u0400-\u04FF]', text))

def process_tags(tags_list):
    """
    Process tags list:
    1. Remove Russian tags
    2. Split combined tags (e.g., "binary search treedynamic programming")
    
    Args:
        tags_list (list): List of raw tags
        
    Returns:
        list: Processed tags list
    """
    # Complete set of known tags
    known_tags = {
        "ad hoc", "advanced js", "algorithms", "asynchrony", "bfs", "binary search", 
        "binary search tree", "bitwise operation", "browser", "brute force", "closure", 
        "code handling", "combinatorics", "constructive", "counting", "crypto", "css", 
        "data structures", "debugging", "deque", "dfs", "dict", "dynamic programming", 
        "dynamic programming 1D", "dynamic programming 2D", "find bugs in the code", 
        "game theory", "geometry", "graph theory", "greedy", "gustokashin", "heap", 
        "http", "implementation", "infrastructure", "intervals intersection", "json", 
        "line handling", "linear search", "machine learing", "math", "number theory", 
        "parsing", "prefix sum", "probabilty theory", "queque", "react", "regular expressions", 
        "scanline", "set", "sliding window", "sort", "sql", "stack", "standard library", 
        "statistics", "std", "strings", "topsort", "tree", "two pass", "two pointers", 
        "verstka", "web api", "work with DOM"
    }
    
    processed_tags = []
    
    for tag in tags_list:
        # Skip Russian tags
        if is_russian_text(tag):
            continue
        
        # Convert to lowercase for better matching
        tag_lower = tag.lower()
        
        # Check if this is a combined tag that needs splitting
        found_tags = []
        
        # Try to find known tags within this tag
        for known_tag in sorted(known_tags, key=len, reverse=True):
            if known_tag in tag_lower:
                found_tags.append(known_tag)
                # Remove the found tag to avoid overlapping matches
                tag_lower = tag_lower.replace(known_tag, " " * len(known_tag))
        
        # If we found known tags, add them
        if found_tags:
            for found_tag in found_tags:
                if found_tag not in processed_tags:
                    processed_tags.append(found_tag)
        # Otherwise, add the original tag if it's not too long (likely not a combined tag)
        elif len(tag) < 30 and not is_russian_text(tag):
            if tag.lower() not in processed_tags:
                processed_tags.append(tag.lower())
    
    return processed_tags

def get_problem_info(problem_id):
    """
    Scrape problem title, description, and tags from coderun.yandex.ru
    
    Args:
        problem_id (str): The problem ID (e.g., 'median-out-of-three')
        
    Returns:
        dict: A dictionary containing 'title', 'description', 'tags', and 'url'
    """
    url = f"https://coderun.yandex.ru/problem/{problem_id}/"
    
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title from the HTML title tag
        title_tag = soup.title
        title = title_tag.text.split('//')[0].strip() if title_tag else "Title not found"
        
        # Extract tags - look for tag elements
        raw_tags = []
        tag_elements = soup.find_all('div', class_=lambda c: c and ('tag' in c.lower() or 'chip' in c.lower()))
        
        if tag_elements:
            for tag_elem in tag_elements:
                tag_text = tag_elem.get_text(strip=True)
                if tag_text and tag_text not in raw_tags:
                    raw_tags.append(tag_text)
        
        # If no tags found with the above method, try another approach
        if not raw_tags:
            # Look for spans that might contain tags
            span_elements = soup.find_all('span', class_=lambda c: c and ('tag' in c.lower() or 'chip' in c.lower()))
            for span in span_elements:
                tag_text = span.get_text(strip=True)
                if tag_text and tag_text not in raw_tags:
                    raw_tags.append(tag_text)
        
        # Process the raw tags to filter out Russian tags and split combined tags
        tags = process_tags(raw_tags)
        
        # Extract description - look for the problem statement content
        description = ""
        
        # Try to find the problem description in the HTML
        # Look for specific elements that might contain the problem description
        description_div = soup.find('div', class_='body-m')
        
        if description_div:
            # Find all section elements within the description div
            sections = description_div.find_all('section')
            
            for section in sections:
                # Get section title if it exists
                section_title = section.find('h2')
                if section_title:
                    description += f"\n## {section_title.text.strip()}\n\n"
                
                # Get all paragraphs in this section
                paragraphs = section.find_all('p')
                for p in paragraphs:
                    description += f"{p.text.strip()}\n\n"
                
                # Get all code snippets in this section
                code_snippets = section.find_all('pre')
                for code in code_snippets:
                    description += f"```\n{code.text.strip()}\n```\n\n"
        
        # If we couldn't extract description using the above method, try a more general approach
        if not description:
            # Try to find any div with class containing "description"
            description_elements = soup.find_all('div', class_=lambda c: c and 'description' in c.lower())
            for elem in description_elements:
                description += elem.get_text(strip=True) + "\n\n"
        
        # If still no description, try to extract from the meta description
        if not description:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc and 'content' in meta_desc.attrs:
                description = meta_desc['content']
        
        return {
            'title': title,
            'description': description,
            'tags': tags,
            'url': url
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching problem {problem_id}: {e}")
        return {
            'title': "Error fetching title",
            'description': f"Error: {str(e)}",
            'tags': [],
            'url': url
        }

def extract_problem_id(folder_name):
    """
    Extract problem ID from folder name by:
    1. Removing the number prefix (e.g., '1_', '7_')
    2. Replacing underscores with hyphens
    
    Args:
        folder_name (str): The folder name (e.g., '1_median_out_of_three')
        
    Returns:
        str: The extracted problem ID (e.g., 'median-out-of-three')
    """
    # Remove the number prefix using regex
    # This matches a number at the beginning followed by an underscore
    without_prefix = re.sub(r'^\d+_', '', folder_name)
    
    # Replace all underscores with hyphens
    problem_id = without_prefix.replace('_', '-')
    
    return problem_id

def find_problem_folders(base_dir='Algorithms/Medium'):
    """
    Find all problem folders in the given directory
    
    Args:
        base_dir (str): The base directory to search in
    
    Returns:
        dict: A dictionary mapping folder names to their problem IDs
    """
    problem_folders = {}
    
    # Check if the directory exists
    if not os.path.exists(base_dir):
        print(f"Directory {base_dir} does not exist.")
        return problem_folders
    
    # List all items in the directory
    for dir_name in os.listdir(base_dir):
        full_path = os.path.join(base_dir, dir_name)
        
        # Check if it's a directory and matches the pattern
        if os.path.isdir(full_path) and re.match(r'^\d+_\w+', dir_name):
            problem_id = extract_problem_id(dir_name)
            problem_folders[full_path] = problem_id
    
    return problem_folders

def main(folder_path='Algorithms/Medium'):
    """
    Main function to process problem folders and generate description files and README.
    
    Args:
        folder_path (str): Path to the folder containing problem directories.
                          Defaults to 'Algorithms/Medium'.
    """
    # Create test directory if it doesn't exist
    test_dir = 'utils/test'
    os.makedirs(test_dir, exist_ok=True)
    
    # Check if command line arguments were provided
    import sys
    if len(sys.argv) > 1:
        # If the argument is a valid directory, use it instead of the parameter
        if os.path.exists(sys.argv[1]) and os.path.isdir(sys.argv[1]):
            folder_path = sys.argv[1]
        # If it's not a directory, treat it as a problem ID
        else:
            problem_id = sys.argv[1]
            print(f"Fetching problem: {problem_id}")
            
            info = get_problem_info(problem_id)
            
            # Create description file in test directory
            desc_path = os.path.join(test_dir, f"{problem_id}_description.md")
            
            with open(desc_path, 'w', encoding='utf-8') as f:
                f.write(f"# {info['title']}\n\n")
                f.write(f"Problem ID: {problem_id}\n\n")
                f.write(f"URL: {info['url']}\n\n")
                if info['tags']:
                    f.write(f"Tags: {', '.join(info['tags'])}\n\n")
                f.write(info['description'])
            
            print(f"Saved description to {desc_path}")
            return
    
    print(f"Processing problems in directory: {folder_path}")
    
    problem_folders = find_problem_folders(folder_path)
    
    if not problem_folders:
        print(f"No problem folders found in {folder_path}. Make sure the directory exists and contains problem folders.")
        return
    
    print(f"Found {len(problem_folders)} problem folders in {folder_path}.")
    
    results = {}
    readme_content = f"# Problem List - {os.path.basename(folder_path)}\n\n"
    
    for i, (folder_path_full, problem_id) in enumerate(problem_folders.items()):
        print(f"Processing {i+1}/{len(problem_folders)}: {folder_path_full} -> {problem_id}")
        
        # Fetch problem info from website
        info = get_problem_info(problem_id)
        
        # Save to results
        results[problem_id] = {
            'folder': folder_path_full,
            'title': info['title'],
            'description': info['description'],
            'tags': info['tags'],
            'url': info['url']
        }
        
        # Create description.md file in the problem folder
        desc_path = os.path.join(folder_path_full, "description.md")
        
        with open(desc_path, 'w', encoding='utf-8') as f:
            f.write(f"# {info['title']}\n\n")
            f.write(f"Problem ID: {problem_id}\n\n")
            f.write(f"URL: {info['url']}\n\n")
            if info['tags']:
                f.write(f"Tags: {', '.join(info['tags'])}\n\n")
            f.write(info['description'])
        
        # Add to README content with links to both web and solution folder
        folder_relative_path = os.path.relpath(folder_path_full, os.path.dirname(os.path.abspath(folder_path)))
        tags_str = f" [{', '.join(info['tags'])}]" if info['tags'] else ""
        readme_content += f"* [{info['title']}]({info['url']}){tags_str} - [Solution]({folder_relative_path})\n"
        
        print(f"  - Saved description to {desc_path}")
        
        # Add a small delay to avoid overloading the server
        time.sleep(0.1)
    
    # Save README file in the base directory
    readme_path = os.path.join(os.path.dirname(os.path.abspath(folder_path)), f"README_{os.path.basename(folder_path)}.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Created {readme_path} with problem list")
    
    # Save all results to a single JSON file for reference
    json_path = os.path.join(test_dir, f'problems_info_{os.path.basename(folder_path)}.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"All problem information has been saved to {json_path}")

if __name__ == "__main__":
    main('ML/Hard')