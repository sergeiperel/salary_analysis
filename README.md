## Анализ динамики уровня средних зарплат в разрезе по видам экономической деятельности за последние 23 года в России.

В проекте используются открытые данные из официальных источников:

[Сайт Росстата](https://rosstat.gov.ru/)

[Таблицы уровня инфляции в России](https://уровень-инфляции.рф)

### Описание файлов в проекте

- `gdp.xlsx`: файл с ВВП
- `inflation.xlsx`: файл с инфляцией
- `salary.xlsx`: файл сл средними зарплатами по отраслям экономики
- `salary_analysis.ipynb`: ноутбук с анализом данных
- `app.py`: файл приложения streamlit

### Описание датасета:

Датасет содержит информацию о среднемесячной номинальной начисленной заработной плате работников организаций в Российской Федерации с 2000 по 2023 годы по различным отраслям экономики.

Каждая строка представляет год и значения заработной платы для трех отраслей: добыча полезных ископаемых, строительство и образование.

Данные также включают годовую инфляцию и ВВП в текущих ценах (на 2024г.) в млрд руб.

__**[Streamlit-приложение можно посмотреть тут!](https://salaryanalysis.streamlit.app/)**__

### Запуск приложения локально

Для запуска Streamlit локально непосредственно в корневой папке репозитория выполните следующее:

```Командная строка
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ streamlit run app.py
```
Откройте http://localhost:8501, чтобы просмотреть приложение.