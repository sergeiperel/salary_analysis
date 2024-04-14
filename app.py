import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import time

df = st.cache_data(pd.read_excel)("salary.xlsx")
df.rename(columns={"Unnamed: 0":"Отрасль"}, inplace=True )
inflation = pd.read_excel("inflation.xlsx")
infl = inflation.iloc[0][2:26][::-1]
data = df.T[1:]
data["Инфляция"] = infl
data = data.rename(columns = {1: "Добыча полезных ископаемых", 2: "Строительство", 3: "Образование"})
gdp = pd.read_excel("gdp.xlsx")
gdp_row = gdp.iloc[0][0:26][::-1]


st.write(
        """
        # Анализ динамики уровня средних зарплат в разрезе по видам экономической деятельности за последние 23 года в России.
        """
    )

st.image('img.png')

st.write("### Данные о зарплатах по отраслям")
st.write(df)
st.write("### Данные об инфляции по годам")
st.write(inflation)
st.write("### Данные по ВВП в текущих ценах (на 2024г.) в млрд руб годам")
st.write(gdp)

st.sidebar.title("Описание датасета")

st.sidebar.write(
                    """
                    Датасет содержит информацию о среднемесячной номинальной начисленной заработной плате работников 
                    организаций в Российской Федерации с 2000 по 2023 годы по различным отраслям экономики.
                 
                    Каждая строка представляет год и значения заработной платы для трех отраслей: добыча полезных 
                    ископаемых, строительство и образование.
                 
                    Данные также включают годовую инфляцию и ВВП в текущих ценах (на 2024г.) в млрд руб.
                    
                    В проекте используются открытые данные из следующих источников:

                    [Сайт Росстата](https://rosstat.gov.ru/)

                    [Таблицы уровня инфляции в России](https://уровень-инфляции.рф)
                    
                    [ВВП](https://gogov.ru/articles/vvp-rf)
                    """
)

years = []
for i in range(24):
    years.append(2000 + i)

mining = df.iloc[1][1:]
construction = df.iloc[2][1:]
education = df.iloc[3][1:]

st.write("### ЗП по отраслям за 2000-2023гг.")

fig, ax = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(20)
plt.plot(years, mining, label = "Добыча полезных ископаемых", marker="o")
plt.plot(years, construction, label = "Строительство", marker="^")
plt.plot(years, education, label = "Образование", marker="s")
plt.xticks(np.arange(2000, 2024, 1.0))
plt.yticks(np.arange(2000, 150000, 10000.0))
plt.xlabel("Год", fontsize=25)
plt.ylabel("Зароботная плата", fontsize=25)
plt.legend(fontsize=25)
plt.grid()
st.pyplot(fig)

st.write(
        """
        **Выводы**
        
        - Из графика "ЗП по отраслям за 2000-2023гг." видно, что зарплаты по данным трем отраслям экономики за 
        период 2000-2023 все время росли.
        
        - Заработная плата в сфере образования увеличилась в 43 раза, в сфере строительства - в 26 раз, 
        а в сфере полезных ископаемых - в 22 раза.
        
        - В течении всего периода времени средняя зарплата работников отрасли "Добыча полезных ископаемых" выше, 
        чем у работников сферы "Строительство", а средняя зарплата работников отрасли "Строительство" выше, чем 
        у работников сферы "Образование".

        """
         )


st.write("### Динамика роста инфляции")

fig, ax1 = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(20)
plt.plot(years, infl, marker="o")
plt.xticks(np.arange(2000, 2024, 1.0))
plt.yticks(np.arange(1, 22, 1.0))
plt.xlabel("Год", fontsize=25)
plt.ylabel("Инфляция", fontsize=25)
plt.grid()
st.pyplot(fig)

data["Добыча полезных ископаемых с инфляцией"] = data["Добыча полезных ископаемых"] / (1 + data["Инфляция"] / 100)
data["Строительство c инфляцией"] = data["Строительство"] / (1 + data["Инфляция"] / 100)
data["Образование c инфляцией"] = data["Образование"]  / (1 + data["Инфляция"] / 100)
# ----------------------------------------------------------------------------------------
st.write("### Отрасли экономики с учетом инфляции и без")

mining_box1 = st.checkbox("Добыча полезных ископаемых (номинальные зп)")
# st.write(mining_box1)
construction_box1 = st.checkbox("Строительство (номинальные зп)")
# st.write(construction_box1)
education_box1 = st.checkbox("Образование (номинальные зп)")
# st.write(education_box1)
mining_box2 = st.checkbox("Добыча полезных ископаемых (реальные зп)")
# st.write(mining_box2)
construction_box2 = st.checkbox("Строительство (реальные зп)")
# st.write(construction_box2)
education_box2 = st.checkbox("Образование (реальные зп)")
# st.write(education_box1)

