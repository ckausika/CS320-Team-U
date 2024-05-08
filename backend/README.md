# CICS Undergraduate Research Finder - CS320 Team U

This web application allows undergraduate students and professors at UMass Amherst to connect over research opportunities. Students can search for professors and labs that are offering research projects. They can view professors' research interests, affiliated labs, and past and ongoing projects. Students can easily contact professors through the application by sharing their research profile, experience, resume, etc. Professors can post information about ongoing research projects and recruit students through the application by viewing their respective research profiles.

## Team
Project Manager: Pablo Almeida - [@pabloooooo](https://www.github.com/pabloooooo)

**Back End Team:**
- Aymaan Shaikh - [@ashaikh23](https://www.github.com/ashaikh23)
- Marco Diaz Moore - [@marco-dm1](https://www.github.com/marco-dm1)
- Michaela Gay - [@Michaela889](https://www.github.com/Michaela889)
- Chandni Kausika - [@ckausika](https://www.github.com/ckausika)

## Back End
### Web Server
Our project's web server is built using Python and the Flask Web Framework. The primary responsibilities of the web server include:

- **API Endpoint Routing:** Handling of API endpoints for various functionalities such as user authentication, data retrieval, and interaction with the front end.
- **Authentication System:** Implementation of authentication system to secure user access.
- **Database Interaction:** Facilitation of data retrieval and storage operations with the project's MongoDB database.

### Web Scraper
Python-based web scraper responsible for gathering data from multiple publicly available Manning CICS webpages. The scraper extracts information related to faculty, labs, research areas, and ongoing research projects. [Scraper ReadME](scraper/README.md)

### Database
MongoDB Atlas Database | Multi-Cloud Database Service: Key aspects of our database setup include:

- **Database Structure:** Utilizing a single MongoDB database with five collections to store various types of information, including user data, professor profiles, lab details, research areas, and ongoing research projects.
- **Data Management:** Implementing efficient data management strategies to organize, retrieve, and update information stored in the database.
- **Scalability:** Leveraging MongoDB Atlas's scalability features to accommodate future growth and increasing data volumes as the application usage expands.
