![Landing Page](/static/readme/landing-page.PNG)
# Milestone Project 3 - XXX
# Table of Contents
* [Introduction](XXX)
* [User Experience Design](XXX)  
  * [User Stories](XXX)
    * [First Time Visitors](XXX)
    * [Returning Visitors](X)
    * [Frequent Users](X)
    * [User Story Screenshots](XXX)
  * [Structure](XXX)
  * [Design](XXX)
    * [Colors](XXX)
    * [Typography](XXX)
    * [Images](XXX)
    * [Sounds](XXX)
    * [Wireframes](X)
    * [Design Deviations](XXX)
  * [Limitations](XXX)
* [Features](XXX)
  * [Current Features](XXX)
  * [Future Features](XXX)
* [Technologies](XXX)
  * [Languages](XXX)
  * [Libraries, Frameworks & Programs Used](XXX)
* [Testing](XXX)
  * [Validation](XXX)
    * [HTML Validation](XXX)
    * [CSS Validation](XXX)
    * [JavaScript Validation](XXX)
    * [Python Validation](XXX)
  * [User Scenarios - Testing](XXX)
    * [First Time User](XXX)
    * [Returning User](XXX)
    * [Frequent User](XXX)
  * [User Testing](XXX)
  * [Currently Known Bugs](XXX)
  * [Major Bugs Fixed During Development](XXX)
  * [Lighthouse Results](XXX)
* [Deployment](XXX)
   * [Project Creation](XXX)
   * [Publishing](XXX)
   * [Local Clone](XXX)
* [Acknowledgements](XXX)
  * [Code](XXX)
  * [Media](XXX)

