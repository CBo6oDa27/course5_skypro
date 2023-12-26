import json
from datetime import datetime

def read_bank_transactions(filename = 'operations.json'):
    '''Прочитаем данные по операциям из файла
    и вернем последние 5 в статусе EXECUTED'''
    with open(filename, 'r') as file:
        transactions = json.load(file)
        sorted_transactions = sorted(
            filter(lambda x: x.get('state') == 'EXECUTED' and 'date' in x, transactions),
            key=lambda x: x['date'], reverse=True
        )
        return sorted_transactions[0:4]

def formated_date(unformated_date):
    '''Преобразует дату к формату день.месяц.год'''
    parsed_date = datetime.strptime(unformated_date, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = parsed_date.strftime("%d.%m.%Y")

    return formatted_date

def formatted_account(attributes):
    '''Возвращает счет со скрытыми цифрами'''
    splited_attributes = attributes.split()
    account_number = splited_attributes[-1]
    if attributes.lower().startswith('счет'):
        masked_account = f'**{account_number[-4:]}'
    else:
        masked_account = f'{account_number[0:4]} {account_number[4:6]}** **** {account_number[-4:]}'

    splited_attributes[-1] = masked_account

    return ' '.join(splited_attributes)


