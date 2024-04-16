from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pymongo
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

def get_user_by_username(username: str) -> dict:
    users_collection = mydb["user_information"]
    return users_collection.find_one({"Username":username})

def get_user_by_email(email: str) -> dict:
    users_collection = mydb["user_information"]
    return users_collection.find_one({"Email":email})

def get_professor_by_name(name: str) -> dict:
    prof_collection = mydb["professor_information"]
    formatted_name = name.split(" ")[1] + ", " + name.split(" ")[0]
    print(formatted_name)
    return prof_collection.find_one({"Professor": formatted_name})

def get_lab_by_name(name: str) -> dict:
    lab_collection = mydb["labs_information"]
    return lab_collection.find_one({"Labs":name}) 

def get_research_area_by_name(name: str) -> dict:
    research_collection = mydb["research_areas_information"]
    return research_collection.find_one({"Research Area":name})

def get_all_professors():
    prof_collection = mydb["professor_information"]
    return prof_collection.find()

def get_all_labs():
    lab_collection = mydb["labs_information"]
    return lab_collection.find()

def get_all_research_areas():
    research_collection = mydb["research_areas_information"]
    return research_collection.find()

def get_all_users():
    users_collection = mydb["user_information"]
    return users_collection.find()

   


