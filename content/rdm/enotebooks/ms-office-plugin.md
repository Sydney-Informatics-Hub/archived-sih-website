+++
redirectTo = "https://sydneyuni.service-now.com/sm?id=kb_article_view&sysparm_article=KB0013721"
date = "2017-06-05T17:25:22+10:00"
title = "eNotebook MS Office Plugin"
draft = false
+++

The eNotebook provides the ability to create and edit Microsoft Office documents within the web browser, using a HTML-based editor. For more information on the HTML-based editor, please see the [LabArchives KnowledgeBase article ](http://labarchives.kayako.com/Knowledgebase/Article/View/96/236/431-office-documents) on the feature. You are also able to work in Microsoft Office and open and save your created files directly from or into your eNotebook with the Microsoft Office plugin.

## How do I install the Microsoft Office Plugin?
Download the appropriate plugin for your system from the [LabArchives website](http://www.labarchives.com/downloads/).

### Windows computers
To install the plugin for Windows:

1. Close any Microsoft Office applications you might have open
1. Open the downloaded plugin file and select **Run** when prompted
1. Follow the prompts to install the plugin

The plugin needs to be configured to log into the Australian LabArchives server. To do this:

1. From Word, select **File** then **Login to LabArchives**
1. Select LA Server Tab and set it to **https://auapi.labarchives.com**
1. Select **User Info Tab**
1. As a UniKey is needed to login to LabArchives, you will need to generate a password token in order to complete the login process. To do this:

	* In LabArchives, select your **Name** (top right), then from the drop-down tab select **LA App authentication**
	* Copy the displayed email address and password token
	* Paste the email address and password token into the login box then select the **Remember Me** checkbox (so that you only have to do this once)
	* Select **OK**

### Mac computers

The Microsoft Office plugin for Mac will automatically add LabArchives to your File menu in Word and Excel. Special instructions are needed to integrate LabArchives with PowerPoint, see information below the installation instructions.

To install the plugin for **Mac**:

1. Close any Microsoft Office applications you might have open
1. Open the file and follow the prompts to install the plugin

The plugin needs to be configured to log into the Australian LabArchives instance. To do this:

1. From Word, select **File** then **LabArchives > Log in**
1. Select LA Server Tab and set it to **https://auapi.labarchives.com**
1. Select **User Info Tab**
1. As a UniKey is needed to login to LabArchives, you will need to generate a password token in order to complete the login process. To do this:

	* In LabArchives, select your Name (top right), then from the drop-down tab select LA App authentication
	* Copy the displayed email address and password token
	* Paste the **email address** and **password token** into the login box then select the **Remember Me** checkbox (so that you only have to do this once)
	* Select **OK**

**Instructions for Installing the Mac Add-in for PowerPoint in Office 2016**

1. From PowerPoint, select the Tools menu, then select Add-ins. This opens a window listing enabled add-ins, and allows you to add others.
1. Select add (+), and then select the LabArchives add-in (LabArchives.ppam). If you cannot see the file, search LabArchives.ppam in the Finder search bar to locate it.
1. When prompted, confirm that the macros are enabled for the add-in
1. The LabArchives add-in should now be listed as enabled

## How do I use the Microsoft Office Plugin?

### Opening files from your eNotebook
Once you have installed the plugin, the menu to open files from your eNotebook is in the File menu. Example menus for Word 2013 for Windows and Word 2016 for Mac is depicted below.

![Office_Plugin_menu-windows](../Office_Plugin_menu-windows.jpg)

eNotebook menu in Word 2013 for Windows


![Office_Plugin_menu-mac](../Office_Plugin_menu-mac.jpg)

LabArchives menu in Word 2016 for Mac

Clicking **File > Open from LabArchives** in Windows and **File > LabArchives > Open** in Mac will bring up a directory of your eNotebooks. You can then select the Office document you wish to open.

If a file has been opened from your eNotebook, clicking Save in the Office program will save directly to your eNotebook, rather than onto your hard drive.

Please note that the plugin is not completely backwards compatible with older file formats of MS Office (1997-2003 formats: .doc, .xls and .ppt). While you can save these file formats to your eNotebook through the plugin (see below), they will not be detected when trying to open these files from your eNotebook.

### **Saving files to your eNotebook**
If you have created a new document in your Office program and wish to save it into your eNotebook, click **File > Save As to LabArchives** in Windows and **File > LabArchives > Save As** for Mac. A directory will appear of all your eNotebooks, select the page to save to and click OK.

Please note that there must be a preexisting page in your eNotebook to save a Office document/file to, you cannot create a new page from the LabArchives Save As directory box.

### **Detaching a document from your eNotebook**
In instances when you have opened a document from your eNotebook and then saved it to your local drive or vice versa, there is a connection between this document and your eNotebook.

Making changes to the version on your hard drive will prompt you to log into your eNotebook when you want to save changes. It will also prompt you to load new changes if the online version has been updated. This ensures that all edits are maintained in both copies.

If you do not want the changes to be saved back to you eNotebook or updated from the eNotebook, you can **Detach the document** in Windows and **Detach** in Mac to sever the connection.
