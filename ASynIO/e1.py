import aiohttp
import time
import asyncio

st = time.time()
url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"


async def get_data(session):
    async with session.get(url) as res:
        return await res.json()



async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for a in range(500):
            tasks.append(asyncio.create_task(get_data(session)))

        response = await asyncio.gather(*tasks)
        for r in response:
            print(r)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("execution time:", time.time()-st)