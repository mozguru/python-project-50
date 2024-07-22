import json
import yaml


def generate_diff(file_path1, file_path2):
    data1 = load_data_from_file(file_path1)
    data2 = load_data_from_file(file_path2)

    diff = analyze_data(data1, data2)
    return format_diff(diff)


def load_data_from_file(file_path):
    with open(file_path) as file:
        if file_path.endswith('.json'):
            return json.load(file)
        else:
            return yaml.safe_load(file)


def analyze_data(data1, data2):
    diff = {}
    for key in sorted(data1.keys() | data2.keys()):
        if key not in data1:
            diff[f'+ {key}'] = data2[key]
        elif key not in data2:
            diff[f'- {key}'] = data1[key]
        elif data1[key] != data2[key]:
            diff[f'- {key}'] = data1[key]
            diff[f'+ {key}'] = data2[key]
        else:
            diff[f'  {key}'] = data1[key]
    return diff


def format_diff(diff):
    result = []
    for key, value in diff.items():
        result.append(f"  {key}: {value}")
    return '{\n' + '\n'.join(result) + '\n}'
