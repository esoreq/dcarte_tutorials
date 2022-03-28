#!/usr/bin/env python
# coding: utf-8

# # Introduction to Linux Based Command Line Interactions
# 
# ## Why would I use a Terminal 
# In the old days, independent devices, or so-called "hard copy terminals" (printer or screen plus keyboard), were used. Modern computers no longer have those, replaced by terminal emulators - programs that provide users with a graphical window for interacting with the shell. As scientists, we rely on powerful computer clusters to reveal answers to many questions and to perform many tasks automatically. There are many ways to interact with these computers. However, the fastest and most reliable way is the terminal emulators, which is the main focus of today's session.
# 
# ## Basic terminology 
# 
# ### graphical user interface (GUI)
# In its most basic form, all computers have some interaction to store, process, create data, take actions, and communicate with other computers and people. There are many ways to interact with the computer. However, the most common is the GUI, which uses a mix of windows, icons, mice, and pointers to perform various tasks. This user interface type makes it easier for users to navigate through and use hundreds of programs, often from within a complex hierarchy.
# 
# ### Command-line interface (CLI)
# Under the hood, all computers have a command-line interface, or CLI, which distinguishes it from the more common GUI, which most people use nowadays. A CLI's heart is a read-evaluate-print loop or REPL: when a user types a command and presses enter, the computer reads the command, runs the command, and prints out the output until the user breaks the cycle. One of the programs in charge of enabling this cycle is called a shell or terminal.
# 
# ### The Shell/Terminal
# The shell is a program that serves as a keyboard-driven interface between the user and the operating system. It includes a command-line interpreter that accepts the user input via the keyboard, evaluates it, starts programs if necessary, and returns the output in the form of text output to the user. Each shell has its programming language, which makes it possible to write scripts that automate complex tasks. Each shell runs in a terminal.
# 
# ### What is Bash
# One of the differences between a shell and any other program is that a shell runs other programs instead of doing calculations. One of the most popular Unix shells is Bash, named for the Bourne Again Shell (derived from a shell originally written by Stephen Bourne). In most modern Unix implementations and most packages designed for Windows, Bash is the default shell.
# 
# ## Context and practicalities
# 
# ### Opening a terminal on your local computer 
# ```{dropdown} Opening a terminal on your local computer 
# 1. On macOS By clicking command+space and writing the word terminal spawn a terminal on your mac os
# 1. on Windows - I dont use windows so if anyone can tell me the shortcut that would be great 
# ```
# ### Command prompt
# Opening the terminal for the very first time, you will be presented with a prompt `$`, indicating that the shell is waiting for your input.
# 
# ```bash
# $
# ```
# 
# 
# ### Shell Commands structure
# You interact with the shell via commands, which can be used to execute CLI programs with names similar to the commands. For each action that you wish to perform using the terminal, you use a program call following this basic scheme:
# 
# ~~~bash
# Command [options] [arguments] 
# ~~~
# 
# 
# 

# ## Commands
# 
# ### Use `ls` to list folder contents 
# The first command we will use is `ls`, which displays the current directory contents. <br>
# 
# ```{admonition} Challenge
# Type `ls` in your open terminal and press the <kbd>Enter</kbd> key to execute it.
# ```
# 
# 
# ### Managing Content in the Filesystem
# The part of the operating system responsible for managing individual files and directories is called the **file system**. This part of the system categorizes our data into files or directories that contain files. 
# 
# 
# ### Creating a sandbox directory using mkdir
# 
# ```{admonition} Challenge
# Make a new directory by typing `mkdir sandbox` in the prompt.
# Here, mkdir is the program name and sandbox is the argument, in this case the name of the directory we are creating.
# ```
# 
# #### mkdir trys to create the same dircetory and return an error 
# Type `mkdir sandbox` again. Now the program returns an error.
# 
# ```{error}
# ```{code-block} console 
# mkdir sandbox  
# mkdir: cannot create directory ‘sandbox’: File exists
# ```
# 
# 

# #### mkdir options allow us to issue more advanced commands
# By adding the --help option, prints out the different options you can use to extend the mkdir program.
# ```{admonition} Challenge
# ```{dropdown} Please type the following command in the prompt. 
# ```{code-block} console 
# mkdir --help
# ```
# 

