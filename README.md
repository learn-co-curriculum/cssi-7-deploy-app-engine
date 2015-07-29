# Deploying an app engine app

We are going to deploy our App Engine app to the Internet! You can `git clone` this repo to get an example app to deploy.

## Instructions

1. Visit the [Google Developers Console](https://console.developers.google.com/project) and click "Create Project"
2. You should see a dialog like this:

  ![Create screen 1](http://i.imgur.com/SME2wp7m.png)
3. Fill in "Project name" with a name -- it could be any name (does not have to match your project folder).

  As you are filling in the project name, there should be small text under the text box that tells you your project id. In this example, our project id is "magnetic-set-102113". You will have a different project id.
  
  **Remember your project id** since we'll need it in a few steps!
  
  ![Create screen 2](http://i.imgur.com/ZXVtYHym.png)
4. Click "Create"
5. Now go to Terminal, and `cd` into the directory of your App Engine project.
  * If you `git clone` this repository, this means you should `cd cssi-7-deploy-app-engine/my-app`
6. Run this command **using your own project id**

  `appcfg.py --oauth2 -A magnetic-set-102113 update .`

  Note: **do not use "magnetic-set-102113"** -- you need to use the project id from step 3!

 This may open up a screen like this in Chrome:
 
 ![Accept auth](http://i.imgur.com/7jYywmRm.png)
 
 If you see this, click "Accept"
 
 The terminal should show something like the following:
 
 ```
Authentication successful.
10:13 AM Scanning files on local disk.
10:13 AM Cloning 1 static file.
10:13 AM Cloning 3 application files.
10:13 AM Uploading 4 files and blobs.
10:13 AM Uploaded 4 files and blobs.
10:13 AM Compilation starting.
10:13 AM Compilation completed.
10:13 AM Starting deployment.
10:13 AM Checking if deployment succeeded.
10:13 AM Deployment successful.
10:13 AM Checking if updated app version is serving.
10:13 AM Completed update of app: magnetic-set-102113, version: 1
vrk-macbookpro2:my-app
```

7. Congratulations, your app should now be live and on the internet!
  
  Check out http://**your-app-id**.appspot.com/, e.g. our example is http://magnetic-set-102113.appspot.com/.  
