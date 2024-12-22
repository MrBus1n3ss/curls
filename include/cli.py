# TODO: create a simple config file to point to project and user,
#       though it is just me
def create_config_file():
    pass


def cli_command(arg):
    if arg == 'config':
        print('update config file')
        return False  # TODO: This are temporary, will need better solution
    elif arg == 'list':
        print('list curl calls')
        return False
    else:
        print('do nothing')
        return False


def parse_args(args):
    try:
        cli_command(sys.argv[1])
    except IndexError:
        print("Show help menu")

