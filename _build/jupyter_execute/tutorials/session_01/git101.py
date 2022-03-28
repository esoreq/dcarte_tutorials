#!/usr/bin/env python
# coding: utf-8

# # Version control, git and github command line tools
# 
# ## Basic terminolgy
# 
# ### what is version control 
# Version control is a type of software that keeps track of every modification to the code in a special kind of database.
# 
# #### Why do we need to use version control when we code? 
# 
# If a mistake is made, developers can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.
# 
# ### What is git 
# 
# Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
# 
# ### What is GitHub 
# 
# GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
# 
# ### What is a repository
# GIT repositories contain a collection of files from various versions of a Project. These files are imported from the repository into the user's local server for additional updates and adjustments to the file's content. A VCS, or Version Control System, is used to produce these versions and save them in a location known as a repository. Cloning refers to the process of copying material from an existing Git Repository using different Git Tools. When the cloning procedure is completed, the user receives the whole repository on his local system. Once the clone is complete, Git expects any future work on the repository will be done as a user.
# 
# ### What is if good for
# Typically, a repository is used to organise a single project. Repositories may hold folders and files, photos, movies, spreadsheets, and data sets – anything your project requires. Frequently, repositories include a README file, which contains information about your project. README files are written in Markdown, a plain text language.
# 
# ### Why command line tools
# Github has some fancy UI - but I have never used it as the command line interface does what I need it to do   
# 

# 
# ## Context and practicalities
# 
# ### Setup
# #### Install git and create a GitHub account 
# We will only be using git on the command line for this lesson. 
# While there are numerous excellent git GUIs (graphical user interfaces), I believe it is only helpful for those that git becomes a daily routine. 
# So the first two things you should do are to sign up for a free GitHub account and install the github command line tools .
# 
# ##### Varify that git is installed on your computer
# 
# ```{code-block} bash
# git --version
# ```
# 
# #### Install the command line tools
# 
# Go to [cli.github.com](cli.github.com) and install the command line tools for any OS
# 
# #### If you don't have a GitHub user account - 
# Create one [here](https://github.com/join)
# 

# 
# ### Create your first repo
# 
# #### Step 1 - create a folder to hold your repo
# Open a terminal and create in your sandbox folder a new folder called `my_first_git`
# 
# ```{dropdown} Solution
# ```{code-block} bash
# mkdir -p ~/sandbox/my_first_git && cd ~/sandbox/my_first_git
# ```
# 
# #### Step 2 - create some basic content 
# In that folder create a file named `README.md` and in it add the following text:
# "# This is [your name] first repo"
# "I will use this repo to track my experiments using dcarte"
# 
# ```{dropdown} Solution
# ```{code-block} bash
# echo "# This is [your name] first repo
# I will use this repo to track my experiments using dcarte" > README.md
# # confirm that the file exists using cat 
# cat README.md
# ```
# 
# #### Step 3 - initialize the repository using git
# We need to use git to add some properties to our new folder we do that using the `git init` command when we are in the root of the folder.
# 
# ```{dropdown} Solution
# ```{code-block} bash
# cd ~/sandbox/my_first_git && git init
# ```
# 
# #### Step 3a - look under the hood 
# If we just use `ls` to list the files in our repo we will find that it contains only the README.md file we created.
# The reason for that is that the init process places all of it's files in what is called a hidden folder that has a dot as a prefix 
# In the first session covering bash we discussed how to use `ls` with arguments to show hidden files so let's do that now to peek into the contents of the `.git` folder we just created 
# 
# ```{dropdown} Solution
# ```{code-block} bash
# ls -a .git
# ```
# 
# As you can see, the command established local tools to be used to curate any modifications made to the folder's contents.
# 

