from dearpygui.dearpygui import start_dearpygui, set_primary_window, show_documentation
from dearpygui.demo import show_demo
from os import environ

from windows.gitlab_connect_window import gitlab_token_window
from windows.main_window import create_main_window
from windows.option_window import create_option_window


def main():
    WIDTH: int = 200
    HEIGH: int = 200

    if environ.get("DEBUG"):
        gitlab_private_token, gitlab_url, gitlab_project_id = environ.get("TOKEN"), environ.get("URL"), environ.get("ID")
    else:
        gitlab_private_token = gitlab_url = gitlab_project_id = ''

    create_main_window(width=WIDTH, height=HEIGH)
    create_option_window()
    gitlab_token_window(gitlab_private_token, gitlab_url, gitlab_project_id)
    set_primary_window(1, True)
    #show_documentation()
    #show_demo()
    start_dearpygui()


if __name__ == '__main__':
    main()

