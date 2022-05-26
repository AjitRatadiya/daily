import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")
tb = db["tata"]
c = tb.tcs
d=c.find_one({"name":"ganesh"})
print(d)
cd = c.find({})
print([a for a in cd])
# c.insert_one({"name":"prakash","age":34})