from os import environ
import time
import dearpygui.dearpygui as dpg
from threading import Thread
from classes.gitlab_job import Gitlab_job_object
from services.windows_ops import update_log_box


class TimerRatioError(Exception):
    pass


class Auto_update_thread(Thread):
    threads = []

    def __init__(self, gitlab_job: Gitlab_job_object, timeout: int, substring: str, lines_up: int, lines_down: int):
        super().__init__()
        self.thread_id = gitlab_job.id
        self.gitlab_job = gitlab_job
        self.timeout = timeout
        self.substring = substring
        self.lines_up = lines_up
        self.lines_down = lines_down
        self.__stop = False
        self.__inner_timer_ratio: int = 100

    def run(self):
        if environ.get("DEBUG"):
            print(f'thread has been started {self.thread_id}')
        inner_piece_of_timeout = self.timeout/self.inner_timer_ratio
        inner_timer = 0
        while not self.__stop and dpg.get_value(f'{self.gitlab_job.id}_checkbox') and \
                dpg.get_item_configuration(self.gitlab_job.id)['show']:
            if inner_timer < self.timeout:
                time.sleep(inner_piece_of_timeout)
                inner_timer += inner_piece_of_timeout
            else:
                update_log_box(self.gitlab_job, self.substring, self.lines_up, self.lines_down)
                inner_timer = 0
        if environ.get("DEBUG"):
            print(f'thread has been finished {self.thread_id}')

    def stop_thread(self):
        if environ.get("DEBUG"):
            print(f'Signal has been sent to {self.thread_id} thread')
        self.__stop = True

    @property
    def inner_timer_ratio(self):
        return self.__inner_timer_ratio

    @inner_timer_ratio.setter
    def inner_timer_ratio(self, value: int):
        if isinstance(value, (int, float)) and 10 < value < 1000:
            self.__inner_timer_ratio = value
        else:
            raise TimerRatioError('Ratio must be between 10 and 1000')

    def __del__(self):
        if environ.get("DEBUG"):
            print(f'Thread {self.thread_id} has been closed')

    def __str__(self):
        return f'Thread id: {self.thread_id}, repeat time: {self.timeout}'

    def __repr__(self):
        return f'Thread id: {self.thread_id}'
