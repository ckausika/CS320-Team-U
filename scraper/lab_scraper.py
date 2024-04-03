import requests 
from bs4 import BeautifulSoup 
import csv 

labs = []
profs = []
body = []
labs_with_no_faculty = ["Digital Forensics Laboratory", "Laboratory in Kine(ma)tics and Geometry (LinKaGe)"]

def update_lab_names(page):
    for lab in page.find_all('h3')[1:]:
        labs.append(lab.text.strip())
    labs.remove("Research Centers")
    labs.remove("Research Labs and Groups")

def update_professor_labs(page):
    labs = page.find_all('div', attrs={'class':'view-content'})
    for lab in labs: 
        temp = []
        professors = lab.find_all('a')
        for prof in professors: 
            temp.append(prof.text)
        profs.append(temp)

def update_body(page):
    paras = page.find_all('p')
    for para in paras:
        body.append(para.text)
    body.remove("Please visit CenterforKnowledgeCommunication.org for more details.")

def writeToCSV(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Labs", "Description", "Professors"])
        for i in range(0, len(labs)):
            if (labs[i] in labs_with_no_faculty):
                profs.insert(i, [])
            writer.writerow([labs[i], body[i],", ".join(profs[i])])
        print("Wrote results to CSV file")

def main():
    URL = "https://www.cics.umass.edu/research/research-groups" 
    r = requests.get(URL) 
   
    soup = BeautifulSoup(r.content, 'html.parser') 

    main_page = soup.find('div', attrs={'id':'block-views-research-groups-block'}).find('div', attrs={'class': 'view-content'})
    update_lab_names(main_page)
    update_professor_labs(main_page)
    update_body(main_page)
    writeToCSV("labs.csv")


if __name__ == "__main__":
    main()