# #### mkdir --parent gives us the ability to form filesystem structures
# By adding the -p (aka parent) option, the mkdir program will create a hierarchical folder structure.
# Please type the following command in the prompt. 
# ```{admonition} Challenge
# ```{dropdown} Please type the following command in the prompt.
# ```{code-block} console
# mkdir -p sandbox/root/{dir_a,dir_b/{leaf_1,leaf_2},dir_c}
# ```
# 

# ### list folder structure
# In order to confirm, we could use wildcards like `ls sandbox/*/*/*` where each astrix corresponds to a different level in the hierarchy folder we created. However, there is a good chance that one of the many options of the `ls` command might be able to solve this problem in a generic way.  
# 
# ```{admonition} Challenge
# Try to use the `ls --help` to figure out what option is the most suitable.
# ```
# 
# ```{dropdown} Solution
# ```{code-block} console
# ls -R sandbox/
# ```
# 
# Here we state the root folder to start listing from, and then use the recursive  option to list all subdirectories recursively to the prompt.

# ### Removing a directory 
# If we add a folder, we should also have the ability to remove it, else we risk having a very messy file system.
# 
# #### The `rm` command 
# If we try to use the `rm` command to remove the `sandbox/` folder we get an error.
# ```{code-block} console
# rm sandbox/
# ```
# 
# ```{dropdown} One potential solution
# ```{code-block} console
# rm -d sandbox/
# ```
# But this ends with an error also 
# 
# ```{dropdown} Real solution
# The solution is to remove all the structure recursively (using the -r option), starting with the empty directories and moving upward in the hierarchy. We add the -f (force) option to handle directories that are not empty.
# ```{code-block} console
# rm -rf sandbox/
# ```
# 
# ### Navigating the filesystem
# To move to and view directories, files, and content, we need some basic navigation skills. 
# 
# #### Change Directory  `CD`
# Navigation is the most fundamental skill in any computer program. The Change Directory command provides us with capability to switch from one place to another. For example, we can go to the Data folder we just created by using the following command:
# 
# ```{code-block} console
# cd sandbox/My_first_project/Data
# ```
# 
# ### Knowing where you are 
# Another important thing is knowing where you are. The print working directory `pwd` will show you where you are currently located. 
# Try to run the pwd command for yourself 
# 
# ```{code-block} bash
# pwd
# ```

# ## Why would we want to use the terminal 
# Clearly, there is an elephant in the room... Why would I want to waste your time by teaching you this ancient interface.
# 
# ```{dropdown} My main reason
# Lies in automation and standardization.
# If I know that the filesystem will look the same for every project I create, I can set up automatic processes that will take that into account. Look at the following line for example. 
# ```{code-block} console
# mkdir -p sandbox/My_first_project/{Data/{pkl,csv,zip},Notebooks,Code,Tmp,Report/{Tables,Figures,Text,Background/{pdf,pptx},Presentation}}
# ls -R sandbox/
# ```

# ## Document your code 
# ### Hash tag - add comments to your code 
# \'#' the hash sign is used as the beginning of the comment in the script. In each line of the statement, the part starting with \'#' is not executed.  
# 
# ```{dropdown} Examples using \'cd' and \'#'
# ```{code-block} bash
# cd / # change directory to the root directory
# cd ~ # change directory to your home directory
# cd ~/sandbox/My_first_project/Report # goto Report dir
# cd "dir name"# if for some reason you created a folder name with spaces
# # (DONT!!!) this is how you call it
# ```

# ## Deeper dive into the bash syntax
# ### listing all folders contents 
# Recall that `ls` contains many options, among the most useful ones are `-a`  which stands for all and means that the command does not ignore entries starting with `.`. Another useful option is `-l` which tells the command to use a long listing format. 
# 
# 
# ```{code-block} bash
# cd sandbox/My_first_project/Data
# ls -al
# ```
# 
# ```{code-block} bash
# drwxr-xr-x 5 jovyan users 4096 May 13 14:31 .
# drwxr-xr-x 8 jovyan users 4096 May 13 14:31 ..
# drwxr-xr-x 2 jovyan users 4096 May 13 14:31 csv
# drwxr-xr-x 2 jovyan users 4096 May 13 14:31 pkl
# drwxr-xr-x 2 jovyan users 4096 May 13 14:31 zip
# ```

# #### Let's unpack one line of the output from right to left 
# - Let's unpack the bottom line from right to left
# 
# |  |  |
# | :-- | :-- |
# | `..` | file/folder name |
# | `May 13 14:31` | The **last** modification time |
# | `4096` | File size in bytes |
# | `users` | Group name |
# | `jovyan` | Owner name |
# | `8` | Number of links |
# | `drwxr-xr-x` | Permissions |
# | | |

