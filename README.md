# Social Ceramics

- [Link](https://social-ceramics.herokuapp.com/) to live site.

## Table of Contents

## Introduction

I developed the idea for *Social Ceramics* after taking a 12-week pottery class which provided me with so much inspiration not only creatively, but gave me the idea for creating a useful platform for a fictional ceramics studio.

The initial idea was to build a sharing platform, hence the name Social Ceramics, where teachers at the studio could post studio updates and useful blog posts that would help the students with their progress, as well as the students being able to share their work, ideas and progress.

## User Experience

### User Stories

#### Site User

- As a **Site User** I can:
  
  - *Register for an account so that I can share my work and view the work of my fellow students.*
  - *Log in with my credentials so that I can share my work and view the work of my fellow students.*
  - *Navigate through the platform easily so that I can interact with my fellow students.*

#### Site Admin

- As a **Site Admin** I can:
  - *Create, read, update and delete posts so that I can manage the Social Ceramics platform.*

## Development

I started the initial planning of the site using Notion, where I wrote down my ideas, user stories and direction for the site including features, which I would then edit down based on viability and to keep on track with an MVP. I found it useful I then created issues, including my user stories which I assigned to the dedicated projects board for the project.

I did find it quite challenging at times but also found it helpful in keeping me focused on the tasks and on track with the overall project.

I also used Figmas FigJam during the planning and development stages which I found helpful to my progress as a visual learner.

I then 

## Design

The overall design is fairly minimalist, which I felt created a good base for the content to be viewed clearly and without too many distractions. I created a logo in Canva which is visible on all pages to maintain consistent branding.

![Social-Ceramics-Logo](./static/images/sc_logo.jpg)

## Features

### Current Features

#### Homepage

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
![Home-not-logged-in](media/images/screenshots/home-not-logged-in.png)

#### About Page

I created an *About* page which provides the user with an introduction to the studio as well as a *Meet the Team* section with an image and brief bio of the studio teachers.

On a desktop the page looks like this.

![About-desktop](media/images/screenshots/meet-the-team-desktop.png)

On devices smaller than 992px the page looks like this.

![About-mobile](media/images/screenshots/meet-the-team-mobile.png)

I created a media query for smaller devices to maximise accessibility and make sure the content was clearly visible as it looked cramped otherwise.

#### Share Your Work

Once a student has logged in, they have the option to share their work. This page becomes visible in the navigation bar as well as on the homepage jumbotron.

#### Student Creations Page

Once the user has logged in, the *Student Creations* page is visible in the navigation bar.

This page acts as a feed to display all of the student posts. It is paginated to show 30 posts per page with each row having 3 columns, so 3 posts per row. Each post shows its user, a caption and the image.

![student-creations](https://media.giphy.com/media/KKCn6jnUpkZH8vT4Nd/giphy.gif)

The user can click the *view post* button to see the post. If the user is the author of the post, the are provided with the option to make changes to or delete their post. This is not visible to other users so that only the author has access to make any changes.

#### Profile

User also have the option of creating a profile with the following fields:

- First Name
- Last Name
- Bio
- Profile Picture

![profile](media/images/screenshots/profile.png)

The user can also edit their profile, for example changing their profile picture and editing their bio.


### Features For Future Implementation

#### Profile

I would like to create a more in-depth profile page for each registered user.

## Issues and Bugs

- Images and font not rendering on deployed site.

- Issue #1
  - I had a problem creating one particular blog post from the admin panel which, when published, it through off the layout.
 ![Bug](media/images/screenshots/bug.png)

  I changed the status of this post to draft, and it went back to normal. I then tested the length of the description, so I edited it down to see if this was causing an issue, but it didn't seem to be. I expected this as I didn't add a max_length to the description field in the post model but wanted to check all options anyway.
  So I then created a new test blog post, and it worked fine.

- Creating a new blog post with the same title, even if one post was in draft status, threw the following error:

  ![Error-message](media/images/screenshots/ErrorMultipleObjects.png)

  I have the title and slug fields set to unique=False, but when I changed the title and slug and the issue was solved.

## Technologies Used

- Gitpod was the platform used to develop the project.
- GitHub was used to build and host the repository, build the projects board and track issues.
- Heroku was used to deploy the site.

### Languages Used

- HTML was used for the layout of all templates.
- CSS was used to style the pages and maintaining brand and styling consistent across the site.

### Frameworks

- Django
  - Django was the main framework, and the backbone of this project, where I created the models, views and forms for the site.
- Bootstrap
  - Bootstrap 5 was used to develop a responsive, mobile friendly site using the predefined classes for a clear and consistent layout.

- Cloudinary

### Libraries

- Summernote
  - Summernote was the WYSIWYG editor used to create posts in the Django admin panel for teachers to use.

- Google Fonts
- Font Awesome
  - Font Awesome was used for the icon that appears when a user is logged in.

## Testing

## Deployment

### Deploying to Heroku

### Forking the Repository

### Cloning the Repository

## Credits

### Content

Content for the blog posts come from:

- [The Little Pot Company](https://thelittlepotcompany.co.uk/blogs/pottery/how-to-centre-clay-the-one-sided-method-beginners-guide)

### Media

- The Social Ceramics logo was created in [Canva](https://www.canva.com/).
  
- All other images used across the site were taken from [Unsplash](https://unsplash.com/), and [Pexels](https://www.pexels.com/).
