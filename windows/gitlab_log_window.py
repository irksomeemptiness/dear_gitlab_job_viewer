from dearpygui.dearpygui import get_value
import dearpygui.dearpygui as dpg
from classes.gitlab_job import Gitlab_job_object


def gitlab_log_window(name, sender, user_data):
    job = user_data()
    job_object = Gitlab_job_object(job=job)
    job_id = job_object.get_id()

    load_indicator_id = int(str('1'+f'{job_id}'))
    if dpg.does_item_exist(job_id):
        dpg.delete_item(item=job_id)
        create_log_window(job_id)
        dpg.add_loading_indicator(parent=job_id, id=load_indicator_id, label='Loading')
    else:
        create_log_window(job_id)
        dpg.add_loading_indicator(parent=job_id, id=load_indicator_id, label='Loading')

    substring = get_value(10)
    lines_up = get_value(11)
    lines_down = get_value(12)

    if lines_up == 0 and lines_down == 0:
        job_full_log = job_object.filter(substring)
    else:
        job_full_log = job_object.wide_filter(substring, lines_up, lines_down)

    dpg.delete_item(item=load_indicator_id)
    dpg.add_checkbox(label="Auto update", parent=job_id)
    dpg.add_text(job_full_log, label="Log", wrap=800, parent=job_id)


def create_log_window(job_id):
    window_label: str = f'Full log ID: {job_id}'
    with dpg.window(id=job_id, label=window_label, show=True, autosize=True, horizontal_scrollbar=True):
        pass
        #dpg.add_checkbox(label="Auto update", parent=job_id)
        #dpg.add_text('', label="Log", wrap=800)