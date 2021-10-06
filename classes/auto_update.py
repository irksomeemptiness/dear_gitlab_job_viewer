from threading import Thread
from classes.gitlab_job import Gitlab_job_object
from services.windows_ops import update_log_box


class Auto_update_thread(Thread):
    def __init__(self, gitlab_job: Gitlab_job_object, timeout: int, substring: str, lines_up: int, lines_down: int):
        super().__init__()
        self.thread_id = gitlab_job.id
        self.gitlab_job = gitlab_job
        self.timeout = timeout
        self.substring = substring
        self.lines_up = lines_up
        self.lines_down = lines_down

    def run(self):
        print(f'thread has been started {self.thread_id}')
        update_log_box(self.gitlab_job, self.timeout, self.substring, self.lines_up, self.lines_down)
        print(f'thread has been finished {self.thread_id}')

    def __del__(self):
        print(f'Thread {self.thread_id} has been closed')

    def __str__(self):
        return f'Thread id: {self.thread_id}, repeat time: {self.timeout}'

    def __repr__(self):
        return f'Thread id: {self.thread_id}'
