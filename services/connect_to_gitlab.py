import gitlab
import requests

from classes.gitlab_connector import GitlabProjectConnector


def gitlab_connection_wrapper(gitlab_link, gitlab_token, project_id):
    from classes.main_window_storage_class import MainWindowStorageClass
    try:
        gitlab_connector = GitlabProjectConnector(gitlab_link=gitlab_link, gitlab_token=gitlab_token, project_id=project_id)
        gitlab_connector.connect_to_project()
        MainWindowStorageClass.gitlab_connection = gitlab_connector

    except gitlab.exceptions.GitlabError as gitlab_exception:
        # The exception wrapper is really odd. I have to work with it in another way.
        if '404' in gitlab_exception.__str__():
            return {'success': False, 'status': {'code': 404, 'message': 'Project Not Found'}}
        if '401' in gitlab_exception.__str__():
            return {'success': False, 'status': {'code': 401, 'message': 'Incorrect token'}}
    except requests.exceptions.ConnectionError:
        return {'success': False, 'status': {'code': 503, 'message': 'Wrong URL'}}
    except Exception as e:
        return {'success': False, 'status': {'code': 500, 'message': f'Something went wrong {e}'}}
    return {'success': True, 'status': {'code': 200, 'message': 'ok'}}