You can find the published website here: [Milestone Project 3](https://milestone-project-3-kn.herokuapp.com/).
# Introduction

The project is part of a Full Stack Developer course run by CodeInstitute. This is Milestone Project 3. This project was to create a full stack web application with CRUD functionality. This web application is a simple budgeting tool, where users can create an account, add their income and outgoings and see a visual representation of each.

## Milestone Project 3

A mockup of the web application can be seen below:

![Mockup Image](/static/readme/mockup.png)

# User Experience Design
## User Stories
### First Time Visitors
* What would I want to see as a first time visitor?
  1. What can I use the web application for?
  2. Where can I register?
  3. Can I change the currency that is shown?
### Returning Visitors
* What would I want to see as a returning visitor?
  1. Where can I log in?
  2. How to add new income or outgoings.
  3. Somewhere to view all of the income or outgoings that have been entered.
### Frequent Users
* What would I want to see as a frequent visitor?
  1. How to edit an previous income or outgoings that are stored.
  2. How to delete any income or outgoings that do not apply any more.

### User Story Screenshots
Below are screenshots relating to some of the user stories.

## Structure
Shown below are elements that correspond to some of the User Stories:
* "thing to correspond to story"
> "story here"

## Design
### Colors
The main colors throughout are white backgrounds, using bold colours that stand out for buttons and pie charts. The aim was to not have any background elements that would clash with the pie chart colours as income and outgoings are added.
### Images
The landing page image is used with thanks to [Mediamodifier](https://unsplash.com/@mediamodifier).
### Wireframes
Wireframes images can be seen below and also found in the "/assets/readme-content" folder. It contains a design for the desktop and mobile version of the dashboard.

* Mobile: <br> ![Mobile Wireframe](XXX)
* Desktop: <br> ![Desktop Wireframe](XXX)

See link for PDF below:
* [Wireframe](XXX)

### Design Deviations
Compared to the original Wireframe there have been multiple deviations.
* The original Wireframe had the pie chart elements on the top of the page.
> On mobile devices when there was no income or outgoing, a blank space was displayed in place of the pie charts. This was easy to change with bootstrap to ensure that the other controls (adding income and outgoings) were displayed on top first.
* Tables displayed a large list of income or outgoings.
> This was changed to introduce a scroll bar in the income and outgoing tables when a certain table size was reached.

Note: these changes were applied to both the desktop and mobile version of the web application.

## Limitations
Currently, there some limitations:

* XXX
* XXX

# Features
## Current Features
* CRUD functionality regarding income and outgoings.
* Pie charts for a visual display of income and outgoings that contribute most.
* Tables showing the all the income and outgoings associated with the account.
* Account registration.
* Currency icon selector (currently GBP, Euro and US Dollar).

## Future Features
Features that could be released in subsequent versions include:
* More chart types could be added. Such as predictive graphs for total savings value based on an amount saved per month.
* Setting the default currency to GBP (£) and then upon selecting from a number of currencies, the value will update according to current currency exchange rates.

# Technologies
Technologies used are as follows.
## Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * Used as the main language to code the web applications content.
* [CSS3](https://en.wikipedia.org/wiki/CSS)
  * Used to incorporate custom styling into the web application and its layout.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * Used to create interactive elements.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * Used to create the back end of the web application.

## Libraries, Frameworks & Programs Used
* [Bootstrap 5](https://getbootstrap.com/)
   * Multiple features of Bootstrap 5 were used to create the website. Including grid system, responsiveness and the navbar.
* [Balsamiq](https://balsamiq.com/)
   * Used to create the wireframes when starting the design.
* [Font Awesome](https://fontawesome.com/)
   * Used for multiple icons throughout the web application..
* [Techsini](http://techsini.com/multi-mockup/index.php)
   * Used to generate the mockup image in this README file, see above.
* [GitHub](https://github.com/)
   * Used as a storage location for the website's content, including code and assets.
* [GitPod](https://www.gitpod.io/)
   * An online IDE used to write and test code that is written.
* [Git](https://git-scm.com/)
   * Used for version control to add, commit, and push files to GitHub.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
   * Used to test different CSS styles in the browser, inspect pages, general debugging, confirming JavaScript functionality with the Console and using Lighthouse.
* [favicon.cc](https://www.favicon.cc/)
    * Used to create the favicon.ico.
* [W3C HTML Validator](https://validator.w3.org/)
    * Used to validate the HTML code.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * Used to validate the CSS code.
* [JSHint](https://jshint.com/)
    * Used to validate the JavaScript code.
* [PYTHON VALIDATION](https://extendsclass.com/python-tester.html) XXX CONFIRM IF SUITABLE XXX
    * Used to validate the Python code.
* [MongoDB](https://www.mongodb.com/)
    * Used as the cloud database provider.
* [Heroku](https://www.heroku.com/)
    * Used as the cloud web application host.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * Python based web framework used for the backend of the web application.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    * Template engine for Python. Used for things like template inheritance and displaying Python variables on the front end. 

# Testing
High level testing plan:
1. CRUD functionality.
2. Responsiveness from 300px to 3000px, on multiple browsers:
  > Google Chrome
  > Mozilla Firefox
  > Opera
3. All buttons working as intended.
4. Interactive parts working as intended.
5. No content areas overlapping other content areas. 

Test Results can be found here: [Test Results](XXX)

## Validation
### HTML Validation
HTML files were run through the [W3C HTML Validator](https://validator.w3.org/), via the direct input method.
* WARNINGS? XXX
### CSS Validation
CSS Stylesheet was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), via the direct input method.
* WARNINGS? XXX
### JavaScript Validation
JavaScript file was run through the [JSHint](https://jshint.com/).
* WARNINGS? XXX
### Python Validation
Python files were run through the [JSHint](https://jshint.com/).
* WARNINGS? XXX
## User Scenarios - Testing
How does the web application design enable the goals of a first time, returning and frequent user?<br>
### First Time User
* XXX STORY
  * COMMENT ON STORY.
### Returning User
* XXX STORY
  * COMMENT ON STORY.
### Frequent User
* XXX STORY
  * COMMENT ON STORY.

## User Testing
A user kindly volunteered to test the web application once overall development was complete.
User's comments were as follows:
* XXX WHAT DID THEY NOTICE?
  * WHAT DID I DO? XXX

## Currently Known Bugs
1. XXX
2. XXX

## Major Bugs Fixed During Development
1. XXX
2. XXX
3. XXX

## Lighthouse Results
Images below show the Lighthouse results on both mobile and desktop:
1. Mobile:<br>![Mobile Lighthouse](XXX)
1. Desktop:<br>![Desktop Lighthouse](XXX)

# Deployment
## Project Creation
To create the project, firstly a Chrome extension called "[Gitpod - Always ready to code](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki?hl=en-GB)" was installed. A CodeInstitute template was use by navigating to the [GitHub Repo](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the "Use this template" button. The repository was named "Milestone-Project-3", the checkbox for "Include all branches" was checked and the green "Create repository from template" button was then clicked. From here, the green "GitPod" was then clicked (must use the above extension) and project folders and files created.

Common Git commands were used as follows:
* git add "filename-here" - used to stage files before commiting them.
* git add . - used to stage all files before commiting them.
* git commit -m "message here" - used to commit changes to the local repositry, with the message containing information on the changes that have occured.
* git status - used to check the tracking status of the file in the project.
* git push - used to push the changes to the GitHub repository.

## Publishing
To publish the project I performed the following steps:
1. XXX HOW DID I DEPLOY TO HEROKU?
2. XXX HOW DID I DEPLOY TO HEROKU?
3. XXX HOW DID I DEPLOY TO HEROKU?
4. XXX HOW DID I DEPLOY TO HEROKU?
5. XXX HOW DID I DEPLOY TO HEROKU?

## Local Clone
To create a local clone of the project you can follow the steps below:
1. Navigate to the project's [Github page](https://github.com/KNFullStack/Milestone-Project-3).
2. Click the "Code" dropdown button.
3. From here there are two options:
     * Option 1: Click the "Download ZIP" button to download the files. This can be unzipped locally and opened with your preferred IDE.
     * Option 2: Copy the link from the HTTPS box shown. Then open your preferred IDE of choice and in the terminal window of your preferred directory, use the command "git clone" followed by the link that was copied. For example "git clone https://github.com/KNFullStack/Milestone-Project-3.git". This will clone the files in the selected directory.
# Acknowledgements
Would like to say thank you to my mentor Spencer Barriball for his help and guidance throughout the project.

## Code
* XXX
* XXX

## Media
* XXX
* XXX