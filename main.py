from dearpygui.dearpygui import start_dearpygui, add_input_text, get_value, add_button, add_checkbox, window, \
    add_menu_item, menu, menu_bar, configure_item, set_primary_window, show_documentation
from dearpygui.demo import show_demo
from os import environ

from windows.gitlab_connect_window import gitlab_token_window
from windows.main_window import create_main_window
from windows.option_window import create_option_window


def main():
    WIDTH: int = 200
    HEIGH: int = 200

    create_main_window(width=WIDTH, height=HEIGH)
    create_option_window()
    gitlab_token_window(gitlab_private_token, gitlab_url, id)
    set_primary_window(1, True)
    # show_documentation()
    # show_demo()
    start_dearpygui()

    # core.start_dearpygui()


if __name__ == '__main__':
    if environ.get("DEBUG"):
        gitlab_private_token, gitlab_url, id = environ.get("TOKEN"), environ.get("URL"), environ.get("ID")
    else:
        gitlab_private_token, gitlab_url, id = '', '', ''
    main()

