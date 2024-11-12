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

    # Iterate through the paths in main.json and replace placeholders with the actual endpoint schema contents
    for endpoint, placeholder in main_schema['paths'].items():
        schema_filename = placeholder.strip("{}").replace(" ", "") + '.json'
        file_path = os.path.normpath(os.path.join(base_path, schema_filename))

        if os.path.exists(file_path):
            endpoint_schema = load_json_file(file_path)
            main_schema['paths'][endpoint] = endpoint_schema
        else:
            print(f"Warning: File not found for endpoint '{endpoint}': {file_path}")

    # Ensure the build directory exists
    build_dir = os.path.normpath(os.path.join(script_dir, '../build/'))
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # Save the consolidated main schema
    output_file = os.path.join(build_dir, f'{api_name}.json')
    save_json_file(main_schema, output_file)
    print(f"Schema for {api_name} API built successfully at {output_file}")

def build_all_schemas():
    build_api_schema('spotify')
    build_api_schema('github')
    build_api_schema('mtg')  # Build schema for Magic: The Gathering API

# Run the build process for all APIs
build_all_schemas()
