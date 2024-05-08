
# CICS Undergraduate Research Finder - Scraper

This is the scraper side of the project. Our python program scrapes results from several publically available Manning CICS webpages for information about faculty, labs, research areas and ongoing research projects.  

## Team
Project Manager: Pablo Almeida - [@pabloooooo](https://www.github.com/pabloooooo)

**Back End Team (Scraper):**
- Aymaan Shaikh - [@ashaikh23](https://www.github.com/ashaikh23)
- Marco Diaz Moore - [@marco-dm1](https://www.github.com/marco-dm1)
- Michaela Gay - [@Michaela889](https://www.github.com/Michaela889)
- Chandni Kausika - [@ckausika](https://www.github.com/ckausika)

#### Python Files
 The python files can be run to re-scrape data off of specific CICS websites. 

 #### CSV Files
 The csv files contain the scraped data that is used to populate our backend servers. 

## Importing Scraped CSV Files into MongoDB

To integrate the scraped data from CSV files into MongoDB follow these steps:

### 1. Ensure MongoDB Setup
Ensure you have set up MongoDB Atlas by signing up for an account and creating a new cluster in the MongoDB Atlas dashboard. Configure cluster settings, including cloud provider (e.g., AWS, Azure, Google Cloud), region, and security options. And choose a cluster tier, this project uses the free tier.

#### Set Up Security
Network Access: Configure network access to restrict connections to your cluster based on IP addresses.
Database Access: Set up database users and passwords to control access to your databases.
Encryption: Enable encryption at rest and in transit to secure your data.

### 2. Identify CSV Files
Locate the CSV files containing the scraped data. These files should contain structured data, organized into rows and columns, representing faculty information, lab details, research areas, and ongoing projects.

### 3. Prepare Data for Import
Before importing, review the structure of your CSV files. Ensure they align with the schema of the MongoDB collections. Each CSV file corresponds to a specific MongoDB collection.

### 4. Use MongoDB Import Tool
MongoDB provides a powerful import tool to facilitate the import of data from various sources, including CSV files.

#### Example Command:
```bash
mongoimport --db <database_name> --collection <collection_name> --type csv --headerline --file <path_to_csv_file>
```

- `<database_name>`: Specify the name of your MongoDB database where you want to import the data.
- `<collection_name>`: Specify the name of the MongoDB collection where the data will be stored.
- `<path_to_csv_file>`: Provide the path to the CSV file containing the data to import.

### 5. Execute Import Command
Run the `mongoimport` command in your terminal, providing the necessary parameters to import each CSV file into the corresponding MongoDB collection.

### 6. Verify Data Import
After executing the import command, verify that the data has been successfully imported into your MongoDB collections. You can use MongoDB Compass or the MongoDB shell to inspect the collections and ensure that the data matches your expectations.

By following these steps, you can import the scraped data from CSV files into MongoDB, enabling your backend servers to access and utilize the data for the CICS Undergraduate Research Finder app.
