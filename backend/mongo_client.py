from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pymongo
import string
import os

# Load environment variables from a .env file
load_dotenv()
# Get the MongoDB URI from environment variables
uri = os.getenv('URL')

# Create a new MongoDB client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to the server to confirm a successful connection
try:
    client.admin.command('ping')
except Exception as e:
    print(e)

# Get a reference to the specific database
mydb = client[os.getenv('DB')]

def obj_to_list(iterator_obj: object) -> list:
    """
    Converts an iterator object to a list.
    
    Args:
        iterator_obj (object): The iterator object to convert.
    
    Returns:
        list: The converted list.
    """
    to_ret = []
    for element in iterator_obj:
        to_ret.append(element)
    return to_ret

def get_user_by_username(username: str) -> list[dict]:
    """
    Retrieves user documents from the 'user_information' collection by username.
    
    Args:
        username (str): The username to search for.
    
    Returns:
        list[dict]: A list of user documents that match the username.
    """
    query = {"Name": {"$regex": "^" + username, "$options": 'i'}}
    users_collection = mydb["user_information"]
    result = users_collection.find(query)
    return obj_to_list(result)

def get_user_by_email(email: str) -> list[dict]:
    """
    Retrieves user documents from the 'user_information' collection by email.
    
    Args:
        email (str): The email to search for.
    
    Returns:
        list[dict]: A list of user documents that match the email.
    """
    query = {"Email": {"$regex": "^" + email, "$options": 'i'}}
    users_collection = mydb["user_information"]
    result = users_collection.find(query)
    return obj_to_list(result)

def get_professor_by_name(name: str) -> list[dict]:
    """
    Retrieves professor documents from the 'professor_information' collection by name.
    
    Args:
        name (str): The professor's name to search for.
    
    Returns:
        list[dict]: A list of professor documents that match the name.
    """
    query = {"Professor": {"$regex": "^" + name, "$options": 'i'}}
    prof_collection = mydb["professor_information"]
    result = prof_collection.find(query)
    return obj_to_list(result)

def get_lab_by_name(name: str) -> list[dict]:
    """
    Retrieves lab documents from the 'labs_information' collection by lab name.
    
    Args:
        name (str): The lab name to search for.
    
    Returns:
        list[dict]: A list of lab documents that match the lab name.
    """
    query = {"Labs": {"$regex": "^" + name, "$options": 'i'}}
    lab_collection = mydb["labs_information"]
    result = lab_collection.find(query)
    return obj_to_list(result)

def get_research_area_by_name(name: str) -> list[dict]:
    """
    Retrieves research area documents from the 'research_areas_information' collection by name.
    
    Args:
        name (str): The research area name to search for.
    
    Returns:
        list[dict]: A list of research area documents that match the name.
    """
    query = {"Research Area": {"$regex": "^" + name, "$options": 'i'}}
    research_collection = mydb["research_areas_information"]
    result = research_collection.find(query)
    return obj_to_list(result)

def get_all_professors() -> list[dict]:
    """
    Retrieves all professor documents from the 'professor_information' collection.
    
    Returns:
        list[dict]: A list of all professor documents.
    """
    prof_collection = mydb["professor_information"]
    result = prof_collection.find()
    return obj_to_list(result)

def get_all_labs() -> list[dict]:
    """
    Retrieves all lab documents from the 'labs_information' collection.
    
    Returns:
        list[dict]: A list of all lab documents.
    """
    lab_collection = mydb["labs_information"]
    result = lab_collection.find()
    return obj_to_list(result)

def get_all_research_areas() -> list[dict]:
    """
    Retrieves all research area documents from the 'research_areas_information' collection.
    
    Returns:
        list[dict]: A list of all research area documents.
    """
    research_collection = mydb["research_areas_information"]
    result = research_collection.find()
    return obj_to_list(result)

def get_all_users() -> list[dict]:
    """
    Retrieves all user documents from the 'user_information' collection.
    
    Returns:
        list[dict]: A list of all user documents.
    """
    users_collection = mydb["user_information"]
    result = users_collection.find()
    return obj_to_list(result)

def insert_opportunity(Title, firstName, lastName, emailAddress, jobTitle, expectedTime, location, jobDescription):
    """
    Inserts a new opportunity document into the 'opportunities_information' collection.
    
    Args:
        Title (str): The title of the opportunity.
        firstName (str): The first name of the contact person.
        lastName (str): The last name of the contact person.
        emailAddress (str): The email address of the contact person.
        jobTitle (str): The job title related to the opportunity.
        expectedTime (str): The expected time commitment.
        location (str): The location of the opportunity.
        jobDescription (str): A description of the job.
    
    Returns:
        ObjectId: The ID of the inserted document.
    """
    opp_collection = mydb["opportunities_information"]
    insert_id = opp_collection.insert_one({
        "Title": Title, 
        "firstName": firstName, 
        "lastName": lastName, 
        "emailAddress": emailAddress, 
        "jobTitle": jobTitle, 
        "expectedTime": expectedTime, 
        "location": location, 
        "jobDescription": jobDescription
    })
    return insert_id

def insert_user(email: str, name: str, pwd: str, role: str = "Student") -> object:
    """
    Inserts a new user document into the 'user_information' collection.
    
    Args:
        email (str): The email address of the user.
        name (str): The name of the user.
        pwd (str): The password of the user.
        role (str): The role of the user, default is "Student".
    
    Returns:
        ObjectId: The ID of the inserted document.
    """
    users_collection = mydb["user_information"]
    insert_id = users_collection.insert_one({"Email": email, "Name": name, "Pwd": pwd, "Role": role})
    return insert_id