# 
# #### Step 4 - Add README to the repo
# When you add or modify files in a folder containing a git repo, git detects that the file exists within the repo. However, unless you expressly tell it to, git will not track the file. Git only saves/manages changes to files it tracks, therefore we'll need to provide a command to ensure that we do, in fact, want git to monitor our new file.
# It is possible to use the `git status` command after you have made the new file. This command tells you which files git knows to be there.
# 
# ```{dropdown} Solution
# ```{code-block} bash
# git status
# ```
# 
# As you can see in our repo, git knows that README is there and tells us that it isn't being tracked.
# It also suggests using `git add` to add it to add README to git tracking system.  
# When you add a file to the repository staging environment, you are literally putting it on an index to be processed.
# 
# ```{dropdown} Solution
# ```{code-block} bash
# git add README.md && git status
# ```
# 
# When you add 'README.md' to the staging environment, it becomes green and is queued for inclusion in the curated files.
# 

# #### Step 5 - commit changes to the repo 
# 
# An integral part of the curation process is documenting (i.e. giving context) the changes you just made. 
# You do this by adding a message after the `git commit` command using the argument `-m`. 
# The main reason that two process are seperated is to allow multiple changes to be aggragated under one context.
# If you leave a clear explanation of your changes, it can be extremely helpful for future programmers (perhaps even future you!) who are trying to figure out why some change was made.
# 
# ```{dropdown} Solution
# ```{code-block} bash
# git commit -m "my first commit" && git status
# ```
# 
# If everything went as expected, you should receive something like this:
# 
# ```{code-block} bash
# On branch main
# nothing to commit, working tree clean
# ```

# #### Step 6 - Branches creation
# 
# In our readme example, we may construct a more complex readme file with more material, but some of it may not be finished and can't be shared just yet. 
# Git branches represent portable references to commits in a repository. The files in your new branch have their histories because Git keeps track of the commit from which your new branch 'branched'.
# 
# To create a workable branch we simply use the command `git checkout -b my_new_branch_name`
# 
# If everything went as expected, you should receive something like this:
# 
# ```{code-block} bash
# Switched to a new branch 'my_new_branch_name'
# ```
# 
# Now let's add some more content to the README.md file 
# 
# ```{code-block} bash
# echo "Adding more info about me to the README file" >> README.md
# git add README.md && git commit -m "my first branch commit" && git status
# ```
# 
# #####  To identify the active branch use:
# 
# ```{code-block} bash
# git branch
# ```
# 
# 
# #####  To switch between branches use `git checkout <branch name>`:
# 
# ```{code-block} bash
# git checkout main
# ```
# 
# #####  To merge two local branches use `git merge <non active branch name>`:
# 
# Git will compare the two files and combine them if no clashes exist 
# 
# ```{code-block} bash
# git merge my_new_branch_name
# ```

