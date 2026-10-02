+++
date = "2017-06-05T17:25:22+10:00"
title = "eNotebook Folder Monitor"
draft = false
+++

[Folder Monitor](http://www.labarchives.com/downloads/) is a desktop application that automatically transfers files from your computer into your eNotebook.

To install FolderMonitor:

1. Download the [Folder Monitor setup file](http://www.labarchives.com/downloads/)
1. Open the file
1. Follow the prompts to install the application

Next you will need to generate a password token to complete the login process. To do this:

1. In LabArchives, select your **Name** (top right), then from the drop-down tab select **LA App authentication**
1. Copy the displayed **email address** and p**assword token**
1. Open **Folder Monitor**
1. When prompted, enter the following login details:
	* **Webservice URL:** http://auapi.labarchives.com/
	* **Login/email:** as per LA App authentication details above
	* **Password:** as per LA App authentication details above

1. Click the **Settings** button on the top right of the folder monitor window, select the checkbox **Login current user automatically on launch**
1. **Add Rule**, will allow you to set up monitoring rules to upload files directly to a location of your choosing in your eNotebook

### How does Folder Monitor work with my eNotebook?

When you set up a new rule, Folder Monitor will scan for all files within the folder (including subfolders if you have selected this option) that conform and ask you to confirm upload of those files. If you have Folder Monitor open, all newly detected files will be automatically uploaded. For more information on setting up rules for upload, see the LabArchives Knowledgebase guide for [Windows](http://labarchives.kayako.com/Knowledgebase/Article/View/243/228/92-folder-monitor-v2-for-windows) or [Mac](http://labarchives.kayako.com/Knowledgebase/Article/View/241/228/93-folder-monitor-v2-for-mac).
