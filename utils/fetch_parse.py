import codecs
import sys
import requests
from bs4 import BeautifulSoup

def get_html_content(problem_id):
    url = f"https://coderun.yandex.ru/problem/{problem_id}"
    
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
        print(f"ERROR: fetching problem info: {e}")
        return None
    
def get_comlex_html(problem_id):
    url = f"https://coderun.yandex.ru/problem/{problem_id}"
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        # Wait for content to load
        page.wait_for_timeout(3000)
        html_content = page.content()
        browser.close()
        return html_content

def extract_tags(html_content):
    if not html_content:
        print("Empty HTML content was provided to get_tags")
        sys.exit(1)
    data = html_content[html_content.find('"tags":') + len('"tags":'):]
    if data[:2] == '[]': return []
    data = data[1:data.find(']')]
    tags = [tag.strip()[1:-1] for tag in data.split(',')]
    return tags

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

        output_start = test_block_text.find(
            '"content"') + len('"content":') + 1
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
        print(f"ERROR processing test block: {e}")
        return {
            'input': "ERROR processing input",
            'output': "ERROR processing output"
        }


def extract_problem_num(html_content):
    if not html_content:
        print('Empty HTML content was provided to get_problem_number')
        sys.exit(1)
    indx = html_content.find('"number":') + len('"number":')
    problem_number = html_content[indx:].split(',')[0]
    if 1 <= len(problem_number) < 10 and problem_number.isdigit():
        return problem_number.split(',')[0]
    else:
        print('ERROR: Could not find a valid problem number')
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


def extract_title(html_content):
    title_start = html_content.find('<title>') + len('<title>')
    title = "Unknown Title"
    for i in range(title_start, len(html_content)-1):
        if html_content[i:i+2] == '//':
            title = html_content[title_start:i].strip()
            break
    if not title:
        print("ERROR: Could not find a valid title")
        sys.exit(1)
    return title


def extract_legend(html_content):
    # Extract legend/description
    legend_start = html_content.find("legend") + 9
    legend_end = html_content.find('\"notes\"') - 2
    legend_data = html_content[legend_start:legend_end].strip()
    legend_data = split_legend(legend_data)
    legend_data = codecs.escape_decode(legend_data)[0].decode('utf-8')
    if not legend_data:
        print("ERROR: Could not find a valid legend")
        sys.exit(1)
    return legend_data

def extract_tests(html_content):
    result = ""
    # Extract test cases
    test_cases_start = html_content.find('\"samples\"') + len('\"samples\"')
    test_cases_end = html_content.find('renderedStatements') - 1
    cases_data = html_content[test_cases_start:test_cases_end].strip()
    cases_data = cases_data.split('"input"')[1:]
    result += "## Example Test Cases\n\n"
    # Process each test case
    for i, case_data in enumerate(cases_data):
        test_block = process_test_block(case_data)
        result += f"### Example {i+1}\n\n"
        result += f"**Input:**\n```\n{test_block['input']}\n```\n\n"
        result += f"**Output:**\n```\n{test_block['output']}\n```\n\n"
    if not result: print("ERROR: Could not find any test cases")
    return result

def extract_math_expressions(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Process inline math expressions
    inline_math_spans = soup.select('span.math.inline')
    for span in inline_math_spans:
        # Find the LaTeX annotation
        annotation = span.select_one('annotation[encoding="application/x-tex"]')
        if annotation:
            latex = annotation.text.strip()
            # Replace the span with the LaTeX in markdown format
            span.replace_with(f"$${latex}$$")
    
    # Process display math expressions
    display_math_spans = soup.select('span.math.display')
    for span in display_math_spans:
        # Find the LaTeX annotation
        annotation = span.select_one('annotation[encoding="application/x-tex"]')
        if annotation:
            latex = annotation.text.strip()
            # Replace the span with the LaTeX in markdown format
            span.replace_with(f"\n$$\n{latex}\n$$\n")
    
    # Extract the problem description content
    description_sections = soup.select('.DescriptionSection_description-section__ntXr_')
    
    result = ""
    for section in description_sections:
        # Get section title
        title_elem = section.select_one('h2')
        if title_elem:
            section_title = title_elem.get_text(strip=True)
            result += f"## {section_title}\n\n"
        
        # Get section content
        content_div = section.select_one('.DescriptionSection_html-section__jgqfx')
        if content_div:
            # Process paragraphs and other elements
            for elem in content_div.children:
                if elem.name == 'p':
                    result += f"{elem.get_text()}\n\n"
                elif elem.name == 'ol' or elem.name == 'ul':
                    for li in elem.find_all('li'):
                        result += f"- {li.get_text()}\n"
                    result += "\n"
    
    return result

def parse_problem_comlex(html_content: str) -> str:
    # Extract the problem title
    soup = BeautifulSoup(html_content, 'html.parser')
    # title_elem = soup.select_one('.ProblemStatement_title__Ku_wX')
    
    # Extract and format the description content
    formatted_content = extract_math_expressions(html_content)
    
    # Combine title and description
    formatted_content = formatted_content.replace('## Формат ввода', '### Input Format:')
    formatted_content = formatted_content.replace('## Формат вывода', '### Output Format:')
    formatted_content = formatted_content[:formatted_content.find('## Ограничения')].strip()
    formatted_content = formatted_content.replace('$$', '$')
    return formatted_content + "\n\n"


def extract_link(html_content):
    start = html_content.find("og:url") + len('og:url" content="')
    html_content = html_content[start:]
    end = html_content.find('"')
    return html_content[:end]

def extract_problem_data(html_content, problem_id=None):
    data = html_content

    title = extract_title(data)
    title_num = extract_problem_num(data)
    if "legend" in data: 
        legend_data = extract_legend(data)
    else:
        print('USE: extracting legend in comlex scenario')
        comlex_html = get_comlex_html(problem_id)
        legend_data = parse_problem_comlex(comlex_html)
    cases_data = extract_tests(data)
    problem_link = extract_link(data)
    tags = extract_tags(data)

    description_text = f"# [{title_num}. {title}]({problem_link})\n\n"
    description_text += f"## Description\n\n{legend_data}\n\n"
    description_text += cases_data
    # Add tags section if tagsexist
    if tags and len(tags) > 0:
        description_text += f"**Tags**: {', '.join(tags)}\n\n"

    output = {
        'title': title,
        'title_num': title_num,
        'legend_data': legend_data,
        'case_data': cases_data,
        'problem_link': problem_link,
        'tags': tags,
        'description_text': description_text,
    }
    print('OK: problem data extracted successfully')
    return output

# if __name__ == '__main__':
    # problem_id = "shortest-path-length"
    # html_content = get_html_content(problem_id)
    # with open('utils/html_content.txt', 'w', encoding='utf-8') as f:
    #     f.write(html_content)
    # print(f"head:{extract_problem_num(html_content)}. {extract_title(html_content)}")
    # print(f"link: {extract_link(html_content)}")
    # print(f"tags: {extract_tags(html_content)}")
    # data = extract_problem_data(html_content)
    # print(data['description_text'])