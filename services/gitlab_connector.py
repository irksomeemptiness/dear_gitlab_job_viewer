from os import environ

import gitlab
import requests
import dearpygui.dearpygui as dpg

from windows.popup_window import create_popup_window
from windows.main_window import successful_connection


def login_connection(sender, app_data, user_data):
    print(sender, app_data)
    gitlab_link: str = user_data['gitlab_url']()
    project_id: int = user_data['repo_id']()
    gitlab_token: str = user_data['token']()
    popup_message: str = ''

    if environ.get("DEBUG"):
        print(f'gitlab link {gitlab_link} token {gitlab_token} repo {project_id}')
    dpg.configure_item(item='login_loading_indicator', show=True)
    connection_json = gitlab_connection(gitlab_link, gitlab_token, project_id)
    if not connection_json['success']:
        if connection_json['status']['code'] == 404:
            popup_message = "Project Not Found"
        if connection_json['status']['code'] == 401:
            popup_message = "Incorrect token"
        if connection_json['status']['code'] == 503:
            popup_message = "Wrong URL. Please write correct url"
        #if connection_json['status']['code'] == 500:
        #    popup_message = "Something went wrong"
        create_popup_window(text=popup_message)
        dpg.configure_item(item='login_loading_indicator', show=False)
    dpg.configure_item(item='login_loading_indicator', show=False)


def gitlab_connection(gitlab_link, gitlab_token, project_id):
    try:
        gl_connect = gitlab.Gitlab(gitlab_link, private_token=gitlab_token)
        gl_connect.auth()
        project = gl_connect.projects.get(project_id)
        jobs = project.jobs.list(all=True)
        successful_connection(jobs)
    except gitlab.exceptions.GitlabError as gitlab_exception:
        # The exception wrapper is really odd. I have to work with it in another way.
        if '404' in gitlab_exception.__str__():
            return {'success': False, 'status': {'code': 404, 'message': 'Project Not Found'}}
        if '401' in gitlab_exception.__str__():
            return {'success': False, 'status': {'code': 401, 'message': 'Incorrect token'}}
    except requests.exceptions.ConnectionError:
        return {'success': False, 'status': {'code': 503, 'message': 'Wrong URL'}}
    except Exception:
        return {'success': False, 'status': {'code': 500, 'message': 'Something went wrong'}}
    return {'success': True, 'status': {'code': 200, 'message': 'ok'}}
