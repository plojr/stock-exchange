# Stock Exchange

## Status
Not finished yet.

## Summary
This project is for learning purposes only.

It’s a very simple API in order to access a database where is located data about stock prices, volumes of shares, etc.

With the API, it's possible to have some information:
- What's the closing price of a specific stock in a specific date;
- How many shares were traded for a specific stock in a specific date;
- The variation of a stock's price, given a period of time;
- Etc.

For this project, I'm coding in Python, using Visual Studio Code under a Linux distribution. The data are stored in a PostgreSQL database. And, for the routes, I'm using Flask framework.

## Prerequisite
- I'm using flask framework, so it must be installed via pip: pip3 install flask.
- In order to run this project, you need to set an enviroment variable called FLASK_APP that equals to the filename of a Python module that contains a Flask application. In this case, it's the routes.py file. On Linux, you need to export FLASK_APP=routes before running this application.
- In order to store the database password, I chose the strategy of setting an environment variable called POSTGRESQL_PASSWORD and then use os.environ to get its value.

## Instructions
- In order to run this, on development environment: go to project root folder and run "flask run". You'll be able to open http://localhost:5000/ on your web browser.

## Database information
DBMS: PostgreSQL
Database, schema and tables: please check sql folder.
