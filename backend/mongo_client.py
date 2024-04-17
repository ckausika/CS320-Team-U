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

def get_all_professors() -> list[dict]:
    prof_collection = mydb["professor_information"]
    profs = []
    for prof in prof_collection.find():
        profs.append(prof)
    return profs

def get_all_labs() -> list[dict]:
    lab_collection = mydb["labs_information"]
    labs = []
    for lab in lab_collection.find():
        labs.append(lab)
    return labs

def get_all_research_areas() -> list[dict]:
    research_collection = mydb["research_areas_information"]
    research_areas = []
    for area in research_collection.find():
        research_areas.append(area)
    return research_areas

def get_all_users() -> list[dict]:
    users_collection = mydb["user_information"]
    users = []
    for user in users_collection.find():
        users.append(user)
    return users


def insert_user(email: str, name: str, pwd: str, role: str = "Student") -> object: 
    users_collection = mydb["user_information"]
    insert_id = users_collection.insert_one({"Email":email, "Name":name, "Pwd":pwd, "Role":role})
    return insert_id


