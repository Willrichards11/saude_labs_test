# A Flask application that provides a simple endpoint to query an example database. 

This repository is provided to satisfy the requirements of the Suade Labs job test. To aid the application, the provided CSV files were mapped to a sqlite database using a python script. This allowed querying from the database using sqlalchemy instead of using a library such as pandas. The database was provided in this git repository to aid the person marking the test in running the codebase (I would not normally include a database in a Git repository). The database can be found in the /app directory. As the task did not specify what to do in the case that no date was provided as an endpoint argument, a default date set to the first date present is used in this case. 

For a given date the endpoint provides the metrics described in the task definition in json format. If the date provided to the endpoint cannot be mapped to the desired format (YYYY-MM-DD) then the endpoint returns a message to the user that the date format may be incorrect. The dates for this application are currently filtered by regex string matches on the YYYY-MM-DD format. This could be improved in future.


## Requirements
To install the requirements listed below, simply execute 'pip install <requirement>' for the following requirements.
- flask
- sqlalchemy
- flask_sqlalchemy
  
The commands required are listed below:
  
'sudo pip install -U Flask'

'sudo pip install -U Flask-SQLAlchemy'

## Code structure

The code is sectioned into the two parts (the app and the unit tests). The application files are described below

### Application
- /app/__init__.py:  Defines the application creation factory. 
- /app/models.py:  Declares sqlalchemy models matching the database schema (datatypes etc).
- /app/queries.py:  Defines queries used to extract data from the sqlite database using sqlalchemy. Also defines a funcion to produce the final jsonified output from the queries.
- /app/routes.py:  Defines the endpoint logic. Takes a request and extracts date argument (if any provided). Returns data to user.
- /app/db.py: Defines key database functions (getdb, closedb etc).

### Unit tests
The unit tests are structured into two files:

- /tests/test_api.py: Defines unit tests for various inputs to the /analytics api endpoint. 
- tests/test_queries: Defines some unit test coverage for the database queries and the function that aggregates data into a single json response object.

## Running the code

Prior to running the code it is essential to set some environment variables. To achieve this we can use the following terminal commands:

- 'export FLASK_APP=app.routes'

The code can then be executed by simplying cd'ing into the project root directory and executing 'flask run'. By default, the application will then be running on http://127.0.0.1:5000/. The simplest way to submit a query is to go to any browser window and search for the address http://127.0.0.1:5000/analytics?date=< date >, where < date > is a date between 2019-08-01 and 2019-09-29 in YYYY-MM-DD format. In the case that no date is provided the endpoint will use a default date of 2019-08-01. Alternatively, the endpoint can be called via the curl command. 


## Unit testing

Unit test coverage is provided for the API endpoint and some query functions. Complete coverage was beyong the time scope of this test. The unit tests can be executed by changing directory to the /tests directory and executing the following command:

- "python -m unittest'

The unit tests assert statements surrounding expected endpoint behaviour. For instance, if no date is provided then make sure it is returning data for the default date described above.
