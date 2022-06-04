import time
import concurrent.futures

def dis(v):

    print("before sleep")
    time.sleep(0.5)
    print("after sleep")
    return v

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor(1) as session:
        for i in range(11):
            data = session.submit(dis, i)
            print(data.result().text)

