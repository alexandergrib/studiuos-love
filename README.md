# studio-love💞
![studio-love](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/amIres.JPG "studio-love")

<span id="project"></span>
## [Code Institute](https://codeinstitute.net)
### Full Stack Web Development Course
#### Valentine's Hackaton February 2022

#### [live website here](http://studiuos-love.herokuapp.com/)
--------------------------------------

<span id="index"></span>
## Index
1. <a href="#ux">UX 🥰</a>
1. <a href="#features">Features 💔</a>
1. <a href="#technologies">Technologies Used 😘</a>
1. <a href="#testing">Testing 💏</a>
1. <a href="#deployment">Deployment 💕</a>
1. <a href="#credits">Credits 😍</a>

<a href="#project">Project Idea ❤️</a>

February Hackaton topic was linked to Valentines day. Our team - Rebecca, Alex, Eric, Justinas, Martin and supervised by Gaff - decided to go for a Romantic Poetry Site with some added functionality as gift ideas, romantic movies or places.

Judging criteria were:
- Clear and substantial value to the user
- Original or innovative idea, design, or implementation
- Well-structured documentation and wireframes
- Well-planned and executed (GitHub Projects or Trello for Kanban Board)
- Realistic and a sense of completeness -> Please think Minimum Viable Product.

<span id="ux"></span>
# 1. UX 🥰
## 1.1 Strategy

Henry Miller said the only thing we never get enough of is love; and the only thing we never give enough of is love. Studio-love is here helping people to be able to give more love and also to feel the love more intense and to find the right person.

### User stories
### Users

| User story | As a/an | I want to be able to | So that I can |
| -----------: | :--------| :--------------------| :------------|
| Viewing and navigation |
| 1 | Visitor | See facts about love | Understand love deeper |
| 2 | Visitor | Access some poetry | So I can read beautiful poems |
| 3 | Visitor | Find romantic movie titles | Get ideas for a movie night |
| 4 | Visitor | Find romantic places in Ireland | Plan for a romantic holiday |
| 5 | Visitor | Find quotes about love | Think and understand |
| 6 | Visitor | Find some gift ideas | Get perfect present for my beloved one |
| 7 | Visitor | Access some dating sites | Find someone when alone |
| 8 | Visitor | Access Social Media accounts | Contact owner and see latest content |
| Registration and User accounts |
| 9 | User | Create an account | Add my details |
| 10 | User | Login or logout | Use account functionality | 
| Registered User Functionality |
| 11 | User | Add poetry | Share my favourite poems | 
| 12 | User | Search poetry | Find appropriate poems | 
| 13 | User | Like poems | Vote for the best poems |

## 1.2 Scope 

Based on the User Stories our Studio-Love will have following features and components:

- Attractive home page with nice hero image
- Structured intuitive navbar
- Footer with Social Media links
- Responsive design
- Page to display facts about love
- Page to display poetry 
- Search bar to find poetry easily
- Notification system with flash messages
- Dating app links
- Top Ten page for places, movies and quotes
- Carousel with gift ideas and link to the shop
- Page with more gift ideas
- Register and login page

## 1.3 Structure

Studio love is written in HTML5 and styled with CSS3 and Bootstrap4 framework. GitHub is used for version control and easier team work.
The core of Studio Love is written using Flask framework and connected to MongoDB. Live website is deployed on Heroku.

## 1.4 Skeleton

The website has consistent Navbar and Footer. The Navbar provides links to Love Facts, Poetry, Top Ten, Gift Ideas. Studio Love button brings you back to the main page. There are login and register links which change to logout link once user is logged in.

The Footer contains GitHub access, Copyright and Social Media buttons.

The content changes dynamically depending on selected page. For easier work, there is Back To Top button which is represented with an upside heart.

Main page contains beautiful hero image with biscuit hearts. Underneath is Check This Out section to highlight popular topics, Carousel with access to the Gift Shop and the links to Dating Apps.

Love Facts page has another attractive image of a couple holding hands. Facts are well organized into smaller articles with pictures and stacked on top of each other. 

Poetry page is decorated with an open book image. Poetry is displayed in carousel. Each element contains a name, written by and text. Some elements also contain pop-up text with copyright information.

