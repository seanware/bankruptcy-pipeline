## Python + Docker + Postgresql

#### One of the most basic forms of data engineering is fetching data from and external api and loading that data into a database as a form of datawarehouse so the information can be acessed by data analysts.


#### In this simple demonstration project i was able to:

Let's understand why we would use Docker for this type of project
Using a container makes it simplier to test, manage and implement different data
setups on your machine

1. download bankruptcy data from a website using python and the requests library.

2. Spin up a Docker container running postgresql with data persistence

3. Load the data into the database using the command line tool psql with a .sql file

The request library is a python library that is often used to acess web api's due to its straight forward interface.

A file called load.py was created to get the data from the American Bankruptcy Institute  and loaded in its raw form.  After loading this data was merged and changed into a .csv format because it is easier to use than .xlsx


### Spin up Docker Container with postgresql

The data then needed to be transferred to a postgresql database and to do this and docker container was created using docker compose.  I used docker compose becuses having a .yml file allows me to store more commands for better process documentation.



```yml
version: "0.1"
services:
  postgres:
    image: "postgres:staging"
    ports:
      - "5433:5432"
    volumes:
      - postgres:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
volumes:
  postgres:
```
The environment variables are stored in a .env file

 Now create and run the container with the command
```bash
 docker compose up -d
```
The -d flag is detached mode so the container will run in the background.

###Load the Data into postgresql

The cases.csv file needed to be copied into the docker container 
```bash
docker cp ./cases.csv bankruptcies_postgres_1:/cases.csv
```

Once the docker container was up an running I was able to load the data from  the merged csv using the command line tool psql. I used this tool to access the postgresql database running on the docker container and created the file create_table.sql

```sql
CREATE TABLE IF NOT EXISTS companies (
  id serial PRIMARY KEY,
  district VARCHAR(3),
  state VARCHAR(3),
  company_name VARCHAR(50),
  assets NUMERIC(8,2),
  liabilities NUMERIC(8, 2)
  ); 
    
```

Load the csv files into the bankruptcies database
  
```sql
COPY companies(district, state, company_name, assets, liabilities)
FROM '/cases.csv'
DELIMITER ','
CSV HEADER;
```

Now all the that the data is loaded into the database I can test the functionality by outputing the fisrt 10 entries

```sql
SELECT * FROM companies
LIMIT 10;
```

###Possible Improvments
1. Use a scheduler like Apache airflow to automate the process of loading and running the scripts when the data changes

2. Load data directly from the website to the database using the pscopg library to connect.

