import pandas

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.


def main():
    file = pandas.read_csv('california_housing_test.csv')
    print(file[file['population'] < 500][['median_house_value']].median()) #Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
    print(file[file['population'] == file['population'].min()][['households']].max()) # Задача 42: Узнать какая максимальная households в зоне минимального значения population.


if __name__=='__main__':
    main()