Top ten page is divided into three sections - romantic movies, places and quotes. Each element is numbered and placed into a colour matching carousel.

Gift ideas page contains large red rose image. Ideas are again separated into sections and decorated with pictures.

On successfull registration visitor can login to access additional features. Logged in user can easily log out 

## Data Modelling

### Poems table

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | Mongo ID |
| author | StringField | Author's name |
| title | StringField | Title of the poem |
| poem_text | StringField | Poem's text |
| copyright | StringField | Author's copyrights |

### Users

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | Mongo ID |
| username | StringField | Full name of the user |
| password | StringField | Hash of the user password |


## 1.5 Surface

For the design a Bootstrap 4 components and systems will be used. Bootstrap navbar will provide us with a dropdown menu and other navigation links. 
Pages shall remain responsive and keep the same format on all screen sizes. Pictures on smaller screens will be stack on top of the text.

#### Font Style - Dancing Script
Google fonts
![Font Style - Dancing Script](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/dancingFont.JPG "Font Style")

#### Colour Scheme
Adobe colour tools
![Color Scheme](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/colour.jpg "Colour Scheme")

#### Wireframes
Balsamiq wireframes

![Wireframes](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/wire.JPG "Wireframes")


<a href="#index">Back to top ☝️ </a>
<span id="features"></span>

# 2. Features 💔
## 2.1 Implemented features

Most features were successfully implemented. 

There is consistent header and footer with appropriate links throughout all pages. Appealing pages with facts about love, poetry, gift ideas and ten top's were created with responsive design for smaller screens.
User's can also register and login/logout to create their profiles and access added functions which might be added later.

Home page is divided into four parts. The top part is displaying appealing hero image to grab users attention. Second - Check this out - a shortcut to suggest user what's not to be missed and to stay on a page. Third one promotes an online shop. This is also for best user experience. Last section is for people who came to find the right person and displays links for most popular dating services.

Love facts page has another hero image and provides people with information to uncover the love, to see the aspects of a true love but also to see the dark and sad side of the love. It also provides hints how to meet people, how to treat them and how to raise self-awareness. For easier readability text is broken down into paragraphs and associated pictures.

Top ten page display nice wedding picture and three carousels with corresponding topics - movies, places to help visitor how to spend a time together and famous quotes to help understand the love little bit better.

Gift Ideas page has satisfying red rose hero image. There are five articles. Four of them offers another view to more gits as heart shaped pizza or delicious chocolate box or stunning flowers. Link to same gift store is provided for visitors who could have missed this on a home page.

Login and register pages provides access to user account and its functionality.

## 2.2 To be implemented

Few more features will be implemented as a quotes and poetry search. Registered users also could have the option to like certain poetry.
However, this features are not necessary for Minimum Viable Product.

<a href="#index">Back to top ☝️ </a>
<span id="technologies"></span>

# 3. Technologies Used 😘

## 3.1 Languages

- HTML/HTML5
Each web page was built using HTML elements.

- CSS
Some HTML elements were styled using CSS

- Python
This app was build using python based framework Python and its packages.

## 3.2 Other libraries and frameworks

- Bootstrap 5
Navbar, Footer and some other elements were implemented using this popular library.

## 3.3 IDE, Version control and hosting

- GitPod
Collaborative development environments in browser

- Git and GitHub
Version control and repository

- Heroku
GitHub repository was linked with Heroku and is hosted here

- Flask
Python based framework for easy and powerful web development

MongoDB
- open source RDBMS used in deployed version


## 3.4 Other tools

- Balsamiq was used to create wireframes

- Adobe Color was used to identify the colour scheme

- Am I Responsive was used to create title image for readme.md

- Chrome Devtools were used to see the behaviour of the elements and their style

<a href="#index">Back to top ☝️ </a>
<span id="testing"></span>

# 4. Testing 💏

## 4.1 Validation

HTML code was checked in W3C validator with no errors - https://validator.w3.org/

CSS code was checked in W3C validator with no errors - https://jigsaw.w3.org/css-validator/

