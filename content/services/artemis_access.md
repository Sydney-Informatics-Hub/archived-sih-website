
redirectTo = "https://sydney.edu.au/sydney-informatics-hub"
+++
date = "2017-11-03T15:25:22+10:00"
title = "Access to Artemis"
draft = false
+++

## ACCESS TO ARTEMIS
Access to Artemis is available to all University of Sydney researchers who are participating in an approved research project and have a Research Data Management Plan (RDMP).

### How do I get a new account on Artemis?
---
To qualify for access to Artemis, you need to:

1. Have a valid University of Sydney UniKey
2. Be part of an approved research project with an approved RDMP. You can submit a new RDMP or update an existing RDMP by logging into the [RDMP tool](https://rdmp.sydney.edu.au/).

Once you've submitted your RDMP you will receive notifications indicating that account creation is in progress - one for HPC and a separate one for RDS. When your account is active you will receive a welcome email with information to help you get started.

Note: The account activation time for HPC is 4 business hours.

### I have an existing RDS account and need access to Artemis
---
If you already have an existing RDS account and an approved RDMP, you need to log into the [RDMP tool](https://rdmp.sydney.edu.au/) and edit your project on the HPC tab to request access to Artemis:

1. In the Manage area, select Edit
2. Select the HPC tab
3. Check Yes for HPC
4. Resubmit the form


### How do I connect to Artemis?
---
Artemis is accessible via SSH using your UniKey and password using the hostname __hpc.sydney.edu.au__

### On-campus

For Windows-based access you can use an SSH client like [Putty](https://sydneyuni.atlassian.net/wiki/spaces/RC/pages/185729027/Getting+Started+with+Artemis+HPC)

On Linux or MacOS you can use the SSH command in the built-in terminal app. To do this, start the Terminal app, then type the following command to log in:

__ssh UniKey@hpc.sydney.edu.au__

You can use the login nodes to gain access to the system, edit files, compile code, analyse data and create job requests for the batch system. They are not intended for computationally intensive processes. Submit these jobs to the batch queuing system. For details, see the [Artemis User Guide](https://rc.sydney.edu.au/artemis-user-guide/index.html).

### Off-campus

The recommended way of accessing Artemis from off-campus is by first connecting to the [University VPN](https://sydneyuni.atlassian.net/wiki/spaces/RC/pages/185729027/Getting+Started+with+Artemis+HPC), then connecting to Artemis via SSH. 

If you cannot use the VPN, you may instead connect via __jump.research.sydney.edu.au__ (an intermediate host). First connect using an SSH client to jump.research.sydney.edu.au:

__ssh unikey@jump.research.sydney.edu.au__

After logging in, connect to Artemis by typing the following into your session:

__ssh unikey@hpc.sydney.edu.au__

If you wish to connect from jump.research.sydney.edu.au to Artemis without typing a password, set up a password-less SSH using SSH key pairs. First, login to jump.research.sydney.edu.au and type:

__ssh-keygen__

and accept all defaults. Then type:

__ssh-copy-id unikey@hpc.sydney.edu.au__

If successful, you will be able to log into Artemis from jump.research.sydney.edu.au without a password by typing:

__ssh unikey@hpc.sydney.edu.au__

__Note:__ For security reasons, SSH key pairs cannot be used between your computer and jump.research.sydney.edu.au

### Data Storage
---
Artemis contains the following short-term storage spaces:

Home directories
Project space
Scratch space

Data will not be backed up so we cannot offer any ability to retrieve lost data. For long term storage please store all data in the University's [Research Data Store (RDS)](https://rc.sydney.edu.au/research-data-store/index.html).

### Home directories

Each researcher will be allocated their own home directory within Artemis. This can be used to store program code, batch scripts and other files. Please note that the home directory has limited space (10 GB per researcher) and is intended for storing code and configuration information. 

The home directories are backed up periodically, however the service cannot guarantee the retrieval of a lost file. Should a file be lost or corrupted, ICT will only attempt to retrieve it in cases of system failure.

### Project space

The default allocation is 1 TB of project storage, shared between all members of the project. Please note that no additional space will be provided. Please refer to your RDMP and store your data, as per the policy for the Research Data Store.

Project storage is a single instance. You are responsible for making sure that critical data is copied back into your Research Data Store allocation. This space is provided on a per-project basis and is available for the duration of the project. Data should be moved between your allocated project space and your RDS project space.

### Scratch space

Artemis scratch space is a pool of storage on the system which can be used during the job. The space is available to everyone on Artemis and there are no restrictions on the amount of data that can be stored.

This directory is intended for data that needs to be saved during the job, but can be deleted once the job completes. As this directory is shared by all users, please do not leave your data in this area for longer than necessary.

Transfer important files to your project space if you need them after your job finishes. Data in the global scratch area is not backed up and data is periodically removed.


### Moving data

As Artemis is purely for computing code, no permanent storage is available on it. You will need to have access to the Research Data Store (RDS) to move data from and to your allocated storage facility.

Currently it is only possible to move data to and from the allocated project area within Artemis.

Data on your local workstation is moved using a secure ftp tool, such as sftp or filezilla. These are also used to retrieve results to your local workstation.

Data in RCOS can be transferred to and from Artemis using the usual unix commands cp, mv. Data in Classic RDS can be transferred to and from Artemis using smbclient, an ftp style command line tool that can talk directly to Classic RDS.

See the [user guide for more information](https://rc.sydney.edu.au/artemis-user-guide/index.html).
