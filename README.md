# Winnin Backend Challenge
This project implements a solution to the Winnin backend challenge.

## Architecture
This solution adopts the principles of the "The Clean Architecture", which abstracts the main elements of the most popular architectures of systems. The blog post [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) by Robert C. Martin (Uncle Bob), explains the concept succinctly.

This project adopts the popular convention of layers defined bellow:
  - **Domain** - The domain model is described in this layer. In the implementation of this solution the domain entities don't represent any complex behavior in their classes, not because of the adoption of an anemic model, but because of the lack of need for such functionalities.
  - **Use case** - Implementation of business rules specific to the application at hand.
  - **Repository** - Provides access to the persisted data in a way that abstracts the specific mechanisms behind data persistence. In our implementation maps database tables to domain objects without modifying them, principle of Persistence Ignorance.
  - **Request/Response** - Aims transport call parameters to the use cases trough Request objects and provides an output trough a Response object also accusing the presence of errors.
  - **Rest** - Implements the resources of the REST API. Validates the requests and calls the use case layer.
  
## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Endpoints
The endpoints developed for the application are:
- **/api/swagger.json** - Documents the api using swagger
 - **/api/users** - Queries for users using the following parameters:
    - **order**:
        - Indicates the attribute used to order the list of posts
        - Required parameter
        - type: string
        - Possible values: ['ups','comments']
                         
 - **/api/posts** - Returns a list of posts in the time period defined by 'start' and end parameters. The results are ordered according to the value of 'order parameter'
     - **order**:
        - Indicates the attribute used to order the list of posts
        - Required parameter
        - type: string
        - Possible values: ['ups','comments']
    - **start**
        - The date that indicates the start of the period
        - Required parameter
        - type: string
        - date string format: '%d-%m-%Y'

    - **end**
        - The date that indicates the end of the period
        - Required parameter
        - type: string
        - date string format: '%d-%m-%Y'


### Prerequisites
 - Python 3.5

### Dependencies
 - 'Flask==1.0.2'
 - 'flask-restful-swagger-2==0.35'
 - 'requests==2.21.0'
 - 'pytz==2018.9'
 - 'peewee==3.8.2'
 - 'apscheduler==3.5.3'

### Installing
It is recommended to install the project in a virtual environment to 

Installation is made trough the python script "setup.py" from the project's root directory, present in the root folder of the project as described by the command line:
```
python setup.py install
```
This script sets up the application including the installation of the python dependencies.

### Configuring
The file  winnin_backend_challenge/settings.py presents some configuration options for the app:
 - Database settings
   - **DATABASE_PATH**: The path of the SQL database to be used by the app.
   - **CREATE_DB_IF_NOT_EXISTS**: Flag that indicates whether a new SQLite DB will be created if the one specified in DATABASE_PATH does not exist.
   - **LOAD_FROM_JSON** : Flag that indicates whether the files in JSON_FILE_ENDPOINT_DATA should be backed up.
   - **JSON_FILE_ENDPOINT_DATA**: Files with data to populate the database. These files must contain the result of a request to the hot posts on the subreddit defined in POSTS_API.

- Backup Scheduler settings
   - **TIMEZONE**: The time zone to be used
   - **HOUR**, **MINUTE**, **SECOND**: Sets the conditions to trigger a backup of hot posts from the endpoint. Accepts values similarly to how the UNIX cron scheduler. e.g. The configuration hour = '13', minute = '0', second= '0' will trigger the backup at 1PM every day. 

- Endpoint settings 
   - **POSTS_API**: The endpoint to the hot posts of the desired subreddit
   - **HOST**: The hostname to listen on 
   - **PORT**: The port of the webserver

## Running an example
The file "example.py" defines a simple example for running the App. It simply executes the app using the default settings. To run the example simply:
```
python example.py
```
This example:
 - Creates a database
 - Populates the database with hot posts from Feb 16
 - Schedules the backup for 1PM of each day
 - Serves the endpoints on 127.0.0.1:5000

Example for getting users: http://127.0.0.1:5000/api/users?order=comments
Examaple for getting posts: http://127.0.0.1:5000/api/posts?order=comments&start=2-3-2018&start=16-2-2019&end=16-2-2019
For viewing API documentation: http://127.0.0.1:5000/api/swagger.json

## Running tests
Elementary tests were devised for the domain layer
To run the tests, go to the test folder and run 
```
python tests.py
```
