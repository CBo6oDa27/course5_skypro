from src.utils import formatted_account, formated_date, read_bank_transactions

def test_formatted_account():
    assert formatted_account('MasterCard 8826230888662405') == 'MasterCard 8826 23** **** 2405'
    assert formatted_account('Счет 96119739109420349721') == 'Счет **9721'

def test_formated_date():
    assert formated_date('2018-07-06T22:32:10.495465') == '06.07.2018'

def test_read_bank_transactions():
    assert read_bank_transactions('src/operations.json')[0]['state'] == 'EXECUTED'