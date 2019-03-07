# UdacityProject 3: Logs Analysis Project
### by matampalli satheesh

Logs Analysis Project, third project in Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does

python program using the `psycopg2` module to connect to the database.

## Need tools

* Vagrant
* VirtualBox
* Python
* psql databse
* any editor


## logs analysis Project contents

This project consists for the following files:

* logqueries.py - main file to execute the queries
* README.md - instructions to install this reporting tool
* results.txt - output file that will shown on the command prompt

## How to Run Project

Download the project zip file to you computer and unzip the file.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
     $ vagrant up
 
  2. Then Log into this using command:
    $ vagrant ssh

  3. Change directory to /vagrant and look around with ls and move to the exact .py path.
  
  4. move to database psql

  5. check the psql commands in gitbash 
    $ python logqueries.py


## Miscellaneous

This README document is based on a template suggested by PhilipCoach in this
Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).