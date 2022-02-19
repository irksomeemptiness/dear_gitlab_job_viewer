import logging
from os import environ


class Config:
    # Windows settings
    # login
    login_window_width = 300
    login_window_height = 200

    # Error popup
    popup_window_width = 200
    popup_window_height = 150

    # Log window
    log_window_width = 650
    log_window_height = 450

    # Options window
    options_window_width = 750
    options_window_height = 450

    if environ.get("DEBUG"):
        gitlab_private_token, gitlab_url, gitlab_project_id = environ.get("TOKEN"), environ.get("URL"), environ.get("ID")
        logging.basicConfig(level=logging.DEBUG)
    else:
        gitlab_private_token = gitlab_url = gitlab_project_id = ''
        logging.basicConfig(level=logging.WARN)

    content_folder = 'content/'
    gitlab_jobs_per_page = 25
