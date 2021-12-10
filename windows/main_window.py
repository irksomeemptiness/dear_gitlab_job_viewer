import dearpygui.dearpygui as dpg

from configuration import Config
from windows.gitlab_log_window import gitlab_log_window


def create_main_window():
    with dpg.window(tag='main', label="main"):
        with dpg.group(horizontal=True):
            dpg.add_input_text(tag='main_key_word', label="key", hint='Please enter a key word', width=200)
            dpg.add_input_int(tag='main_strings_above', label="Strings above", width=100)
            dpg.add_input_int(tag='main_strings_below', label="Strings below",  width=100)
            dpg.add_separator(parent='main')

        with dpg.menu_bar(parent='main'):
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Options", callback=open_options_window)


def open_options_window():
    dpg.configure_item(item="options_window", show=True)
    dpg.configure_item(item="option_gitlab_scope", default_value=Config.gitlab_selected_scope)


def successful_connection(jobs):
    dpg.configure_item(item='login', show=False)
    for job in jobs:
        dpg.add_group(tag=f"{job.id}_group", horizontal=True, parent='main')
        dpg.add_text(tag=f"{job.id}_textfield", default_value=f"{job.id} - {job.status}", parent=f"{job.id}_group")
        dpg.add_button(tag=f"{job.id}_button", parent=f"{job.id}_group", label="Open Log", callback=gitlab_log_window,
                       user_data=lambda a=job: a)