# ### Basics of permissions
# 
# - Permission settings are grouped in a string of characters (-, r, w, x)
# - The characters r, w, and x stand for **read**, **write**, and **execute**.
# classified into four sections:
# - <span style="color:DARKRED">-</span>rwxrwxrwx - File type has three possibilities:
# - regular file (–)
# - a directory (d)
# - or a link (i)
# - -<span style="color:DARKRED">rwx</span>rwxrwx - File permission of the user (owner)
# - -rwx<span style="color:DARKRED">rwx</span>rwx - File permission of the owner’s group
# - -rwxrwx<span style="color:DARKRED">rwx</span>- File permission of other users

# ### Changing permissions
# 
# - Any Linux user, will at some point need to modify the permission settings of a file/directory.
# - This can be done using the `chmod` command.
# - The basic syntax is:
# 
# ```{code-block} bash
# chmod [permission] [file_name]
# # one way that is the simplest to remember
# chmod u=rwx,g=rwx,o=rwx [file_name]
# ```
# 
# - rwx stand for r(ead),w(rite) and (e)x(ecute)
# - and ugo stand for u(ser), g(roup) and o(ther)

# ## File system navigation
# ### Knowing how to go home
# 
# A program that tracks your location provides an opportunity to discuss the difference between **relative** and **absolute** locations. The `pwd` command returns the absolute path to where you are. The shell contains two important variables, both of which are subjective. The first is the environment variable `$PWD`, which specifies your current active location. The other is `$HOME`, which is the active user's home folder. We can create our own variables in the shell to make navigation easier. When do you think this following code snippet can be useful?  
# 
# ```{code-block} bash
# ORIGIN=$PWD
# cd $HOME
# # do stuff
# cd $ORIGIN
# ```
# 
# ```{dropdown} My explanation
# Here we create a variable named `ORIGIN` which represents our starting position, so we can go to other places, such as our home directory, run a program there, and eventually return to our origin.
# ```

# ## Advanced Bash
# ### Alias
# - Shell aliases are used to reference a command. 
# - They can be used to avoid typing long commands or to correct incorrect input. 
# - It can reduce keystrokes for common patterns and increase efficiency. 
# - Consider using it for complex commands with frequently used options, or even simple commands with commonly used options.
# - The format is simple and this is a good opportunity to share with you some cool examples of using ls 
# 
# ```{code-block} bash
# alias ls='ls -h --color'
# alias ll="ls -lv"
# alias lm='ll | more' # Pipe through 'more'
# alias lr='ll -R' # Recursive ls.
# alias la='ll -A' # Show hidden files.
# alias lx='ll -XB' # Sort by extension.
# alias lk='ll -Sr | sr' # Sort by size, biggest first.
# alias lt='ll -tr | sr' # Sort by date, most recent first.
# alias # list all current aliases
# ```
# 

# ### creating content in the terminal (Old-school)
# In the last section for this episode we will cover different ways to generate files via the terminal. 
# 
# #### `echo`
# - Prints text to the terminal window
# - The most basic process in any programming language is the ability to output information.
# - The `echo` command prints text to the terminal window and is typically used in shell scripts and batch files to output
# status text to the screen or a computer file.
# - Echo is also particularly useful for showing the values of environmental variables, which tell the shell how to behave
# as a user works at the command line or in scripts.
# 
# ```{code-block} bash
# cd ~/sandbox/My_first_project/Report 
# echo $ORIGIN
# echo $HOME
# echo $PWD
# ```
# 

# ### Examples using `echo` 
# 
# ```{code-block} bash
# cd sandbox
# echo Some text to print out
# # any string after the command will be printed
# echo *
# # Will Print all the files/folder using echo command
# echo *.jpeg
# # Will Print all the files of a specific kind
# echo "Some text to add to a file" > file.txt
# # Use redirect operator to store output to a file
# echo "Some other text to add to a file" >> file.txt
# # Use redirect append operator >> to add output to file
# ```

# ### Examples using `cat` 
# ```{code-block} bash
# cat file.txt
# # Displaying Contents of a File
# cat file_2.txt
# # Allows to write text interactively
# cat file_2.txt > file_1.txt
# # It is possible to redirect to output like echo
# # However the above command overwrites the file contents
# cat file.txt file_1.txt file_2.txt
# # We can also view contents of multiple files
# cat file_1.txt >> file.txt
# # file_1 content will be appended at the end of file
# ```

