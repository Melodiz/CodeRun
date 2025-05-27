# import os
import requests
# from bs4 import BeautifulSoup
# import json
# import time
import re
import codecs
import sys

def get_html_content(problem_id):
    url = f"https://coderun.yandex.ru/problem/{problem_id}/"
    
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching problem info: {e}")
        return None
    
def process_test_block(test_block_text):
    """
    Process a test block to extract input and output data
    
    Args:
        test_block_text (str): The test block text
        
    Returns:
        dict: A dictionary containing 'input' and 'output' data
    """
    try:
        input_start = test_block_text.find('"content"') + len('"content":') + 1
        test_block_text = test_block_text[input_start:]
        input_end = test_block_text.find('}') - 1
        input_data = test_block_text[:input_end].strip()

        output_start = test_block_text.find('"content"') + len('"content":') + 1
        test_block_text = test_block_text[output_start:]
        output_end = test_block_text.find('}') - 1
        output_data = test_block_text[:output_end].strip()
        input_data = codecs.escape_decode(input_data)[0].decode('utf-8')
        output_data = codecs.escape_decode(output_data)[0].decode('utf-8')
        
        return {
            'input': input_data,
            'output': output_data
        }
    except Exception as e:
        print(f"Error processing test block: {e}")
        return {
            'input': "Error processing input",
            'output': "Error processing output"
        }
    

def get_problem_number(html_content):
    if not html_content:
        print('Empty HTML content was provided to get_problem_number')
        sys.exit(1)
    indx = html_content.find('"number":') + len('"number":')
    problem_number = html_content[indx:].split(',')[0]
    if 1<= len(problem_number) < 10 and problem_number.isdigit():
        return problem_number.split(',')[0]
    else: 
        print('Could not find a valid problem number')
        sys.exit(1)

def split_legend(legend_data):
    pre_start = 0
    pre_end = legend_data.find('","inputFormat":"')
    pre_content = legend_data[pre_start:pre_end].strip()
    legend_data = legend_data[pre_end + len('","inputFormat":"'):]
    inp_end = legend_data.find('","outputFormat":"')
    inp_content = legend_data[:inp_end].strip()
    out_content = legend_data[inp_end + len('","outputFormat":"'):]
    result = pre_content
    result += f"\n### Input Format:\n\n{inp_content}\n\n### Output Format:\n\n{out_content}"
    return result


def get_problem_readme(html_content):
    """
    Generate a README.md file from the problem HTML content
    
    Args:
        html_content (dict): Dictionary containing HTML content
    """
    data = html_content
    if not data: 
        print('Empty HTML content was provided to get_problem_readme')
        sys.exit(1)
    
    # Extract title
    title_start = data.find('<title>') + len('<title>')
    title = "Unknown Title"
    for i in range(title_start, len(data)-1):
        if data[i:i+2] == '//': 
            title = data[title_start:i].strip()
            break
    title_num = get_problem_number(data)
    
    # Extract legend/description
    legend_start = data.find("legend") + 9
    legend_end = data.find('\"notes\"') - 2
    legend_data = data[legend_start:legend_end].strip()
    legend_data = split_legend(legend_data)
    legend_data = codecs.escape_decode(legend_data)[0].decode('utf-8')
    
    # Extract test cases
    test_cases_start = data.find('\"samples\"') + len('\"samples\"')
    test_cases_end = data.find('renderedStatements') - 1
    cases_data = data[test_cases_start:test_cases_end].strip()
    cases_data = cases_data.split('"input"')[1:]
    
    # Build the result markdown
    link = get_link_from_html(html_content)
    result = f"# [{title_num}. {title}]({'link'})\n\n"
    result += f"## Description\n\n{legend_data}\n\n"
    result += "## Example Test Cases\n\n"
    
    # Process each test case
    for i, case_data in enumerate(cases_data):
        test_block = process_test_block(case_data)
        result += f"### Example {i+1}\n\n"
        result += f"**Input:**\n```\n{test_block['input']}\n```\n\n"
        result += f"**Output:**\n```\n{test_block['output']}\n```\n\n"
    
    return result

def get_link_from_html(html_content):
    start = html_content.find("og:url") + len("og:url")
    html_content = html_content[start:]
    start = html_content.find('"') + 1
    html_content = html_content[start:]
    end = html_content.find('"')
    return html_content[:end]
        

if __name__ == "__main__":
    problem_id = 'three-numbers'
    html_content = get_html_content(problem_id)
    print(get_problem_number(html_content))
