import dearpygui.dearpygui as dpg
from windows.gitlab_log_window import gitlab_log_window


def create_main_window():
    with dpg.window(id='main', label="main"):
        dpg.add_input_text(id='main_key_word', label="key", hint='Please enter a key word', width=200)
        dpg.add_same_line()
        dpg.add_input_int(id='main_strings_above', label="Strings above", width=100)
        dpg.add_same_line()
        dpg.add_input_int(id='main_strings_below', label="Strings below",  width=100)
        dpg.add_separator(parent='main')

        with dpg.menu_bar(parent='main'):
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Options",
                                  callback=lambda: dpg.configure_item(2, show=True))
            with dpg.menu(label="Options"):
                dpg.add_menu_item(label="Bla",
                                  callback=lambda: dpg.configure_item(2, show=True))


def successful_connection(jobs):
    dpg.configure_item(item='login', show=False)
    for job in jobs:
        dpg.add_text(parent='main', default_value=f"{job.id} - {job.status}")
        dpg.add_same_line(parent='main')
        dpg.add_button(parent='main', label="Open Log", callback=gitlab_log_window, user_data=lambda a=job: a)
