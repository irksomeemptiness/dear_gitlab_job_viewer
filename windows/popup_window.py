import logging

import dearpygui.dearpygui as dpg
from services.windows_ops import centralize_main_pos
from configuration import Config


def create_popup_window(text: str):
    window_pos = centralize_main_pos([getattr(Config, 'popup_window_width', 200),
                                      getattr(Config, 'popup_window_height', 150)])
    logging.debug(f'window_pos {window_pos}')
    with dpg.window(tag='modal_login_window', label='Error!', modal=True, pos=window_pos):
        dpg.add_text(text)
        dpg.add_button(parent='modal_login_window', label="Close", callback=lambda: dpg.delete_item('modal_login_window'),
                       #pos=[getattr(Config, 'popup_window_width')/2, getattr(Config, 'popup_window_height')/2],
                       tag='modal_button')
