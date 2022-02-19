import logging
import dearpygui.dearpygui as dpg
import requests

from configuration import Config
from classes.main_window_storage_class import MainWindowStorageClass
from services.connect_to_gitlab import gitlab_connection_wrapper
from windows.popup_window import create_popup_window
from windows.gitlab_log_window import gitlab_log_window


class MainWindow:
    @classmethod
    def create_window(cls):
        with dpg.window(tag='main', label="main"):
            with dpg.group(horizontal=True):
                dpg.add_input_text(tag='main_key_word', label="key", hint='Please enter a key word', width=200)
                dpg.add_input_int(tag='main_strings_above', label="Strings above", width=100)
                dpg.add_input_int(tag='main_strings_below', label="Strings below", width=100)
                dpg.add_button(tag='main_reload_jobs_button', label="Reload jobs", callback=cls.reload_jobs, enabled=False)
                dpg.add_loading_indicator(tag='main_reload_load_indicator', label='Loading', show=False)
                dpg.add_separator(parent='main')

            with dpg.menu_bar(parent='main'):
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="Options", callback=cls.open_options_window)
        dpg.set_primary_window('main', True)

    @classmethod
    def open_options_window(cls):
        dpg.configure_item(item="options_window", show=True)
        dpg.configure_item(item="option_gitlab_scope", default_value=MainWindowStorageClass.gitlab_selected_scope)

    @classmethod
    def put_jobs_on_main(cls):
        jobs = MainWindowStorageClass.gitlab_connection.gitlab_get_jobs(get_all=False,
                                                                        page=MainWindowStorageClass.current_page)

        dpg.configure_item(item='login', show=False)
        for job in jobs:
            dpg.add_group(tag=f"job_{job.id}_group", horizontal=True, parent='main')
            dpg.add_text(tag=f"job_{job.id}_textfield", default_value=f"{job.id} - {job.status}", parent=f"job_{job.id}_group")
            dpg.add_button(tag=f"job_{job.id}_button", parent=f"job_{job.id}_group", label="Open Log", callback=gitlab_log_window,
                           user_data=lambda a=job: a)
            MainWindowStorageClass.job_objects_list.append(f"job_{job.id}_textfield")
            MainWindowStorageClass.job_objects_list.append(f"job_{job.id}_button")
            MainWindowStorageClass.job_objects_list.append(f"job_{job.id}_group")

        # footer generator
        cls.create_jobs_footer()

    @classmethod
    def login_connection(cls, sender, app_data, user_data):
        logging.debug(f'{sender}, {app_data}')
        gitlab_link: str = user_data['gitlab_url']()
        project_id: int = user_data['repo_id']()
        gitlab_token: str = user_data['token']()
        popup_message: str = ''

        logging.debug(f'gitlab link {gitlab_link} token {gitlab_token} repo {project_id}')
        dpg.configure_item(item='login_button', enabled=False)
        dpg.configure_item(item='login_loading_indicator', show=True)
        connection_json = gitlab_connection_wrapper(gitlab_link, gitlab_token, project_id)
        if not connection_json['success']:
            if connection_json['status']['code'] == 404:
                popup_message = "Project Not Found"
            if connection_json['status']['code'] == 401:
                popup_message = "Incorrect token"
            if connection_json['status']['code'] == 503:
                popup_message = "Wrong URL. Please write correct url"
            if connection_json['status']['code'] == 500:
                popup_message = "Something went wrong"
            create_popup_window(text=popup_message)
            dpg.configure_item(item='login_loading_indicator', show=False)
            dpg.configure_item(item='login_button', enabled=True)
            return
        MainWindowStorageClass.number_of_jobs = len(
            MainWindowStorageClass.gitlab_connection.gitlab_get_jobs(get_all=True))
        dpg.configure_item(item='login_loading_indicator', show=False)
        dpg.configure_item(item='login_button', enabled=True)

        cls.put_jobs_on_main()
        dpg.configure_item(item='main_reload_jobs_button', enabled=True)

    @classmethod
    def clear_jobs_data_from_window(cls):
        for job_object in MainWindowStorageClass.job_objects_list:
            dpg.delete_item(str(job_object))
        MainWindowStorageClass.job_objects_list.clear()

    @classmethod
    def create_jobs_footer(cls):
        dpg.add_separator(parent='main', tag='main_footer_separator')
        footer_group = dpg.add_group(tag='main_footer_jobs_list', horizontal=True, parent='main')

        for i in range(1, round(MainWindowStorageClass.number_of_jobs / Config.gitlab_jobs_per_page)):
            dpg.add_button(tag=f'main_footer_{i}', label=f'{i}', parent=footer_group, callback=cls.__change_page_callback, user_data=i)
            MainWindowStorageClass.job_objects_list.append(f'main_footer_{i}')
        MainWindowStorageClass.job_objects_list.append(f"main_footer_jobs_list")
        MainWindowStorageClass.job_objects_list.append(f"main_footer_separator")

    @classmethod
    def reload_jobs(cls):
        dpg.configure_item(item='main_reload_jobs_button', enabled=False)
        dpg.configure_item(item='main_reload_load_indicator', show=True)
        cls.clear_jobs_data_from_window()
        try:
            cls.put_jobs_on_main()
        except requests.exceptions.ConnectionError:
            popup_message = "Connection Error"
            create_popup_window(text=popup_message)

        dpg.configure_item(item='main_reload_load_indicator', show=False)
        dpg.configure_item(item='main_reload_jobs_button', enabled=True)

    @classmethod
    def __change_page_callback(cls, sender, app_data, user_data):
        MainWindowStorageClass.current_page = user_data
        cls.reload_jobs()

