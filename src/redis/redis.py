from redis import asyncio as aioredis

redis = aioredis.from_url(
        'redis://localhost:6379',
        encoding='utf8',
        decode_responses=True
    )
