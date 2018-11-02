[![Build Status](https://travis-ci.org/kelraf/store-manager-api-db.svg?branch=develop)](https://travis-ci.org/kelraf/store-manager-api-db)

# store-manager-api-db
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.


# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose

# Prerequisites
Git
Postgresql
Postman
Python 3.6

# Installing
Clone the Repo

Checkout to develop branch 

To test API locally, set up a virtual environment in the base project folder

Activate it and install the requirements

<code>pip install -r requirements.txt</code>

Run tests

<code>pytest --cov-report term-missing --cov=app</code>

Test The endponts with postman


# The following endpoints should work 
https://documenter.getpostman.com/view/5714154/RzZ4q21c

# Built With

<code>Python 3.6</code>

<code>Flask</code>

<code>Flask Restful</code>

# Contributing

Clone the repo

Create your feature <code>branch git branch somefeature then git checkout somefeature</code>

Commit your changes <code>git commit "Add some feature"</code>

Push to the <code>branch git push origin somefeature</code>

Create a new pull request
