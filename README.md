
# CICS Undergraduate Research Finder - CS320 Team U

This web application allows undergraduate students and professors at UMass Amherst to connect over research opportunities. Students can search for professors and labs that are offering research projects. They can view professors' research interests, affiliated labs, and past and ongoing projects. Students can easily contact professors through the application by sharing their research profile, experience, resume, etc. Professors can post information about ongoing research projects and recruit students through the application by viewing their respective research profiles.


## Team
Project Manager: Pablo Almeida - [@pabloooooo](https://www.github.com/pabloooooo)

**Front End Team:**
- Shrey Bahadur - [@shreyBaha](https://www.github.com/shreyBaha)
- Attila Palabiyik - [@attilapalabiyik](https://www.github.com/attilapalabiyik)
- Srihari Srivatsa - [@ss9214 ](https://www.github.com/ss9214 )
- Dongpei Zhang - [@DongpeiZ](https://www.github.com/DongpeiZ)

**Back End Team:**
- Aymaan Shaikh - [@ashaikh23](https://www.github.com/ashaikh23)
- Marco Diaz Moore - [@marco-dm1](https://www.github.com/marco-dm1)
- Michaela Gay - [@Michaela889](https://www.github.com/Michaela889)
- Chandni Kausika - [@ckausika](https://www.github.com/ckausika)

## Front End
TBD

## Back End
### Web Server
Our project's web server is built with Python and the Flask Web Framework. The web server handles API endpoint routing as well as the site's authentication system and any data retrieval from the project's database.

### Web Scraper
Our python program scrapes results from several publically available Manning CICS webpages for information about faculty, labs, research areas and ongoing research projects.  

### Database
MongoDB Atlas Database | Multi-Cloud Database Service: currently one database with 4 collections.


## Project Installation

### Backend Virtual Environment Setup

```
  cd backend
  python -m venv .venv              # Create venv
  pip install -r requirements.txt   # Install python packages
```

### Running Flask Server

#### Windows

```
  cd backend
  .venv\Scripts\activate            # Enter venv
  flask --app app run               # Run Flask App
```

#### Mac OS / Linux

```
  cd backend
  source .venv/bin/activate         # Enter venv
  flask --app app run               # Run Flask App
```

### Frontend Quickstart

```
  cd frontend/project
  npm install
  npm install -g @angular/cli
  ng serve --open
```
