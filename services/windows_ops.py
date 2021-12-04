import logging
import tkinter as tk
import dearpygui.dearpygui as dpg


def centralize_main_pos(window_size: list):
    main_x, main_y = dpg.get_viewport_client_width(), dpg.get_viewport_client_height()
    return int(main_x / 2 - window_size[0] / 2), int(main_y / 2 - window_size[1] / 2)


def update_log_box(gitlab_job, substring, lines_up, lines_down):
    logging.debug(f'Thread {gitlab_job.id} works')
    dpg.configure_item(f'{gitlab_job.id}_text', default_value='')
    dpg.add_loading_indicator(parent=gitlab_job.id, id=f'{gitlab_job.id}_auto_update_indicator', label='Loading')
    text = gitlab_job.filter(substring, lines_up, lines_down)
    dpg.configure_item(f'{gitlab_job.id}_text', default_value=text)
    dpg.delete_item(item=f'{gitlab_job.id}_auto_update_indicator')


def define_main_window_position():
    root = tk.Tk()
    windows_resolution_width, windows_resolution_height = root.winfo_screenwidth(), root.winfo_screenheight()
    dpg.setup_viewport()
    viewport_x, viewport_y = dpg.get_viewport_width(), dpg.get_viewport_height()
    dpg.set_viewport_title(title='Gitlab Jobs Viewer')
    dpg.set_viewport_pos(
        [windows_resolution_width / 2 - viewport_x / 2, windows_resolution_height / 2 - viewport_y / 2])
