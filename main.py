import sys
import json
import requests
from datetime import datetime
from include import filesystem, sql, config, cli


config = config.Config()
filesystem = filesystem.FileSystem(config.get_data())


def post():
    print('post')


def get(config_dict, endpoint):
    request = requests.get(endpoint)
    return request


def put():
    print('put')


def delete():
    print('delete')


def parse_verb(verb,
               config_dict,
               endpoint,
               params='',
               http='http',
               query=''):
    endpoint = create_endpoint(config_dict, endpoint, params, http, query)
    verb = verb.lower()
    if verb == 'get':
        return get(config_dict, endpoint), endpoint
    if verb == 'post':
        post()
    if verb == 'put':
        put()
    if verb == 'delete':
        delete()


def create_endpoint(config_dict, endpoint, params, http, query):
    return f"{http}://{config_dict['URI']}:{config_dict['PORT']}{endpoint}"


# program verb body=False auth=False URI
# bicep GET http/s://uri
# bicep POST key=value uri
# bicep PUT key=value uri
# bicep DELETE uri

def main():
    filesystem.create_file('test')
    # config_dict = config.get_data()
    # print(config_dict)
    # print(cli.init(sys.argv))
    """

    verb = sys.argv[1]
    endpoint = sys.argv[2]
    config_dict = config.get_data()
    request, uri = parse_verb(verb, config_dict, endpoint)
    # config.add_data('jrichardson12', 'localhost', '8000')
    # parse_args(sys.argv)
    # request = requests.get('http://localhost:8000')
    # print(get_data(request))
    # create_db()
    """

if __name__ == "__main__":
    main()
