import requests
import threading
import time

st = time.time()
def print_data():
    url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
    t1 = requests.get(url)
    print(t1.json())

def get_data():

    for r in range(500):
        threading.Thread(target=print_data).start()

get_data()

et = time.time()
print("exection time:", et-st)