from dearpygui.dearpygui import get_value
import dearpygui.dearpygui as dpg
from services.gitlab_connector import gitlab_connect_api
from services.windows_ops import centerlize_main_pos
from configuration import Config


def gitlab_login_window():
    gitlab_private_token = getattr(Config, 'gitlab_private_token')
    gitlab_url = getattr(Config, 'gitlab_url')
    gitlab_project_id = getattr(Config, 'gitlab_project_id')

    login_pos_x, login_pos_y = centerlize_main_pos([getattr(Config, 'login_window_width'),
                                                    getattr(Config, 'login_window_height')])

    with dpg.window(id='login', label="Login", show=True, autosize=True, no_collapse=True, no_close=True,
                    width=300, height=200, pos=[login_pos_x, login_pos_y]):
        dpg.add_text(id="login_text", default_value="Please enter a gitlab, token")
        gitlab_link = dpg.add_input_text(label="Gitlab link", default_value=gitlab_url)
        rep_link = dpg.add_input_text(label="Project ID", default_value=gitlab_project_id)
        gitlab_token = dpg.add_input_text(label="Gitlab Token", password=True, default_value=gitlab_private_token)

        dpg.add_button(id="login_button", label="Enter", callback=gitlab_connect_api,
                       user_data={'gitlab_url': lambda a=gitlab_link: get_value(a),
                                  'repo_id': lambda a=rep_link: get_value(a),
                                  'token': lambda a=gitlab_token: get_value(a)}
                       )