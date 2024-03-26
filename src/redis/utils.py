import csv
import json

from .redis import redis


async def load_data_to_redis():
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
        '../app/data/skills.csv', 
        'r', newline='', 
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
        '../app/data/specialization.csv', 
        'r', newline='', 
        encoding='UTF-8'
    ) as csvfile:
        sp = csv.DictReader(csvfile, 
                            delimiter=',')
        spec = []
        for row in sp:
            spec.append(row['name'])
        await redis.set('specialization', 
                        json.dumps(spec))
