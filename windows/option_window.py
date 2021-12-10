import logging

import dearpygui.dearpygui as dpg
from configuration import Config
from windows_ops import centralize_main_pos

OPTIONS = {}


def create_option_window():
    with dpg.window(tag="options_window", label="Options", on_close=options_window_close_callback, show=False,
                    pos=centralize_main_pos([Config.options_window_height, Config.options_window_width])):
        dpg.add_input_int(tag="option_gitlab_jobs_limit", width=100, default_value=Config.gitlab_jobs_per_page,
                          label="Gitlab jobs per a page")
        dpg.add_combo(tag="option_gitlab_scope", items=Config.gitlab_scopes, label='Choose scope')
        dpg.add_button(callback=save_options, label="Save changes")


def options_window_close_callback(sender, data):
    dpg.configure_item(item="options_window", show=False)


def save_options():
    Config.gitlab_jobs_per_page = dpg.get_value("option_gitlab_jobs_limit")
    Config.gitlab_selected_scope = dpg.get_value("option_gitlab_scope")
    logging.debug(f'{dpg.get_value("option_gitlab_jobs_limit")=}, {dpg.get_value("option_gitlab_scope")=}')
    dpg.configure_item(item="options_window", show=False)
