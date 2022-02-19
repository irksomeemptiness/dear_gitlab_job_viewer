import logging

import dearpygui.dearpygui as dpg
from configuration import Config
from main_window_storage_class import MainWindowStorageClass
from windows.main_window import MainWindow
from windows_ops import centralize_main_pos


class OptionsWindow:
    @classmethod
    def create_window(cls):
        with dpg.window(tag="options_window", label="Options", on_close=cls.options_window_close_callback, show=False,
                        pos=centralize_main_pos([Config.options_window_height, Config.options_window_width])):
            #dpg.add_input_int(tag="option_gitlab_jobs_limit", width=100, default_value=MainWindowStorageClass.gitlab_jobs_per_page,
            #                  label="Gitlab jobs per a page")
            dpg.add_combo(tag="option_gitlab_scope", items=MainWindowStorageClass.gitlab_scopes, label='Choose scope')
            dpg.add_button(tag='option_save_button', callback=cls.save_options, label="Save changes")
            dpg.add_loading_indicator(tag='option_reload_load_indicator', label='Loading', show=False)

    @classmethod
    def options_window_close_callback(cls, sender, data):
        dpg.configure_item(item="options_window", show=False)

    @classmethod
    def save_options(cls):
        dpg.configure_item(item='option_save_button', enabled=False)
        dpg.configure_item(item='option_reload_load_indicator', show=True)

        MainWindowStorageClass.gitlab_selected_scope = dpg.get_value("option_gitlab_scope")
        logging.debug(f'{dpg.get_value("option_gitlab_scope")=}')
        logging.debug(f'{MainWindowStorageClass.gitlab_selected_scope=}')
        MainWindowStorageClass.number_of_jobs = len(
            MainWindowStorageClass.gitlab_connection.gitlab_get_jobs(get_all=True))

        dpg.configure_item(item='option_save_button', enabled=True)
        dpg.configure_item(item='option_reload_load_indicator', show=False)
        dpg.configure_item(item="options_window", show=False)
        MainWindow.reload_jobs()

