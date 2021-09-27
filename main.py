import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo
import tkinter as tk

from windows.gitlab_connect_window import gitlab_login_window
from windows.main_window import create_main_window
from windows.option_window import create_option_window
from services.fonts_registration import font_registration


def main():
    root = tk.Tk()
    windows_resolution_width, windows_resolution_height = root.winfo_screenwidth(), root.winfo_screenheight()
    dpg.setup_viewport()
    viewport_x, viewport_y = dpg.get_viewport_width(), dpg.get_viewport_height()
    dpg.set_viewport_title(title='Gitlab Jobs Viewer')
    dpg.set_viewport_pos([windows_resolution_width/2-viewport_x/2, windows_resolution_height/2-viewport_y/2])

    font_registration()
    create_main_window()
    create_option_window()
    gitlab_login_window()
    dpg.set_primary_window('main', True)
    #show_documentation()
    #show_demo()
    dpg.start_dearpygui()


if __name__ == '__main__':
    main()
