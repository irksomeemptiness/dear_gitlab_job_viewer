import dearpygui.dearpygui as dpg
from services.windows_ops import define_main_window_position
from windows.gitlab_login_window import LoginWindow
from windows.main_window import MainWindow
from windows.option_window import OptionsWindow
from services.fonts_registration import font_registration
from windows.windows_initializer import WindowsInitializer


def main():
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()
    define_main_window_position()
    font_registration()

    windows_list: list = [LoginWindow,
                          MainWindow,
                          OptionsWindow,
                          ]
    WindowsInitializer.create_windows(windows_list)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
