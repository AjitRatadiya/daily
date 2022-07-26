import pickle
f=open("f.txt", "rb")
l=[1,2,3,4]
a=pickle.load(f)
print(a)
f.close()
