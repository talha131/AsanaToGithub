from asana import asana
from optparse import OptionParser
from github import Github

def parse() :
    """Returns OptionParser instance to parse the command line parameters"""

    parser = OptionParser("usage: %prog [options] Asana-API-Key Github-username Github-password")
    parser.add_option("-w", "--workspace", dest="workspace", help="workspace which has the project you want to export to github. If none is specified a list of available workspaces is printed.")
    parser.add_option("-p", "--project", dest="project", help="project which has the items you want to export to github. If none is specified a list of available projects is printed.")
    parser.add_option("-r", "--repo", dest="repo", help="Github repository to whose issue tracker Asana tasks will be copied to. If none is specified a list of available repos is printed.")
    parser.add_option("-i", "--interactive", action="store_true", dest="interactive", default=False, help="request confirmation before attempting to copy task to Github")
    parser.add_option("--copy-completed-tasks", action="store_true", dest="copy_completed", default=False, help="completed Asana tasks are not copied. Use this switch to force copy of completed tasks.")
    parser.add_option("--dont-apply-tag", action="store_true", dest="apply_tag", default=False, help="every task copied to Github gets a tag copied-to-github at Asana. Use this switch to disable it.")
    parser.add_option("--dont-apply-label", action="store_true", dest="apply_label", default=False, help="every issue copied to Github gets a label copied-from-asana at Github. Use this switch to disable it.")
    parser.add_option("--dont-apply-project-label", action="store_true", dest="apply_project_label", default=False, help="Asana project is applied as label at Github to the copied task. Use this switch to disable it.")
    return parser

def print_workspaces(asana_api_object) :
    """Prints a list of available workspaces on stdout
    
    :Parameter:
        - `asana_api_object`: an instance of Asana
    """

    my_spaces = asana_api_object.list_workspaces()
    print "Following workspaces are available:"
    for item in my_spaces :
        print item['name']

def get_workspace_id(asana_api_object, workspace) :
    """Returns id of the workspace

    :Parameters:
        - `asana_api_object`: an instance of Asana
        - `workspace`: name or id of the workspace
    """

    my_spaces = asana_api_object.list_workspaces()
    w_id = None
    for item in my_spaces :
        if item['name'] == workspace or item['id'] == workspace :
            w_id = item['id']
            break
    return w_id

def print_projects(asana_api_object, workspace_id) :
    """Prints a list of available projects in the workspace on stdout
    
    :Parameters:
        - `asana_api_object`: an instance of Asana
        - `workspace_id`: id of the workspace whose projects are to be listed
    """

    my_projects = asana_api_object.list_projects(workspace_id)
    print "Following projects are available:"
    for item in my_projects :
        print item['name']

def get_project_id(asana_api_object, workspace_id, project) :
    """Returns id of the project 
    
    :Parameters:
        - `asana_api_object`: an instance of Asana
        - `workspace_id`: id of the workspace that has the project
        - `project`: name of id of the project
    """

    my_projects = asana_api_object.list_projects(workspace_id)
    p_id = None
    for item in my_projects :
        if item['name'] == project or item['id'] == project :
            p_id = item['id']
            break
    return p_id

def get_tasks(asana_api_object, project_id) :
    """Returns all the tasks present in the project
    
    :Parameters:
        - `asana_api_object`: an instance of Asana
        - `project_id`: id of the project whose tasks are to be fetched
    """

    return asana_api_object.get_project_tasks(project_id)

def get_project_id_from_asana(asana_api_object, options) :
    """Returns project id and handle cases when workspace or project is not specified at command line

    :Parameters:
        - `asana_api_object`: an instance of Asana
        - `options`: options parsed by OptionParser
    """

    project_id = None
    if not options.workspace :
        print_workspaces(asana_api_object)
    else :  
        workspace_id = get_workspace_id(asana_api_object, options.workspace)
        if not workspace_id :
            print "Workspace not found. Make sure you have entered correct workspace name."
        else :
            print "Workspace {} found".format(options.workspace)
            if not options.project :
                print_projects(asana_api_object, workspace_id)
            else :
                project_id = get_project_id(asana_api_object, workspace_id, options.project)
                if not project_id :
                    print "Project not found. Make sure you have entered correct project name."
                else :
                    print "Project {} found".format(options.project)
    return project_id

def print_repos(github_api_object) :
    """Prints a list of available repos on stdout
    
    :Parameter:
        - `github_api_object`: an instance of Github
    """

    my_repos = github_api_object.get_user().get_repos() 
    print "Following repositories are available:"
    for item in my_repos :
        print item.full_name

def get_repo(github_api_object, repo_full_name) :
    """Return an instance of repo
    
    :Parameters:
        - `github_api_object`: an instance of Github
        - `repo_full_name`: full name of the repo on Github, for example, talha131/try
    """

    my_repos = github_api_object.get_user().get_repos() 
    my_repo = None
    for item in my_repos :
        if item.full_name == repo_full_name :
            my_repo = item
            break
    return my_repo

def get_repo_from_github(github_api_object, options) :
    """Return an instance of repo and handle cases when repo is not specified or is invalid
    
    :Parameters:
        - `github_api_object`: an instance of Github
        - `options`: options parsed by OptionParser
    """

    my_repo = None
    if not options.repo :
        print_repos(github_api_object)
    else :
        my_repo = get_repo(github_api_object, options.repo)
        if not my_repo :
            print "Repository not found. Make sure you have entered complete repository name correctly."
        else :
            print "Repository {} found.".format(options.repo)
            if not my_repo.has_issues :
                print "Issues tracker is disabled for this repo. Make sure you have enabled it in the repository settings at Github."
                my_repo = None
            else :
                print "Issue tracker is enabled"
    return my_repo

def main() :
    parser = parse()
    (options, args) = parser.parse_args()

    if len(args) != 3 :
        if len(args) == 0  :
            parser.error("Asana API Key is required")
        if len(args) == 1 :
            parser.error("Github username is required")
        if len(args) == 2 :
            parser.error("Github password is required")
        exit(1)

    asana_api = asana.AsanaAPI(args[0], debug=True)  
    project_id = get_project_id_from_asana(asana_api, options)
    if not project_id :
        exit(1)

    github_api = Github(args[1], args[2])
    git_repo = get_repo_from_github(github_api, options)
    if not git_repo:
        exit(1)

    exit(0)

if __name__ == '__main__' :
    main()
