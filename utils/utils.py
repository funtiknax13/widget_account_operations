from datetime import datetime


def hide_number(number):
    """
    Функция для скрытия номера карты или счёта
    :param number: номер карты или счёта
    :return: строку с зашифрованным номером
    """
    if number[:4] == "Счет":
        return f"{number[:-20]}**{number[-4:]}"
    else:
        return f"{number[:-16]}{number[-16:-12]} {number[-12:-10]}** **** {number[-4:]}"


def create_operation_message(operation):
    """
    создание читаемого сообщения об операции
    :param operation: словарь с информацией по операции
    :return: сообщение об операции
    """
    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    # проверка наличия перевода от, создание сообщения с направлением перевода
    if 'from' in operation:
        direction = f"{hide_number(operation['from'])} -> {hide_number(operation['to'])}\n"
    else:
        direction = f" -> {hide_number(operation['to'])}\n"

    result_message = f"{date} {operation['description']}\n{direction}"\
                     f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
    return result_message


def select_last_operations(operations):
    """
    выбор 5-и последних выполненных операций
    :param operations: список всех операций
    :return: список последних 5-и операций
    """
    # сортировка по дате
    sorted_data = sorted(operations, key=lambda d: d['date'], reverse=True)
    last_operations = []
    operation_index = 0
    while len(last_operations) < 5 and operation_index < len(operations):
        if sorted_data[operation_index]["state"] == "EXECUTED":
            last_operations.append(sorted_data[operation_index])
        operation_index += 1
    return last_operations
