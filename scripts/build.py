import json
import os

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def build_api_schema(api_name):
    script_dir = os.path.dirname(__file__)
    base_path = os.path.normpath(os.path.join(script_dir, f'../schemas/{api_name}/'))
    main_schema = load_json_file(os.path.join(base_path, 'main.json'))

    for endpoint in main_schema['paths']:
        placeholder = main_schema['paths'][endpoint].strip().replace(" ", "")
        file_path = os.path.normpath(os.path.join(base_path, placeholder.strip("{}") + '.json'))
        
        if os.path.exists(file_path):
            endpoint_schema = load_json_file(file_path)
            main_schema['paths'][endpoint] = endpoint_schema
        else:
            print(f"File not found: {file_path}")

    build_dir = os.path.normpath(os.path.join(script_dir, '../build/'))
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    save_json_file(main_schema, os.path.join(build_dir, f'{api_name}.json'))

def build_all_schemas():
    build_api_schema('spotify')
    build_api_schema('github')

build_all_schemas()
