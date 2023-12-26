from src.utils import read_bank_transactions, formatted_account, formated_date

transactions_to_show = read_bank_transactions()
for transaction in transactions_to_show:
    operation_info = transaction['operationAmount']
    if 'from' not in transaction:
        transaction_from = ''
    else:
        transaction_from = formatted_account(transaction['from'])

    if 'to' not in transaction:
        transaction_to = ''
    else:
        transaction_to = formatted_account(transaction['to'])

    print(f'{formated_date(transaction['date'])} {transaction['description']}\n'
          f'{transaction_from} -> {transaction_to}\n'
          f'{operation_info['amount']} {operation_info['currency']['name']}\n')
