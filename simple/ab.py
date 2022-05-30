import pymongo

mydb=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

db=mydb["emp"]
c=db.collection
d={
    "name":"ganesh",
    "age":14,
    "class":10
}

# c.find()          #find
# c.insert_one(d)  #insert_many()
#
# c.update_one({"firstname":"parsotam"},            #update_many()
#              {"$set":{"lastname":"prabhari"}})
#
# c.replace_one({"firstname":"parsotam"},
#               {"firstname":"sprin","lastname":"boot","age":17})
#
# c.delete_one({"firstname":"mahabali"})
# c.delete_many({})


# import pymongo
#
# db=pymongo.MongoClient("mongodb+srv://dbfirst:12345@first.uso7i.mongodb.net/test") #for atlas
# tb=db["rec"]
# c=tb.stu
# data={
#     "name":"prabhas",
#     "class":5,
#     "age":10
# }
# c.insert_one(data)