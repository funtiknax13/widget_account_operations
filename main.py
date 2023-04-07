import json
from utils.utils import select_last_operations, create_operation_message


def main():
    # загрузка данных по операциям
    with open("data/operations.json", "r", encoding="utf-8") as file:
        operations = json.load(file)
    # вывод последних 5 операций
    for value in select_last_operations(operations):
        print(create_operation_message(value))
        print()


if __name__ == '__main__':
    main()

