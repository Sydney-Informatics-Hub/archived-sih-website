+++
date = "2017-05-06T17:25:22+10:00"
title = "Making your code public"
draft = false
+++

This procedure is provided to show how to synchronise the contents of a GitHub repository stored on the University’s internal GitHub Enterprise to a repository stored on the public GitHub.com. This process is intended to support external collaboration and publishing efforts.
A similar process can be used to transfer a repository from GitHub.com, Bitbucket.com, Gitlab.com, etc repository to GitHub Enterprise.

**IMPORTANT: Your repository must have a license file.  Refer to [adding a license to a repository](https://help.github.com/enterprise/2.11/user/articles/adding-a-license-to-a-repository/)**

Git is primarily a client based tool. Most of the significant operations undertaken by a Git user occur on the client and not on the repository server. The purpose of the repository server is to provide a central point for collaboration and distribution.

The process of synchronising repositories occurs on your own workstation. This guide will cover performing these tasks using the Git command line tool.

### Tips and Caveats

#### The history will be public too

Please note that the entire commit history of the repository will be visible in the destination Github.com repository, including files that have been removed during the life of the repository. If this is not appropriate for your project the commit history may need to be cleaned up prior, ICT support staff may be able to assist. Git provides several options for changing the sequence of commits: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History.

#### What is *not* transferred?

Only the code in your repository is transferred in the process described below.  Project management features of GitHub are not transferred.  A tool like [GitMover](https://github.com/ahadik/git_mover) may assist to transfer GitHub Issues, Labels and Milestones to your new GitHub.com or GitHub Enterprise location.  Other features such as Pull Requests and the list of collaborators allowed to access/modify your repository need to be transferred manually between GitHub.com and GitHub Enterprise.

#### Keeping the public copy in sync

Note that if you only want to transfer code to maintain a public *copy* of your private GitHub Enterprise repository, you can perform the procedure describe below repeatedly to re-synchronise the GitHub.com fork with the Enterprise instance.

### Prerequisites:

-	You must have an account on and access to the University Github Enterprise server: https://github.sydney.edu.au.

-	You must have read access to a repository stored on https://github.sydney.edu.au/ – this will be the source repository that will be synchronised to Github.com.

-	You must have an account on and access to the public github.com https://github.com.

-	You must have write access to a repository stored on https://github.com – this will be the destination repository.

-	You must have the Git client installed on your local workstation.

-	Assuming the repository has a single branch labelled master (the default initial configuration for any repository).

## Procedure:

1.	Access the source repository on the University server and populate it with relevant files. Follow the guides and instructions on the GitHub Enterprise server to achieve this.

2.	Clone the source repository to your local workstation:

	1.	Create a new folder/directory, and open a terminal/command prompt in that location.

	2.	Run the git command to clone the **master branch of the repository**:

		```
		git clone https://github.sydney.edu.au/<username>/<repositoryname>.git
		```

		If you want to clone *all* branches (and tags), use:

		```
		git clone --mirror https://github.sydney.edu.au/<username>/<repositoryname>.git
		```

	3.	Substitute `<username>` and `<repositoryname>` with the values specific to your **source** repository.

	4.	You would be required to enter your Unikey credentials (and/or personal access token if you have enabled two factor authentication) to the git command to complete this operation.

3.	Tell the local copy of the repository where to find the destination public repository.  We will tag this destination with label **public**.

	1.	In the terminal/command prompt in the local repository location run the git command:

		```
		git remote add public https://github.com/<username>/<repositoryname>.git
		```

	2.	Substitute `<username>` and `<repositoryname>` with the values specific to your **destination** repository.

4.	Push the contents of the local repository to the destination repository.

	1.	In the terminal/command prompt in the local repository location run the git command:

		```
		git push public master
		```

		If you want to push *all* branches (and tags), use:

		```
		git push --mirror public
		```

	2.	You may be required to enter your public Github.com credentials to the git command to complete this operation.

5.	Confirm that the contents of both the University and public repositories are identical. This can be done by visual inspecting the repository contents via the web interfaces, or alternatively cloning both repositories into different folders on your local workstation and using other tools.

6.	If you have created the local copy of the repository purely for synchronising to Github.com, it would be safe to remove this copy from your local workstation.

7.	When you push future work to a remote repository (GitHub Enterprise or GitHub.com) make sure you are pushing to the right remote, e.g. the one named `public` here vs. the one which Git automatically names `origin`.
