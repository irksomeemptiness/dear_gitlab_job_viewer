from threading import Thread
from gitlab.v4.objects import ProjectJob
from classes.gitlab_job import Gitlab_job_object
import dearpygui.dearpygui as dpg
import time


class Auto_update_thread(Thread):
    def __init__(self, gitlab_job: Gitlab_job_object, timeout: int, substring: str, lines_up: int, lines_down: int):
        super().__init__()
        self.gitlab_job = gitlab_job
        self.timeout = timeout
        self.substring = substring
        self.lines_up = lines_up
        self.lines_down = lines_down

    def run(self):
        print(f'thread has been started {self.timeout}')
        while dpg.get_value(f'{self.gitlab_job.id}_checkbox'):
            a: int = 0
            while a < self.timeout:
                print(self.timeout, a)
                time.sleep(1)
                a += 1
            text = self.gitlab_job.filter(self.substring, self.lines_up, self.lines_down)
            dpg.configure_item(f'{self.gitlab_job.id}_text', default_value=text)

    def __del__(self):
        #super().__del__()
        print('thread has been closed')
