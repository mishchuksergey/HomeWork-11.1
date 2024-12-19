import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import list_transactions


@pytest.mark.parametrize("transactions_USD",
        [({'id': 939719570,
          'state': 'EXECUTED',
          'date': '2018-06-30T02:08:58.425572',
          'operationAmount': {
              'amount': '9824.07',
              'currency': {
                  'name': 'USD',
                  'code': 'USD'
              }
          },
          'description': 'Перевод организации',
          'from': 'Счет 75106830613657916952',
          'to': 'Счет 11776614605963066702'},
          ),
         ({'id': 142264268,
          'state': 'EXECUTED',
          'date': '2019-04-04T23:20:05.206878',
          'operationAmount': {
              'amount': '79114.93',
              'currency': {
                  'name': 'USD',
                  'code': 'USD'
              }
          },
          'description': 'Перевод со счета на счет',
          'from': 'Счет 19708645243227258542',
          'to': 'Счет 75651667383060284188'
          }
         )
         ]
)
def test_filter_by_currency(list_transactions, transactions_USD):
    """
    Тест функции-генератор отфильтрованной по ключу 'currency' "USD"
    """
    generator = filter_by_currency(list_transactions, "USD")
    next(generator)


def test_list_transactions_not_usd(list_transactions_not_usd):
    """
    Тест на ошибку функции-генератор отфильтрованной по ключу 'currency' "USD"
    """
    with pytest.raises(Exception):
        generator =filter_by_currency(list_transactions, "RUB")
        next(generator)

def test_list_transactions_empty():
    """
    Тест на ошибку при обработке пустого списка
    """
    with pytest.raises(Exception):
        generator = filter_by_currency(list_transactions_empty, "USD")
        next(generator)



def test_transaction_descriptions():

