import asyncio
from asyncio import tasks
from time import time

import aiohttp


# use sinchronous function is no good idea, is there only for illustration
def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)
