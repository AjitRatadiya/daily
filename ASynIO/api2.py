import aiohttp
import asyncio
import time

start_time = time.time()


async def get_data(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon


async def main():

    async with aiohttp.ClientSession() as session:
        url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
        tasks = []
        for number in range(100):
            tasks.append(asyncio.ensure_future(get_data(session, url)))

        data = await asyncio.gather(*tasks)
        for d in data:
            print(d)


asyncio.get_event_loop().run_until_complete(main())
print("execution time:", time.time()-start_time)