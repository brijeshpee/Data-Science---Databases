
import pymongo 
import urllib 

username = urllib.parse.quote_plus('****')
password = urllib.parse.quote_plus('****')
client = pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.hchsr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" % (username, password))
db = client.test
print(db)


#1. db
db1=client['customers']

#2. Reading database
client.list_database_names()

#3. Creating a table

col1=db1["customer_demo"]

#4. Creating Dict

dict1 ={"name" : "brijesh",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com"}
col1.insert_one(dict1)

dict2 ={"name" : "brijesh",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com",
       "phone":"01010100101"}
col1.insert_one(dict2)

mylist=[{"name" : "brijesh",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com"},
        {"name" : "rajesh",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com"},
        {"name" : "jitendra",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com"},
        {"name" : "mahendra",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com"},
        {"name" : "rajendra",
       "email" : "bp@gmail.com",
       "product":["one","two","three"],
       "www": "www.bp.com"}
        ]
col1.insert_many(mylist)

#########################################################
# fetching the records
#########################################################

#q1:
for i in col1.find():
    print(i)

#q2:        
for i in col1.find({"name" : "rajendra"}):
    print(i)

#q3:    
for i in col1.find({"name" : {"$in": ["raj","dsdsd"]}}):
    print(i)

#########################################################
# other code
#########################################################

#q4:  fetching greater and lesser 
col1.find({"name" : "rajendra"}).pretty()

#q5:  fetching greater and lesser     
for i in col1.find({"qty" :{'$gt' :25}}):
    print(i)

#########################################################
# update document
#########################################################

#q6: updating the document
col1.update_many({"name":'brijesh'},{"$set":{"name":'brijesh kumar'}})

#q7: printint selected sample
for i in col1.find().limit(2):
    print(i)

#q8: fetching less than eq to
for i in col1.find({'qty':{"$not":{"$lte": 100}}}):
    print(i)

#q9: 
col1.delete_many({"name" : "rajendra"})


    