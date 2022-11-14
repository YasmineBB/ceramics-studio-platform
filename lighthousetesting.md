# Lighthouse Testing

Below are the results of the Google Lighthouse testing for the site. I tested each page of the site on a mobile device and on a desktop. I also tested each page, when applicable, for when a user was logged in or logged out.

## Homepage | Logged In | Desktop

![home-logged-in-desktop](media/images/screenshots/lh-home-desktop-loggedin.png)

## Homepage | Logged In | Mobile

![home-logged-in-mobile](media/images/screenshots/lh-home-mobile-loggedin.png)

## Homepage | Logged Out | Desktop

![home-logged-out-desktop](media/images/screenshots/lh-home-desktop-loggedout.png)

## Homepage | Logged Out | Mobile

![home-logged-out-mobile](media/images/screenshots/lh-home-mobile-loggedout.png)

## Log In | Desktop

![login-desktop](media/images/screenshots/lh-login-desktop.png)

## Log In | Mobile

![login-mobile](media/images/screenshots/lh-login-mobile.png)

## Sign Up | Desktop

![sign-up-desktop](media/images/screenshots/lh-signup-desktop.png)

## Sign Up | Mobile

![sign-up-mobile](media/images/screenshots/lh-signup-mobile.png)

## Log Out | Desktop

![log-out-desktop](media/images/screenshots/lh-logout-desktop.png)

## Log Out | Mobile

![log-out-mobile](media/images/screenshots/lh-logout-mobile.png)

## Post Detail | Logged Out | Desktop

![post-detail-logged-out-desktop](media/images/screenshots/lh-postdetail-desktop-loggedout.png)

## Post Detail | Logged Out | Mobile

![post-detail-logged-out-mobile](media/images/screenshots/lh-postdetail-mobile-loggedout.png)

## Post Detail | Logged In | Desktop

![post-detail-logged-in-desktop](media/images/screenshots/lh-postdetail-desktop-loggedin.png)

## Post Detail | Logged In | Mobile

![post-detail-logged-in-mobile](media/images/screenshots/lh-postdetail-mobile-loggedin.png)

## Student Creations | Desktop

![student-creations-desktop](media/images/screenshots/lh-student-creations-desktop.png)

## Student Creations | Mobile

![student-creations-mobile](media/images/screenshots/lh-student-creations-mobile.png)

## Image Detail | Desktop

![image-detail-desktop](media/images/screenshots/image-detail-dekstop.png)

## Image Detail | Mobile

![image-detail-mobile](media/images/screenshots/image-detail-mobile.png)

## Share Post | Desktop

![share-post-desktop](media/images/screenshots/lh-share-desktop.png)

## Share Post | Mobile

![share-post-mobile](media/images/screenshots/lh-share-mobile.png)

## Create Profile | Desktop

![create-profile-desktop](media/images/screenshots/lh-createprofile-desktop.png)

## Create Profile | Mobile

![create-profile-mobile](media/images/screenshots/lh-createprofile-mobile.png)

## Edit Profile | Desktop

![edit-profile-desktop](media/images/screenshots/lh-editprofile-desktop.png)

## Edit Profile | Mobile

![edit-profile-mobile](media/images/screenshots/lh-editprofile-mobile.png)

## About | Desktop | Logged In

![about-desktop-logged-in](media/images/screenshots/lh-about-desktop-logged-in.png)

## About | Mobile | Logged In

![about-mobile-logged-in](media/images/screenshots/lh-about-mobile-loggedin.png)

## About | Desktop | Logged Out

![about-desktop-logged-out](media/images/screenshots/lh-about-desktop-logged-out.png)

## About | Mobile | Logged Out

![about-mobile-logged-out](media/images/screenshots/lh-about-mobile-logged-out.png)

Unfortunately there were some big issues with the about pages which had very low scores on performance and best practices which mostly came down to image sizing. The image links were to the external image source. When I saved the images to my static files and accessed them the links were displayed as broken on the page.

My paths were set up correctly in settings.py and the files were being accessed as they should in the template. After spending a lot of time looking into it and trying different fixes to no avail, I decided to keep the images as they are so that they display for the purpose of the project and due to the time constraints at the time of conducting Lighthouse testing. Going forward I will conduct testing earlier on in development to avoid this problem and will properly implement correct image sizing with Cloudinary.

Overall, the main issues on the other pages were performance on mobile devices. Going forward I will look into image resizing and will also adjust the aspect ratio on the Edit Profile page as this has reduced the score on Best Practices.
