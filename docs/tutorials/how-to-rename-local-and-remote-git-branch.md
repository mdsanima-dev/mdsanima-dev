# {octicon}`telescope;1em;sd-text-secondary` `HOW TO RENAME LOCAL AND REMOTE GIT BRANCH`

When you want rename local and remote Git branches you can do very easily using the `git branch -m`
command on you terminal.

This quick tutorial explains how to rename local and remote Git branches. You only need to push the
renamed local branch and delete the branch with the old name.

## RENAMING `GIT BRANCH`

First step is a switching to the local branch wchich you want to rename, type in the terminal:

```shell
git checkout <old-branch-name>
```

Next step is a rename the local branch, type in the terminal:

```shell
git branch -m <new-branch-name>
```

Push the local `<new-branch-name>` to the remote repository and reset the upstream branch by typing
in the terminal:

```shell
git push origin -u <new-branch-name>
```

When the new branch is on remote repository, go to `Settings` in Github or Azure repository and
change default branch to `main` then confirm the changes.

Finnaly you can delete the remote `<old-branch-name>` by typing in the termianl:

```shell
git push origin --delete <old-branch-name>
```

You have saccessfully renamed the local and remnote Git branch.
