from os import environ

import gitlab
import requests

from windows.popup_window import create_popup_window
from windows.main_window import successful_connection


def gitlab_connect_api(sender, app_data, user_data):
    print(sender, app_data)
    gitlab_link: str = user_data['gitlab_url']()
    project_id: int = user_data['repo_id']()
    gitlab_token: str = user_data['token']()

    if environ.get("DEBUG"):
        print(f'gitlab link {gitlab_link} token {gitlab_token} repo {project_id}')
    try:
        gl_connect = gitlab.Gitlab(gitlab_link, private_token=gitlab_token)
        gl_connect.auth()
        project = gl_connect.projects.get(project_id)
        jobs = project.jobs.list(all=True)
        successful_connection(jobs)
    except gitlab.exceptions.GitlabError as gitlab_exception:
        # The exception wrapper is really odd. I have to work with it in another way.
        if '404' in gitlab_exception.__str__():
            print(f'Project Not Found')
            create_popup_window(text="Project Not Found")
        if '401' in gitlab_exception.__str__():
            print(f'Unauthorized')
            create_popup_window(text="Incorrect token")
    except requests.exceptions.ConnectionError as exception:
        print(f'Wrong URL {exception}')
        create_popup_window(text="Wrong URL. Please write correct url.")
