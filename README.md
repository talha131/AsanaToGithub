# Asana To Github

AsanaToGithub copies your tasks from an Asana project to your Github repository's issue tracker. It copies Asana task title, notes, comments and attachments to Github issues. It supports UTF-8 encoding. 

Asana task's title and note is created as Github issue. The comments and attachments of the task are added as a comment to the Github issue. AsanaToGithub supports linking the Asana task and Github issue together by means of adding links in the comments at both sites.

# How to Install

Use `pip` to install

```bash
pip install git+https://github.com/talha131/AsanaToGithub.git
```

Alternatively, you can download and install it manually.

```bash
git clone git://github.com/talha131/AsanaToGithub.git
cd AsanaToGithub
python setup.py install
```

# How to use

Once you have install AsanaToGithub it will be available as `asanatogithub` on your terminal. Three arguments are required to use AsanaToGithub.

1. Your Asana API key. Get your API key from [this link](http://app.asana.com/-/account_api)
1. Your Github user name. For example talha131
1. Your Github password.

To work as intended, AsanaToGithub needs your Asana workspace, Asana project and Github repository name. Following are the switches used to provide these arguments.

* `-w` Asana workspace name. This workspace should contain the project that has the tasks you want to copy to Github. If this isn't provided, AsanaToGithub prints a list of available workspaces of your Asana account.
* `-p` Asana project name. If this isn't provided, AsanaToGithub prints a list of available projects in your selected workspace.
* `-r` Github repository. You should give its full name, like `username/repo`. If this isn't provided, AsanaToGithub prints a list of available repositories. 

The Github repository should have issue tracker enabled. 

Here is an example,

```bash
asanatogithub Nmklki.Popsdsq1sdfff talha131 guess_my_pwd -w Personal -p Example -r talha131/AsanaToGithub
```

This will copy all items of "Example" project, which is in my "Personal" workspace to the issue tracker of AsanaToGithub repository. 

Use `--help` to see all the options.

```bash
asanatogithub --help
```

# Customizations

## Skip particular tasks from copy

AsanaToGithub batch processes all the tasks. But if you want to review each item before it is copied, you can use `-i`. This will force AsanaToGithub to print the task title and its URL with a yes/no prompt. Press `y` to copy it and `n` to skip it.

## Create a link between Gitub issue and Asana task

The body of the Github issue has the link to Asana item. Similarly, link of Github issue is appended as a comment to the task. If you don't want Asana to have the Github link use `--dont-update-story`.

## Copy completed items too

By default, AsanaToGithub only copies incomplete tasks from Asana. But you can force it to copy completed tasks too by using `--copy-completed-tasks`.

## Don't copy Asana comments and attachments to Github

Asana comments and attachments are called stories. Stories of the task are added as a comment to the Github issue. But you can override it with `--dont-copy-stories`.

## Labels and tag for the copied tasks

Each task that is copied to Github gets a new tag "copied-to-github". You can disable it with `--dont-apply-tag`.

Each issue created at Github from Asana, gets a label "copied-from-asana". Also the Asana project name is applied as label to the issue. You can disable these options with `--dont-apply-label` and `--dont-apply-project-label` respectively.
