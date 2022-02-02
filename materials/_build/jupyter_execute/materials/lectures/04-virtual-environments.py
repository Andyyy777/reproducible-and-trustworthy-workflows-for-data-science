#!/usr/bin/env python
# coding: utf-8

# # Virtual environments

# #### Attribution
# 
# The conda virtual environment section of this guide
# was originally published at http://geohackweek.github.io/ under a CC-BY license
# and has been updated to reflect recent changes in conda,
# as well as modified slightly to fit the MDS lecture format.
# 
# ## Topic learning goals
# 
# By the end of the lecture you will be able to:
# 
# 1. Explain what a virtual environment is and why it can be useful for reproducible data analyses
# 2. Discuss the advantages and limitations of virtual environment tools (e.g., `conda` and `renv`) in the context of reproducible data analyses
# 3. Use, create and share virtual environments (for example, with conda and `renv`)

# ## Virtual environments
# 
# Virtual environments let's you have multiple versions of programming languages 
# packages, and other programs on the same computer, while keeping them isolated
# so they do not create conflicts with each other.
# In practice virtual environments are used in one or multiple projects.
# And you might have several virtual environments stored on your laptop,
# so that you can have a different collection of versions programming languages 
# and their packages for each project, as needed.
# 
# Most virtual environment tools have a sharing functionality which aids in making
# data science projects reproducible, 
# as not only is there a record of the computational environment,
# but that computational environment can be shared to others computer - 
# facilitating the reproduction of results from data and code.
# This facilitation comes from the fact that programming languages 
# and their packages are not static - they change! 
# There are new features added, bugs are fixed, etc,
# and this can impact how your code runs! 
# Therefore, for a data science project to be reproducible across time, 
# you need the computational environment in addition to the data and the code.
# 
# There are several other major benefits of using environments:
# 
# - If two of your projects on your computer rely on different versions of the same package,
#   you can install these in different environments.
# - If you want to play around with a new package,
#   you don't have to change the packages versions you use for your data analysis project
#   and risk messing something up 
#   (package version often get upgraded when we install other new packages that share dependencies).
# - When you develop your own packages,
#   it is essential to use environments,
#   since you want to to make sure you know exactly which packages yours depend on,
#   so that it runs on other systems than your own.
# 
# 
# There are **MANY** version virtual environment tools out there, 
# even if we just focus on R and Python. 
# When we do that we can generate this list:
# 
# #### R virtual environment tools
# - `packrat`
# - `renv`
# - `conda`
# 
# #### Python virtual environment tools
# - `venv`
# - `virtualenv`
# - `conda`
# - `mamba`
# - `poetry`
# - `pipenv`
# - ... there may be more that I have missed.
# 
# 
# In this course, we will learn about `conda` and `renv`. 
# `conda` is nice because it can work with both R and Python.
# Although a downside of `conda` is that it is not as widely adopted in the R community 
# as Python is, and therefore there are less R packages available from it, 
# and less recent versions of those R packages than available directly from the R package index (CRAN).
# It is true, that you can create a `conda` package for any R package that exists on CRAN, 
# however this takes time and effort and is sometimes non-trivial.
# 
# Given that, we will also learn about `renv` - a new virtual environment tool in R 
# that is gaining widespread adoption. 
# It works directly with the packages on CRAN, 
# and therefore allows users to crete R virtual environments with
# the most up to date packages, and all R packages on CRAN, with less work compared to `conda`.
# 
# > Note on terminology: Technically what we are discussing here in this topic are referred to as virtual environments.
# > However, in practice we often drop the "virtual" when discussing this and refer to these as simply "environments".
# > That may happen in these lecture notes, as well as in the classroom.

