# Домашняя работа 11.1 "Включения и Генераторы"

## Цель проекта

* Использовать конвейеры для обработки больших объемов данных. 
* Поработать с функциями map, filter, chain.
* Узнать, как использовать генераторы списков.
* Рассмотреть генераторные выражения
* Разобраться, как работать с функциями-генераторами
* Зачем нужно ключевое слово yield и чем оно отличается от return.

## Инструкция по установке

1. Клонируйте репозиторий:

   git@github.com:mishchuksergey/HomeWork-11.1.git

2. Установите зависимости:

    pip install -r requirements.txt

### Новые функции

   В домашнем задании добавлен новый модуль *generators.py*, 
    в котором реализованы новые функции:
    - filter_by_currency (возвращает итератор, отфильтрованный по ключу 'USD')
    - transaction_descriptions (возвращает описание каждой операции)
    - card_number_generator (генерирует номер карты в формате от 0000 0000 0000 0001 до 9999 9999 9999 9999)

### Тестирование

Тестирование функций проводится с помощью фреймворка ***pytest***.
Для установки наберите в консоли:

    pip install pytest


*Добавлены следующие модули для тестирования функций:*
- *test_widget*
- *test_masks*
- *test_processing*
- *test_generators*

Тесты используют фикстуры из модуля ***conftest.py***, а также параметризацию.
В докстрингах тестов приведены краткие описания их работы.

### **Покрытие тестами (coverage) составляет 97%**.
Более подробная информация по покрытию каждого модуля представлена в директории ***htmlcov***.

## Лицензия