
import pandas as pd

# l = ["a", "b", "c", "d"]
# s1=pd.Series(l,index=[1, 2, 3, 4])

# # print(s1)

# l1 = [{"a":1, "b":2}, {"c":3, "d":4}]
# df1 = pd.DataFrame(l1)

# print(df1)

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv',nrows=3)
# print(csv1)

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv',header=0)
# print(csv1)

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv',index_col=0)
# print(csv1)

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv',skiprows=1)
# print(csv1)

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv',prefix="$", header=None)
# print(csv1)

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.head(2))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.tail(2))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.fillna(method="bfill"))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.fillna({"name":"not given","age":"not born"}))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.replace(to_replace="a",value="A"))

# csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.replace(["a","b","v"],["A","B","C"]))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.replace({"name":"a","class":"a"},"A"))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.replace(11,method="bfill"))

csv1 = pd.read_csv('C://Users/SMART/PycharmProjects/Basic/a1.csv')
# print(csv1.interpolate())

d1={"id":[1,2,3,4],"name":["aj","bj","cj","ej"]}

d2={"id":[1,2,3,4],"class":["bj","bj","bj","bj"]}

