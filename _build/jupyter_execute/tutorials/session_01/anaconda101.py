#!/usr/bin/env python
# coding: utf-8

# # Anaconda environment 101
# 
# ## Basics
# ### What is Conda?
# Conta is a package and environment manager based on Python. It assists in the development of reproducible analysis pipelines using crowd-sourced and version-controlled packages. It might be a bit confusing for an individual who is new to this type of approach. In order to make sure we all understand each other, let's establish some quick vocabulary:
# 
# ### What is an environment?
# 
# In a computing environment, people use an assortment of programs, language libraries, etc. to operate a computer.  
# Depending on the context, the word environment can have many different meanings, like a generalized term for an ecological ecosystem that can refer to anything from a puddle to a continent.  
# As far as we're concerned, an environment is simply a set of tools that are put together to assist us in exploring data-driven questions in a reproducible manner.
# 
# ### What is an package?
# As the name implies, a package is a collection of software, including things like programs  (e.g. Python), programming libraries (e.g. Bash), or other useful tools.  
# Using the Conda package management system, you can combine packages and make complex environments.  
# It can be summed up like this: Conda creates self-contained modules that contain all of the necessary programs, etc, in order to complete a specific task of computing.
# 
# ### What is dependency hell
# The term dependency hell refers to the problems that users generally face when they rely on many interdependent packages.  
# The main source of complications or bugs in dependency hell are changes made to third-party packages that are no longer compatible with one another.
# 
# 
# ### How does Conda manage dependencies
# Conda helps manage dependencies in two primary ways:
# Allows the creation of environments that isolate each project, thereby preventing dependency conflicts between projects.  
# Provides identification of dependency conflicts at time of package installation, thereby preventing conflicts within projects/environments.
# 
# 
# ### What is version control 
# Version control is what, exactly? Version control tools allow you to keep track of the changes you make to your work over time.  
# This feature is a little like "track changes" in Google Docs, but with the difference that you can save changes across several files, not just within one.
# 
# 
# ### Why is Conda useful?
# 
# Using Conda as part of analysis workflows has a lot of advantages:
# 
# 1. It helps keep your computing environment organized so you're less likely to end up in "dependency hell".
# 1. Since packages are version-controlled, you can easily switch versions if one doesn't work.
# 1. Operating systems aren't really an issue (it runs on Mac, Windows, Linux). However, not every package is available for every OS.
# 1. We can replicate and share environments, so our analysis is more accurate.
# 
# 
# ### Conda in Practice
# 1. One thing we ultimately want is having full control over the environment
# 1. The following is true to your local computer as well as any cluster
# 1. Anaconda gives us this power exactly

# ## Context and practicalities
# 
# ### Check if anaconda is installed
# The simplest way to test if anaconda is installed on your computer is to issue the command `conda info`
# 
# ```{code-block} bash
# conda info
# ```
# 
# ### If anaconda isn't installed 
# Go to [Anaconda site](https://docs.anaconda.com/anaconda/install/index.html) and install it

# ## Creating and Managing Environments
# 
# Now that we've confirmed that Conda is operational, we can begin learning how to utilise it as an environment-based package manager.
# Environments are essential components of Conda-based processes.
# They are modules that are adaptable, replicable, and shareable that include the resources for a certain activity or group of activities.
# Environments also assist in avoiding "dependency hell," which occurs when necessary programmes are incompatible with previously installed programmes or programme versions. Today's goal is to put up a Python environment to facilitate future analytics using dcarte.
# 
# ### View installed enviorments 
# 
# To start with, let's see what environments we currently have set up.  
# This will list all of the environments available for us to use along with their locations.
# 
# ```{code-block} bash
# conda env list
# ```
# 
# By default, an environment called `base` is created when installing and intializing Conda.  
# `base` contains a number of standard Python packages that may or may not be useful.

# ### Kernels
# Kernels are autonomous programming language processes that interact with Jupyter Applications and their user interfaces.
# ipykernel is a Jupyter kernel developed on top of IPython that provides a strong environment for interactive Python computation.
# The IPython project is maintained by the Jupyter team, and it is provided as the default kernel (as ipykernel) in a number of Jupyter clients. In addition to Python, several more languages may be utilised in the notebook. Many additional language kernels are maintained by the community, and new kernels are released on a regular basis. 
# 
# ### View installed Kernels 
# Remember that a kernel is just a program that runs and inspects your code: it provides computation and communication with frontend UIs, like  notebooks.  
# The Jupyter Notebook Application has three main kernels: the IPython (python3), IRkernel (ir) and IJulia (julia-1.6) kernels.  
# XPython and bash are two additional kernels that are common in cloud.  
# XPython is primarily used for debugging python code, and we have been using the bash kernel since we began the course and it provides direct access to bash programs.
# 
# ```{code-block} bash
# jupyter kernelspec list
# ```

