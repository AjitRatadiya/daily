import pymongo
import gridfs

db = pymongo.MongoClient("mongodb://localhost:27017")
tb = db["users"]

fs = gridfs.GridFS(tb)
#
file_name = "copy.png"
# file = open("../static/copy.png", "rb")
# file_data = file.read()

'''****** uploading file in database'''
#
# fs.put(file_data, filename=file_name)
# print("complete")


'''****** retriving data from database****'''

id = tb.fs.files.find_one({"filename":file_name})["_id"]
data = fs.get(id).read()

f = open("../mongo_db/"+file_name, "wb")
f.write(data)
f.close()
print("got")