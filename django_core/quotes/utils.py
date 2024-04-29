from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://pavlokorjov9200:jx0UR4Y8LBDBeGSl@cluster0.44nxlqc.mongodb.net/")
    db = client.test
    return db
