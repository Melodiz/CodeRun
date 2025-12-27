import codecs
import sys
import requests
import re
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
        test_block_text (str): The test block text (starts after "input" split)

    Returns:
        dict: A dictionary containing 'input' and 'output' data
    """
    try:
        # The test_block_text starts after "input" was split, so it should start with ": "content": ..." or similar
        # First, find where the input value starts (after the colon)
        input_text = test_block_text.strip()
        if input_text.startswith(':'):
            # Remove the leading ':'
            input_text = input_text[1:].strip()
        
        # Check if it's an s3File structure (new format) or content (old format)
        input_s3file_start = input_text.find('"s3File"')
        input_content_start = input_text.find('"content"')
        
        # Handle s3File format (new format where test data is in S3)
        if input_s3file_start != -1 and (input_content_start == -1 or input_s3file_start < input_content_start):
            # Extract URL from s3File structure
            url_start = input_text.find('"url":') + len('"url":')
            url_text = input_text[url_start:].strip()
            if url_text.startswith('"'):
                # Find the closing quote
                quote_end = 1
                while quote_end < len(url_text) and url_text[quote_end] != '"':
                    if url_text[quote_end] == '\\' and quote_end + 1 < len(url_text):
                        quote_end += 2
                    else:
                        quote_end += 1
                if quote_end < len(url_text):
                    url_raw = url_text[1:quote_end]
                    # Decode the URL - handle both Python escapes and Unicode escapes
                    try:
                        # First decode Python string escapes
                        url_decoded = codecs.escape_decode(url_raw)[0].decode('utf-8')
                        # Then decode Unicode escapes like \u0026
                        url = url_decoded.encode('utf-8').decode('unicode_escape')
                    except:
                        # Fallback: try direct unicode_escape
                        try:
                            url = url_raw.encode('utf-8').decode('unicode_escape')
                        except:
                            url = url_raw
                    # Fetch the content from the URL
                    try:
                        response = requests.get(url, timeout=10)
                        response.raise_for_status()
                        input_data = response.text
                    except Exception as e:
                        print(f"Warning: Could not fetch input from S3 URL: {e}")
                        input_data = f"[S3 URL: {url}]"
                else:
                    raise ValueError("Could not find closing quote for s3File URL")
            else:
                raise ValueError("Could not parse s3File URL")
        elif input_content_start != -1:
            # Extract from "content": "escaped_string"
            content_start = input_text.find('"content":') + len('"content":')
            input_text_after_content = input_text[content_start:].strip()
            
            if input_text_after_content.startswith('"'):
                # Find the closing quote, handling escaped quotes
                quote_end = 1
                while quote_end < len(input_text_after_content) and input_text_after_content[quote_end] != '"':
                    if input_text_after_content[quote_end] == '\\' and quote_end + 1 < len(input_text_after_content):
                        quote_end += 2  # Skip escaped character
                    else:
                        quote_end += 1
                if quote_end < len(input_text_after_content):
                    input_data_raw = input_text_after_content[1:quote_end]
                    input_data = codecs.escape_decode(input_data_raw)[0].decode('utf-8')
                else:
                    raise ValueError("Could not find closing quote for input content")
            else:
                # Try to find content in braces: {"content": "..."}
                brace_start = input_text_after_content.find('{')
                if brace_start != -1:
                    brace_end = input_text_after_content.find('}', brace_start)
                    if brace_end != -1:
                        content_value = input_text_after_content[brace_start+1:brace_end]
                        # Extract the string value
                        if '"' in content_value:
                            str_start = content_value.find('"') + 1
                            str_end = content_value.rfind('"')
                            if str_end > str_start:
                                input_data_raw = content_value[str_start:str_end]
                                input_data = codecs.escape_decode(input_data_raw)[0].decode('utf-8')
                            else:
                                raise ValueError("Could not parse input content in braces")
                        else:
                            raise ValueError("Could not find string in input content braces")
                    else:
                        raise ValueError("Could not find closing brace for input content")
                else:
                    raise ValueError("Could not find input content structure")
        else:
            raise ValueError("Could not find 's3File' or 'content' field for input")
        
        # Extract output - look for "output" field in the remaining text
        output_start_marker = '"output"'
        output_start = test_block_text.find(output_start_marker)
        if output_start == -1:
            raise ValueError("Could not find 'output' field")
        
        output_text = test_block_text[output_start + len(output_start_marker):].strip()
        if output_text.startswith(':'):
            output_text = output_text[1:].strip()
        
        # Check if it's an s3File structure or content
        output_s3file_start = output_text.find('"s3File"')
        output_content_start = output_text.find('"content"')
        
        # Handle s3File format for output
        if output_s3file_start != -1 and (output_content_start == -1 or output_s3file_start < output_content_start):
            # Extract URL from s3File structure
            url_start = output_text.find('"url":') + len('"url":')
            url_text = output_text[url_start:].strip()
            if url_text.startswith('"'):
                quote_end = 1
                while quote_end < len(url_text) and url_text[quote_end] != '"':
                    if url_text[quote_end] == '\\' and quote_end + 1 < len(url_text):
                        quote_end += 2
                    else:
                        quote_end += 1
                if quote_end < len(url_text):
                    url_raw = url_text[1:quote_end]
                    # Decode the URL - handle both Python escapes and Unicode escapes
                    try:
                        # First decode Python string escapes
                        url_decoded = codecs.escape_decode(url_raw)[0].decode('utf-8')
                        # Then decode Unicode escapes like \u0026
                        url = url_decoded.encode('utf-8').decode('unicode_escape')
                    except:
                        # Fallback: try direct unicode_escape
                        try:
                            url = url_raw.encode('utf-8').decode('unicode_escape')
                        except:
                            url = url_raw
                    # Fetch the content from the URL
                    try:
                        response = requests.get(url, timeout=10)
                        response.raise_for_status()
                        output_data = response.text
                    except Exception as e:
                        print(f"Warning: Could not fetch output from S3 URL: {e}")
                        output_data = f"[S3 URL: {url}]"
                else:
                    raise ValueError("Could not find closing quote for s3File URL")
            else:
                raise ValueError("Could not parse s3File URL")
        elif output_content_start != -1:
            # Extract from "content": "escaped_string"
            content_start = output_text.find('"content":') + len('"content":')
            output_text_after_content = output_text[content_start:].strip()
            
            if output_text_after_content.startswith('"'):
                quote_end = 1
                while quote_end < len(output_text_after_content) and output_text_after_content[quote_end] != '"':
                    if output_text_after_content[quote_end] == '\\' and quote_end + 1 < len(output_text_after_content):
                        quote_end += 2
                    else:
                        quote_end += 1
                if quote_end < len(output_text_after_content):
                    output_data_raw = output_text_after_content[1:quote_end]
                    output_data = codecs.escape_decode(output_data_raw)[0].decode('utf-8')
                else:
                    raise ValueError("Could not find closing quote for output content")
            else:
                # Try to find content in braces
                brace_start = output_text_after_content.find('{')
                if brace_start != -1:
                    brace_end = output_text_after_content.find('}', brace_start)
                    if brace_end != -1:
                        content_value = output_text_after_content[brace_start+1:brace_end]
                        if '"' in content_value:
                            str_start = content_value.find('"') + 1
                            str_end = content_value.rfind('"')
                            if str_end > str_start:
                                output_data_raw = content_value[str_start:str_end]
                                output_data = codecs.escape_decode(output_data_raw)[0].decode('utf-8')
                            else:
                                raise ValueError("Could not parse output content in braces")
                        else:
                            raise ValueError("Could not find string in output content braces")
                    else:
                        raise ValueError("Could not find closing brace for output content")
                else:
                    raise ValueError("Could not find output content structure")
        else:
            raise ValueError("Could not find 's3File' or 'content' field for output")

        return {
            'input': input_data,
            'output': output_data
        }
    except Exception as e:
        print(f"ERROR processing test block: {e}")
        import traceback
        traceback.print_exc()
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
    # Try using BeautifulSoup first for more robust parsing
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            title_text = title_tag.get_text(strip=True)
            # Title format is usually "Problem Name // CodeRun" or similar
            if '//' in title_text:
                title = title_text.split('//')[0].strip()
            else:
                title = title_text
            if title and title != "Unknown Title":
                return title
    except Exception as e:
        print(f"Warning: BeautifulSoup title extraction failed: {e}")
    
    # Fallback to original method
    title_start = html_content.find('<title>')
    if title_start == -1:
        print("ERROR: Could not find <title> tag")
        sys.exit(1)
    title_start += len('<title>')
    title = "Unknown Title"
    for i in range(title_start, len(html_content)-1):
        if html_content[i:i+2] == '//':
            title = html_content[title_start:i].strip()
            break
        elif html_content[i:i+7] == '</title>':
            # If we hit </title> before finding //, take everything up to </title>
            title = html_content[title_start:i].strip()
            if '//' in title:
                title = title.split('//')[0].strip()
            break
    if not title or title == "Unknown Title":
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
    # Try new selector first (DescriptionSection_Root__z2w73)
    description_sections = soup.select('.DescriptionSection_Root__z2w73')
    
    # Fallback to old selector if not found
    if not description_sections:
        description_sections = soup.select('.DescriptionSection_description-section__ntXr_')
    
    result = ""
    for section in description_sections:
        # Get section title - try h2, h3, or look for title in the section
        title_elem = section.select_one('h2, h3')
        if title_elem:
            section_title = title_elem.get_text(strip=True)
            # Skip if it's the problem number/title
            if not section_title.startswith(('##', '#')) and len(section_title) > 3:
                result += f"## {section_title}\n\n"
        
        # Get section content - try new selector first
        content_div = section.select_one('.DescriptionSection_html-section__jgqfx, .HtmlStatements_html-statements__Ixo77, div[class*="html"], div[class*="statement"]')
        
        if not content_div:
            # If no specific content div, use the section itself
            content_div = section
        
        if content_div:
            # Process paragraphs and other elements
            for elem in content_div.children:
                if elem.name == 'p':
                    text = elem.get_text(strip=True)
                    if text:
                        result += f"{text}\n\n"
                elif elem.name == 'div':
                    # Check if it's a text div
                    text = elem.get_text(strip=True)
                    # Skip if it's very short (likely metadata) or contains tags
                    if text and len(text) > 10 and 'tag' not in str(elem.get('class', [])).lower():
                        result += f"{text}\n\n"
                elif elem.name == 'ol' or elem.name == 'ul':
                    for li in elem.find_all('li'):
                        result += f"- {li.get_text(strip=True)}\n"
                    result += "\n"
                elif elem.name in ['h2', 'h3', 'h4']:
                    # Add headers
                    text = elem.get_text(strip=True)
                    if text and not text.startswith('#'):
                        level = '##' if elem.name == 'h2' else '###' if elem.name == 'h3' else '####'
                        result += f"{level} {text}\n\n"
    
    # If still no result, try extracting from the main description div
    if not result:
        desc_div = soup.find('div', class_='Description_description__o1B3I')
        if desc_div:
            # Find the HtmlStatements div which contains the actual problem text
            html_statements = desc_div.find('div', class_='HtmlStatements_html-statements__Ixo77')
            if html_statements:
                # Extract all paragraphs and other content
                for elem in html_statements.find_all(['p', 'div', 'h2', 'h3', 'ul', 'ol']):
                    if elem.name == 'p':
                        text = elem.get_text(strip=True)
                        if text:
                            result += f"{text}\n\n"
                    elif elem.name in ['h2', 'h3']:
                        text = elem.get_text(strip=True)
                        if text:
                            level = '##' if elem.name == 'h2' else '###'
                            result += f"{level} {text}\n\n"
                    elif elem.name in ['ul', 'ol']:
                        for li in elem.find_all('li'):
                            result += f"- {li.get_text(strip=True)}\n"
                        result += "\n"
    
    return result

def fix_math_spacing(text: str) -> str:
    """
    Fix spacing around LaTeX math expressions ($...$) to ensure proper markdown formatting.
    Adds spaces before and after math expressions when they're adjacent to text.
    """
    # Pattern to match LaTeX math expressions: $...$ 
    # Matches $ followed by any characters (including spaces, backslashes) until closing $
    math_pattern = r'\$[^$\n]+\$'
    
    def add_spacing(match):
        math_expr = match.group(0)
        start_pos = match.start()
        end_pos = match.end()
        
        # Get characters before and after (using the original text via closure)
        char_before = text[start_pos - 1] if start_pos > 0 else ''
        char_after = text[end_pos] if end_pos < len(text) else ''
        
        # Add space before if preceded by letter, digit, hyphen, colon, or Cyrillic character
        # But not if it's already a space or opening bracket/parenthesis
        needs_space_before = (char_before and 
                             char_before not in ' \n\t([{' and
                             (char_before.isalnum() or char_before in '-—:'))
        
        # Add space after if followed by letter, digit, or opening parenthesis (for ranges like $R$($8...))
        # But not if it's already a space or closing bracket/parenthesis/comma
        needs_space_after = (char_after and 
                            char_after not in ' \n\t,.;:!?)]}' and
                            (char_after.isalnum() or char_after in '—('))
        
        result = math_expr
        if needs_space_before:
            result = ' ' + result
        if needs_space_after:
            result = result + ' '
        
        return result
    
    # Replace all math expressions with properly spaced versions
    result = re.sub(math_pattern, add_spacing, text)
    
    # Clean up multiple spaces (but preserve single spaces)
    result = re.sub(r'  +', ' ', result)
    
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
    
    # Remove sections we don't want (Constraints, Notes if empty/incomplete)
    # Stop at Constraints section
    constraints_pos = formatted_content.find('## Ограничения')
    if constraints_pos != -1:
        formatted_content = formatted_content[:constraints_pos].strip()
    
    # Remove empty or incomplete Note sections
    note_pos = formatted_content.find('## Примечание')
    if note_pos != -1:
        note_section = formatted_content[note_pos:]
        # Check if the note section is mostly empty (just title and maybe one line)
        lines_after_note = note_section.split('\n')
        non_empty_lines = [line for line in lines_after_note[1:] if line.strip()]
        if len(non_empty_lines) <= 2:  # If only 1-2 lines of content, remove it
            formatted_content = formatted_content[:note_pos].strip()
    
    # Clean up math expressions - replace $$ with $ for inline math
    formatted_content = formatted_content.replace('$$', '$')
    
    # Fix spacing around math expressions
    # Process line by line to preserve structure
    lines = formatted_content.split('\n')
    fixed_lines = []
    for line in lines:
        # Only fix spacing in non-header lines (headers start with #)
        if line.strip() and not line.strip().startswith('#'):
            fixed_lines.append(fix_math_spacing(line))
        else:
            fixed_lines.append(line)
    formatted_content = '\n'.join(fixed_lines)
    
    # Clean up extra newlines
    formatted_content = '\n\n'.join([line.strip() for line in formatted_content.split('\n') if line.strip()])
    
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