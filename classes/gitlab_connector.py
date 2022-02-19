from typing import Optional
import gitlab
from gitlab.v4.objects import Project
from configuration import Config


class GitlabProjectConnector:
    def __init__(self, gitlab_link: str, gitlab_token: str, project_id: int) -> None:
        self.gitlab_link = gitlab_link
        self.gitlab_token = gitlab_token
        self.project_id = project_id
        self._gitlab_project_connection: Optional[Project] = None

    def connect_to_project(self) -> Project:
        gl_connect = gitlab.Gitlab(self.gitlab_link, private_token=self.gitlab_token, per_page=Config.gitlab_jobs_per_page)
        gl_connect.auth()
        project = gl_connect.projects.get(self.project_id, lazy=True)
        self._gitlab_project_connection = project
        return self._gitlab_project_connection

    def gitlab_get_jobs(self, page: int = None, get_all: bool = True) -> list:
        from main_window_storage_class import MainWindowStorageClass
        if self._gitlab_project_connection == '':
            raise ConnectionError('There are no saved connection. Call connect_to_project() firstly.')
        if MainWindowStorageClass.gitlab_selected_scope:
            jobs = self._gitlab_project_connection.jobs.list(all=get_all, lazy=True, scope=MainWindowStorageClass.gitlab_selected_scope, page=page)
        else:
            jobs = self._gitlab_project_connection.jobs.list(all=get_all, lazy=True, page=page)
        return jobs

