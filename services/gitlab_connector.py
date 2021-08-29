from os import environ

import gitlab
from dearpygui.dearpygui import configure_item, add_text, add_button
from windows.gitlab_log_window import gitlab_log_window


def gitlab_connect_api(sender, data, user_data):
    gitlab_link: str = user_data['gitlab_url']()
    project_id: int = user_data['repo_id']()
    gitlab_token: str = user_data['token']()

    if environ.get("DEBUG"):
        print(f'gitlab link {gitlab_link} token {gitlab_token} repo {project_id}')

    gl_connect = gitlab.Gitlab(gitlab_link, private_token=gitlab_token)
    gl_connect.auth()
    project = gl_connect.projects.get(project_id)
    configure_item(item=3, show=False)
    jobs = project.jobs.list()

    # TODO: to move it somewhere
    # TODO: to group elements together
    for job in jobs:
        add_text(parent=1, default_value=f"{job.id} - {job.status}")
        add_button(parent=1, label="Open Log", callback=gitlab_log_window, user_data=lambda a=job: a)
