# MLS_project
How to run:

- Via flask

export FLASK_APP=wind.py

python3 -m flask run


- Via docker

docker build -t wind-app .

docker run -d -p 5000:5000 wind-app


Go to 127.0.0.1:5000.

--------------
Contents:

Dockerfile - for running docker 

.gitignore - files that don't need to be uploaded

LICENSE  - a license

Project.ipynb - the jupyter notebook where we calculated our parameters for the polynomials of best fit for our models

__pycache__  - ignorable directory of cached python stuff

README.md - this README

requirements.txt - a list of the required packages, for Docker

templates - a directory containing the html file  

wind.csv - the wind/energy data

wind.py - our script to perform the calculations upon user input from the HTML file
