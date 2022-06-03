import pandas as pd

def pandaFun():
    df=pd.read_csv("../85/b1.csv")
    d1 =pd.DataFrame({"id": [1, 2, 3, 4], "name": ["aj", "bj", "cj", "ej"]})
    d2 =pd.DataFrame({"id": [1, 2, 3, 4], "class": ["bj", "bj", "bj", "bj"]})
    d3 = [{"a":1, "b":2}, {"c":3, "d":4}]

    # v = pd.DataFrame(df) #columns=["name", "id", "email"]
    # print(v)
    # a = v.groupby("age").get_group(23)
    # print(a)
    con = pd.concat([d1, d2], axis=1)

    print(con)
# def getTotalCount(dfl):
#     total = dfl['id']
#     return total


pandaFun()