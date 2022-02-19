import dearpygui.dearpygui as dpg
from configuration import Config
from services.find_thread import find_and_terminate_thread
from classes.gitlab_job import Gitlab_job_object
from classes.auto_update import Auto_update_thread


def gitlab_log_window(name, sender, user_data):
    job = user_data()
    job_object = Gitlab_job_object(job=job)
    job_id = job_object.id

    if dpg.does_item_exist(job_id):
        dpg.delete_item(item=job_id)
        create_log_window(job_id, job=job_object)
        dpg.add_loading_indicator(parent=job_id, tag=f'{job_id}_load_indicator', label='Loading')
    else:
        create_log_window(job_id, job=job_object)
        dpg.add_loading_indicator(parent=job_id, tag=f'{job_id}_load_indicator', label='Loading')

    substring: str = dpg.get_value("main_key_word")
    lines_up: int = dpg.get_value("main_strings_above")
    lines_down: int = dpg.get_value("main_strings_below")
    job_full_log = job_object.filter(substring, lines_up, lines_down)

    dpg.delete_item(item=f'{job_id}_load_indicator')
    dpg.add_text(job_full_log, tag=f'{job_id}_text', label="Log", wrap=800, parent=job_id)


def create_log_window(job_id, job):
    window_label: str = f'Full log ID: {job_id}'
    height = getattr(Config, 'log_window_height', 450)
    width = getattr(Config, 'log_window_width', 600)
    with dpg.window(tag=job_id, label=window_label, show=True, horizontal_scrollbar=True, height=height, width=width):
        dpg.add_checkbox(tag=f'{job_id}_checkbox', label="Auto update", parent=job_id, callback=checkbox_click_callback,
                         user_data={'job': job})
        dpg.add_same_line(parent=job_id)
        dpg.add_input_int(parent=job_id, tag=f'{job_id}_button', label="Timeout", width=100, default_value=5,
                          min_value=5, max_value=60)
        dpg.add_separator(parent=job_id)


def checkbox_click_callback(name, sender, user_data):
    timeout = dpg.get_value(f"{user_data['job'].id}_button")
    substring: str = dpg.get_value("main_key_word")
    lines_up: int = dpg.get_value("main_strings_above")
    lines_down: int = dpg.get_value("main_strings_below")

    if sender:
        auto_update_thread = Auto_update_thread(gitlab_job=user_data['job'], timeout=timeout, substring=substring,
                                                lines_up=lines_up, lines_down=lines_down)
        Auto_update_thread.threads.append(auto_update_thread)
        auto_update_thread.start()
    else:
        find_and_terminate_thread(user_data['job'].id)
