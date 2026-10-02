## Bulding new pages on the site

Each new page should have some frontmatter in **.toml** markup. E.g.
```
+++
date = "2017-06-05T17:25:22+10:00"
title = "Training"
draft = false
type = "sidebar"
stream = "all"
+++
```

* The **title** tag set the the title text. A *thumbnail* tag can be inlcuded to give the page a thumbnail, and this image will also appear at the top of the page if it is in a news page.
* **date** sets the authorship date of the page. Pages will not appear on the site until after the date set in the frontmatter.
* **draft** identifies the page as a draft -- draft pages will aso not appear on the site (unless it is built with the draft flag, which it will not be).
* If you want your page to show the _sidebar_ (which includes the search box and some other context-dependent widgets), then set **type = "sidebar"**. If you also want a news feed, then set **stream** to "news", "blogs", or "all" for both.


## Including a website project summary from a JIRA PIPE ticket

[See instructions here](https://github.sydney.edu.au/informatics/SIHWebCode/blob/master/WebsiteProjectSummaries.pdf)

# How to install Hugo in OSX #

In the terminal...

### Install OSX command line tools

`xcode-select --install`

### Install Homebrew
(following [Homebrew install instructions](https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/) )

`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### Install Hugo version 0.54

`brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/6c0c7919de42ee5d629d3a9786fb111f4498dab3/Formula/hugo.rb`


## How to compile the website on OSX

`cd path/to/directory`

`hugo server --renderToDisk`

Then go to the website address as indicated e.g. http://localhost:1313/



# Instructions for making the Redhat server work

### Installing Hugo
follow https://www.tecmint.com/linuxbrew-package-manager-for-linux/ to install linuxbrew

then install hugo: https://gohugo.io/getting-started/installing/#linuxbrew-linux

however...hugo 0.55.x breaks our template so we need to install hugo 0.54.0 like this:
`brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/6c0c7919de42ee5d629d3a9786fb111f4498dab3/Formula/hugo.rb`

then copy over to /usr/bin so that jenkins can find it:
(rename existing verion if necessary: `sudo mv /usr/bin/hugo /usr/bin/hugo-old`)
then
`sudo cp /home/linuxbrew/.linuxbrew/Cellar/hugo/0.54.0/bin/hugo /usr/bin/hugo`


### Install Jenkins
This stuff makes Jenkins (continuous integration server) work

`sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo`

`sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key`

`sudo yum install jenkins`

`sudo yum install java`

`sudo service jenkins start`

`sudo chkconfig jenkins on`

(can replace start with stop/restart)

This stuff gives Jenkins (continuous integration server) permission to modify the files served by the apache server

`sudo chown -R .jenkins /var/www/html/`

`chmod -R g+w /var/www/html/`

`sudo find /var/www/html/ -type d -exec chmod -R {} g+s \;`

### To set up Jenkins
Go to port 8080 on the server (from within USyd campus)  [http://sihwpw01035.srv.sydney.edu.au:8080/](http://sihwpw01035.srv.sydney.edu.au:8080/)

Github enterprise repository url
https://USER@github.sydney.edu.au/informatics/SIHWebCode.git
replace USER with your Github enterprise user id.

Add credentials for this user to jenkins in credential manager.

Branches to build
`*/master`

Periodic build schedule (builds every 15 minutes)
`H/15 * * * *`

Shell command to compile website
`rm -r ./public/*`
`hugo`

Shell command to copy to apache server's directory
`rsync -r ./public/* /var/www/html/`

### Change owner of www folder to jenkins so that it can read/write properly
`sudo chown -R jenkins:jenkins /var/www/`

### Troubleshooting when the apache server goes down
Become root
`sudo bash`

Look at the error message (last five lines of the latest error log)
`tail -5 $(ls /var/log/httpd/error* | tail -1 )`

Look at running processes for the http daemon
`ps -ef | grep httpd`

Restart the apache server
`apachectl start`



Restart the apache server...to include chages to the .htaccess file
`sudo service httpd restart `

### Bash for resizing profile images to 300px wide
`sips -Z 300 *.jpg`