# ## Conda
# 
# [**conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system for any programming language**;
# though it is most popular in the Python community.
# `conda` was originally developed by [Anaconda Inc.](https://www.anaconda.com/products/individual) 
# and bundled with their Anaconda distribution of Python. 
# However, `conda`'s widespread popularity 
# and utility led to its decoupling into its own package.
# 
# It is now available for installation via:
# - Anaconda Python distribution
# - Miniconda Python distribution (this is what we recommended most of you install for this course)
# - Miniforge (this is what we recommended folks with Mac ARM machines install for this course)
# 
# Conda builds of R and Python packages, are in fact R and Python packages and built from
# R and Python source code, but they are packaged up and built differently, 
# and with a different tool chain.
# How to create `conda` packages from R and Python source code 
# is beyond the scope of this course.
# However, we direct keen learners of this topic to the documentation on how to do this:
# - [Conda-build documentation](https://docs.conda.io/projects/conda-build/en/latest/)
# 
# What we will focus on learning is how to use `conda`
# to create virtual environments, 
# record the components of the virtual environment
# and share the virtual environment with collaborators 
# in a way that they can recreate it on their computer.
# 
# ### Managing Conda
# 
# Let's first start by checking if conda is installed (it should be if we followed the recommended course computer setup instructions) by running:
# 
# ```
# conda --version
# ```
# 
# To see which conda commands are available,
# type `conda --help`.
# To see the full documentation for any command of these commands,
# type the command followed by `--help`.
# For example,
# to learn about the conda update command:
# 
# ```
# conda update --help
# ```
# 
# Let's update our conda to the latest version.
# Note that you might already have the latest version since we downloaded it recently.
# 
# ```
# conda update conda
# ```
# 
# You will see some information about what there is to update
# and be asked if you want to confirm.
# The default choice is indicated with `[]`,
# and you can press <kbd>Enter</kbd> to accept it.
# It would look similar to this:
# 
# ```
# Using Anaconda Cloud api site https://api.anaconda.org
# Fetching package metadata: ....
# .Solving package specifications: .........
# 
# Package plan for installation in environment //anaconda:
# 
# The following packages will be downloaded:
# 
#     package                    |            build
#     ---------------------------|-----------------
#     conda-env-2.6.0            |                0          601 B
#     ruamel_yaml-0.11.14        |           py27_0         184 KB
#     conda-4.2.12               |           py27_0         376 KB
#     ------------------------------------------------------------
#                                            Total:         560 KB
# 
# The following NEW packages will be INSTALLED:
# 
#     ruamel_yaml: 0.11.14-py27_0
# 
# The following packages will be UPDATED:
# 
#     conda:       4.0.7-py27_0 --> 4.2.12-py27_0
#     conda-env:   2.4.5-py27_0 --> 2.6.0-0
#     python:      2.7.11-0     --> 2.7.12-1
#     sqlite:      3.9.2-0      --> 3.13.0-0
# 
# Proceed ([y]/n)? y
# 
# Fetching packages ...
# conda-env-2.6. 100% |################################| Time: 0:00:00 360.78 kB/s
# ruamel_yaml-0. 100% |################################| Time: 0:00:00   5.53 MB/s
# conda-4.2.12-p 100% |################################| Time: 0:00:00   5.84 MB/s
# Extracting packages ...
# [      COMPLETE      ]|###################################################| 100%
# Unlinking packages ...
# [      COMPLETE      ]|###################################################| 100%
# Linking packages ...
# [      COMPLETE      ]|###################################################| 100%
# ```
# 
# In this case,
# conda itself needed to be updated,
# and along with this update some dependencies also needed to be updated.
# There is also a NEW package that was INSTALLED in order to update conda.
# You don't need to worry about remembering to update conda,
# it will let you know if it is out of date when you are installing new packages.

# ### Managing `conda` environments
# 
# #### What is a conda environment and why is it so useful?
# 
# Using `conda`, you can create an isolated R or Python virtual environment for your project.
# The default environment is the `base` environment,
# which contains only the essential packages from Miniconda 
# (and anything else you have installed in it since installing Miniconda).
# You can see that your shell's prompt string is prefaced with `(base)`
# when you are inside this environment:
# 
# ```{bash}
# (base) Helps-MacBook-Pro:~ tiffany$
# ```
# 
# In the computer setup guide,
# we asked you to follow instructions so that this environment 
# will be activatd by default every time you open your terminal.
# 
# To create another environment on your computer, 
# that is isolated from the `(base)` environment 
# you can either do this through:
# 
# 1. Manual specifications of packages.
# 2. An environment file in YAML format (`environment.yaml`).
# 
# We will now discuss both, as they are both relevant workflows for data science. 
# When do you use one versus the other?
# I typically use the manual specifications of packages when I am creating
# a new data science project.
# From that I generate an environment file in YAML format 
# that I can share with collaborators (or anyone else who wants to reproduce my work).
# Thus, I use an environment file in YAML format when I join a project as a collaborator 
# and I need to use the same environment that has been previously used for that project,
# or when I want to reproduce someone else's work.

