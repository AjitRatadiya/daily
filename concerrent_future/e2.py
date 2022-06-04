import time
import concurrent.futures
import requests

st = time.time()


def get_data(url):
    d = []
    for i in range(100):
        res = requests.get(url)
        d.append(res.json())
    return d


if __name__ == '__main__':
    url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'

    with concurrent.futures.ThreadPoolExecutor(1) as exe:
        data = exe.submit(get_data, url)
        for i in data.result():
            print(i)
        print("total time:", time.time() - st)