fig, ax2 = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(20)
if mining_box1:
    plt.plot(data.index, data["Добыча полезных ископаемых"], label="Добыча полезных ископаемых (номинальные зп)", marker="o")
if mining_box2:
    plt.plot(data.index, data["Добыча полезных ископаемых с инфляцией"], label="Добыча полезных ископаемых (реальные зп)", marker="^", linestyle="--")
if construction_box1:
    plt.plot(data.index, data["Строительство"], label="Строительство (номинальные зп)", marker="o")
if construction_box2:
    plt.plot(data.index, data["Строительство c инфляцией"], label="Строительство (реальные зп)", marker="^", linestyle="--")
if education_box1:
    plt.plot(data.index, data["Образование"], label="Образование (номинальные зп)", marker="o")
if education_box2:
    plt.plot(data.index, data["Образование c инфляцией"], label="Образование (реальные зп)", marker="^", linestyle="--")
plt.plot(data.index, data[0], label="Средняя зарплпта по всей России", marker="o")

plt.xticks(np.arange(2000, 2024, 1.0))
plt.yticks(np.arange(2000, 150000, 10000.0))
plt.xlabel('Год', fontsize=25)
plt.ylabel('Заработанная плата', fontsize=25)
plt.legend(fontsize=25)
plt.grid()
st.pyplot(fig)

data_change = data
data_change["Добыча полезных ископаемых с инфляцией (пред.)"] = data["Добыча полезных ископаемых с инфляцией"].shift(1)
data_change["Строительство c инфляцией (пред.)"] = data["Строительство c инфляцией"].shift(1)
data_change["Образование c инфляцией (пред.)"] = data["Образование c инфляцией"].shift(1)
data_change["Влияние инфляции на Добычу полезных ископаемых"] = (data_change["Добыча полезных ископаемых с инфляцией"] / data_change["Добыча полезных ископаемых с инфляцией (пред.)"] - 1) * 100
data_change["Влияние инфляции на Строительство"] = (data_change["Строительство c инфляцией"] / data_change["Строительство c инфляцией (пред.)"] - 1) * 100
data_change["Влияние инфляции на Образование"] = (data_change["Образование c инфляцией"] / data_change["Образование c инфляцией (пред.)"] - 1) * 100


st.write("### Влияние инфляции на изменение зарплаты по сравнению с предыдущим годом в период 2000-2023гг.")

fig, ax2 = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(20)

plt.plot(data_change.index, data_change["Влияние инфляции на Добычу полезных ископаемых"], label="Добыча полезных ископаемых", marker="o")
plt.plot(data_change.index, data_change["Влияние инфляции на Строительство"], label="Строительство", marker="^")
plt.plot(data_change.index, data_change["Влияние инфляции на Образование"], label="Образование", marker="s")
plt.plot(data_change.index, data_change["Инфляция"], label="Годовая инфляция", marker="+")
plt.xticks(np.arange(2000, 2024, 1.0))
plt.yticks(np.arange(0, 70, 5.0))
plt.xlabel('Год', fontsize=25)
plt.ylabel('Заработанная плата', fontsize=25)
plt.legend(fontsize=25)
plt.grid()
st.pyplot(fig)

st.write(
    """
    **Выводы**

    - Практически во все годы заработные платы опережают темпы инфляции.

    - В некоторые годы, а именно в 2009, 2010, 2014, 2015, 2020, 2022 годы можно заметить, что темпы инфляции 
    опережают изменения в заработных платах.

    - Данные наблюдения можно объяснить различными кризисами, нестабильной ситуацией в стране и мире или 
    другими экономическими факторами.

    """
)

data["ВВП"] = gdp_row
data.drop(['Добыча полезных ископаемых с инфляцией (пред.)', 'Строительство c инфляцией (пред.)', 'Образование c инфляцией (пред.)', 0], axis= 1 , inplace= True )


st.write("### Дополнительные исследования: корреляционная матрица")


fig, ax = plt.subplots()
sns.heatmap(data.corr(), ax=ax, cmap='coolwarm')
st.write(fig)

st.write(
    """
    **Выводы**

    - Из корреляцилнной матрицы видно, что существует тесная связь между зарплатами в России и уровнем ВВП, что 
    говорит о том, что экономический рост влияет на увеличение доходов работников всех отраслей экономики.
    
    - Те же наблюдения можно констатировать и для зарплат с учетом инфляции.

    - Также наблюдается обратно пропорциональная зависимость между годовой инфляцией и всеми зарплатами по отраслям, а 
    также годовой инфляцией и ВВП. Это означает, что инфляция растет, а зарплаты снижатся. Инфляция растет, 
    а ВВП падает.
    
    - Также видна положительная корреляция между показателями инфляции и влиянием инфляции на изменение заработных 
    плат по сравнению с предыдущим годом.

    """
)