Python code was checked in pep8 online and errors were fixed. White spaces at the end of lines, and lines with non compliant length were the only issues.  - https://pep8online.com/

Responsivness was tested in Chrome and Firefox on Win10 with Devtools, ipad mini 6th gen, onePlus 7pro phone and Am I Responsive website. Iphone 5 was used in Devtools as standard for smallest screen. Bootstrap Display properties, Grid system and CSS media queries were used to adapt responsive layout.

## 4.2 Features testing

Tests were completed on iPhone5, iPad and 1200px screen sizes. 


### Navbar
Navbar links were tested to ensure the user is redirected to appropriate page. Mobile drop-down navbar is displayed on pages under 992px.

### @app.route("/")
Route is working as expected and rendering the index.html page correctly.

### @app.route("/love_facts")
Route is working as expected and rendering the love_facts.html page correctly.

### @app.route("/topten")
This route is also working as expected and rendering topten.html page correctly.

### @app.route("/poetry")
This route handles two requests - GET and POST. GET request renders poems.html. POST request handles a form input and stores it in the MongoDB. These functionalities are working as expected. Flash messages are not displaying correctly. This will be reviewed.

### @app.route("/register")
Again this route accepts two requests - GET and POST. GET request renders register.html page. POST request is taking data from user registration form and stores them in user table in MongoDB. On successful registration the user name is stored in Session and user is logged in. For security reasons, passwords are hashed before storing. All functionalities work with no problem.

### @app.route("/login", methods=["GET", "POST"])
Another route taking GET and POST requests. GET request renders login.html page. POST request takes input from login form. If user name is found in DB it proceeds with password verification. When password verification is successful a user name is stored in session and user is logged in. When password is incorrect a flash message is returned that either username or password are not correct. Same message is returned if user name is not found in DB. This is for enhanced security in a case attacker is trying to guess user names and passwords. These parts are working correctly. Flash messages are not displaying. This will be also reviewed.

### @app.route("/logout")
This route removes user from session and user is logged out. User is redirected to index.html. This is correct.

Apart Flash messages few more issues were found. Form validation will be implemented to avoid some system attacks. More confirmation request can be added for user convenience, e.g. to confirm log out action. More routes can also be added to handle HTML error status codes.

No other issues were found in HTML code. Links are working as expected. Navbar is responsive on screens smaller than 992px and comes with burger drop down button.

<a href="#index">Back to top ☝️ </a>
<span id="deployment"></span>

# 5. Deployment 💕

Heroku deployment guideline
1. Create Heroku account
1. Select Create New app
1. Provide name and your region and create the app
1. Select Deploy tab and under deployment method select Connect to GitHub
1. Find corresponding repository and select Connect
1. You can enable Automatic Deploys from corresponding branch
1. Secret variables from local env<span>.</span>py had to be added to Heroku config variables. This can be found under Settings tab - Reveal Config Vars
1. Select Open app button to run the app

MongoDB guideline
1. Create MongoDB account
1. Create New Project
1. Build a cluster - free cluster was selected for this project
1. AWS cloud based in Ireland was chosen
1. When cluster is created click collections
1. Add your own data
1. Choose appropriate name for database and also for collection
1. You can add data / insert documents into DB
1. Create user / admin account to maintain DB
1. Configure IP address which can access this DB
1. Click connect in clusters tab and select connect your application
1. Select driver and version for your project and copy connection string

<a href="#index">Back to top ☝️ </a>
<span id="credits"></span>

# 6. Credits 😍

A big thank belongs to:

- CODE INSTITUTE family
- Our team - Rebecca, Alex, Eric, Justinas, Martin and Gaff
- Our families and friends for their patience and support
- All other people we have learnt from

## 6.1 References

- Pictures
    https://www.pexels.com/
    https://www.pixabay.com/
    
- Fonts
    https://fonts.google.com/

- Top Places
    https://www.wildernessireland.com/blog/most-romantic-places-in-ireland/

- Top Quotes
    https://nosweatshakespeare.com/quotes/literature/love-proverbs/

- Top Movies
    https://www.theguardian.com/film/filmblog/2013/oct/07/top-10-romantic-movies
