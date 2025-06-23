import sys


# TODO: create a simple config file to point to project and user,
#       though it is just me
def create_config_file():
    pass


def cli_command(arg):
    if arg == 'config':
        print('update config file')
    elif arg == 'list':
        print('list curl calls')
    elif arg == 'build':
        print('build')
    else:
        print('do nothing')

"""
def parse_args(args):
    try:
        cli_command(sys.argv[1])
    except IndexError:
        print("Show help menu")
"""


def check_verb(args_list):
    if 'get' in args_list:
        return True
    elif 'post' in args_list:
        return True
    elif 'put' in args_list:
        return True
    elif 'delete' in args_list:
        return True
    else:
        return False


def check_args(args_list):
    is_uri = False
    is_auth = False
    has_body = False
    for arg in args_list:
        if 'http' in arg:  # TODO: may want to validate
            is_uri = True
        elif '-a' in arg or '--auth' in arg:
            is_auth = True
        elif '-b' in arg or '--body' in arg:
            has_body = True
    return is_uri, is_auth, has_body


def lower_args(args_list):
    for i in range(0, len(args_list)):
        args_list[i] = args_list[i].lower()
    return args_list


def create_endpoint(args_list):
    pass



# program verb body=False auth=False URI
# bicep GET http/s://uri
# bicep POST key=value uri
# bicep PUT key=value uri
# bicep DELETE uri
def init(*args):
    cli_table = {'config': {'update': 'project', 'help': None},
                 'list': ['all', 'project', 'help'],
                 'build': ['help'],
                 'run': ['help'],
                 'help': None}
    args_list = lower_args(args[0])
    if not (len(args_list) > 1):
        print_help()
    is_verb = check_verb(args_list)
    is_uri, is_auth, has_body = check_args(args_list)
    # TODO: auth 
    print(is_verb, is_uri, is_auth, has_body)


def print_help():
    print('HELLLLLLPPPPP!!!!')
