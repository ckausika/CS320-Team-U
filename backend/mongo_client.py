from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pymongo
import string
import os

load_dotenv()
uri = os.getenv('URL')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
except Exception as e:
    print(e)

mydb = client[os.getenv('DB')]

def obj_to_list(iterator_obj : object) -> list:
    to_ret = []
    for element in iterator_obj:
        to_ret.append(element)
    return to_ret

def get_user_by_username(username: str) -> list[dict]:
    query = {"Name": {"$regex": "^"+username,"$options" :'i'}}
    users_collection = mydb["user_information"]
    result = users_collection.find(query)
    return obj_to_list(result)

def get_user_by_email(email: str) -> list[dict]:
    query = {"Email": {"$regex": "^"+email,"$options" :'i'}}
    users_collection = mydb["user_information"]
    result = users_collection.find(query)
    return obj_to_list(result)

def get_professor_by_name(name: str) -> list[dict]:
    query = {"Professor": {"$regex": "^"+name,"$options" :'i'}}
    prof_collection = mydb["professor_information"]
    result =  prof_collection.find(query)
    return obj_to_list(result)

def get_lab_by_name(name: str) -> list[dict]:
    query = {"Labs": {"$regex": "^"+name,"$options" :'i'}}
    lab_collection = mydb["labs_information"]
    result =  lab_collection.find(query) 
    return obj_to_list(result)

def get_research_area_by_name(name: str) -> list[dict]:
    query = {"Research Area": {"$regex": "^"+name,"$options" :'i'}}
    research_collection = mydb["research_areas_information"]
    result = research_collection.find(query)
    return obj_to_list(result)

def get_all_professors() -> list[dict]:
    prof_collection = mydb["professor_information"]
    result = prof_collection.find()
    return obj_to_list(result)

def get_all_labs() -> list[dict]:
    lab_collection = mydb["labs_information"]
    result = lab_collection.find()
    return obj_to_list(result)

def get_all_research_areas() -> list[dict]:
    research_collection = mydb["research_areas_information"]
    result = research_collection.find()
    return obj_to_list(result)

def get_all_users() -> list[dict]:
    users_collection = mydb["user_information"]
    result = users_collection.find()
    return obj_to_list(result)

def insert_user(email: str, name: str, pwd: str, role: str = "Student") -> object: 
    users_collection = mydb["user_information"]
    insert_id = users_collection.insert_one({"Email":email, "Name":name, "Pwd":pwd, "Role":role})
    return insert_id
