# A Flask application that provides a simple endpoint to query an example database. 

This repository is provided to satisfy the requirements of the Suade Labs job test.


## Requirements
To install the requirements listed below, simply execute 'pip install <requirement>' for the following requirements.
- flask
- sqlalchemy
- flask_sqlalchemy
  
The commands required are listed below:
  
'sudo pip install -U Flask'

'sudo pip install -U Flask-SQLAlchemy'


## Running the code

Prior to running the code it is essential to set some environment variables. To achieve this we can use the following terminal commands:

- 'export FLASK_APP=app.routes'

The code can then be executed by simplying cd'ing into the project root directory and executing 'flask run'. By default, the application will then be running on http://127.0.0.1:5000/. The simplest way to submit a query is to go to any browser window and search for the address http://127.0.0.1:5000/analytics?date=< date >, where < date > is a date between 2019-08-01 and 2019-09-29 in YYYY-MM-DD format. In the case that no date is provided the endpoint will use a default date of 2019-08-01. Alternatively, the endpoint can be called via the curl command. 
