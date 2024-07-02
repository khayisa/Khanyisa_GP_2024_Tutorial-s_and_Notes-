 # Introduction to the Git Series 
## What is Git  ?
Git is a  version control system that allows us to keep track of files and their changes
 ### Git init and hidden folder 
 *************************
 - We can download Git on the following website <https://git-scm.com/downloads>
 - open the file after downloading and install 
 - after installation we can verify is git is installed by opening our terminal and typing ` git --version `
 ### Writing Git commands on the terminal 
 **************************************************
 - To Create a Directory we use the follwing command 
  ` mkdir directoryOne directoryTwo directoryThree `

  - We now have to check the status of our git to know if the repository we created are on Git, we use the following command ` git status `

  - To track our folders using git we firt have to enter the directory we want to track using the following command `cd directoryOne` this will takes us into the director, we then type ` git init` to initialise the Git software thus making our Directory tracable in by git 

  - Now we initialise the git software using the following command `git init `

  ### Git commit and logs 
  ********************************************* 
  - Git commit statements also called check points, the whole idea behind commit statements is **Write**, **Add**, **Commit**
  1. Have to make a working Directory 
     - now that we have created or directory , we can the create files for our directory using the following commands ` echo > test1.txt  test2.txt `
     
  1. Run a command of ` git add `
     - now lets track the files we created, using the git add command ` git add test1.txt `
  1. Leading us to the staging area
     - because we have only tracked one file and not all the files we created we find ourselves in the <mark> Staging area</mark>

  1. Git commmit  
      - lets now look into commiting, the git commit command must always come with a message or rather a reason as to why we are commiting 
      we use the following command to commit ` git commit -m "add file one" ` 

1.  Repo state 
     - We use `git status` to check the status of our git 
     - Now we will add the second file we have created using the ` git add test2.txt ` command  and  type `git status ` to check if we are in the staging area 
     - Now we commit our second file ` git commit -m "add second file " `

1. Git log 
   - The ` git log` command is used to display the commit history of the repository , it shows a list of commits made in the repo 
   - The ` git log --online ` command gives a summary of the commit history in one line 

- Atomic commits 
   - Git follows a principle of atomic commits meaning, one commit does the one job 

-  Short Cut to adding and commiting at the same time 
     > git commit -am "updated file" 
   


### Git Internal working and configs 
******************************

##### Git Config 
1. Open Terminal
1. Set a Git username 
   > git config --global user.name  "Khanyisa Faith"
   

   >git config --global email.name "khanyisa@Pycentric.net" 
1. Documentation for git config is available [here](https://git-scm.com/docs/git-config)

##### Gitignore 
A `.gitignore` file is used in Git repositories to specify which files directories should be ignored by git 
1. lets create a gitignore file 
    > echo > .gitignore
    - the gitignore file allows us to place all the files we dont want git to keep track of 

2. we open the gitignore files and we type all the files we dont want git to keep track of 
     > .vscode 

3. we type in the terminal ` git status `  to check the files git keeps track of 
4. we type the command `git add.` and then `git commit`


### Git Branches 
***********************************
Git Branch is a pointer to a specific commit, it allows us to create an independent line of development within our own project.

- Master or Main branch is the default/primary branch  
    - We check for the master branch in our terminal using the following line of code 
    > git branch 
- Creating a new git branch 
   > git branch nav-bar
- Switching to the another branch 
   > git checkout bugfix/ git switch bugfix 
- we can verify if the pointer has switch by typing the ` git branch ` command
- commit before switching to another branch 
- go to .git folder and cheockout the HEAD file 

#### Merging the branches 
1. Ensure that you are on the master branch by typing ` git branch ` to check 
2. we use the command ` git merge bugfix` to merge the alternative branch with the main branch 

#### Deleting the Branch
- we use the folowing command to delete a branch 
> git branch -d bugfix

### Git diff and Git Stash
************************
#### Git Diff
 - The ` git diff --staged` command helps us review changes before committing them 
 - `---` represents the file before staging 
 - `+++` represents the file after staging 
 - we can also  ` git diff ` using the different id's we get from git log after we commit to see the difference or review the chnages made 

 ### Git stash
 - The ` git stash` command allows us to temporarily save change's made to our working directory before commiting them 
 - `git stash `  is essential for a team settting as it allows us to help each other fix bugs or assist one another without us having to commit the changes first 
 - when we type ` git stash`  followed by ` git switch bugfix `it allows us to switch branches in our working directory  
 - ` git stash pop` brings back the changes 
 - ` git stash apply` opens changes and keeps them in stash


 ### More Commands 
 ****************
 - `git checkout <Hash> ` Detach Head : new branch 
 - ` git switch main` (re-attach Head)
 - ` git checkout HEAD~2 ` look at 2 commits prior
 - ` git restore filename` gets back to last commit version

 ### Git Rebase
 ************************
 Git Rebase is an alternative to merging, clean up tool (cleans up commits )
 and it essential rewrites the commit history 
 - `git rebase master ` command is used to rewrite the the timeline 
 - <mark>Never Rebase the commits shared with other people</mark>

 ### GitHub
 **********************
 #### Creating a new repository
 >echo "# tutorial" >> README.md<br>
 git init<br>
git add README.md<br>
git commit -m "first commit"<br>
git branch -M main<br>
git remote add origin https://github.com/khayisa/tutorial.git<br>
git push -u origin main

#### Github Push 
> git remote add origin https://github.com/khayisa/tutorial.git <br>
git branch -M main<br>
git push -u origin main


### Open Source Contribution
******************
#### open source 
1. Talk 
1. Open an issue
1. get an issue assigned
1. work and add value
1. Make PR and iterate over it 
1. Have Patience 
1. Making PR os not a job gurantee 

#### Pull Request 
A pull request is a way to propose changes to a repository and request that they be reviewed or merged

- Steps on how to ake the pull request
  1. **Fork the repository** 
     - Enter the repository you want to contribute to on github 
     - click the "Fork" button, this will create a copy of the repository into your github account 
   1. **Clone the Forked Repository**
      - Open your terminal or cmd and clone your forked repository to you local machine using the following command 
      >git clone https://github.com/your-username/repository-name.git
      - enter the repository using the cd command 
      > cd repo-name
      - create and switch to new branch 
      >git checkout -b feature-branch-name
   1. **Make Changes**   
      - make changes and add to staging files 
      > git add
   1. **Commit changes** 
      > git commit -m "changes made " 
   1. **Push changes made**
      > git push origin feature-branch-name
   1. **Create the Pull Request**
       - Go to your forked repository on GitHub.
       - You should see a banner saying you've recently pushed a branch. Click the "Compare & pull request" button.
       - Fill in the details for your pull request:<br>
              - Title: A short, descriptive title for your changes.<br>
              - Description: A detailed explanation of what changes you made and why.
       - Choose the base repository and branch you want to merge into, typically main or master.
       - Click the "Create pull request" button.




   












  







 


  






 



