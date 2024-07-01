 # Introduction to the Git Series 
## What is Git  ?
Git is a  version control system that allows us to keep track of files and their changes
 ### Git init and hidden folder 
 - We can download Git on the following website <https://git-scm.com/downloads>
 - open the file after downloading and install 
 - after installation we can verify is git is installed by opening our terminal and typing ` git --version `
 ### Writing Git commands on the terminal 
 - To Create a Directory we use the follwing command 
  ` mkdir directoryOne directoryTwo directoryThree `

  - We now have to check the status of our git to know if the repository we created are on Git, we use the following command ` git status `

  - To track our folders using git we firt have to enter the directory we want to track using the following command `cd directoryOne` this will takes us into the director, we then type ` git init` to initialise the Git software thus making our Directory tracable in by git 

  - Now we initialise the git software using the following command `git init `

  ### Git commit and logs  
  - Git commit statements also called check points, the whole idea behind commit statements is **Write**, **Add**, **Commit**
  1. Have to make a working Directory 
     - now that we have created or directory , we can the create files for our directory using the following commands ` touch test1.txt  test2.txt `
     
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
   


### Git Internal working and configs 

##### Git Config 
1. Open Terminal
1. Set a Git username 
   > git config --global user.name  "Khanyisa Faith"
   

   >git config --global email.name "khanyisa@Pycentric.net" 
1. Documentation for git config is available [here](https://git-scm.com/docs/git-config)

##### gitignore 
1. lets create a gitignore file 
    > touch .gitignore
    - the gitignore file allows us to place all the files we dont want git to keep track of 

2. we open the gitignore files and we type all the files we dont want git to keep track of 
     > .vscode 

3. we type in the terminal ` git status `  to check the files git keeps track of 
4. we type the command `git add.` and then `git commit`




   






 



