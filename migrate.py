from asana import asana
from optparse import OptionParser
from github import Github

def parse() :
    """Returns OptionParser instance to parse the command line parameters"""

    parser = OptionParser("usage: %prog [options] Asana-API-Key Github-username Github-password")
    parser.add_option("-w", "--workspace", dest="workspace", help="workspace which has the project you want to export to github. If none is specified a list of available workspaces is printed.")
    parser.add_option("-p", "--project", dest="project", help="project which has the items you want to export to github. If none is specified a list of available projects is printed.")
    parser.add_option("-r", "--repo", dest="repo", help="Github repository to whose issue tracker Asana tasks will be moved to. If none is specified a list of available repos is printed.")
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
    """Finds id of the workspace

    :Parameter:
        - `asana_api_object`: an instance of Asana
        - `workspace`: name or id of the workspace

    :Returns:
        Returns the worksapce id or -1 in case workspace is not found
    """

    my_spaces = asana_api_object.list_workspaces()
    w_id = -1
    for item in my_spaces :
        if item['name'] == workspace or item['id'] == workspace :
            w_id = item['id']
            break
    return w_id

def print_projects(asana_api_object, workspace_id) :
    """Prints a list of available projects in the workspace on stdout
    
    :Parameter:
        - `asana_api_object`: an instance of Asana
        - `workspace_id`: id of the workspace whose projects are to be listed
    """

    my_projects = asana_api_object.list_projects(workspace_id)
    print "Following projects are available:"
    for item in my_projects :
        print item['name']

def get_project_id(asana_api_object, workspace_id, project) :
    """Finds id of the project 
    
    :Parameter:
        - `asana_api_object`: an instance of Asana
        - `workspace_id`: id of the workspace that has the project
        - `project`: name of id of the project
    
    :Returns:
        Returns the project id or -1 in case project is not found
    """

    my_projects = asana_api_object.list_projects(workspace_id)
    p_id = -1
    for item in my_projects :
        if item['name'] == project or item['id'] == project :
            p_id = item['id']
            break
    return p_id

def get_tasks(asana_api_object, project_id) :
    """Returns all the tasks present in the project
    
    :Parameter:
        - `asana_api_object`: an instance of Asana
        - `project_id`: id of the project whose tasks are to be fetched
    """

    return asana_api_object.get_project_tasks(project_id)

def get_project_id_from_asana(asana_api_object, options) :
    """Returns project id and handle cases when workspace or project is not specified at command line

    :Parameter:
        - `asana_api_object`: an instance of Asana
        - `options`: options parsed by OptionParser
    """

    if not options.workspace :
        print_workspaces(asana_api_object)
    else :  
        workspace_id = get_workspace_id(asana_api_object, options.workspace)
        if workspace_id < 0 :
            print "Workspace not found. Make sure you have entered correct workspace name."
            return
        else :
            print "Workspace {} found".format(options.workspace)

    if not options.project :
        print_projects(asana_api_object, workspace_id)
    else :
        project_id = get_project_id(asana_api_object, workspace_id, options.project)
        if project_id < 0 :
            print "Project not found. Make sure you have entered correct project name."
            return
        else :
            print "Project {} found".format(options.project)

    return project_id

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

    my_tasks = get_tasks(asana_api, project_id)
    print my_tasks

    return

if __name__ == '__main__' :
    main()
