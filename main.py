import dearpygui.dearpygui as dpg
from services.windows_ops import define_main_window_position
from windows.gitlab_connect_window import gitlab_login_window
from windows.main_window import create_main_window
from windows.option_window import create_option_window
from services.fonts_registration import font_registration


def main():
    define_main_window_position()
    font_registration()
    create_main_window()
    create_option_window()
    gitlab_login_window()
    dpg.set_primary_window('main', True)
    dpg.start_dearpygui()


if __name__ == '__main__':
    main()
