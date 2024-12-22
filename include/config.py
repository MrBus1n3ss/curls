from pathlib import Path


class Config():
    def __init__(self):
        self.root_dir = Path.cwd()
        if not Path(self.root_dir / 'config.env').is_file():
            Path.touch(self.root_dir / 'config.env')

    def add_data(self, user, uri, port):  # TODO: will need to have an init
        if len(user) > 0 and len(uri) > 0 and len(port) > 0:
            with open(self.root_dir / 'config.env', 'w') as file:
                file.write(f'USER={user}\n')
                file.write(f'URI={uri}\n')
                file.write(f'PORT={port}\n')

    def get_data(self):
        with open(self.root_dir / 'config.env', 'r') as file:
            text = file.read()
        config_dict = {}
        for line in text.split('\n'):
            if len(line) > 0:
                line = line.split('=')
                config_dict[line[0]] = line[1]
        return config_dict

    def update_data(self, key, value):
        pass
