import dearpygui.dearpygui as dpg


def centralize_main_pos(window_size: list):
    main_x, main_y = dpg.get_viewport_client_width(), dpg.get_viewport_client_height()
    return int(main_x / 2 - window_size[0] / 2), int(main_y / 2 - window_size[1] / 2)
