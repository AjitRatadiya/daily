import pymongo
import pandas as pd

# DAtabase connection
db = pymongo.MongoClient("mongodb://localhost:27017")
tb = db["student"]
c = tb.result
c.insert_one({"name":"ajit", "rollno":1, "maths":45, "science":78, "english":72})
#data retrieving
# d = pd.read_csv("../simple/a1.csv")
# # d = d.to_json()
# c.insert_one({"no": 1, "name": "nakum", "city": "rajkot"})




# import pymongo
#
# db = pymongo.MongoClient("mongodb://localhost:27017")
# tb = db["tata"]
# c = tb.tcs
# d=c.find_one({"name":"ganesh"})
# print(d)
# cd = c.find({})
# print([a for a in cd])
# # c.insert_one({"name":"prakash","age":34})