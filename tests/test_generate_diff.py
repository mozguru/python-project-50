import os
from gendiff.diff import generate_diff


def test_generate_diff():
    path1 = './tests/fixtures/file1.json'
    path2 = './tests/fixtures/file2.json'
    result_filename = 'result.json'
    result_path = os.path.join('./tests/fixtures', result_filename)

    with open(result_path) as result_file:
        expected_result = result_file.read()
        assert generate_diff(path1, path2) == expected_result


def test_generate_diff_yaml():
    path1 = './tests/fixtures/file1.yml'
    path2 = './tests/fixtures/file2.yml'
    result_filename = 'result.yml'
    result_path = os.path.join('./tests/fixtures', result_filename)

    with open(result_path) as result_file:
        expected_result = result_file.read()
        assert generate_diff(path1, path2) == expected_result


