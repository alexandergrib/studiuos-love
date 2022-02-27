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

Top ten page is divided into three sections - romantic movies, places and quotes. Each element is numbered and text is enlarged for easier readability on mouse hover.

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
