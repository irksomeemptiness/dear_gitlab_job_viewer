import dearpygui.dearpygui as dpg
from services.windows_ops import centralize_main_pos
from configuration import Config


def create_popup_window(text: str):
    window_pos = centralize_main_pos([getattr(Config, 'popup_window_width'),
                                      getattr(Config, 'popup_window_height')])
    print(f'window_pos {window_pos}')
    with dpg.window(id='modal_login_window', label='Error!', modal=True, pos=window_pos):
        dpg.add_text(text)
        #print(dpg.get_item_pos('login'))
        dpg.add_button(parent='modal_login_window', label="Close", callback=lambda: dpg.delete_item('modal_login_window'),
                       #pos=[getattr(Config, 'popup_window_width')/2, getattr(Config, 'popup_window_height')/2],
                       id='modal_button')
