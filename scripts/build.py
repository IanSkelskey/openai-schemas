import json
import os

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def resolve_references(schema, base_path):
    if isinstance(schema, dict):
        # Replace $ref with inline schema
        if "$ref" in schema:
            ref_path = schema["$ref"].strip("./")
            ref_file = os.path.join(base_path, ref_path)
            if os.path.exists(ref_file):
                ref_schema = load_json_file(ref_file)
                return resolve_references(ref_schema, base_path)
            else:
                print(f"Warning: Reference file not found: {ref_file}")
                return schema
        # Recursively resolve references in nested dictionaries
        return {key: resolve_references(value, base_path) for key, value in schema.items()}
    elif isinstance(schema, list):
        # Recursively resolve references in lists
        return [resolve_references(item, base_path) for item in schema]
    else:
        # Return the schema as is if it's neither a dict nor a list
        return schema

def build_api_schema(api_name):
    script_dir = os.path.dirname(__file__)
    base_path = os.path.normpath(os.path.join(script_dir, f'../schemas/{api_name}/'))
    main_schema = load_json_file(os.path.join(base_path, 'main.json'))

    # Iterate through the paths in main.json and replace placeholders with resolved endpoint schema contents
    for endpoint, placeholder in main_schema['paths'].items():
        if isinstance(placeholder, str):
            # Handle direct references to other files
            schema_filename = placeholder.strip("{}").replace(" ", "") + '.json'
            file_path = os.path.normpath(os.path.join(base_path, schema_filename))
            if os.path.exists(file_path):
                endpoint_schema = load_json_file(file_path)
                main_schema['paths'][endpoint] = resolve_references(endpoint_schema, base_path)
            else:
                print(f"Warning: File not found for endpoint '{endpoint}': {file_path}")
        else:
            # Inline resolve references for embedded schema data
            main_schema['paths'][endpoint] = resolve_references(placeholder, base_path)

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
