from dearpygui.dearpygui import get_value
import dearpygui.dearpygui as dpg
from classes.gitlab_job import Gitlab_job_object


def gitlab_log_window(name, sender, user_data):

    job = user_data()
    job_object = Gitlab_job_object(job=job)
    job_id = job_object.get_id()
    #job_full_log = job_object.parse_log_file()
    #job_full_log = job_object.filter(get_value(10))

    substring = get_value(10)
    lines_up = get_value(11)
    lines_down = get_value(12)
    #print(f'string {substring}')

    if lines_up == 0 and lines_down == 0:
        job_full_log = job_object.filter(substring)
    else:
        job_full_log = job_object.wide_filter(substring, lines_up, lines_down)
    # because i have no ideas how to find the particular object by ID.
    try:
        #dpg.configure_item(job_id, show=True)
        dpg.delete_item(item=job_id)
        create_log_window(job_id, job_full_log)
    except:
        create_log_window(job_id, job_full_log)


def create_log_window(job_id, job_full_log):
    window_label: str = f'Full log ID: {job_id}'
    with dpg.window(id=job_id, label=window_label, show=True, autosize=True, horizontal_scrollbar=True):
        dpg.add_text(job_full_log, label="Log", wrap=800)