# ### cp,mv - 
# 
# - Copy, move or rename files and directories
# 
# - Using cp, you can copy a file, a group of files, or a directory. A file is copied as an exact copy with a different file name to a disk. It is necessary to pass at least two file names to cp.
# 
# ```{code-block} bash
# cp [OPTION] Source Destination
# cp [OPTION] Source Directory
# cp [OPTION] Source-1 Source-2 Source-3 Source-n Directory
# ```
# 

# ### Examples
# 
# ```{code-block} bash
# cd ~/sandbox # make sure we are at sandbox
# output=dir_root/dir_branch/dir_leaf
# # make a variable to store path
# mkdir -p $output # verify that output exists and if not create it
# mkdir -p dir_root/dir_branch2
# # Create  another branch in dir_root
# cp file $output # copy file to path
# mv file_1 $output # move file_1 to output
# ls $output # list files in output
# mv file $output/file_renamed
# # move file to output and rename it
# mkdir -p dir_1 dir_2
# mv -t dir_root/dir_branch2 dir_1 dir_2
# # move folders to --target-directory (long form of -t)
# cp -R dir_root/dir_branch2 $output
# # recursively copy folder content to path
# ls -FR $output # list files in output again
# ```

# ### `echo multiline` — Often we would like to write multi line files
# Here we read the contents of standard input, emit it to standard output, and makes a copy of it into the specified file(s) or variables.
# The purpose of this example is to create a `.bash_aliases` file containing all of your aliases and learn how to use more about the `echo` command. 
# We understand what aliases are. However, it's vital to comprehend that the aliases you create will only remain as long as the shell is open.
# Hence, it is useful to keep all aliases in one file.
# 
# 
# #### Example 
# 
# ```{code-block} bash
# echo "
# alias ls='ls -h --color'
# alias ll='ls -lv --group-directories-first'
# alias lm='ll | more' # Pipe through 'more'
# alias lr='ll -R' # Recursive ls.
# alias la='ll -A' # Show hidden files.
# alias lx='ll -XB' # Sort by extension.
# alias lk='ll -Sr | sr' # Sort by size, biggest first.
# alias lt='ll -tr | sr' # Sort by date, most recent first.
# " >> ~/.bash_aliases
# ```
# 
# You can see we are using the >> argument, which appends the content into the filename. What might happen if we won’t use that option?
# 
# ### How do we use these? 
# In bash we need to source a file to make its contents avaliable we do this using the command `source`
# 
# ```{code-block} bash
# source ~/.bash_aliases
# ```
# 
# we have now made all these aliases active and we can use them 

# ## Functions
# ### Using the concept of relative path we can create our first generlised Bash function 
# In bash we can pass arguments to a function, arguments are seperated by spaces and the first argument is always \$1 
# In bash there are protected symbols that in order to pass them we need to make the software ignore them we do this using what is called an escape sequence which is just a backslash in front of the symbol 
# 
# ```{code-block} bash
# echo " 
# function mcd {
#     mkdir -p \$1
#     cd \$1
# }" >> functions.sh
# ```
# 
# Here we are making a function called mcd which combines mkdir and cd into one unified process
# let's test this function 
# 
# ```{code-block} bash
# source functions.sh
# mcd my_new_folder
# pwd
# ```
# 

# ### Finally let's create a useful function to organise your projects further
# 
# ```{code-block} bash
# echo " 
# function make_folder_structure {
#    echo Creating folder structure in \$1
#    mkdir -p \$1/{Notebooks,Code,Tmp,Data,Report,Presentation}
#    mkdir -p \$1/Data/{raw,processed,share}
#    mkdir -p \$1/Report/{Tables,Figures,Text}
#    mkdir -p \$1/Background/{pdf,pptx}
#    echo Dont forget to add README > \$1/README.md}" >> functions.sh
# ```
# 
# Try to explain what this function is doing 

# ## Links to expand your understanding 
# 
# As a scientist in a data-infested field, your knowledge should always be refreshed, clarified, and expanded. Here are some links to support you in that: 
# 
# - [introduction-to-shell](https://learn.datacamp.com/courses/introduction-to-shell)
# - [Introduction to Bash Scripting](https://learn.datacamp.com/courses/introduction-to-bash-scripting)
# - [command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
