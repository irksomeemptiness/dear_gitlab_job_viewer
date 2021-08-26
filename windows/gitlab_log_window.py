from dearpygui.dearpygui import get_value
import dearpygui.dearpygui as dpg
from classes.gitlab_job import Gitlab_job_object


def gitlab_log_window(name, sender, user_data):
    job = user_data()
    job_object = Gitlab_job_object(job=job)
    job_full_log = job_object.parse_log_file()
    job_id = job_object.get_id()
    # because i have no ideas how to find the particular object by ID.
    try:
        dpg.configure_item(job_id, show=True)
    except:
        window_label: str = f'Full log ID: {job_id}'
        with dpg.window(id=job_id, label=window_label, show=True, autosize=True):
            dpg.add_input_text(label="Log", multiline=True, default_value=job_full_log, tab_input=True, width=600,
                               height=600)
