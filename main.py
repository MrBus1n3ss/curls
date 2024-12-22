import sys
import requests
from include import db, sql, config


db = db.DB_Connect()
config = config.Config()


def post():
    print('post')


def get(config_dict, endpoint='/', params='', is_https=False, query=''):
    http = 'http'
    if len(params) > 0:
        print('do stuff')
    if len(query) > 0:
        print('do stuff')
    if is_https:
        http = 'https'
    endpoint = f"{http}://{config_dict['URI']}:{config_dict['PORT']}{endpoint}"
    request = requests.get(f"{http}://{config_dict['URI']}:{config_dict['PORT']}{endpoint}")
    return endpoint, request


def put():
    print('put')


def delete():
    print('delete')


def parse_verb(verb):
    verb = verb.lower()
    if verb == 'get':
        get()
    if verb == 'post':
        post()
    if verb == 'put':
        put()
    if verb == 'delete':
        delete()


def main():
    verb = sys.argv[1]
    endpoint = sys.argv[2]
    sql.init_config(db.cursor)
    config_dict = config.get_data()
    get(config_dict)
    # config.add_data('jrichardson12', 'localhost', '8000')
    # parse_args(sys.argv)
    # request = requests.get('http://localhost:8000')
    # print(get_data(request))
    # create_db()


if __name__ == "__main__":
    main()
