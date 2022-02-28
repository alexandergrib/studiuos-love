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

February Hackatons topic was linked to Valentines day. Our team - Rebecca, Alex, Eric, Justinas, Martin and supervised by Gaff - decided to go for a Romantic Poetry Site with some added funcionality as gift ideas, romantic movies or places.

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
| 10 | User | Login or logout | Use account funcionality | 
| Registeres User Funcionality |
| 11 | User | Add poetry | Share my favourite poems | 
| 12 | User | Search poetry | Find appropriate poems | 
| 13 | User | Like poems | Vote for the best poems |

## 1.2 Scope 

Based on the the User Stories our Studio-Love will have folowing features and components:

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
The core of Studio Love is written using Flask framework and conected to MongoDB. Live website is deployed on Heroku.

## 1.4 Skeleton

The website has consistent Navbar and Footer. The Navbar provides links to Love Facts, Poetry, Top Ten, Gift Ideas. Studio Love button brings you back to the main page. There are login and register links which change to logout link once user is logged in.

The Footer contains GitHub access, Copyright and Social Media buttons.

The content changes dynamically depending on selected page. For easier work, there is Back To Top buttom which is represented with an upside heart.

Main page contains beautiful hero image with biscuit hearts. Underneath is Check This Out section to highlight popular topics, Carousel with access to the Gift Shop and the links to Dating Apps.

Love Facts page has another attractive image of a couple holding hands. Facts are well organized into smaller articles with pictures and stacked on top of each other. 

Poetry page is decorated with an open book image. Poetry is displayed in carousel. Each element contains a name, written by and text. Some elements also contain pop-up text with copyright information.

Top ten page is divided into three sections - romantic movies, places and quotes. Each element is numbered and placed into a colour matching carousel.

Gift ideas page contains large red rose image. Ideas are again separated into sections and decorated with pictures.

On sucessfull registration visitor can login to access aditional features. Logged in user can easily log out 

## Data Modeling

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

For the design a Bootsrap 4 components and systems will be used. Bootstrap navbar will provide us with a dropdown menu and other navigation links. 
Pages shall remain responsive and keep the same format on all screen sizes. Pictures on smaller screens will be stack on top of the text.

#### Font Style - Dancing Script
Google fonts
![Font Style - Dancing Script](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/dancingFont.JPG "Font Style")

#### Color Scheme
Adobe color tools
![Color Scheme](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/colour.jpg "Color Scheme")

#### Wireframes
Balsamiq wireframes

![Wireframes](https://github.com/alexandergrib/studiuos-love/blob/main/static/img/wire.JPG "Wireframes")


<a href="#index">Back to top ☝️ </a>
<span id="features"></span>

# 2. Features 💔
## 2.1 Implemented features

Most features were sucesfully implemented. 

There is consistent header and footer with appropriate links throughout all pages. Appealing pages with facts about love, poetry, gift ideas and ten top's were created with responsive desing for smaler screens.
User's can also register and login/logout to create their profiles and access added functions which might be added later.

Home page is divided into four parts. The top part is displaying appealing hero image to grab users attention. Second - Check this out - a shortcut to suggest user what's not to be missed and to stay on a page. Third one promotes an online shop. This is also for best user experience. Last section is for people who came to find the right person and displays links for most popular dating services.

Love facts page has another hero image and provides people with information to uncover the love, to see the aspects of a true love but also to see the dark and sad side of the love. It also provides hints how to meet people, how to treat them and how to raise self-awareness. For easier readability text is broken down into paragraphs and associated pitures.

Top ten page display nice wedding picture and three carousels with corresponding topics - movies, places to help visitor how to spend a time togetger and famous quotes to help understand the love little bit better.

Gift Ideas page has satysfying red rose hero image. There are five articles. Four of them offers another view to more gits as heart shaped pizza or delicious chocolate box or stunning flowers. Link to same gift store is provided for visitors who could have missed this on a home page.

Login and register pages provides access to user account and its funcionality.

## 2.2 To be implemented

Few more features will be implemented as a quotes and poetry search. Registered users also could have the option to like certain poetry.
However this features are not necessary for Minimum Viable Product.

<a href="#index">Back to top ☝️ </a>
<span id="technologies"></span>

# 3. Technologies Used 😘

## 3.1 Languages

- HTML/HTML5
Each web page was built using HTML elements.

- CSS
Some HTML elements were styled using CSS

- Python
This app was build using python based framework Django and its packages.
Crispy Forms - library for python to work fast and efficiently with forms.

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
Python based framework for easy and powerfull web development

MongoDB
- open source RDBMS used in deployed version


## 3.4 Other tools

- Balsamiq was used to create wireframes

- Adobe Color was used to identify the colour scheme

- Am I Responsive was used to create title image for readme.md

- Chrome Devtools were used to see the behaviour of the elements and their style

<a href="#index">Back to top 💏 </a>
<span id="testing"></span>

# 4. Testing 💉

## 4.1 Validation

HTML code was checked in W3C validator with no errors - https://validator.w3.org/

CSS code was checked in W3C validator with no errors - https://jigsaw.w3.org/css-validator/

JS code was checked in BeautifyTools with no errors - http://beautifytools.com/javascript-validator.php

Python code was checked in pep8 online and errors were fixed. White spaces at the end of lines, and lines with non compliant lenght were the only issues.  - https://pep8online.com/

Responsivness was tested in Chrome and Firefox on Win10 with Devtools, ipad mini 6th gen, onePlus 7pro phone and Am I Responsive website. Iphone 5 was used in Devtools as standard for smallest screen. Bootstrap Display properties, Grid system and CSS media queries were used to adapt responsive layout.

## 4.2 Features testing

Tests were completed on iPhone5, iPad and 1200px screen sizes. 

