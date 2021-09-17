from dearpygui.dearpygui import start_dearpygui, set_primary_window, show_documentation, setup_viewport, \
    set_viewport_title, set_viewport_pos, get_viewport_height, get_viewport_width
from dearpygui.demo import show_demo
import tkinter as tk

from windows.gitlab_connect_window import gitlab_login_window
from windows.main_window import create_main_window
from windows.option_window import create_option_window


def main():
    root = tk.Tk()
    windows_resolution_width, windows_resolution_height = root.winfo_screenwidth(), root.winfo_screenheight()
    setup_viewport()
    viewport_x, viewport_y = get_viewport_width(), get_viewport_height()
    set_viewport_title(title='Gitlab Jobs Viewer')
    set_viewport_pos([windows_resolution_width/2-viewport_x/2, windows_resolution_height/2-viewport_y/2])

    create_main_window()
    create_option_window()
    gitlab_login_window()
    set_primary_window('main', True)
    #show_documentation()
    #show_demo()
    start_dearpygui()


if __name__ == '__main__':
    main()

