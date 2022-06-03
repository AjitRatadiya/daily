import asyncio
import aiohttp

import time

st = time.time()
url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'


async def get_data():
    async with aiohttp.ClientSession() as session:
        for r in range(500):
            async with session.get(url) as response:
                j = await response.json()
                print(j)


asyncio.get_event_loop().run_until_complete(get_data())
et = time.time()
print("exection time:", et - st)
