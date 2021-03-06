"""
File: skeleton.py
Application module to deal with flask application skeleton
"""
from modules.strings.app_initialization import *
from .utilities import Common
import os


class Skeleton:

    def __init__(self, app_name, path, **kwargs):
        self.app_name = Common.to_snake_case(app_name)
        self.path = path
        self.api = kwargs['api'] if 'api' in kwargs else False
        self.web = kwargs['web'] if 'web' in kwargs else False
        self.web_login = kwargs['web_login'] if 'web_login' in kwargs else False
        self.gitignore = kwargs['gitignore'] if 'gitignore' in kwargs else False
        self.readme = True
        self.requirements = True

    def create_app(self):

        def create_folders():
            os.mkdir(os.path.join(self.path, self.app_name))
            os.mkdir(os.path.join(self.path, self.app_name, "configuration"))
            os.mkdir(os.path.join(self.path, self.app_name, "src"))
            os.mkdir(os.path.join(self.path, self.app_name, "src", "models"))
            os.mkdir(os.path.join(self.path, self.app_name, "src", "controllers"))
            os.mkdir(os.path.join(self.path, self.app_name, "src", "utilities"))
            if self.web:
                os.mkdir(os.path.join(self.path, self.app_name, "src", "controllers", "web"))
                os.mkdir(os.path.join(self.path, self.app_name, "src", "views"))
                os.mkdir(os.path.join(self.path, self.app_name, "src", "views", "pages"))
                os.mkdir(os.path.join(self.path, self.app_name, "src", "views", "static"))
                os.mkdir(os.path.join(self.path, self.app_name, "src", "views", "static", "img"))
                os.mkdir(os.path.join(self.path, self.app_name, "src", "views", "static", "css"))
                os.mkdir(os.path.join(self.path, self.app_name, "src", "views", "static", "js"))
            if self.api:
                os.mkdir(os.path.join(self.path, self.app_name, "src", "controllers", "api"))

        def create_files():
            with open(os.path.join(self.path, self.app_name, self.app_name + ".py"), 'w') as f:
                f.write(init.format(self.app_name))
            with open(os.path.join(self.path, self.app_name, "configuration", "__init__.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "configuration", "development.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "configuration", "production.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "__init__.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "models", "__init__.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "controllers", "__init__.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "utilities", "__init__.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "utilities", "setup.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "utilities", "configuration.py"), 'w'): pass
            with open(os.path.join(self.path, self.app_name, "src", "utilities", "commons.py"), 'w'): pass

            if self.web:
                with open(os.path.join(self.path, self.app_name, "src", "controllers", "web", "__init__.py"), 'w'): pass
                with open(os.path.join(self.path, self.app_name, "src", "controllers", "web", "index.py"), 'w'): pass
                with open(os.path.join(self.path, self.app_name, "src", "views", "layout.html"), 'w'): pass
                with open(os.path.join(self.path, self.app_name, "src", "views", "pages", "index.html"), 'w'): pass

            if self.api:
                with open(os.path.join(self.path, self.app_name, "src", "controllers", "api", "__init__.py"), 'w'): pass
                with open(os.path.join(self.path, self.app_name, "src", "controllers", "api", "index.py"), 'w'): pass

            if self.readme:
                with open(os.path.join(self.path, self.app_name, "README.md"), 'w'): pass
            if self.gitignore:
                with open(os.path.join(self.path, self.app_name, ".gitignore"), 'w'): pass

        def fill_files():
            pass

        try:
            if os.path.exists(self.path):
                create_folders()
                create_files()
                fill_files()
            else:
                raise OSError("Path '{}' does not exist".format(self.path))
        except OSError as e:
            print("Failed to create Flask app in '{}'".format(self.path))
            print("Due to:", str(e))
        else:
            print("Successfully create Flask project:", self.app_name)
