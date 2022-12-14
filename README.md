# Social Ceramics

![home](media/images/screenshots/homepage.png)

- [Link](https://social-ceramics.herokuapp.com/) to live site.

## Table of Contents
<!-- TOC -->

- [Social Ceramics](#social-ceramics)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Planning and Development](#planning-and-development)
    - [User Experience](#user-experience)
      - [User Stories](#user-stories)
        - [Site User](#site-user)
        - [Site Admin](#site-admin)
      - [Strategy](#strategy)
      - [Scope](#scope)
      - [Structure](#structure)
        - [Site User Map](#site-user-map)
        - [Site Admin Map](#site-admin-map)
      - [Skeleton](#skeleton)
      - [Surface](#surface)
        - [Design](#design)
  - [Agile Development Phase](#agile-development-phase)
  - [Features](#features)
    - [Current Features](#current-features)
      - [Homepage](#homepage)
        - [Navigation](#navigation)
        - [User Authentication](#user-authentication)
      - [Blog Detail Page](#blog-detail-page)
      - [About Page](#about-page)
      - [Share Your Work](#share-your-work)
      - [Student Creations Page](#student-creations-page)
      - [Student Creations Image Detail](#student-creations-image-detail)
      - [Profile](#profile)
    - [Future Features](#future-features)
      - [Student Profile](#student-profile)
      - [Classes](#classes)
  - [Issues and Bugs](#issues-and-bugs)
    - [Fixed Issues \& Bugs](#fixed-issues--bugs)
    - [Current Issues \& Bugs](#current-issues--bugs)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks \& Libraries](#frameworks--libraries)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Code Validation](#code-validation)
      - [W3C Markup Validator](#w3c-markup-validator)
      - [Jigsaw Validator](#jigsaw-validator)
      - [Python Validation](#python-validation)
    - [Lighthouse Testing](#lighthouse-testing)
  - [Deployment](#deployment)
    - [Deploying to Heroku](#deploying-to-heroku)
    - [Forking the Repository](#forking-the-repository)
    - [Cloning the Repository](#cloning-the-repository)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

<!-- /TOC -->
## Introduction

I developed the idea for *Social Ceramics* after taking a 12-week pottery class which provided me with so much inspiration not only creatively, but gave me the idea for creating a useful platform for a fictional ceramics studio.

The initial idea was to build a sharing platform, hence the name Social Ceramics, where teachers at the studio can post studio updates and useful blog posts that would help the students with their progress, as well as the students being able to share images that show their work, ideas and progress.

This project is the fourth of five portfolio projects to complete during my full Stack Software Development programme with Code Institute.

## Planning and Development

I started the initial planning of the site using Notion, where I brainstormed my ideas, user stories and direction for the site including all features I'd like to have, which I then edited down based on viability and to keep on track with an MVP. I used GitHub to create issues for my user stories which I assigned to the dedicated projects board for the project.

### User Experience

#### User Stories

I have categorised the proposed users for this project as the following:

##### Site User

- Current Site User
  - Students who are involved with Social Ceramics and are registered on the platform.
- Prospective Site User
  - Students who are involved with Social Ceramics but aren't yet registered on the platform.
  - Prospective students of Social Ceramics.

As a **Current Site User** I can:
  
- *Log in with my credentials so that I can share my work and view the work of my fellow students.*
- *Navigate through the platform easily so that I can interact with my fellow students.*
- *View blog posts from the studio so that I can gain knowledge, tips and skills to improve my practice.*
- *Comment on blog posts so that I can interact with the teachers and my fellow students.*
- *View the comments made on blog posts by other users so that I can interact with my fellow potters at the studio*.
- *View the work of other students so that I can be active in the Social Ceramics community.*
- *Share my work on the platform so that I can be an active member of the Social Ceramics studio.*
- *Make changes to my shared posts so that I can ensure I share exactly what I want to or edit any spelling mistakes.*
- *Delete my shared posts so that I can share exactly what I want to.*
- *Comment and like on student posts.*
- *Create a profile so that my experience feels more personal.*
- *Edit my profile so that my experience feels more personal.*
- *View other students profiles so that my experience feels more personal*

As a **Prospective Site User** I can:

- *View blog posts from the studio so that I can judge whether I want to be more involved in the studio.*
- *Sign up for an account so that I can share my work and view the work of my fellow students.*

##### Site Admin

In this case, the Site Admin are the teachers at the studio. The teachers will be posting blog posts to the site which appear on the homepage and these posts are visible to all users, whether they have created an account on the platform, or whether they are a current student at the studio without an account, or a prospective student.

The idea is that the blog posts will cover interesting topics that a ceramics student, or someone who is interested in getting into ceramics, may find useful. This serves the needs of current students at the studio as the posts will be practical and applicable to their practice. This should also entice prospective students by drawing awareness to the studio and the engaging manner it operates in.

- As a **Site Admin** I can:

  - *Create, read, update and delete posts so that I can manage the Social Ceramics platform.*
  - *Approve comments on posts so that I can filter objectionable comments.*
  - *Assign staff status to other teachers so that they can create blog posts and manage the Social Ceramics platform.*

I dropped the following User Stories due to time constraints but plan to implement these in future development of this project.

- *View other students profiles so that my experience feels more personal*
- *Comment and like on student posts.*

#### Strategy

As a ceramics studio, the importance of maximising the students' learning and development is key. As with all skills, the learning process should be engaging and informative to keep the students involved and ensure they are getting the most out of the process.

Being part of a like-minded community and making the experience social can help to encourage the students to reach their full potential by being involved with the studio.

Social Ceramics aims to build this community by:

- Providing useful information that students can make use of alongside their practice, in the form of blog posts by the studio teachers.
- Providing students with a platform to share their work and view the work of their fellow students at the studio.

I created the following strategy table to determine the trade-off of importance versus viability of my user stories:

| Feature      | Importance | Viability |
| -------- | -----------| ------------------|
| Create an account / log in to access the sites features | 5 | 5 |
| Navigate throughout the site with ease | 5 | 5 |
| View teacher blog posts  | 5 | 5 |
| View comments / likes on teacher blog posts | 4 | 4 |
| Comment on blog posts | 4 | 4 |
| Like blog posts | 4 | 4 |
| Share my work | 5 | 5 |
| Make changes to my image posts | 5 | 5 |
| Delete my image posts | 5 | 5 |
| Create a profile | 3 | 3 |
| Edit my profile | 4 | 4 |
| View other students profiles | 3 | 2 |
| Admin CRUD | 5 | 5 |
| Admin approve/delete comments | 5 | 5 |
| Assign staff status | 3 | 5 |
| Admin view user profiles | 5 | 5 |
| Admin delete users/user profiles | 5 | 5 |
| Total | 70 | 76 |

#### Scope

The scope was defined, guided by the strategy to align the features. The following categories explain what is required for this:

- Content Requirements
  - Students are able to:
    - View informative and interesting blog posts.
    - View other users comments on the blog posts.
    - View other students work.

- Functionality Requirements
  - Students are able to
    - Share their work.
    - Comment and like blog posts.
    - Navigate across the site easily.
    - Create a profile for a more personalised experience.

#### Structure

I created two site maps that visualise the user journey around the site. The maps below show the journey for the:

- Site User
- Site Admin

##### Site User Map

![site-map](media/images/screenshots/site-map.png)

##### Site Admin Map

![site-map-admin](media/images/screenshots/site-map-admin.png)

Below is the Entity Relationship Diagram for the project:

![erd](media/images/screenshots/ERD..png)

#### Skeleton

- [Wireframes](wireframes.md) can be found here.

#### Surface

##### Design

The overall design is fairly minimalist, which I felt created a good base for the content to be viewed clearly and without too many distractions. I created a logo in Canva which is visible on all pages to maintain consistent branding.

![Social-Ceramics-Logo](./static/images/sc_logo.jpg)

I used a white background as a base to provide a clear backdrop for the content on the site which is mostly images.

The homepage contains a background image above the blog posts with a call-to-action prompting the user to log in or create an account to continue to experience the full features of the site.

All of the CTA buttons on the site are consistent in styling, are prominent against the white background and the colours represent the desired action. For example the *Log In*, *Share* buttons are blue to represent a positive action. The *Edit* button on the users image and the *Read More* button under the blog posts on the home page are outlined in black to represent a neutral action. Finally, the *Delete Image* button in the users image detail page and *Sign Out* button on the Sign Out page are red because, as it denotes danger, it naturally gives the user pause before completing the action.

## Agile Development Phase

As mentioned earlier, I used GitHub to track my progress during the development of this project. I created issues for User Stories, assigned acceptance criteria and tasks for each one.

Projects Board In Progress:

![progress](media/images/screenshots/in-progress.png)

Projects Board In Done:

![done](media/images/screenshots/project-done.png)

I did find it quite challenging to implement everything as planned, but I do believe that with continued practice and development and the strengthening of my coding ability going forward, the process will be easier to undertake and stick to. I did though find it helpful in keeping me focused on the tasks and on track with the overall project.

## Features

### Current Features

#### Homepage

The homepage displays blog posts made by teachers at the studio and all visitors, logged in or out can view the content. There are clear call-to-action buttons to prompt the user to log-in or sign-up.

![home](media/images/screenshots/home-1.png)

The page contains pagination to display 6 blog posts per page and users can navigate to the following pages using the links.

![pagination](media/images/screenshots/home3.png)

At the bottom of the page there is a simple footer linking to the studios social media platforms. These arent made but in future production they would be.

##### Navigation

The navigation bar is visible on all pages on the site, allowing clear routing for the user to access all of the site pages and features. The sign-posting is clear and the user can see whether they are signed in or not. If they are not, they will see the *Sign Up* and *Log In* buttons which will direct them to the dedicated pages.

![Nav-logged-out](media/images/screenshots/nav-logged-out.png)

Once they have logged in, they will see a personalised message showing they are logged in, with a *Log Out* button. In this case *Hi admin*, and of course the name will change according to the logged-in user.

![Nav-logged-in](media/images/screenshots/nav-logged-in.png)

The navigation changes in the instance that they are logged in as the *Student Creations* page is now visible.

##### User Authentication

Using Djangos built in authentication system, django-allauth, the user is able to register on the site, log-in and log-out.

If the user is authenticated the features they see differ slightly. For example on the homepage, if the user is logged in, they are prompted to share their work.

![Home-logged-in](media/images/screenshots/home-logged-in.png)

If they are not logged in, they are prompted to Sign In.

![Home-not-logged-in](media/images/screenshots/home-sign-in.png)

Ideally, I would like to implement an authorisation system so that only students who are involved with the studio, either using the studio space or taking classes, can register for an account. For example, they sign up with credentials which would include selecting the class they are taking, with this information being checked against a database.

Another idea is that they are sent a sign-up link where they can create an account, the sign-up option would then not be visible on the homepage only the option to log-in. This would be more secure, but I haven't looked into that for the purpose of this project!

#### Blog Detail Page

Once the user clicks on the *Read More* button on each blog post, they are taken to a separate page to read the post.

![blog-detail](media/images/screenshots/blog-detail.png)

Comments are displayed at the bottom of the post and if the user isn't logged in, they are prompted to in order to comment and like.

![comments](media/images/screenshots/comments.png)

Once logged in, the user can leave comments.

![comments-logged-in](media/images/screenshots/comments2.png)

#### About Page

I created an *About* page which provides the user with an introduction to the studio as well as a *Meet the Team* section with an image and brief bio of the studio teachers.

On a desktop the page looks like this.

![About-desktop](media/images/screenshots/meet-the-team-desktop.png)

On devices smaller than 992px the page looks like this.

![About-mobile](media/images/screenshots/meet-the-team-mobile.png)

I created a media query for smaller devices to maximise accessibility and make sure the content was clearly visible as it looked cramped otherwise.

#### Share Your Work

Once a student has logged in, they have the option to share their work. This page becomes visible in the navigation bar as well as on the homepage jumbotron.

![share](media/images/screenshots/share-page.png)

#### Student Creations Page

Once the user has logged in, the *Student Creations* page is visible in the navigation bar.

This page acts as a feed to display all of the student posts. It is paginated to show 30 posts per page with each row having 3 columns, so 3 posts per row. Each post shows its user, a caption and the image.

![student-creations](https://media.giphy.com/media/KKCn6jnUpkZH8vT4Nd/giphy.gif)

The user can click the *View Post* button to see the post. If the user is the author of the post, the are provided with the option to make changes to or delete their post. This is not visible to other users so that only the author has access to make any changes.

#### Student Creations Image Detail

Once clicked on the *Read More* button, the user is taken to a page that displays the image.

![image-detail](media/images/screenshots/image-detail.png)

If the image is one posted by the logged-in user, they have the ability to edit and delete their post.

![edit-view](media/images/screenshots/edit-delete-buttons.png)

They can make changes to the image or the caption or exit without saving.

![edit-view2](media/images/screenshots/edit-delete-view.png)

#### Profile

When a user has created an account, in the navigation bar under the *Profile* dropdown, they are provided with the option to *Create Profile*.

![create-profile-nav](media/images/screenshots/create-profile-nav.png)


Once they have created a profile, this option changes to *View Profile*.

![view-profile-nav](media/images/screenshots/view-profile-nav.png)

The user can create a profile with the following fields:

- First Name
- Last Name
- Bio
- Profile Picture

![profile](media/images/screenshots/profile.png)

The user can also edit their profile, for example changing their profile picture and editing their bio.

### Future Features

#### Student Profile

I would like to implement the ability for users to view each others profile and wanted to do so in this project but couldn't due to time constraints. I also wanted to provide the user with the ability to delete their profile but haven't yet for the same reason. However, these are things I plan to implement going forward.

#### Classes

When I first developed the idea for this project, I wanted to feature a class booking system where students could log in and book onto classes at the studio. This is another feature I would like to implement going forward.

## Issues and Bugs

### Fixed Issues & Bugs

**Bug** When a user signed up with an email address, an OSError was thrown.

- **Solution** - I added
  - ```ACCOUNT_EMAIL_VERIFICATION = "none"``` in settings.py

**Bug** I had a problem creating one particular blog post from the admin panel which, when published, it through off the layout.

![Bug](media/images/screenshots/bug.png)

- **Solution** I changed the status of this post to draft, and it went back to normal. I then tested the length of the description, so I edited it down to see if this was causing an issue, but it didn't seem to be. I expected this as I didn't add a max_length to the description field in the post model but wanted to check all options anyway.
So I then created a new test blog post, and it worked fine.

**Bug** Creating a new blog post with the same title, even if one post was in draft status, threw the following error:

  ![Error-message](media/images/screenshots/ErrorMultipleObjects.png)

  I have the title and slug fields set to unique=False, but when I changed the title and slug and the issue was solved.

**Bug** I had an issue with blog posts incorrectly displaying on the *Student Creations* page rather than just the home page.

- **Solution** In hindsight I should have created a separate field in the model for filtering. However, in the end I set a filter on the posts queryset in the StudentUpload view to filter by draft status as the posts uploaded by students were considered drafts in the database, compared to the teacher blog posts which had a status of published to be displayed on the home page.

**Bug** I had an issue with Summernote when I copied and pasted content into the editor. The format was thrown off, and it wasn't responsive on the site.

- **Solution** By selecting the Helvetica Neue font and justifying the content, it seemed to work fine. When typing directly into the editor the font inherits the Alumni Sans font from the stylesheet. At the moment this wasn't a big issue and in theory the teachers will be writing their own content for the site but it's something I'll look into further going forward.

### Current Issues & Bugs

**Bug** When a user comments on a blog post, the comments that are already there disappear. I wasn't able to find a solution to this in time but will look into it in the future.

![comments-issue-2](media/images/screenshots/comments-2.png)

![comments-issue-1](media/images/screenshots/comments-1.png)

**Bug** I had removed the description that I initially chose to display on the homepage blog article cards. However, after adding it back in to test out, a similar issue I faced earlier reoccurred with the layout being thrown off. Nothing else was changed, so I'm unsure what caused this. I removed and re added the splice filter, the safe filter but the issue still remained. I decided to keep it without the description anyway, ending it with a *Read More* CTA button.

![post-description-bug](media/images/screenshots/bug2.png)

**Bug** When a user needs to reset their password, an error is thrown after entering an email address. I created a basic custom error page to display to the user as couldn't fix this in time.

![server-error](media/images/screenshots/custom-error.png)

I plan to look further into this as it's an important feature to have.

## Technologies Used

- Gitpod was the platform used to develop the project.
- GitHub was used to build and host the repository, build the projects board and track issues.
- Heroku was used to deploy the site.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [drawio](https://app.diagrams.net/) was used to create the site maps.

### Languages Used

- HTML was used for the layout of all templates.
- CSS was used alongside Bootstrap to style the pages and keep branding and styling consistent across the site.
- Python was used to implement Django functionality.
- JavaScript - Summernote Library and short piece of code to set a timer on messages displayed.

### Frameworks & Libraries

- Django
  - Django was the main framework, and the backbone of this project, where I created the models, views and forms for the site.
- Bootstrap
  - Bootstrap 5 was used to develop a responsive, mobile friendly site using the predefined classes for a clear and consistent layout.
- Cloudinary
  - Was used as cloud storage for all image uploads on the site.
- Summernote
  - Summernote was the WYSIWYG editor used to create posts in the Django admin panel for teachers to use.
- Crispy Forms
  - Used to style forms on the site.
- Google Fonts
  - *Alumni Sans* is the main font family used across the site.
- Font Awesome
  - Used for the profile icon that appears when a user is logged in as well as the like and comment icons on the post detail page.

## Testing

### Manual Testing

I conducted manual testing on all my user stories and the results are as follows:

As a **Current Site User** I can:

**Log in with my credentials so that I can share my work and view the work of my fellow students**

Several test accounts were used to log in and worked as they should. The user is taken to the homepage with full access visible in the navigation bar. If incorrect login details are entered, the user receives a message saying the *username and/or password you specified are not correct* and prompted to sign in again.

**Navigate through the platform easily so that I can interact with my fellow students**

Links in the navigation bar work correctly and take the user to each intended page. The links work for users who are logged in and out. The option to log out for the logged-in user is always visible and there are CTA buttons on the home page to prompt users.

**View blog posts from the studio so that I can gain knowledge, tips and skills to improve my practice**

Accessing the site without an account and also testing the view from several test accounts display the blog posts on the homepage with pagination and the links to each post take the user to the respective pages.

**Comment on blog posts so that I can interact with the teachers and my fellow students**

I tested commenting on blog posts from different test accounts and the comments were sent to the admin panel for approval by admin. Once approved in the admin panel they appear on the post detail page. There is a bug with this feature which I have explained in the *Current Issues & Bugs* section.

**View the comments made on blog posts by other users so that I can interact with my fellow potters at the studio**

Comments made are visible on the blog detail page.

**View the work of other students so that I can be active in the Social Ceramics community**

Once logged in, the shared work by other students are visible to the user on the *Student Creations* page. A new post was created as a separate user for testing, which displayed on the page and was visible to on the page from other user accounts.

**Share my work on the platform so that I can be an active member of the Social Ceramics studio**

Images were uploaded with several test accounts to make sure they were displaying correctly on the *Student Creations* page which they were.

**Make changes to my shared posts so that I can ensure I share exactly what I want to or edit any spelling mistakes**

The caption and image shared were changed by clicking *Edit Image* and these changed were displayed.

**Delete my shared posts so that I can share exactly what I want to**

An image was shared and then deleted by clicking the *Delete Image* button. The image was no longer visible on the *Student Creations* page.

**Create a profile so that my experience feels more personal**

Under the *Profile* dropdown in the navigation bar, if a user has created a profile, the option *View Profile* appears. If the user hasn't created a profile, the option *Create Profile* appears. A new user was created to test it works which it does. Their profile displays and the user can edit their profile from there.

**Edit my profile so that my experience feels more personal**

After creating a profile, the *Edit Profile* button was clicked and changed were made. The changes save to the users profile which is displayed after making the changes.

As a **Prospective Site User** I can:

**View blog posts from the studio so that I can judge whether I want to be more involved in the studio**

The site was accessed, and all the intended pages were displayed to users without an account.

**Sign up for an account so that I can share my work and view the work of my fellow students**

Several test accounts were created and users are taken to the homepage once they have created an account. The user is displayed a message that their *username is unique and cannot be changed*. If they create an account with a username that is already in the database, a message is displayed stating that.

As a **Site Admin** I can :

**Create, read, update and delete posts so that I can manage the Social Ceramics platform**

Once logged in with admin credentials, a new post was created and published. In the admin panel, any changes made to the content were also displayed on the home page after saving. Posts that were deleted from the admin panel are also removed from the home page.

**Approve comments on posts so that I can filter objectionable comments**

After posting a new comment from a test account, the post became visible in the admin panel with the option to approve or delete.

**Assign staff status to other teachers so that they can create blog posts and manage the Social Ceramics platform**

A 'teacher' account was created and assigned admin status. They are able to create, view, edit and delete posts as well as approve or delete comments made.

### Code Validation

#### W3C Markup Validator

All pages were passed through the W3C Validator. The only issue was on the post detail page, the validator showed there was a stray closing p tag. However after several checks I couldn't find this stray tag in my code and description has a safe filter on it so believe it is caused by the Summernote editor.

![validator-bug](media/images/screenshots/validator-bug.png)

#### Jigsaw Validator

The code from the one CSS stylesheet was passed through the Jigsaw validator with no errors.

![jigsaw](media/images/screenshots/jigsaw.png)

#### Python Validation

At the time of testing, the PEP8 Online website was down so the pycodestyle Gitpod extension was used instead. The errors shown are from the settings.py file, stating that lines are too long, however there isn't a way to shorten them in this file.

The only other error is in my edit_profile view. After taking several steps to fix a late issue with the page not rendering correctly, the only method that fixed this problem at the time was a try/except block. I thought it was better to have an explained error than to leave out the feature all together. However, I will look into finding a better way around this in future development of this project.

![pep8-error](media/images/screenshots/python-testing.png)

### Lighthouse Testing

Lighthousetesting results can be found [here](lighthousetesting.md).

## Deployment

### Deploying to Heroku

To deploy the site from the GitHub repository to Heroku, the following steps were taken:

1. Create the Heroku App:
   - Click the 'New' button on the Heroku dashboard.
   - Click 'Create New App':
2. Give the app a unique name:
   - I gave this project the name social-ceramics
3. Select the region:
   - In my case I selected Europe.
4. Add the database:
   - Click on the Resources tab
   - In the 'Add-ons' box search for 'Heroku Postgres' and click it to add it to the project.
   - Select 'Hobby Dev - free' from the 'plan name' dropdown and click 'Submit Order Form'.
5. Prepare the environment:
   - Click on the Settings tab.
   - Click 'Reveal Config Vars' to display the DATABASE_URL.
   - Copy the url next to DATABASE_URL.
   - Return to the GitPod workspace.
   - Create a file called env.py in the main directory.
   - In the env.py file, set the following environment variables:
     - Set the DATABASE_URL by pasting in the url copied from Heroku.
     - Set the SECRET_KEY to your chosen value.
   - Add the SECRET_KEY value to Config Vars in Heroku.
6. Set up settings.py:
   - At the top of the file, add the following:
     - ```import os```
     - ```import dj_database_url```
     - ```if os.path.isfile('env.py'):import env```
   - In the SECRET_KEY section, remove the insecure key and add in the environment variable:
     - ```SECRET_KEY = os.environ.get('SECRET_KEY')```
   - Set up the Postgres database:
     - Delete the value from the DATABASES section and replace it with the following:
     - ```DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL) }```
   - Add Cloudinary libraries into INSTALLED_APPS section:
     - ```INSTALLED_APPS = [ 'cloudinary_storage', 'django.contrib.staticfiles', 'cloudinary' ]```
   - From the Cloudinary dashboard, copy the API Environment Variable by selecting 'copy to clipboard'.
   - In the env.py file, set the CLOUDINARY_URL to the value copied from the clipboard. (Note: Remember to remove the CLOUDINARY_URL= part from the beginning of the copied value.)
   - In your Heroku dashboard, add CLOUDINARY_URL to the Config Vars and paste the value copied from the clipboard.
   - At the end of the settings.py file add the following:
     - ```STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'```
     - ```STATICFILES_DIRS = [os.path.join.(BASE_DIR, 'static')]```
     - ```STATIC_ROOT = os.path..join(BASE_DIR, 'staticfiles')```
     - ```MEDIA_URL = '/media/'```
     - ```DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'```
   - Let Django know where templates will be stored by adding the following to the top of the file, under BASE_DIR:
     - ```TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')```
   - In the TEMPLATES setting, change the DIRS key to the following:
      - ```'DIRS': [TEMPLATES_DIR]',```
   - Add Heroku host name into ALLOWED_HOSTS:
      - ```ALLOWED_HOSTS = ['appname.herokuapp.com', 'localhost']```
   - Create the following three folders in the main directory:
     - media
     - static
     - templates
   - Create a file named 'Procfile' in the main directory and enter the following in the file:
     - ```web: gunicorn appname.wsgi```
7. Commit and deploy to Heroku:
   - Make an initial commit and push to the GitHub repository:
     - ```git add .```
     - ```git commit -m 'Initial deployment'```
     - ```git push```
   - Return to your Heroku dashboard.
   - Click on the Deploy tab.
   - Select GitHub for deployment method. (note: Connect your GitHub account if it isn't already connected.)
   - In the Connect to GitHub section, search for your repository.
   - Click connect.
   - Scroll down to Manual Deploy.
   - Click 'Deploy Branch'.
   - Once the app has been deployed successfully, you can click 'Open App' to view. You should see a screen with the message 'The install worked successfully! Congratulations!'.

### Forking the Repository

In order to fork the project, the following steps are to be followed:

1. Log in to GitHub.
2. Navigate to the repository.
3. Find the 'Fork' button to the top right of the page.
4. Once you click this button the fork will be in your repositories.

### Cloning the Repository

In order to run this project locally, the following steps are to be followed:

1. Install the Gitpod Browser Extension for Chrome.
2. After installation, restart the browser.
3. Log into GitHub or create an account.
4. Locate the GitHub Repository.
5. Click the green 'Gitpod' button in the top right corner of the repository. This will trigger a new Gitpod workspace to be created from the code in GitHub where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into GitHub or create an account.
2. Locate the GitHub Repository.
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```git clone https://github.com/USERNAME/REPOSITORY```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub here

## Credits

### Content

The following sites were used for blog content on the site:

- [The Little Pot Company](https://thelittlepotcompany.co.uk/blogs/pottery/how-to-centre-clay-the-one-sided-method-beginners-guide)
- [The Crucible](https://www.thecrucible.org/guides/ceramics/handbuilding/)
- [The Spruce Crafts](https://www.thesprucecrafts.com/the-basics-of-building-coil-pots-2745832)
- [The Spruce Crafts](https://www.thesprucecrafts.com/how-to-make-handles-for-pottery-2745736)
- [Expert Clay](https://expertclay.com/tips-throw-taller-pots-pottery-wheel/)

### Media

- The Social Ceramics logo was created in [Canva](https://www.canva.com/).
  
- All other images used across the site including all user uploads and blog posts were taken from [Unsplash](https://unsplash.com/), and [Pexels](https://www.pexels.com/).

### Code

- The Code Institute Django blog tutorial was used as a helpful basis. Commenting and likes features were used from the tutorial.
- [Stack Overflow](https://stackoverflow.com/) various articles for general help.
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) documentation.
- [YouTube](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) was also a helpful source and the Codemy Django playlist was especially so.

### Acknowledgements

Special shoutout to my amazing mentor Richard Wells for his help and guidance during this process! Also, thanks to tutor support who were super helpful with certain issues that frazzled my brain!
