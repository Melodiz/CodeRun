import os
import json
import glob

def concatenate_json_files(pattern='utils/test/problems_info_*.json', output_file='utils/test/concatenated.json'):
    """
    Read all JSON files matching the given pattern and concatenate their contents into a single JSON file.
    
    Args:
        pattern (str): Glob pattern to match JSON files. Default is 'utils/test/problems_info_*.json'.
        output_file (str): Path to the output JSON file. Default is 'utils/test/concatenated.json'.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    # Find all JSON files matching the pattern
    json_files = glob.glob(pattern)
    
    if not json_files:
        print(f"No JSON files found matching pattern: {pattern}")
        return False
    
    print(f"Found {len(json_files)} JSON files to concatenate:")
    for file in json_files:
        print(f"  - {file}")
    
    # Initialize an empty dictionary to store the combined data
    combined_data = {}
    
    # Read each JSON file and merge its contents
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Add the data to the combined dictionary
                combined_data.update(data)
                
            print(f"Successfully read {len(data)} entries from {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    # Write the combined data to the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=2)
        
        print(f"Successfully wrote {len(combined_data)} entries to {output_file}")
        return True
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
        return False

def main():
    """
    Main function to run the concatenation process.
    """
    import sys
    
    # Check if custom pattern and output file are provided
    pattern = sys.argv[1] if len(sys.argv) > 1 else 'utils/test/problems_info_*.json'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'utils/test/all_problems_info.json'
    
    print(f"Concatenating JSON files matching pattern: {pattern}")
    print(f"Output will be saved to: {output_file}")
    
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Run the concatenation
    success = concatenate_json_files(pattern, output_file)
    
    if success:
        print("Concatenation completed successfully!")
    else:
        print("Concatenation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()