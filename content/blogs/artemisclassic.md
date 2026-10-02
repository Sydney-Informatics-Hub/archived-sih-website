+++
date = "2018-09-25T00:00:00+10:00"
title = "Getting your data from RDS Classic to Artemis"
draft = false
type = "sidebar"
blog = true
stream = "blogs"

thumbnail = "/images/blog/rdsartemis.png"
summary = "How to get your research data from RDS Classic to Artemis as efficiently as possible."

authorname = "Hayim Dar"
authoravatar = "/people/HayimDar.jpg"
authorbio = "Works in in the Research Computing team, focussing on Artemis HPC, modelling and simulation."
+++

I recently had a question from a researcher trying to get a whole bunch of data off of RDS Classic, and onto Artemis HPC. Since we don't really cover this in the [Introduction to Data Transfer Queue and RDS](/training/#rdshpc) course, I thought it would be the perfect topic for a new Blog post!

## Like oil and water..

Anyone who has ever tried to use _Artemis HPC_ with data stored on _RDS Classic_ has probably discovered that Artemis and RDS Classic just don't mix. The reason is simple: Artemis is a Linux computing cluster, RDS Classic is a Windows-based file store, and Linux and Windows aren't really friends.

This is not a problem that most researchers should be having: When you sign up for a **Research Data Management Plan** (_[dashR](https://dashr.sydney.edu.au/)_) with Artemis HPC access, you will be given data storage on _RCOS_, the **Research Computing Optimised Storage**. RCOS is the University's Linux-based data store, which connects seamlessly to Artemis.

The issue arises when research groups have **existing data** they might never have intended to use on HPC, and this data is on _RDS Classic_, but now they would like to process this data on Artemis.[^1]

## The solution: **smbclient**

**smbclient** is a Linux command-line tool for connecting to [samba](https://www.samba.org/) (ie Windows) file shares. It works much like any other secure file transfer protocol (SFTP) software. On the command line, this generally means that it will connect you to the host file-server and leave you at a command prompt. For example:

```
[jdar4135@login3 ~]$ smbclient //research-data.shared.sydney.edu.au/RDS-01/ -W SHARED
Enter jdar4135's password:
Domain=[SHARED] OS=[Unix] Server=[FluidFS]
smb: \>
```

From that _**smb: \>**_ prompt, I can then execute the regular Unix-style commands such as _**ls, cd, pwd**_, etc. Most command-line SFTP programs also let you execute those commands on your _local_ computer as well, by appending an '!' or the letter 'l' before them: so _**!ls, !cd, !pwd**_, etc. NB also that we needed to specify a user domain, or workgroup when connecting, using flag '-W' --- your domain may be different on different file shares.

More to the point, you can then transfer files back and forth with SFTP's standard _**put**_ and _**get**_ commands, which will grab or drop files to or from the local or host, at wherever you happen to be in each filesystem.


### Transferring big data

So far so good, but not so helpful if you need to transfer hundreds or thousands of files. If you simply need to grab everything from a folder, you're in luck:

```
smb: \> prompt off; recurse on; mget *
```

In these simple commands, we have asked smbclient not to prompt us before each file transfer; told it to recurse through subdirectories to operate on all files in the directory tree; and then used _**mget**_ to grab multiple files at once, selecting everything (__'\*'__). Or swap in _**mput**_ to transfer back. But don't forget to change into the right directories at each end beforehand!

Simple. Now go get that Classic data on and off Artemis!

<img src="/images/blog/art2rds.png" style="height:250px" />

<br>
## Transferring only some of your big data: A small case study

Unfortunately, you won't always be working with your whole dataset at the same time, or may not wish to transfer it all. The good news is that **smbclient** can accept a string of commands using the ``` -c ``` flag, each separated by a semicolon ';', rather like a script. This was the problem that the researcher had come to me with, and here is how we solved it.

#### 1. Getting your transfer list

The researcher had a list of subjects whose data they wanted to transfer, in a file we called _**subjects.confg**_. This list was a simple comma-separated list, looking something like

```
FOO_026_BAR,BLA_145_BLA,XXX_072_YYY,ABC_114_DEF,SUM_003_TNG,...
```
with various text around a number. We only needed the numbers, however, as that's how the data folders were named. So before we could write our smbclient command, we needed to clean up the inputs.

First step, though, was to get this list into a nice Bash variable. What is Bash? Bash is just a command line interpreter, the thing that actually executes the commands you type at a command line prompt. Bash scripting is a big part of using Artemis, so it's worth learning a few tricks.

```
config=$(<subjects.config)
```

This first command loads the text of the subjects file into a variable, called **config**. In Bash, all variables are referenced using the dollar symbol **```'$'```**. Next, we split that text around the commas, and created a Bash array variable from the result. Using Bash's in-built '[parameter](https://www.cyberciti.biz/tips/bash-shell-parameter-substitution-2.html) [expansion](https://www.tldp.org/LDP/abs/html/parameter-substitution.html)', this is all done in one command:[^2]

```
list=(${config//,/ })
```

If, on the other hand, your data list was one entry per line, like a column vector, you could more simply use the ```cut -f1``` command to get the first (or only) column, as

```
list=($(cut -f1 subjects.config))
```

#### 2. Cleaning your list

Second, we had to isolate just the numbers. Another simple find-all and replace (```'//foo/bar'```) does most of the work, replacing all non-numbers with nothing:
```
list=(${list//[^0-9]/})
```

However we were still left with leading zeros on some numbers, like '072', which did not match the folder names of the researcher's data. We needed to strip these zeros. The easiest way was to use a 'remove front pattern' expansion (```'##'```), which removes matched patterns from the front of strings. But as the number of leading zeros was different for different numbers, we made use of an extended capability set in Bash by enabling the '[extended globbing](https://www.linuxjournal.com/content/bash-extended-globbing)' option, allowing us to match one or more of a given pattern (```'+()'```), in this case '0':
```
# use extended globbing
shopt -s extglob

list=(${list##+(0)})   
```
Our **list** variable was now just an array of numbers with no leading zeros, as required!


#### 3. Writing the smbclient script

Finally, we were ready to compose the smbclient script -- or in reality, commands string. For this we used a simple for-loop:

```
smbstr=
for id in ${list[@]}; do
	smbstr+=$(echo "cd $id; get ${id}_data_file; cd ..; ")
done
smbstr="cd path/to/data; $smbstr"
```

In this loop, we iteratively added to a string called **smbstr**: Each loop, we get the next number from the **list** array as **$id**, and append the string **"cd $id; get ${id}_data_file; cd ..; "**, which enters the subject's numbered directory, gets the file we wanted, and then exits back out.[^3] Note how every command is separated by a semicolon ';'. Finally, we prepend a call to change into the directory where these folders are located, as we wont be able to send that command separately.

Now that this is all done, we can simply give this big string of commands to **smbclient**:

```
smbclient //address.of.file.share/ -W WORKGROUP -c "$smbstr"
```

Success! If you need help using **smbclient**, or Bash variable manipulation, be sure to drop us an email! [sih.training@sydney.edu.au](mailto:sih.training@sydney.edu.au).

<br>

[^1]: Why are there two different University Research Data Store (RDS) systems? Partly due to historical reasons -- the Windows one came first -- but mainly because they really are each more convenient for different users. Many researchers use tools and software entirely in a Windows-based ecosystem, so a Linux file share would just cause headaches for them. But when it comes to high performance computing on Artemis, Linux-based RCOS is what you want.

[^2]: This command first does a find-all and replace of all ',' in the string with a space ' ' via ```${config//,/ }```, and then encloses the results in parentheses ```( )``` to create an _array_ variable. Bash creates arrays from space-separated lists, eg ```array=(one two three)```, which is why we needed to replace the commas.

[^3]: We need to explicitly enter and exit each folder rather than prepend the folder to the filename (like ```"get 23/23_data_file"```), as otherwise the files we download would all have the folder name prepended to them, (ie ```"23/23_data_file"```). This isn't the end of the world, but wasn't ideal! Yes, smbclient is quirky like this.
