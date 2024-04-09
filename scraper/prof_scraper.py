#Python program to scrape website  
import requests 
from bs4 import BeautifulSoup 
import csv 
   
profs = []  # global list to store professors
links = [] # global list to store links
pos = [] # global list to store positions
emails = [] # global list to store emails
phones = [] # global list to store phone numbers
locs = [] # global list to store office locations

def callAll(element):
    """ Calls all the functions for a given beautifulSoup element
    Args: 
        element: BeautifulSoup Element
    Returns: None 
    """
    addProfandLink(element)
    addPosition(element)
    addEmail(element)
    addPhone(element)
    addLocation(element)

def addProfandLink(element):
    """ Populates the professors list with the professor and their homepage link for a given beautifulSoup element
    Args: 
        element: BeautifulSoup Element
    Returns: None 
    """
    professor = element.find('div', attrs = {'class': 'views-field views-field-title'})
    a = professor.find("a")
    profs.append(a.text)
    links.append("https://www.cics.umass.edu"+a['href'])

def addPosition(element):
    """ Populates the pos list with the positions of a professor for a given beautifulSoup element
    Args: 
        element: BeautifulSoup Element
    Returns: None 
    """
    position = element.find('div', attrs = {'class': 'views-field views-field-field-position'})
    pos.append(str(position.text).strip())

def addEmail(element):
    """ Populates the emails list with the emails of a professor for a given beautifulSoup element
    Args: 
        element: BeautifulSoup Element
    Returns: None 
    """
    try: 
        e_address = element.find('div', attrs = {'class': 'views-field views-field-field-email'})
        a = e_address.find("a")
        emails.append(a.text)
    except: 
        emails.append("NA") # placeholder for unavailable information

def addPhone(element):
    """ Populates the phones list with the phone numbers of a professor for a given beautifulSoup element
    Args: 
        element: BeautifulSoup Element
    Returns: None 
    """
    try:
        number = element.find('div', attrs = {'class': 'views-field views-field-field-phone'})
        phones.append(str(number.text).removeprefix(" P:     "))
    except:
        phones.append("NA") # placeholder for unavailable information 

def addLocation(element):
    """ Populates the locs list with the office location of a professor for a given beautifulSoup element
    Args: 
        element: BeautifulSoup Element
    Returns: None 
    """
    try:
        location = element.find('div', attrs = {'class': 'views-field views-field-field-location'})
        span = location.find('span', attrs={"class": "field-content"})
        locs.append(span.text)
    except:
        locs.append("NA") # placeholder for unavailable information

def writeToCSV(filename):
    """ Writes the values in the global lists to a CSV file
    Args:
        filename: Name of the file to write to
    Returns: None 
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Professor", "Homepage Link", "Position", "Email", "Phone", "Office Location"])
        for i in range(0, len(profs)):
            writer.writerow([profs[i], links[i], pos[i], emails[i], phones[i], locs[i]])
        print("Wrote results to CSV file")


def main():

    URL = "https://www.cics.umass.edu/people/all-faculty-staff" 
    r = requests.get(URL) 
   
    soup = BeautifulSoup(r.content, 'html.parser') 

    main_page = soup.find('div', attrs={'id':'block-system-main'})
    alphabets = main_page.find_all('div', attrs={'class': 'clearfix'})

    for alphabet in alphabets:
        j = 1
        while(True):
            oddoreven = "even" if j % 2 == 0 else "odd" 
            oddoreven = oddoreven + " views-row-first" if j == 1 else oddoreven
            cls = "views-row views-row-"+str(j)+" views-row-"+oddoreven+" col-xs-6 equalheight"   
            try:
                element = alphabet.find('div', attrs = {'class': cls})
                if (element is None):
                    raise Exception
                callAll(element)
                j+= 1
            except Exception: # for the last block in the div
                if j == 1:
                    cls =  "views-row views-row-1 views-row-odd views-row-first views-row-last col-xs-6 equalheight"
                else:
                    oddoreven = "even views-row-last" if j % 2 == 0 else "odd views-row-last"
                    cls = "views-row views-row-"+str(j)+" views-row-"+oddoreven+" col-xs-6 equalheight"  
                element = alphabet.find('div', attrs = {'class': cls})
                callAll(element)
                break
    
    if (len(profs) != len(links) or len(profs) != len(pos) or len(profs) != len(emails) or len(profs) != len(phones) or len(profs) != len(locs)):
        raise Exception("ERROR: Scraping lengths unequal") # throw error if lengths are unequal
    
    print("TOTAL PROFS: ", len(profs))

    writeToCSV("faculty.csv")

if __name__ == "__main__":
    main()