# ## How do we create a new environment in anaconda
# 
# 1. In Anaconda, you can create an environment by typing the following: `conda create --name myenv`, where myenv is the name of your environment.
# 1. This creates an empty environment named myenv in `$HOME/env/`. 
# 1. To create an environment with a particular version of Python, simply type in `conda create --name myenv python=3.8` Keep in mind that this will create a very large folder, so be careful.
# 1. To create an environment with specific packages, simply list the packages you wish to include:  `conda create --name myenv numpy pandas matplotlib`
# 1. To specify the location of an environment (i.e. in a place different to the default location) use the `--prefix` option as follows :   `conda create --prefix ~/some_path/myenv`
# 1. To remove an environment, in your terminal run: `conda remove --name myenv --all`

# ### Let's create a basic environment 
# 
# ```{code-block} bash
# conda create --name basic && conda env list
# ```
# 
# Using a double `&` symbol in bash means that the next command is only executed if the first one was successful.
# 
# 
# ### To activate the environment
# 
# ```{code-block} bash
# conda activate basic
# ```
# 
# ### Get the list of packages installed in Anaconda
# 
# ```{code-block} bash
# conda list
# ```
# 
# ### This environment is empty lets add some basic tools we will use later on
# Numpy is the primary numeric library in Python, pandas is the primary tabular data wrangling tool in Python, and matplotlib is the most basic plotting tool available. We also need a software called `ipykernel` which is a powerful interactive Python shell and a Jupyter kernel to work with Python code in Jupyter notebooks and other interactive frontends. And finally we need a local installation of a notebook interface.
# 
# ```{note} 
# This example does not rely on any other software to function; everything we will require will be installed in the following step and so will be reproducible on any other platform.
# ```
# 
# ```{code-block} bash
# conda install numpy pandas matplotlib ipykernel jupyterlab
# ```
# 
# What we are installing are the different dependencies that these three tools rely on and if we use `conda list` now our local list will be massive. 
# 
# ### Sometimes it is useful to have the environment installed in the local project directory 
# 
# ```{code-block} bash
# conda create --prefix ~/some_path/basic
# ```
# 
# The main reason for doing that would be when we have specific tools needed only for one project or an inability to install on your home directory
# 
# ### Most of the times you will need to register our environment to Jupyter KernelSpec
# 
# It is the *KernelSpec* that determines what kernels are available on our Jupyter portal.  
# If we create a new environment and want it to be available we need to install it which in essence simply means adding it in a list somewhere.  
# The following code registers the new environment we created and creates a folder in your hidden `.local` folder that stores the information needed to run that kernel. 
# 
# ```{code-block} bash
# python -m ipykernel install --user --name=basic && jupyter kernelspec list
# ```
# 
# If we were succsesful we should see our basic kernel in the list. 
# 
# ### Export a yml snapshot to allow you to recreate the setup on a different computer 
# 
# ```{code-block} bash
# conda env export --name basic > $PWD/basic_env.yml
# ```
# 
# ### Spawn Jupyter to see if all the hard work was worth it 
# 
# ```{code-block} bash
# jupyter lab
# ```
# 
# All of this effort may be saved if vscode is used (on your local computer) but we will keep that for the next session.
# 
# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Conda Essentials](https://learn.datacamp.com/courses/conda-essentials)
# - [Building and Distributing Packages with Conda](https://learn.datacamp.com/courses/building-and-distributing-packages-with-conda)
# - [Some background on ipython and jupyter](https://www.datacamp.com/community/blog/ipython-jupyter)
# - [Jupyter Notebook Tutorial: The Definitive Guide](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)
# - [FreeCodeCamp’s Python Tutorial ](https://www.youtube.com/watch?v=rfscVS0vtbwl)
# - [Udemy’s Python for Data Science and Machine Learning Bootcamp](https://bit.ly/dataprofessor-udemy-python-ds)
# - [Coursera Python Course](https://www.coursera.org/learn/python)
# - [Introduction to Python](https://learn.datacamp.com/courses/intro-to-python-for-data-science)
# - [Intermediate Python](https://learn.datacamp.com/courses/intermediate-python)
# 
# 
