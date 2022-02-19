from dearpygui.dearpygui import get_value
import dearpygui.dearpygui as dpg
from windows.main_window import MainWindow
from services.windows_ops import centralize_main_pos
from configuration import Config


class LoginWindow:
    @classmethod
    def create1_window(cls):
        gitlab_private_token = getattr(Config, 'gitlab_private_token')
        gitlab_url = getattr(Config, 'gitlab_url')
        gitlab_project_id = getattr(Config, 'gitlab_project_id')

        login_pos_x, login_pos_y = centralize_main_pos([getattr(Config, 'login_window_width', 300),
                                                        getattr(Config, 'login_window_height', 200)])

        with dpg.window(tag='login', label="Login", show=True, autosize=True, no_collapse=True, no_close=True,
                        width=300, height=200, pos=[login_pos_x, login_pos_y]):
            dpg.add_text(tag="login_text", default_value="Please enter a gitlab, token")
            gitlab_link = dpg.add_input_text(label="Gitlab link", default_value=gitlab_url)
            rep_link = dpg.add_input_text(label="Project ID", default_value=gitlab_project_id)
            gitlab_token = dpg.add_input_text(label="Gitlab Token", password=True, default_value=gitlab_private_token)

            with dpg.group(horizontal=True):
                dpg.add_button(tag="login_button", label="Enter", callback=MainWindow.login_connection,
                               user_data={'gitlab_url': lambda a=gitlab_link: get_value(a),
                                          'repo_id': lambda a=rep_link: get_value(a),
                                          'token': lambda a=gitlab_token: get_value(a)}
                               )
                dpg.add_loading_indicator(tag='login_loading_indicator', show=False)