# #### Creating environment by manually specifying packages
# 
# We can create `test_env` conda environment by typing `conda -n <name-of-env>`.
# However,
# it is often useful to specify more than just the name of the environment,
# e.g. the channel from which to install packages, the Python version,
# and a list of packages to install into the new env.
# In the example below,
# I am creating the `test_env` environment
# that uses python 3.7 and a list of libraries: `jupyterlab` and `pandas`.
# 
# ```
# conda create -n test_env -c conda-forge python=3.7 jupyterlab pandas=1.0.2
# ```
# 
# conda will solve any dependencies between the packages like before
# and create a new environment with those packages.
# Usually,
# we don't need to specify the channel,
# but in this case I want to get the very latest version of these packages,
# and they are made available in `conda-forge`
# before they reach the default conda channel.
# 
# To activate this new environment,
# you can type `conda activate test_env`
# (and `conda deactivate` for deactivating).
# Since you will do this often,
# we created an alias shortcut `ca`
# that you can use to activate environments.
# To know the current environment that you're in you can look at the prefix
# of the prompt string in your shell which now changed to (`test_env`).
# And to see all your environments,
# you can type `conda env list`.

# #### Seeing what packages are available in an environment
# 
# We will now check packages that are available to us.
# The command below will list all the packages in an environment, in this case `test_env`.
# The list will include versions of each package, the specific build,
# and the channel that the package was downloaded from.
# `conda list` is also useful to ensure that you have installed the packages that you desire.
# 
# ```
# conda list
# ```
# 
# ```
# # packages in environment at //miniconda/envs/test_env:
# #
# Using Anaconda Cloud api site https://api.anaconda.org
# blas                      1.1                    openblas    conda-forge
# ca-certificates           2016.9.26                     0    conda-forge
# certifi                   2016.9.26                py27_0    conda-forge
# cycler                    0.10.0                   py27_0    conda-forge
# freetype                  2.6.3                         1    conda-forge
# functools32               3.2.3.2                  py27_1    conda-forge
# libgfortran               3.0.0                         0    conda-forge
# ```

# #### Installing conda package
# 
# Under the name column of the result in the terminal or the package column in the Anaconda Cloud listing,
# shows the necessary information to install the package.
# e.g. conda-forge/rasterio.
# The first word list the channel that this package is from and the second part shows the name of the package.
# 
# To install the latest version available within the channel, do not specify in the install command. We will install version 0.35 of `rasterio` from conda-forge into `test_env` in this example. Conda will also automatically install the dependencies for this package.
# 
# ```
# conda install -c conda-forge rasterio=0.35
# ```
# 
# If you have a few trusted channels that you prefer to use, you can pre-configure these so that everytime you are creating an environment, you won't need to explicitly declare the channel. 
# 
# ```
# conda config --add channels conda-forge
# ```

# #### Removing a conda package
# 
# We decided that rasterio is not needed in this tutorial, so we will remove it from `test_env`.
# Note that this will remove the main package rasterio and its dependencies (unless a dependency was installed explicitly at an earlier point in time or is required be another package).
# 
# ```
# conda remove -n test_env rasterio
# ```
# 
# ```
# Using Anaconda Cloud api site https://api.anaconda.org
# Fetching package metadata .........
# Solving package specifications: ..........
# 
# Package plan for package removal in environment //anaconda/envs/test_env:
# 
# The following packages will be REMOVED:
# 
#     rasterio: 0.35.1-np111py27_1 conda-forge
# 
# Proceed ([y]/n)? y
# 
# Unlinking packages ...
# [      COMPLETE      ]|#######################################################################################################| 100%
# ```

