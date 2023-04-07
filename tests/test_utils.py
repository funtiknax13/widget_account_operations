from utils import utils
import json


with open("tests/test_data/test_operations.json", "r", encoding="utf-8") as file:
    test_operations = json.load(file)

select_last_operations_result = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
           'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
          {'id': 522357576, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230',
           'operationAmount': {'amount': '51463.70', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'},
          {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
           'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
          {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
           'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'},
          {'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246',
           'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод организации', 'from': 'Счет 10848359769870775355', 'to': 'Счет 21969751544412966366'}]

create_operation_message_result_1 = "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
create_operation_message_result_2 = "23.03.2018 Открытие вклада\n -> Счет **2431\n48223.05 руб."


def test_select_last_operations():
    assert utils.select_last_operations(test_operations) == select_last_operations_result


def test_create_operation_message():
    assert utils.create_operation_message(test_operations[0]) == create_operation_message_result_1
    assert utils.create_operation_message(test_operations[3]) == create_operation_message_result_2


def test_hide_number():
    assert utils.hide_number(test_operations[0]["from"]) == "Maestro 1596 83** **** 5199"
    assert utils.hide_number(test_operations[0]["to"]) == "Счет **9589"


