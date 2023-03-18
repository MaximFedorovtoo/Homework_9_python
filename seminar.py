import pandas



# Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
# Посмотреть сколько в нем строк и столбцов
# Определить какой тип данных имеют столбцы
# Проверить есть ли в файле пустые значения
# Показать median_house_value где median_income < 2
# Показать данные в первых 2 столбцах
# Выбрать данные где housing_median_age < 20 и median_house_value > 70000
# Определить какое максимальное и минимальное значение median_house_value
# Показать максимальное median_house_value, где median_income = 3.1250
# Узнать какая максимальная population в зоне минимального значения median_house_value

file = pandas.read_csv('california_housing_test.csv')
colums = file.columns


def print_head(n = 10)-> list():
    return file.head(n) # первые 10 элементов
def print_tall(n = 10)-> list():
    return file.tail(n) # последние 10 элементов 
def size()-> list():
    return file.shape # количества строк и столбцов
def find_null()-> list():
    return file.isnull().sum() # поиск стоки с пустым значением
def type_data():
    return file.dtypes # проверка какой тип данных имеют столбцы
print(file[file['median_income'] < 2]['median_house_value']) # Показать median_house_value где median_income < 2
print(file[['longitude', 'latitude']])# Показать данные в первых 2 столбцах
print(file[(file['housing_median_age'] < 20) & (file['median_house_value'] > 70000)][['housing_median_age','median_house_value']]) #Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(file[['median_house_value']].min()) # Определить какое максимальное и минимальное значение median_house_value
print(file[['median_house_value']].max())
max_median_house_value = file[['median_house_value']].max()
print(file[file['median_income'] == 3.1250]['median_house_value'].max())# Показать максимальное median_house_value, где median_income = 3.1250
print(file[file['median_house_value'] == file['median_house_value'].min()][['population']])# Узнать какая максимальная population в зоне минимального значения median_house_value
print(print_head())
