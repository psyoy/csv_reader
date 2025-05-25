# Генератор отчетов по выплатам сотрудникам

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue )](https://www.python.org/ )

## Что делает
Программа создает таблицы с расчетом выплат сотрудникам на основе CSV-файлов. Автоматически находит колонку с зарплатными ставками (hourly_rate, rate или salary) и рассчитывает выплаты по формуле: **часы * ставка**.

## Как использовать
1. Установите Python 3.10+
2. Клонируйте репозиторий:
```bash
git clone https://github.com/psyoy/csv_reader
 
cd csv_reader

```

3. Запустите скрипт с CSV-файлами:
```bash
python main.py data1.csv data2.csv --report payout
```

Пример CSV
```code
name,email,department,hours_worked,hourly_rate
John Doe,john@example.com,HR,160,30
```
Пример вывода

![Пример работы](https://github.com/user-attachments/assets/5f0271c5-82db-4f06-aa15-f62e41c14c39)

Требования к CSV 

    Обязательные колонки: name, email, department, hours_worked
    Одна из колонок со ставкой: hourly_rate/rate/salary
     

