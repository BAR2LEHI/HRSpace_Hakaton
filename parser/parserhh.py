import requests
import pandas as pd
import os


def get_data(job, pages=10):
    """
    Получает данные о вакансиях с HH API.
    job (str): Название вакансии для поиска.
    pages (int, optional): Количество страниц результатов для получения. По умолчанию 10.
    """
    url = 'https://api.hh.ru/vacancies'
    data = []
    for i in range(pages):
        par = {'text': job, 'per_page': '50', 'page': i}
        r = requests.get(url, params=par)
        data.append(r.json())
    return data


def process_data(data):
    """
    Обрабатывает данные о вакансиях и преобразует их в pandas DataFrame.
    data (list): Данные о вакансиях для обработки.
    DataFrame: pandas DataFrame, содержащий обработанные данные.
    """
    df = pd.DataFrame(columns=['name', 'salary', 'city'])
    for i, d in enumerate(data):
        for j, item in enumerate(d['items']):
            name = item['name']
            salary = item['salary']['from'] if item['salary'] is not None else None
            city = item['area']['name'] if 'area' in item and item['area'] is not None else None
            if salary is not None:
                df.loc[len(df)] = [name, salary, city]
    df['salary'] = pd.to_numeric(df['salary'], downcast='integer')
    return df


def save_data(df, job):
    """
    Сохраняет данные о средней зарплате в файл CSV.
    df (DataFrame): DataFrame, содержащий данные о зарплате.
    job (str): Название вакансии.
    """
    directory = job
    if not os.path.exists(directory):
        os.makedirs(directory)
    avg_salary_name = os.path.join(directory, f"avg{job}.csv")
    with open(avg_salary_name, 'w', encoding='utf-8') as f:
        f.write(f"Средняя зарплата по всей России: {round(df['salary'].mean())}\\n")


def main():
    """
    Главная функция, которая организует получение, обработку и сохранение данных.
    """
    job_title = ["UI"]  # Название профессии
    for job in job_title:
        data = get_data(job)
        df = process_data(data)
        save_data(df, job)
        print(f"Данные {job} успешно извлечены. Найдено {len(df)} вакансий.")


if __name__ == "__main__":
    main()
