from classes.gitlab_connector import GitlabProjectConnector


class MainWindowStorageClass:
    gitlab_connection: GitlabProjectConnector
    job_objects_list: list[str] = []
    current_page: int = 1
    number_of_jobs: int = 0
    gitlab_scopes = ('created', 'pending', 'running', 'failed', 'success', 'canceled', 'skipped', 'manual')
    gitlab_selected_scope = ''
