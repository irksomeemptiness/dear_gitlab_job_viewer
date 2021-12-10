import dearpygui.dearpygui as dpg
from dearpygui import demo

from services.windows_ops import define_main_window_position
from windows.gitlab_connect_window import gitlab_login_window
from windows.main_window import create_main_window
from windows.option_window import create_option_window
from services.fonts_registration import font_registration


def main():
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()
    #demo.show_demo()
    define_main_window_position()
    font_registration()
    create_main_window()
    create_option_window()
    gitlab_login_window()

    dpg.set_primary_window('main', True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
