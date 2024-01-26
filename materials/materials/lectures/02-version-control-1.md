# Version control (for transparency and collaboration) I

## Topic learning objectives

By the end of this topic, students should be able to:

1. Explain why and how data analysis projects benefit from both local and remote version control
2. Use Git's basic functions to save changes to local and remote version control, as well as view and restore older versions of files

## Version control - a review

> *"Version control is the process of keeping a record of changes to documents, including when the changes were made and who made them, throughout the history of their development. It also provides the means both to view earlier versions of the project and to revert changes."*
>
> -- [*Data Science: A First Introduction*](https://datasciencebook.ca/version-control.html)

In this course we will learn to use the most popular version control software tools, Git and GitHub. A schematic of local and remote version control repositories using these tools is shown below:

<img src="https://ubc-dsci.github.io/introduction-to-datascience/_main_files/figure-html/vc1-no-changes-1.png" width=800>

Source: [*Data Science: A First Introduction*](https://datasciencebook.ca/version-control.html)

### A poll!

We expect some introductory version control knowledge before the contents of this chapter.
Essentially, what is covered in 
[Chapter 12: Collaboration with version control](https://datasciencebook.ca/version-control.html) 
from Data Science: A First Introduction. 
Here's a poll to check you have the prerequisite knowledge for this chapter. 
If you cannot easily answer these questions we recommend you go back to 
[Chapter 12: Collaboration with version control](https://datasciencebook.ca/version-control.html) 
from Data Science: A First Introduction and read (or re-read) it.

**1. Which of these is untrue about the Git and GitHub version control software?**

*a. Allows you to view and/or retrieve older snapshots of the files and directories in a project.*

*b. Automatically snapshots your work every 2 minutes.*

*c. Provides transparency on who made what changes to files and directories in a document.*

*d. Can act as a way to back-up your work.*


**2. GitHub is the software you use locally on your computer (i.e., your laptop) to commit changes to the version control history. True or False?**

*a. True*

*b. False*

*c. Neither true or false.*


**3. You changed two files (`notes.txt` and `eda.ipynb`) but you only want to commit changes to one of them (`eda.ipynb`) to the version control history. Which Git command allows you to specify this?**

*a. Add*

*b. Commit*

*c. Push*

*d. Push*


**4. At a minimum, how often should you push your work to GitHub?**

*a. Every 5 min.*

*b. Every 30 min.*

*c. At the end of every work session.*

*d. Once a week.* 


**5. You try to push your most recent commit from your locale version control repository to your remote repository on GitHub and it fails because Git says the `remote contains work that you do not have locally`. What do should you do next?**

*a. Commit the changes you made recently in your working directory.*

*b. Force push your changes.*

*c. Pull the changes from the remote repository that you do not have locally.*


**6. You pull changes that exist in your remote version control repository on GitHub that you do not have in your local version control repository, and you get the message `Auto-merging in <FILENAME> CONFLICT (content): Merge conflict in <FILENAME> Automatic merge failed; fix conflicts and then commit the result`. What do you need to do?**

*a. Push the changes from the local repository that you do not have remotely.*

*b. Force pull the changes.*

*c. Manually open the file with the conflict and edit it to have the desired version of the changes, as well as remove the special Git syntax used to identify the merge conflict.*

## Common Git commands at the command line

In the assigned textbook reading we use the JupyterLab Git extension tool to run Git version
control commands (adding to the staging area, committing, pushing, pulling).
However, here we will start using Git commands at the command line (i.e., Bash shell/terminal)
because these commands are more stable than most Git graphical user interfaces
(such as the JupyterLab Git extension tool).
Additionally, the Git command line tool provides access to all Git features,
some of which are missing in several Git graphical user interfaces
Thus, below we list the most common Git commands that you would need at the command line:

| Description | Command |
|---------|-------------|
| Clone a remote version control repository from GitHub.com to your local computer | `git clone` |
| Checking the status of the local version control repository | `git status` |
| Adding a file to the staging area | `git add <FILENAME>` |
| Committing staged file to the version control history | `git commit -m "Some relevant message about the changes"` |
| Push changes to the local version control repository to the remote repository on GitHub.com | `git push` |
| Pull changes from the remote version control repository on GitHub.com to the local repository | `git pull` |
| Viewing the version control history | `git log` |

## Hands on practice with merge conflicts!

One of the major blockers getting used to using version control is dealing with merge conflicts! 😱

Git can automatically handle merging two versions of a file if each collaborator changes different lines, however when two collaborators change the same line, Git throws up its hands and says, I cannot handle this responsibility, I need help from a human!

<img src="https://media.giphy.com/media/4SZxcPTtlGAZa/giphy.gif">

When this happens, your human task is to find the merge conflict markers, remove them, and settle on which version of the line(s) where the conflict occurred should remain. Merge conflict markers include:

- `<<<<<<< HEAD` to indicate the beginning of the merge conflict 
- `>>>>>>>` to indicate the end of the merge conflict
- `=======` between the markings mentioned above to indicate the boundary between the two proposed changes. The version of the change before the separator is your > change, and the version that follows the separator was the change that existed on GitHub. 

### Exercise: Resolving merge conflicts

We are going to now generate and resolve merge conflicts.I have set-up a template GitHub repository for you so that you can easily generate a merge conflict to resolve. We will do this twice, once with a simple plain text file (*e.g.*, an R script) and once with a more complex text file (*e.g.*, a Jupyter notebook).

#### Resolving merge conflicts in a simple text file:

**Steps:**

1. Click the green “Use this template” button from [this GitHub repository](https://github.com/ttimbers/r-cube) to obtain a copy of it for yourself (do not fork it).

2. Clone this repository to your computer.

3. Click on the Actions tab, and then click on the workflow .github/workflows/main.yml. You then should see a “Run workflow” button with a drop down menu, from that menu select “Run workflow” (this will trigger GitHub Actions to create a commit in your remote repository).

4. Locally on your computer, fix the second line in `cube.r` so that it calculates the cube, not the square (e.g., change `x^2` to `x^3`). Commit your changes to version control via Git and push your changes to GitHub.

5. Resolve the merge conflict them so that you can see your changes on GitHub.


#### Resolving merge conflicts in a more complex text file:

**Steps:**

1. Click the green “Use this template” button from [this GitHub repository](https://github.com/ttimbers/r-cube-notebook) to obtain a copy of it for yourself (do not fork it).

2. Clone this repository to your computer.

3. Click on the Actions tab, and then click on the workflow .github/workflows/main.yml. You then should see a “Run workflow” button with a drop down menu, from that menu select “Run workflow”  (this will trigger GitHub Actions to create a commit in your remote repository).

4. Fix the second line in the code cell in `cube.ipynb` so that it calculates the cube, not the square (e.g., change `x^2` to `x^3`). Commit your changes to version control via Git and push your changes to GitHub.

5. Resolve the merge conflict them so that you can see your changes on GitHub.


## Git ignore

What about pesky files that exist on our computer, that change sometimes but we don't really actively use (e.g., `.DS_Store`, `.ipynb_checkpoints`, etc). We can tell Git to ignore such irrelevant files by creating and using a `.gitignore` file

### Create a `.gitignore` file

Using the plain text editor of your choice, create a file called `.gitignore` inside the root of your Git repository. 
Inside the text file, list the files and folders you would like to ignore, one per line. For example:

```
.ipynb_checkpoints/
.DS_Store
```

Save the file, and add and commit it with Git. 
Next time you go to use version control, 
Git will not bother you about the files you listed there, even if they have changed!

#### `.gitignore` tips and tricks

- append `**/` to the beginning of any file/folder names listed in the `.gitignore` file to have them ignored in subdirectories within the repo as well
- create a [global `.gitignore` file](https://help.github.com/articles/ignoring-files/#create-a-global-gitignore) so that you do not have to create the same `.gitignore` for all your homework repos


## Going back in time!

### Just going for a look:

The easiest way to go back in time in your version control repository is to use the GitHub.com website. To do this, we click the commits link:

<img src="img/releases.png" width=800>

Then we can view the history, along with the commit messages. To view the state of a repository at that time, we click on the "**<>**" button:

<img src="img/commits_eg.png" width=800>

### Travelling in time or bringing something something from the back from the past:

Sometimes you want to be able to explore and run the files from the past, or bring a past version of a file to the future. When we need to do either of those things, we should be working with Git in our local repository. 

Here's the same history as viewed above, but using the JupyterLab Git extension:

<img src="img/jupyter-git-history.png" width=800>

To see what was changed at a given point in history, click the down arrow associated with the commit. You can then diff the file (see what was changed for a particular file by clicking the file icon beside it.

<img src="img/jupyter-view-changes.png">

#### Travelling in time to the past

If you wanted to move your project's file and directories (so entire state) back to this point in time you can do that by clicking the clock icon. **NOTE: If you do this, be sure you pushed your changes, as it will discard anything more recent than this commit on your local computer (i.e., this is a hard reset).**

<img src="img/jupyter-hard-reset.png" width=500>

Again, because this is a hard reset, Git will warn you about the consequences:

<img src="img/jupyter-hard-reset-warning.png" width=500>

Once, you have done this, you will see the more recent commits in your history are GONE!

<img src="img/jupyter-after-hard-reset.png" width=500>

#### Exercise:

1. Clone [this GitHub repository](https://github.com/ttimbers/data_analysis_pipeline_eg) to your computer.

2. View the names of the files that were changed in commit `44c17be`, and the specific changes made to the file `doc/count_report.Rmd`.

3. Do a hard reset to the state of the repository as it was in commit `44c17be`.

4. Then pull the Git remote repository to go back to where you started.

*Question - could you have gone back to where you started if the work was not stored in the remote repository?*


#### Bringing something something from the back from the past

There is not a nice and easy way (that I am aware of) of cherry-picking a version of single file from the past using the JupyterLab Git extension. To do this, I resort to the Git command line tool in the terminal. The general command is:

```
git checkout <HASH> <FILE>
```

For example, to checkout the version of the `doc/count_report.Rmd` from the commit whose hash starts with `5837143`, we would type: 

```
git checkout 5837143 doc/count_report.Rmd
```

That will bring that version of the `doc/count_report.Rmd` into our working directory. We can view it, run it or use it, et cetera. If we want to keep that version going forward for our project, we would have to then add and commit that version of the file to do so.

> ##### What Git tool to use?
>
> There are many many many different tools for using Git. We have so far discussed two in this class (the JupyterLab Git extension,
> and the Git command line). Others include GitHub Desktop, GitKraken, Source Tree, RStudio's Git GUI, and VSCode's Git GUI.
> Which one should you use? Anyone that fits you best! I recommend experimenting with a few and then settling in with the one
> that you find easiest to use. One note is that some commands are limited in some tools (e.g., the example above with the
> JupyterLab Git extension). If you hit that case in your favorite tool, you can use the Git command line tool to get around it
> and then go back to primarily using your tool of choice.

