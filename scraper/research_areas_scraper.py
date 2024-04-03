import requests 
from bs4 import BeautifulSoup 
import csv 

profs = []
labs = []
desc = []
URLs  = ["artificial-intelligence", "computational-biology-and-bioinformatics", "data-management",
             "electronic-teaching", "health-informatics", "human-language-technologies","human-computer-interaction",
             "information-visualization", "machine-learning", "mobile-and-sensor-systems", "networking-and-distributed-systems",
             "quantum-information-systems", "robotics-computer-vision-and-graphics", "security-and-privacy", "software-systems-and-architecture",
             "theoretical-computer-science"]

def update_profs(soup):
    main_page = soup.find('div', attrs={'id':'block-views-research-areas-block-2'})
    faculty = main_page.find_all('a')
    curr_area = []
    for member in faculty:
        curr_prof = member.text
        curr_prof = curr_prof.split(",")[0]
        curr_area.append(curr_prof)
    profs.append(curr_area)

def update_labs(soup):
    main_page = soup.find('div', attrs={'id':'block-views-research-areas-block-3'})
    if (main_page == None):
        labs.append([])
        return
    laboratories = main_page.find_all('a')
    curr_area = []
    for lab in laboratories:
        curr_area.append(lab.text)
    labs.append(curr_area)
   
def update_desc(soup):
    main_page = soup.find('div', attrs={'id': 'block-system-main'})
    curr_desc = main_page.find('p')
    if (curr_desc == None):
        desc.append("")
        return
    desc.append(curr_desc.text)

def writeToCSV(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Research Area", "Description", "Professors", "Labs"])
        for i in range(0, len(URLs)):
            curr_area = " ".join(URLs[i].split("-")).capitalize()
            curr_desc = desc[i]
            curr_profs = ", ".join(profs[i])
            curr_labs = ", ".join(labs[i])
            writer.writerow([curr_area, curr_desc, curr_profs, curr_labs])
        print("Wrote results to CSV file")

def main():
    base_URL = "https://www.cics.umass.edu/research/area/"

    for URL in URLs: 
        full_URL = base_URL + URL
        r = requests.get(full_URL) 
        soup = BeautifulSoup(r.content, 'html.parser') 
        update_profs(soup)
        update_labs(soup)
        update_desc(soup)
    
    writeToCSV("research_areas.csv")

if __name__ == "__main__":
    main()