+++
date = "2017-09-18T17:25:22+10:00"
title = "FAQ: University Code Repository"
draft = false
toc = true
+++

# Functions & Features FAQ

## Is there a limit to the number of repositories I can use?

Users have the opportunity to create an unlimited number of repositories – both [public and private](#what-s-the-difference-between-a-public-and-private-repository) – making the code repository ideal for classroom use and personal projects.

## What can I store in the code repository?
The code repository uses the open source Git-distributed version control system with the GitHub management application, and it’s not just for storing code.
Documents, blogs, research papers, and other text-based work can use the platform for version control, sharing, and collaboration. The barrier to entry is low and may appeal to researchers, academic faculty, and students working on projects across the University and other institutions.
However, the code repository is not intended for storing large data sets, videos, audio files or other non-text based work, for which we provide [other solutions](/rdm/platforms-comparison/).  Storage is monitored to ensure performance of the platform.

## What is the difference between this repository (based on GitHub Enterprise) and GitHub.com?
The University’s code repository platform (GitHub Enterprise) includes virtually the same set of features as GitHub.com but is self-contained and managed by the University. All repository data is stored on servers that the University controls, and access is integrated with the University's authentication system (UniKey).
GitHub Enterprise is specifically designed to not compete with GitHub.com as far as public offering. "Public" inside of the University’s code repository is public to the university, not the world.
If a given project is truly open source, then it may be more appropriate to host it at GitHub.com with a personal account. Refer [here](../makingyourcodepublic/) for details on how to make a repository open to the world.
Internal groups, called "Organisations", allow for finer-granularity in specifying which users have access to group-owned repositories.

## How do I login and get started?
Simply log in with your UniKey at https://github.sydney.edu.au

The platform can be accessed from anywhere in the world.

A simple bootcamp for getting started can be found [here](https://guides.github.com/activities/hello-world/).

## I get an error telling me I "cannot authenticate as an Organization" when I try to log in - what do I do?

There may be a UniKey conflict with an existing organisation.  Contact the ICT Service Desk via the University Service Desk on +61 2 9351 2000 (select option 2 for ICT) and advise them that you cannot log into GitHub and it tells you that your Unikey is an organization account.

[Back to top](.)

# Access FAQ

## Eligibility/how to request access?
The University has established GitHub Enterprise as the institution’s code repository.  Faculty, staff, students and invited external collaborators are eligible for access to the code repository. Access is granted using UniKey credentials.

## How do I invite an external collaborator?
External collaborators will need to have a UniKey to access the code repository.
If they do not have one already, this can be requested [here](https://sydney.service-now.com/selfservice/catalogue_view.do?uri=com.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D5b97e64984326c009b7f5eba7ca87e2c%26sysparm_no_search%3Dtrue&sysparm_document_key=sc_cat_item,5b97e64984326c009b7f5eba7ca87e2c).

Approvers for this type of request must meet the following criteria:

UniKey requests must be approved by a University of Sydney employee who is a supervisor or manager.  This qualification is determined by the approver’s position in HR’s organisational chart; only members of staff who have the title of manager or director, and/or have at least 1 report will be considered valid approvers.
Project Managers and Program Managers are not valid approvers, unless they have at least 1 report according to the Organisation Chart.  If you are unable to nominate a University of Sydney employee who is a supervisor or manager, please nominate your IT Relationship/Service Delivery Manager

After the request is approved, the external collaborator’s password will be posted to them.

Once the UniKey is set-up, you can invite them into a repository following the instructions [here](https://help.github.com/enterprise/2.11/user/articles/inviting-collaborators-to-a-personal-repository/).

[Back to top](.)

# Data Security & Intellectual Property FAQ

## What do I need to be aware of with GitHub and antivirus?
It is strongly recommended that you have antivirus installed on any device that you use GitHub with.

If you see code that appears to be suspicious or any general misuse within the University Code Repository platform, please report it to the ICT Service Desk - they can be contacted via the University Service Desk on +61 2 9351 2000 (select option 2 for ICT).

## Who owns the IP within the platform?

All information stored within the platform is governed by the various applicable University Policies including but not limited to the Intellectual Property Policy and/or any Grant Approval Conditions.
For further information, refer to the following useful links:

-	[Intellectual Property Policy 2016](http://sydney.edu.au/policies/showdoc.aspx?recnum=PDOC2016/418&RendNum=0)

-	[University of Sydney Research Code of Conduct](http://sydney.edu.au/policies/showdoc.aspx?recnum=PDOC2013/321&RendNum=0)

-	[Faculty of Engineering and Information Technologies – Research Data Management Provisions 2015](http://sydney.edu.au/policies/showdoc.aspx?recnum=PDOC2015/382&RendNum=0)

-	[Australian Code for the Responsible Conduct of Research](https://www.nhmrc.gov.au/about-us/publications/australian-code-responsible-conduct-research-2018)

## Is my data secure?
The Code Repository is protected by the University’s internal firewalls and additionally, SSH is enabled.  The platform operates in high availability mode which is designed to minimise any service disruption.  There are 2 GitHub Enterprise servers – Active and Passive with all changes made to the Active server replicated to the Passive server.  If required, traffic will be redirected between the Active and Passive servers.

A backup/archive function is maintained on a GitHub Enterprise Backup Utilities server.

## Can I store passwords in plain text within my code?
You can, however this has potential to expose the credentials to users who shouldn't have access to them.
It is recommended that passwords are not stored anywhere in plain text.

## Where is the data stored?
The code repository platform is accessible anywhere in the world, with the platform and associated data is stored on various University-controlled servers located within Sydney, Australia.

## What is Two-Factor authentication?
Two-factor authentication, or 2FA, is a way of logging into websites that requires more than just a password – it requires a user entering in additional information to sign in.
With the code repository, this additional information will be an authentication code.  Once 2FA is enabled, GitHub will generate an authentication code any time someone attempts to sign into your code repository.

## How do I enable Two-Factor authentication?

Before you enable two-factor authentication, it is recommended that you notify your organisation members and external collaborators and ask them to set up 2FA for their accounts.
Refer to the following for instructions on [securing your account with two-factor authentication](https://help.github.com/enterprise/2.11/user/articles/securing-your-account-with-two-factor-authentication-2fa/).

***Warnings***

-	When you require use of two-factor authentication for your organisation, members and external collaborators (including bot accounts) who do not use 2FA will be removed from the organisation and lose access to its repositories. They will also lose access to their forks of the organisation's private repositories. You can reinstate their access privileges and settings if they enable two-factor authentication for their personal account within three months of their removal from your organisation.
-	If an organisation owner, member, or external collaborator disables 2FA for their personal account after you've enabled required two-factor authentication, they will automatically be removed from the organisation.
-	If you're the sole owner of an organisation that requires two-factor authentication, you won't be able to disable 2FA for your personal account without disabling required two-factor authentication for the organisation.

## How do I check if users in my organisation have 2FA enabled?

Refer to the following for instructions on [viewing whether users in your organisation have 2FA enabled](https://help.github.com/enterprise/2.11/user/articles/viewing-whether-users-in-your-organization-have-2fa-enabled/).

## How do I set up 2FA?

 Please see the following for instructions:

-	[Providing your 2FA authentication code](https://help.github.com/enterprise/2.11/user/articles/providing-your-2fa-authentication-code/)

-	[When you’ll be asked for a personal access token as a password](https://help.github.com/enterprise/2.11/user/articles/providing-your-2fa-authentication-code/#when-youll-be-asked-for-a-personal-access-token-as-a-password)

-	[Creating a personal access token for the command line](https://help.github.com/enterprise/2.11/user/articles/creating-a-personal-access-token-for-the-command-line/)

Note: If 2FA is turned on, you need to generate and use a Personal Access Token, as the method for git command line operations using HTTPS.

Please ensure you keep a copy of your Personal Access Tokens in a safe place as you will need to generate a key for each device, or share the key between those devices.

This can be set up post 2FA, but you won’t be able to command line clone over https until it is done.

## Can I connect to the code repository with SSH?
Yes, see [connecting to GitHub with ssh](https://help.github.com/enterprise/2.11/user/articles/connecting-to-github-with-ssh/) for more information.

Users will need to follow the guidelines on GitHub Help for SSH keys:

-	[Adding a new SSH key to your GitHub account](https://help.github.com/enterprise/2.11/user/articles/adding-a-new-ssh-key-to-your-github-account/)

-	[Checking for existing SSH keys](https://help.github.com/enterprise/2.11/user/articles/checking-for-existing-ssh-keys/)

-	[Generating a new SSH key and adding it to the ssh agent](https://help.github.com/enterprise/2.11/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

Once these have been set up, connection with SSH will work.

[Back to top](.)

# Collaboration and Publishing FAQ

## What’s the difference between a “public” and “private” repository?

Repositories can be set to either “public” or “private” - refer to [creating a new repository](https://help.github.com/enterprise/2.11/user/articles/creating-a-new-repository/) for instructions.

* **Private** on **GitHub Enterprise**
    * free
    * only accessible to you (or the host "organisation") and specified
      collaborators with University of Sydney accounts
    * easy to change to public on GitHub Enterprise
    * code can be [easily transferred](../makingyourcodepublic/) to a repository on GitHub.com (e.g. if your account at University of Sydney is being closed), but project management features (particularly Pull Requests, Projects, lists of authorised collaborators) are harder to migrate
    * stored locally, on university-controlled servers under NSW legal jurisdiction
* **Public** on **GitHub Enterprise**
    * free
    * accessible to *all* University of Sydney accounts (including students, academic and proffessional staff and associates); not accessible to anyone else
    * code can be [easily transferred](../makingyourcodepublic/) to a repository on GitHub.com, but project management features (particularly Pull Requests, Projects, lists of authorised collaborators) are harder to migrate
    * stored locally, on university-controlled servers under NSW legal jurisdiction
* **Private** on **GitHub.com**
    * paid monthly subscription for unlimited accounts
    * only accessible to you (or the host "organisation") and speicified
      collaborators with GitHub.com accounts
    * easy to change to public on GitHub.com
    * may be suitable where the project is likely to become free open source and you want to retain GitHub's project management features.
* **Public** on **GitHub.com**
    * free
    * accessible to anyone
    * suitable for free open source projects

In all cases, only authorised users can change content.
In all cases, anyone who can access the repository can see any file that was ever in the repository (unless you fix this carefully by ["rewriting the commit history"](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History); ICT support may be able to assist in doing so).

## How do I add a license to my repository?

The license will need to be added manually by creating a LICENSE.md file in the root of your repository and then populate it with the license information.

## How do I make a repository public (to the world)?

Refer to [making your code public](../makingyourcodepublic/).

## How do I join The-University-Of-Sydney organization on GitHub.com?
Raise a ticket with the ICT Service Desk via the University Service Desk on +61 2 9351 2000 (select option 2 for ICT) or [ict.support@sydney.edu.au](mailto:ict.support@sydney.edu.au) to request to become a member of The-University-Of-Sydney organisation.

## I’ve made my code public, how do I add it into The-University-Of-Sydney organization on GitHub.com?
You need to first become a member of The-University-Of-Sydney organisation before you can add your code to this organisation.

## How do I invite people into a repository?
You can invite users to become collaborators on your private repository – refer to this [guide](https://help.github.com/enterprise/2.11/user/articles/inviting-collaborators-to-a-personal-repository/).
You can invite users to your repository using their name or UniKey – users need to have logged into GitHub already.

Note: for external collaborators, see [How do I invite an external collaborator?](#how-do-i-invite-an-external-collaborator)

## What is a Digital Object Identifier (DOI)?
A Digital Object Identifier (DOI) is a specific type of Handle and can be assigned to any object that is a form of intellectual property. DOI should be interpreted as 'digital identifier of an object' rather than 'identifier of a digital object'.
A DOI consists of a unique, case-insensitive, alphanumeric character sequence that is divided into two parts, a prefix and a suffix, separated by a forward slash. The prefix is assigned by a DOI Registration Agency and always starts with '10.' This distinguishes it as a DOI as opposed to other types of Handle. The suffix is assigned by the publication agent, the agency supplying the information about the object, and must be unique within a prefix.
A DOI is typical used as a citation mechanism for published material, including code or algorithm.

## How to mint a DOI/process for GitHub?
GitHub.com has a feature to enable you to mint a DOI, refer to this [guide](https://guides.github.com/activities/citable-code/).
If you need information on how to make your code public, refer to these [instructions](./makingyourcodepublic/).

[Back to top](.)

# Group Management FAQ

## What is the difference between organisations and teams?
Refer to [organisations and teams](https://help.github.com/enterprise/2.11/admin/guides/user-management/organizations-and-teams/).

## How do I set up an organisation in the code repository?
Organisations are typically linked to the University’s Active Directory groups. An example of an organisation could be a particular faculty, school or subject with its own repository/s limited to members of that organisation.

Administrator rights can be assigned to one or more individuals within the organisation after initial set-up, allowing these to be autonomous once established.

All users have access to create organisations and you need to be part of an organisation to create a team.  If you encounter issues with creating an organisation, contact the ICT Service Desk - they can be contacted via the University Service Desk on +61 2 9351 2000 (select option 2 for ICT).

If you have administrator rights to an organisation repository, permissions can be managed. Refer to this [guide](https://help.github.com/enterprise/2.11/user/articles/managing-an-individual-s-access-to-an-organization-repository/).

## How do I manage team membership?
Teams are created within the platform either by inviting individual members or by connecting to a group in the Active Directory.  You may be automatically part of a team if you belong to an Active Directory group linked to a repository.
Note: for team repositories that are connected to an Active Directory (AD) group, membership will be determined by the AD. For example, if a particular subject has a repository, the membership of that team will depend on the enrolment for the semester, and membership will be automatically revoked once the individual is no longer enrolled in that subject.

[Back to top](.)

# Migration & Integration FAQ

## I already have a personal GitHub or BitBucket account – can I migrate my repositories?
Yes. Further information about migrations can be found [here](https://help.github.com/enterprise/2.11/admin/guides/migrations/about-migrations/).

With instructions available [here](https://help.github.com/enterprise/2.11/admin/guides/migrations/importing-migration-data-to-github-enterprise/).

## GitHub Enterprise tells me my large file exceeds the file size limit. What can I do?

You might see an error like the following when trying to import a repository with a large file in it:

    remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
    remote: error: File xxxxx.xxx is 111.11 MB; this exceeds GitHub Enterprise's file size limit of 100.00 MB

Git is designed to store mostly text files like code and documentation.  If you want to store data, Git might not be the right solution, but we support [other platforms](/rdm/platforms-comparison/) for that purpose.

We do, however, support [Git Large File Storage](https://help.github.com/articles/configuring-git-large-file-storage/) (Git LFS), which allows versioned tracking of files larger than the basic limit on GitHub Enterprise.

If the large file is part of an existing repository, then you may need to [rewrite your repository's commit history](https://help.github.com/articles/moving-a-file-in-your-repository-to-git-large-file-storage/) to remove the file and place it in Git LFS or an alternative storage option.
To get assistance with this, contact the ICT Service Desk.

## Can I use Artemis with GitHub Enterprise?
Yes.  Artemis, by default, has an early version of git 1.7.1, however running `module load git` installs the latest version 2.8X.

The latest version will work but you need to start your command with:

    module load git

## Can I import from my subversion of mercurial repositories?
Yes. Instructions can be found [here](https://help.github.com/enterprise/2.11/admin/guides/migrations/importing-data-from-third-party-version-control-systems/).

## Can I integrate JIRA with GitHub Enterprise for Project Management?
Yes. Instructions can be found [here](https://help.github.com/enterprise/2.11/admin/guides/installation/project-management-using-jira/).

[Back to top](.)

# Help & Support

Contact the ICT Service Desk via the University Service Desk on +61 2 9351 2000 (select option 2 for ICT) for all UniKey or access related enquiries.

To find out about Git, refer to [Git - What you need to know](https://rc.sydney.edu.au/git-user-guide/index.html).

For help and user guides for using the platform	GitHub Enterprise has extensive online user guides and wikis available [here](https://help.github.com/enterprise/2.11/user/articles/managing-an-individual-s-access-to-an-organization-repository/).

If you can't find what you are looking for in the FAQs, you can raise a ticket with the ICT Service Desk via the University Service Desk on +61 2 9351 2000 (select option 2 for ICT) or [ict.support@sydney.edu.au](mailto:ict.support@sydney.edu.au).

[Back to top](.)
