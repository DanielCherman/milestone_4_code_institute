
## This is the final Milestone Project 4, from Daniel Cherman, for Code Institute.

### A Freelance Platform for designers caller "Graphic Designer"

#### This freelance platform designed for graphic designers to sell their skills.

# UX

## Goals


The target audience to the web store would be:
- Business owners who needs logos or webdesign
- Mid Cap companies who need rebrending
- Startups


### User Stories:
As a new User to this website, I want to:
* be able to set the requirements for my logo or design
* get a price quote
* find a freelancer
* be able to review the order
* get work done

### Wireframes: 
* The wireframes were created using Balsamiq during the inception phase of the design and planning process for this project.
[Wireframes](https://drive.google.com/file/d/1DMNe8_GrfIEr4uJGoM2aPQSHLn9XSKsn/view?usp=sharing)

## Features

### Layout
This is a multi-page layout, but designed with simplicity in mind. There are three different templates used:
1. Base template for the home page, login, logout, register, forgot password
2. Order template used for order and review the work
3. As a Freelancer get and deliver work


### Buttons
The buttons are big, bright and simple. They are in Gradient Color The Buttons on this application are from the Bootstrap Framework.


#### The Footer

The Footer is on every page except of register page. The footer has been kept clean and simple. Links to External Sites, Social Media links and The company name and caption. Also included at the bottom of the logo is Copyright 2022 & name of the project.

#### The Contact Form

The contact page contains a form for the user to fill in to send any questions to the service admin

#### The Register Page

The user can either log in to existing account or register new
 

### Features Left to Implement
* Integrate payment system

* Extend Freelancer profile functionality with having smooth work history page and rating

## Main Technologies Used

### Languages used

* This project uses **HTML**, **CSS**, **JavaScript** and **Python** programming languages.


## Databases

### Databases used

Django normally works with SQL databases and comes prepacked with sqlite3. During development on my local machine I worked with the standard sqlite3 database installed with Django. On deployment, the SQL database provided by Heroku is a PostgreSQL database.

## Testing

Manual QA testing. Performance Testing, CI testing

#### Manual User testing:
As soo as i have my small business i had audience to test this service

### Below are the list of Internet Browsers that were used to test the display of the website:

1. Google Chrome (Version 77.0)
2. Mozilla Firefox
3. Microsoft Edge
4. Internet Explorer 11

Manual testing was using the above browsers. 

### Below are the list of websites I used to test the HTML, CSS and JS code:

1. [W3C HTML Validator](https://validator.w3.org/) This is a HTML online validitor.
2. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) This is a CSS online validitor.
3. [CSS Lint](http://csslint.net/) CSS Lint is an open source CSS code quality tool I used.

#### As a new User to the web application, I want to be able to easily navigate around the website.

The webstore has been setup so that there is no confusion when a user visits the site. The Nav bar is of a neutral color, the Nav items are clearly readable, the buttons are big, bright and visualy rich and simplistic.

## Deployment

### Local Deployment

This project was developed using the Visual Studio Code, committed to git and pushed to GitHub using the built in function within Visual Studio Code.

The GitHub Repository: https://github.com/DanielCherman/milestone_4_code_institute
The application live here: https://milestone-4-project.herokuapp.com/

To deploy this project locally, on your own IDE, folow the steps below:

 Firstly, ensure of the following:
    - You have an IDE, such as VS Code.
    - The following must be installed locally on your computer:
        1.  git
        2.  PIP
        3.  Python 3
            

Instructions for Installation:

1. Make your own folder and navigate to it on the terminal. Then enter the following in the terminal:

```
$ git clone https://github.com/DanielCherman/milestone_4_code_institute.git

```
2. Open your locally installed IDE, unzip the downloaded file and open the terminal window.

3. Create a virtual environment
```
$ python -m venv env
$ pip3 install -r requirements.txt

Set migrations 
$ python3 manage.py makemigrations
$ python3 manage.py migrate

Run server 
$ python3 manage.py runserver

Create super user
$python3 manage.py createsuperuser


### Acknowledgements

- I'd like to thank my code institue for this experience, this project was developed in a hurry because i had huge desease and wasn't able to work on it, and I was ashamed to put it off a second time. Hope you will enjoy using it.


### The content of this website is for educational purposes only. 
### Thank you.
