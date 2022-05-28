# Stock Exchange API

This project is for learning purposes only.

It’s a very simple API in order to access a database where is located data about stock prices, volumes of shares, etc.

With the API, it's possible to have some information:
- What's the closing price of a specific stock in a specific date;
- How many shares were traded for a specific stock in a specific date;
- The variation of a stock's price, given a period of time;
- Etc.

For this project, I'm coding in Python, using Visual Studio Code under a Linux distribution. The data are stored in a PostgreSQL database. And, for the routes, I'm using Flask framework.

Prerequisite:
- It must be set environment variables for database, user and password, and they're called POSTGRESQL_DATABASE, POSTGRESQL_USER and POSTGRESQL_PASSWORD, respectively.
- I'm using flask framework, so it must be installed via pip.

In order to run this project on development environment, go to the project folder, and run "flask run".
