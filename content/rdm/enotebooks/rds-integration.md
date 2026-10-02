+++
redirectTo = "https://sydneyuni.service-now.com/sm?id=kb_article_view&sysparm_article=KB0013721"
date = "2017-06-05T17:25:22+10:00"
title = "eNotebook RDS Integration Widget"
draft = false

+++

 ![usyd_rds_link](../USYD_link_widget.png)

* [Features](#Features)
* [Operating System/Browser Differences](#OSBD)
* [How to use USYD RDS Link](#use)
* [Frequently Asked Questions](#FAQ)


The eNotebook supports uploads of files up to 4GB each, with no size limit to total amount of data that can be stored.

However, there are functional limitations to storing the following types of files:

* Files greater than 4GB (e.g. high definition video files, genomic datasets)
* Large file series (e.g. image series with hundreds of sequential images)
* Files that need to edited regularly by programs that must access the file locally (e.g. nVivo libraries, coding)

We recommend that the above file types are stored on the University of Sydney [Research Data Store (RDS)](https://sydneyuni.service-now.com/sm?id=kb_article_view&sysparm_article=KB0010833). The RDS is a University maintained Network Attached Storage device. You may request storage through the [Research Data Management Planning (RDMP) tool](https://informatics.sydney.edu.au/rdm/dashr/). RDS Classic is mountable to your local computer and can therefore act as an additional hard drive on your local system. There are rigorous back up and disaster recovery protocols which ensure that your research data is stored more securely than it would be on your own system or on external hard drives.

A widget called **USYD RDS Link** can be used to link eNotebook entries with files stored on the RDS, allowing research data files to be connected to the broader research context recorded in the eNotebook.

### <a name="Features"></a> Features

The USYD RDS Link widget has the following functionality:

* Ability to view any RDS Classic partitions* you have access to
* Ability to select any number of files/folders in your RDS partition
* Saving to page will generate links on your eNotebook page**
* Basic metadata (file size and last accessed) are recorded with links
* When links are clicked, the directory will be mounted or the file will be opened directly**
* Double-clicking/editing the widget entry will show if files have changed
* Updated/deleted files will be flagged
* Collaborators with different RDS access can include extra links but they do not wipe over links you have generated previously when editing the entry

*RDS Research Computing Optimised Storage (RCOS) is not currently supported

**Different operating systems and browsers vary, see Operating System/Browser Differences below

### <a name="OSBD"></a>Operating System/Browser Differences
USYD RDS Link has been tested with Windows Internet Explorer, Firefox and Chrome as well as Mac Safari, Firefox and Chrome. The widget behaves slightly differently depending on the operating system and browser being used.

These differences are:

Windows Internet Explorer: full functionality as listed above
Windows Chrome: links are unable to be clicked to open/mount the drive
Windows Firefox: full functionality with an [additional add-on](https://addons.mozilla.org/en-US/firefox/addon/local-filesystem-links/) to enable opening of links. See FAQ [Why can’t I open the linked folder/files in Firefox? ](#FAQ10)for more details.
Mac, all browsers: when clicking on a link to a file (rather than a folder) the file will not open directly, instead the folder it is in will mount to the desktop


## <a name="use"></a>How to Use the Widget


### Adding the widget to a page

1. In any page go to the **Add Entry** bar near the top of the page, select **More > Widget**
1. In the window **Select a widget to work with** choose **USYD RDS Link **from dropdown menu
1. Click **Use USYD RDS Link** - a new entry will populate on the page
1. Enter your **Unikey** and **Password**
1. Click **Login** or press Enter

![RDS_widget_adding_entry](../RDS_widget_adding_entry.jpg)

### Adding links

1. Use arrow keys to open folders and navigate to your intended folders/files
1. Select any folders or files – multiple files/folders can be selected
1. Click **save to page**
1. A file path link will be generated in the entry with basic metadata in brackets after the file path (with the exception of Windows Chrome, see [Operating System/Browser differences](#OSBD) )

![RDS_widget_adding_links1-3](../RDS_widget_adding_links1-3.jpg)
![RDS_widget_adding_links4](../RDS_widget_adding_links4.jpg)


### Accessing linked files/folders

1. Clicking the link will take you to your directory or open the file directly - see Operating System/Browser differences for more information
1. You will only be able to access files/folders within RDS directories for which you have been granted access


### Editing links/checking file changes
You can add or remove links by editing the entry. Editing the entry also allow you to check if files were deleted or modified since you last interacted with the entry. Please note that this is a basic file check based on file size and date last accessed and is not a perfect control for file integrity.

**To edit links:**

1. **Hover** over the entry and **click on the pencil** symbol
1. Enter your **Unikey** and **password** if necessary
1. **Select** new files/folders or **deselect** linked files/folders
1. Click **Save to page**

**To check file/folder changes:**

1. **Hover** over the entry and **click on the pencil** symbol
1. Enter your **Unikey** and **password** if necessary
1. Editing the widget entry will automatically check basic metadata of files or folders against the last time the widget entry was saved
1. If files or folders have been have been moved*, deleted or changed they will be flagged with **Deleted** or **Updated** respectively
1. You may now save these flags to the page by clicking **Save to page**

*Please note the widget is unable to distinguish between moved or deleted files and both will be flagged as Deleted

## <a name="FAQ"></a>Frequently Asked Questions

* [Can I access my linked files outside the University network (e.g. at home)?](#FAQ1)
* [Why can’t I see my RCOS directories in the USYD RDS Link?](#FAQ2)
* [What does the refresh button do?](#FAQ3)
* [Will the links be preserved when I reorganise my files on the RDS?](#FAQ4)
* [What do the “Updated” and “Deleted” flags indicate?](#FAQ5)
* [Who has access to the linked files in my eNotebook?](#FAQ6)
* [Will sharing my eNotebook will collaborators give them access to my files on the RDS?](#FAQ7)
* [Why can’t I open a file/folder?](#FAQ8)
* [Why can’t I interact with links when I use Google Chrome in Windows?](#FAQ9)
* [Why can’t I open the linked folder/files in Firefox?](#FAQ10)
* [How do I access linked file folders on shared computers?](#FAQ11)

**<a name="FAQ1"></a>Can I access my linked files outside the University network (e.g. at home)?**

When using your computer outside the University network, you will need a VPN connection to access your RDS directories. For more information on VPN connections refer to this page: [What is the Virtual Private Network (VPN)?](https://sydneyuni.service-now.com/sm?id=kb_article_view&sysparm_article=KB0011460)

**<a name="FAQ2"></a>Why can’t I see my RCOS directories in the USYD RDS Link?**

RCOS is not currently supported by the widget, although we hope to introduce this functionality soon.

**<a name="FAQ3"></a>What does the refresh button do?**

Clicking refresh will remove links from deleted files and remove any generated flags. It is essentially creating the links anew.

**<a name="FAQ4"></a>Will the links be preserved when I reorganise my files on the RDS?**

No, links are broken when files or folders are moved to any other directory. They will be flagged as deleted if the widget entry is edited.

**<a name="FAQ5"></a>What do the “updated” and “deleted” flags indicate?**

When editing the entry, the widget will check if the listed files/folders have been modified or deleted by checking basic metadata against the last time the widget entry was saved. A tag “updated” or “deleted” will appear in front of the link if a change has been detected. The metadata (last date updated and file size) will be updated to reflect the new attributes of the file/folder.

**<a name="FAQ6"></a>Who has access to the linked files in my eNotebook?**

When clicking on a linked file, only Unikey holders who have been granted access to the appropriate RDS directories will be able to open folders or files linked in the eNotebook. Granting access to the eNotebook is not enough to share a file stored on the RDS.

Access to RDS directories is determined by the RDMP for that project, with any listed contributors having access to that RDS directory. Changing access to RDS directories can either be administered by the PI through the RDMP tool or otherwise requests can be lodged with ICT.

**<a name="FAQ7"></a>Will sharing my eNotebook will collaborators give them access to my files on the RDS?**

You can share parts of your eNotebook with other Unikey holders or external collaborators. They will be able to see the links but they will not be able to access them unless their Unikey has also been granted access that specific directory in the RDS.

See above FAQ [Who has access to the linked files in my eNotebook?](#FAQ1) for more information. You are able to request an affiliate Unikey with ICT if you require an external collaborator to access a file stored in the RDS.

**<a name="FAQ8"></a>Why can’t I open a file/folder?**

For Windows Chrome or Windows Firefox users, see FAQs below.

For other browsers, you only will be able to open files/folders that are located in directories where your Unikey has been granted access. Otherwise you will see an error messages such as “Windows cannot access…” or “…can’t be opened because you don’t have permission to see its contents”. Depending on your browser, this error message will vary.

If you are outside the university network, you are required to connect to your VPN to open links. See FAQ “Can I access my linked files outside the University network (e.g. at home)?”

**<a name="FAQ9"></a>Why can’t I interact with links when I use Google Chrome in Windows?**

When using Windows OS and Chrome the added file/folder paths are not active links. You need to open the same page in Firefox or Internet Explorer to access the file/folders. Additionally, you can copy the link(s) from the entry and paste them into the Windows Explorer to locate the file.

**<a name="FAQ10"></a>Why can’t I open the linked folder/files when I use Firefox in Windows?**

To be able to open the linked folder/files in Firefox you need to install an [additional add-on](https://addons.mozilla.org/en-US/firefox/addon/local-filesystem-links/). To do this:


1. Click the 3 horizontal lines in the top right corner of your browser
1. Select **Add-ons**
1. Search for **Local Filesystem Links**
1. Click **Install**

![RDS_widget_firefoxaddon](../RDS_widget_firefoxaddon.jpg)

**<a name="FAQ11"></a>How do I access linked file folders on shared computers?**

When using a shared computer, the best practice is to login and log out with every session. If you are logged in with your own Unikey credentials then the widget may use the computer login credentials to validate your RDS access. If the shared computer uses a non-unikey profile, you can choose to map your network drive with your Unikey credentials using the instructions at this page: [How do I map my network drive so I can access my network storage?](https://sydneyuni.service-now.com/selfservice/?id=kb_article_view&sys_kb_id=add54e3edb01bbc8c8a5773c349619ae&sysparm_tsqueryId=410ad93fdb36334c5beaf9b7f496198e&sysparm_rank=4)

Please ensure you logout of the computer when you are done to prevent unintended access to files stored on your RDS.
