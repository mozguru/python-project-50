from gendiff.diff import generate_diff
from gendiff.parsing import get_parsed_arg


def main():
    args = get_parsed_arg()

    diff = generate_diff(
        args.first_file,
        args.second_file
    )

    print(diff)


if __name__ == '__main__':
    main()
