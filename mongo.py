#載入pymongo
import pymongo
from bson.objectid import ObjectId
#連線到 mongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://karta1376136:geac1864@mydata.yasgy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# 把資料放進資料庫中
db = client.website #選擇操作 XXX 資料庫
collection = db.users #選擇操作 XXX 集合

#篩選集合中的文件資料
# doc = collection.find_one({
#     "email":"karta1376146@yahoo.com.tw"
# })
# print("取得的資料的名字欄位",doc["name"])

#複合篩選條件
# doc = collection.find_one({
#     "$and":[
#         {"email":"karta1376146@yahoo.com.tw"},
#         {"password":"abc787"}
#     ]
# })
# print("取得的資料",doc)

#篩選結果排序
cur = collection.find({
    "$or":[
        {"level":"2"},
        {"email":"karta1176136@yahoo.com.tw"}
    ]
},sort=[
    ("level", pymongo.ASCENDING)
])
for doc in cur:
    print(doc)

#刪除集合中的一筆文件資料
# result = collection.delete_one({
#     "email":"karta1376136@yahoo.com.tw"
# })
# print("實際上刪除的資料有幾筆",result.deleted_count)

#刪除集合中的多筆文件資料
# result = collection.delete_many({
#     "level":4
# })

# print("符合條件的文件數量",result.deleted_count)


#更新集合中的一筆文件資料
# result = collection.update_one({
#     "email":"karta1376136@yahoo.com.tw"
# },{
#     "$mul":{
#         "level":0.5
#     }
# })
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)

#更新集合中的多筆文件資料
# result = collection.update_many({
#     "level":4
# },{
#     "$set":{
#         "level":4
#     }
# })
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)

#取得集合中的第一筆文件資料
#data=collection.find_one()
#print(data)

#根據objectID取得文件資料
# data = collection.find_one(ObjectId("626e48f936c740bb3f55035a"))
# print(data)

# #取得文件資料中的欄位
# print(data["_id"])
# print(data["email"])

#一次取得多筆文件資料
# cursor = collection.find()
# print(cursor)
# for doc in cursor:
#     print(doc["name"])

#一次新增多筆資料，取得多筆資料的編號
# result = collection.insert_many([{
#     "name":"小787",
#     "email":"karta1376146@yahoo.com.tw",
#     "password":"abc7787",
#     "level":2
# },{
#     "name":"7778",
#     "email":"karta1176136@yahoo.com.tw",
#     "password":"abc8117",
#     "level":4
# }])

# #把資料新增到集合中，取得新增資料的編號
# result = collection.insert_one({
#     "name":"小宇",
#     "email":"karta1376136@yahoo.com.tw",
#     "password":"abc87",
#     "level":2
# })

#print("資料新增成功")
#print(result.inserted_ids)