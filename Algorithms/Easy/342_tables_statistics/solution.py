import json
import csv

def build_node_info(nodes_data_dict):
    id_to_node_info = {}

    def traverse(node_id, current_node_data, parent_path_segments):
        node_name = current_node_data.get('name')
        if node_name is None:
            return
        current_full_path_segments = parent_path_segments + [node_name]
        path_str = "/" + "/".join(current_full_path_segments)
        link_target = current_node_data.get('link')
        id_to_node_info[node_id] = {
            'id': node_id,
            'name': node_name,
            'path_str': path_str,
            'link_target': link_target,
            'resolved_path_str': None
        }
        if 'values' in current_node_data and isinstance(current_node_data['values'], dict):
            for child_id, child_node_data in current_node_data['values'].items():
                if isinstance(child_node_data, dict):
                    traverse(child_id, child_node_data, current_full_path_segments)
    
    for root_id, root_data in nodes_data_dict.items():
        traverse(root_id, root_data, [])
        
    return id_to_node_info

def resolve_all_paths(id_to_node_info):

    resolved_paths_cache = {}

    def get_resolved_path_for_single_id(node_id_to_resolve):
        if node_id_to_resolve in resolved_paths_cache:
            return resolved_paths_cache[node_id_to_resolve]

        current_resolution_chain = []
        current_id_in_chain = node_id_to_resolve

        while True:
            if current_id_in_chain not in id_to_node_info:
                resolved_paths_cache[node_id_to_resolve] = None
                return None

            if current_id_in_chain in current_resolution_chain:
                resolved_paths_cache[node_id_to_resolve] = None
                return None
            current_resolution_chain.append(current_id_in_chain)

            node_details = id_to_node_info[current_id_in_chain]
            
            if node_details['link_target']:
                current_id_in_chain = node_details['link_target']
            else:
                final_path_str = node_details['path_str']
                resolved_paths_cache[node_id_to_resolve] = final_path_str
                for visited_id_in_chain in current_resolution_chain:
                    if visited_id_in_chain not in resolved_paths_cache:
                        resolved_paths_cache[visited_id_in_chain] = final_path_str
                return final_path_str

    for original_node_id in id_to_node_info:
        resolved_path = get_resolved_path_for_single_id(original_node_id)
        id_to_node_info[original_node_id]['resolved_path_str'] = resolved_path


def count_target_folder_accesses(logs_filepath, nodes_data_filepath, target_path_prefix):
    with open(nodes_data_filepath, 'r', encoding='utf-8') as f:
        nodes_data = json.load(f)
    id_to_node_info = build_node_info(nodes_data)
    resolve_all_paths(id_to_node_info)
    
    access_count = 0
    
    with open(logs_filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if 'id' not in reader.fieldnames:
            return 0
                
        for row in reader:
            accessed_id = row['id'].strip()
            if accessed_id in id_to_node_info:
                node_info = id_to_node_info[accessed_id]
                resolved_path = node_info.get('resolved_path_str')
                
                if resolved_path and resolved_path.startswith(target_path_prefix):
                    access_count += 1
    return access_count

if __name__ == "__main__":
    logs_file = 'logs.csv'
    nodes_file = 'sample.json'
    target_prefix = '/home/statistics'
    
    count = count_target_folder_accesses(logs_file, nodes_file, target_prefix)
    print(f"The folder '{target_prefix}' and its contents were accessed {count} times.")