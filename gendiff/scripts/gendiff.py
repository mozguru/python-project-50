import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='Sets format of output')

    args = parser.parse_args()

    print(args.first_file)
    print(args.second_file)
    print(args.format)


if __name__ == '__main__':
    main()

