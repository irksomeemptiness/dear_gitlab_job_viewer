from dearpygui.dearpygui import get_value
import dearpygui.dearpygui as dpg
from services.gitlab_connector import gitlab_connect_api


def gitlab_token_window(gitlab_private_token, gitlab_url, id):
    with dpg.window(id=3, label="Login", show=True, autosize=True, no_collapse=True, no_close=True):
        dpg.add_text(default_value="Please enter a gitlab, token")
        gitlab_link = dpg.add_input_text(label="Gitlab link", default_value=gitlab_url)
        rep_link = dpg.add_input_text(label="Project ID", default_value=id)
        gitlab_token = dpg.add_input_text(label="Gitlab Token", password=True, default_value=gitlab_private_token)
        dpg.add_checkbox(label="Save creds", default_value=False)
        dpg.add_button(label="Enter", callback=gitlab_connect_api,
                        user_data={'gitlab_url': lambda a=gitlab_link: get_value(a),
                                   'repo_id': lambda a=rep_link: get_value(a),
                                   'token': lambda a=gitlab_token: get_value(a)}
                       )
