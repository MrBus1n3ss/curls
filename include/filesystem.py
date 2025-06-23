from pathlib import Path
from datetime import datetime


root_dir = Path.cwd()
data_dir = root_dir / 'data'


class File:
    def __init__(self, name, count, verb,  uri, user, last_call, project):
        self.name = name
        self.count = count
        self.verb = verb
        self.uri = uri
        self.user = user
        self.last_call = last_call
        self.project = project

    def get_data(self):
        project_dir = data_dir / self.project
        file = project_dir / self.name
        if Path.is_file(file):
            with open(file, 'r') as f:
                text = f.read()
                file_dict = {}
            for line in text.split('\n'):
                if len(line) > 0:
                    line = line.split('=')
                    file_dict[line[0]] = line[1]
        return file_dict

    def add_data(self, data):
        self.count = 0
        self.verb = data['verb']
        self.uri = data['uri']
        self.user = data['user']
        self.last_call = datetime.now()


class FileSystem:
    def __init__(self, config):
        self.config = config
        self.project = self.config['PROJECT']
        if not (Path(self.project).is_dir()):
            Path.mkdir(data_dir / self.project)
        self.project_dir = data_dir / self.project

    def create_file(self, name):
        file = self.project_dir / name
        if Path.is_file(file):
            Path.touch(file)
        # TODO: update the file

    def get_file(name):
        pass

    def delete_file():
        pass

    def list_files():
        pass
