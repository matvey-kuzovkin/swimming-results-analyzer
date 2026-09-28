# 🏊 Swimming Results Analyzer

Программа для обработки и анализа результатов соревнований по плаванию.

Проект демонстрирует работу с данными: чтение Excel, очистку, расчёт статистики, визуализацию и сохранение результатов.

---

## Возможности

- Чтение результатов из Excel-файла
- Преобразование времени из формата `ММ,СС,сс` в секунды
- Расчёт среднего, лучшего и худшего результата
- Группировка по дистанциям и полу
- Построение графиков
- Сохранение обработанных данных

## Как запустить

1. Установи зависимости:

```bash
pip install pandas openpyxl matplotlib
```

2. Положи файл `competition_data.xlsx` в папку `data/`

3. Запусти программу:

```bash
python main.py
```

## Формат входных данных

Excel-файл должен содержать лист `Результаты` со следующими колонками:

| Колонка        | Описание                          | Пример          |
|----------------|-----------------------------------|-----------------|
| last_name      | Фамилия                           | Иванов          |
| first_name     | Имя                               | Иван            |
| event_name     | Дистанция                         | 50м вольный     |
| time_seconds   | Время в формате ММ,СС,сс          | 00,28,45        |
| gender         | Пол (M / F)                       | M               |
| team           | Команда                           | ДЮСШ            |

## Пример вывода

```
==================================================
🏊 SWIMMING RESULTS ANALYZER
==================================================

📊 ОБЩАЯ СТАТИСТИКА
Всего результатов: 42
Среднее время: 34.67 сек
Лучшее время:  28.12 сек
Худшее время:  51.03 сек
```

## Автор

**Matvey Kuzovkin**  
17 лет, Уфа  
Готовлюсь к поступлению в Турцию на IT / Computer Engineering

- Telegram: [@ya_moy](https://t.me/ya_moy)
- GitHub: [matvey-kuzovkin](https://github.com/matvey-kuzovkin)
- Portfolio: [matvey-kuzovkin.github.io](https://matvey-kuzovkin.github.io)

---

# 🏊 Swimming Results Analyzer (English)

A tool for processing and analyzing swimming competition results.

This project demonstrates data handling skills: reading Excel files, cleaning data, calculating statistics, creating visualizations, and saving results.

## Features

- Reading results from Excel
- Converting time from `MM,SS,ss` format to seconds
- Calculating average, best and worst results
- Grouping by event and gender
- Creating charts
- Saving processed data

## How to run

```bash
pip install pandas openpyxl matplotlib
python main.py
```

## Author

**Matvey Kuzovkin**  
17 y.o. from Ufa, Russia  
Preparing to study Computer Engineering in Turkey

- Telegram: [@ya_moy](https://t.me/ya_moy)
- GitHub: [matvey-kuzovkin](https://github.com/matvey-kuzovkin)
- Portfolio: [matvey-kuzovkin.github.io](https://matvey-kuzovkin.github.io)