# #### Sharing Environments with others
# 
# To share an environment, you can export your conda environment to an environment file,
# which will list each package and its version
# in the format `package=version=build`.
# 
# Exporting your environment to a file called `environment.yaml`
# (it could be called anything,
# but this is the conventional name
# and using it makes it easy for others
# to recognize that this is a conda env file,
# the extension can be either `.yaml` or `.yml`):
# 
# ```
# conda env export -f environment.yaml
# ```
# 
# Remember that `.yaml` files are plain text,
# so you can use a text editor such as VS Code to open them.
# If you do,
# you will realize that this environment file has A LOT more packages
# than `jupyterlab` and `pandas`.
# This is because the default behavior is to also list the dependencies
# that were installed together with these packages,
# e.g. `numpy`.
# This is good in the sense that it gives an exact copy of *everything*
# in your environment.
# 
# However,
# some dependencies might differ between operating systems,
# so this file *might* not work with someone from a different OS.
# To remedy this,
# you can append the `--from-history` flag,
# which look at the history of the packages you explicitly told conda to install
# and only list those in the export.
# The required dependencies will then be handled in an OS-specific manner during the installation,
# which guarantees that they will work across OSes.
# This `environment.yaml` file would be much shorter and look something like this:
# 
# ```yaml
# name: test_env
# channels:
#   - conda-forge
#   - defaults
# dependencies:
#   - conda
#   - python=3.7
#   - pandas==1.0.2
#   - jupyterlab
# ```
# 
# Importantly,
# this will not include the package version
# unless you included it when you installed 
# with the `package==version` syntax.
# For an environment to be reproducible,
# you **NEED** to add the version string manually.

# #### Creating environment from an environment file
# 
# Now, let's install `environment.yaml` environment file above so that we can create a conda environment called `test_env`.
# 
# ```
# $ conda env create --file environment.yaml
# ```

# #### Copying an environment
# 
# We can make an exact copy of an environment to an environment with a different name.
# This maybe useful for any testing versus live environments or different Python 3.7 versions for the same packages.
# In this example, `test_env` is cloned to create `live_env`.
# 
# ```
# conda create --name live_env --clone test_env
# ```

# #### Deleting an environment
# 
# Since we are only testing out our environment,
# we will delete `live_env` to remove some clutter.
# *Make sure that you are not currently using `live_env`.*
# 
# ```
# conda env remove -n live_env
# ```

# #### Making environments work well with JupyterLab
# 
# In brief,
# you need to install a kernel in the new conda environment
# in any new environment your create (`ipykernel` for Python
# and the `r-irkernel` package for R),
# and the `nb_conda_kernels` package needs to be installed
# in the environment where JupyterLab is installed.
# 
# By default,
# JupyterLab only sees the conda environment where it is installed.
# Since it is quite annoying to install JupyterLab and its extensions separately in each environment,
# there is a package called `nb_conda_kernels` that makes it possible
# to have a single installation of JupyterLab access kernels in other conda environments.
# This package needs to be installed in the conda environment
# where JupyterLab is installed.
# For the computer setup for this course, we did that in the `base` environment, 
# so that is where you would need to install `nb_conda_kernels` to make this work.
# 
# 
# *More details are available in the [nb_conda_kernels README](https://github.com/Anaconda-Platform/nb_conda_kernels#installation)).*

# Remeber that when you forget a specific command
# you can type in the help command we have created `mds-help`
# in you terminal to see a list of all commands we use in MDS.

# ## `renv`
# 
# In R,
# environments can also be managed by `renv`,
# which works with similar principles as `conda`,
# and other virtual environment managers,
# but the commands are different.
# To see which commands are used in `renv`,
# you can [visit the project website](https://rstudio.github.io/renv/articles/renv.html).
# Briefly,
# `renv::init()` is used to create a new env,
# `renv::snapshot` is used to save/export the environment to a file (`renv.lock`),
# and installing and removing packages are done as usual
# via the `install.packages()` and `remove.packages()` commands.