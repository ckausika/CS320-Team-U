from mongo_client import insert_opportunity

# Create an account given a username and password
def createOpportunity(title, firstName, lastName, emailAddress, jobTitle, expectedTime, location, jobDescription):
    # Insert a new opportunity in the database
    insert_opportunity(title, firstName, lastName, emailAddress, jobTitle, expectedTime, location, jobDescription)
    # Return a success response
    return True
