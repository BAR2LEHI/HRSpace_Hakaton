import csv
import json

from .redis import redis


async def load_data_to_redis():
    """Функция загрузки данных из редиса"""
    with open(
        '../app/data/job_titles.csv',
        'r', newline='',
        encoding='UTF-8'
    ) as csvfile:
        jt = csv.DictReader(csvfile,
                            delimiter=',')
        job_titles = []
        for row in jt:
            job_titles.append(row['name'])
        await redis.set('job_titles',
                        json.dumps(job_titles))
    with open(
<<<<<<< HEAD
        '../app/data/skills.csv',
        'r', newline='',
=======
        '../app/data/skills.csv', 
        'r', newline='', 
>>>>>>> dfa82200a681b7fa2968eb096b3dfec7d5dbe342
        encoding='UTF-8'
    ) as csvfile:
        sk = csv.DictReader(csvfile,
                            delimiter=',')
        skills = []
        for row in sk:
            skills.append(row['name'])
        await redis.set('skills',
                        json.dumps(skills))
    with open(
<<<<<<< HEAD
        '../app/data/specialization.csv',
        'r', newline='',
=======
        '../app/data/specialization.csv', 
        'r', newline='', 
>>>>>>> dfa82200a681b7fa2968eb096b3dfec7d5dbe342
        encoding='UTF-8'
    ) as csvfile:
        sp = csv.DictReader(csvfile,
                            delimiter=',')
        spec = []
        for row in sp:
            spec.append(row['name'])
        await redis.set('specialization',
                        json.dumps(spec))
