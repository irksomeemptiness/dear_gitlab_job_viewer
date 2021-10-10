import time
import dearpygui.dearpygui as dpg


def centralize_main_pos(window_size: list):
    main_x, main_y = dpg.get_viewport_client_width(), dpg.get_viewport_client_height()
    return int(main_x / 2 - window_size[0] / 2), int(main_y / 2 - window_size[1] / 2)


def update_log_box(gitlab_job, substring, lines_up, lines_down):
    print(f'Thread {gitlab_job.id} works')
    dpg.configure_item(f'{gitlab_job.id}_text', default_value='')
    dpg.add_loading_indicator(parent=gitlab_job.id, id=f'{gitlab_job.id}_auto_update_indicator', label='Loading')
    text = gitlab_job.filter(substring, lines_up, lines_down)
    dpg.configure_item(f'{gitlab_job.id}_text', default_value=text)
    dpg.delete_item(item=f'{gitlab_job.id}_auto_update_indicator')
