import json
from utils.utils import check_last_operations, create_operation_message


def main():
    with open("data/operations.json", "r", encoding="utf-8") as file:
        operations = json.load(file)

    for value in check_last_operations(operations):
        print(create_operation_message(value))
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