# ## Moving to the cloud
# 
# You don't need to utilise GitHub if you just want to keep track of your own code. You can use GitHub if you wish to work with a team or keep your project files in an external location that you can access from many machines.
# 
# ### Step 1 - We'll use the command line tools we installed earlier to upload our local repository to our github account.  
# 
# Github makes it very simple to do you just use the command `gh repo create` and follow the instructions 
# 
# We will 
# 1. Push an existing local repository to GitHub
# 2. Path to local repository = this should be left as `.` if you are still in the folder 
# 3. Repository name my_first_git
# 4. Description = add anything you want here
# 5. Visibility = If you choose private only you can access 
# 6. Add a remote? Yes - this just links the local repo with the cloud hosted one 
# 7. What should the new remote be called? origin
# 
# ### Step 2 - Push the contents of you new repo online 
# 
# The new repo exists, but it is empty. To populate it with information, we must push our committed material to the cloud using the 'git push' command.
# 
# ```{code-block} bash
# git push
# ```
# 
# ### Step 3 - Adding multiple files 
# What about directories containing many files - do we need to add each file individually?
# As you would expect, the `git add` command has arguments; we can view these by viewing the help for the function. 
# In general, calling a function with the `--help` argument will open the functions documentation that will show the file's contents.
# To exit the help just press `q` that stands for quit.
# Going over the documentation try to find the solution to include many files at once. 
# 
# ```{code-block} bash
# git add --help
# ```
# 
# ```{dropdown} Solution
# The solution is to pass the `--all` argument; however, in our current situation, this won't work since we only have one file in our new repository.
# ```{code-block} bash
# git add --all  && git status
# ```
# 
# To simulate a complex structure let's populate our repo with some folders and some files in them. 
# These pieces of code are dense on purpose - for those interested, consider them an extension to the previous part demonstrating some of the more complex aspects of bash; for those who aren't, execute them in your terminal to populate your repo with some synthetic files.
# 
# #### create a complex folder structure in one line of code 
# ```{code-block} bash
# mkdir -p $PWD/{Notebooks,Code,Tmp,Data/{raw,processed,share},Report/{Tables,Figures,Text},Presentation,Background/{pdf,pptx}}
# ```
# 
# #### populate the folder with some fake data
# ```{code-block} bash
# for i in {1..5}; do echo "id, name, value\n $i, $i, ${i}" > Data/raw/data_${i}.csv; done
# for i in {g..h}; do echo "# notebook $i" > Notebooks/notebook_${i}.ipynb; done
# for i in {a..c}; do echo "# presentation $i" > Presentation/presentation_${i}.pptx; done
# ```
# 
# #### Test add --all again
# Now that we have enough meat in our repository, we can test the add all functionality.
# 
# ```{dropdown} Solution
# The solution is to pass the `--all` argument; Now, that we have multiple files in our new repository we should see all of them waiting to be commited.
# ```{code-block} bash
# git add --all 
# ```
# 
# #### Roll back all files to unstaged status 
# For the sake of this example we want to reset the staging status of all of our files. The `git reset` command does that exactly. 
# If you wish to unstage a specific file use `git restore --staged <file>` as suggested by the function
# 
# ```{code-block} bash
# git reset && git status
# ```
# 
# #### Step 4 - add .gitignore to the repo root 
# Before moving forward, it is handy to exclude specific folders and types of files from the cloud. In projects involving sensitive data, like UKDRI-CRT, excluding sensitive files is particularly important. Having some data locally is beneficial in terms of processing speed and ease of use, but sharing this data (especially in healthcare) to the public domain is a severe violation of IG protocols. Creating and populating the hidden *.gitignore* file is a simple way to exclude any data files from being uploaded into the cloud. 
# 
# ```{admonition} Challenge
# 1. Create a new file in the root of the repository called `.gitignore`
# 2. The file should have the following lines included 
# Data/
# Tmp/
# ```
# 
# ```{dropdown} Solution
# ```{code-block} bash
# echo "Data/
# Tmp/" > .gitignore
# ```
# 
# #### Step 5 - Add all files with the new .gitignore exclusion criteria
# Now that we protected ourselves, we can use git add all without any worry.
# 
# ```{code-block} bash
# git add --all  && git status && git commit -m "adding multiple files" && git push
# ```
# As you can see, only files in the authorised directories are uploaded to the staging area, and when we go online to our new Github repo, we can see that the files have been successfully added to the cloud.
# 
# #### Step 6 - What about pushing branches to the cloud? 
# Working using branches can simplify the process of collaborating on projects with numerous persons working on similar overlapping aims.
# For example, research may examine the same patient group to create distinct markers from the same data. 
# In this case, we would have a single repository for the project because all of the base scripts are used to analyse the data, but higher branches would take alternative approaches to the processed data. The project leaders may eventually wish to combine these various branches into a standard updated repo (which is beyond the scope of this tutorial, but you can get the gist of what needs to be done).
# 
# ```{code-block} bash
# git push origin my_new_branch_name
# ```
# 
# #### Step 7 - Cloning a repo to your local storage 
# To work on your source code, you need a location to store it locally, but how can you get the contents of your remote repository into your local storage? 
# Here comes Cloning. Cloning generates a repository clone with a link back to the original. 
# Each repository can only pull, retrieve, and push back. 
# Pushing may not function because repositories are protected from being edited by anybody except the repository owners and contributors. 
# In a way cloning is like downloading a file from a read-only folder to your computer. 
# But it is the simplest way to contribute to a project. 
# Let us clone the dcarte repo to our local drive. 
# 
# ```{code-block} bash
# cd ~/sandbox && git clone https://github.com/esoreq/dcarte
# ```
# 
# This process downloads the latest version of dcarte to your local drive. 
# The benefit of having a local snapshot of the code is that you can change parts of it and not wait for changes to roll out in the proper pip installation 
# Another benefit lies in your ability to contribute to the project if you find an overlooked problem.
# 
