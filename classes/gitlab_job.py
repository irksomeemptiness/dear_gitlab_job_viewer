from typing import Union
from gitlab.v4.objects import ProjectJob
from requests import exceptions
from classes.log_parser import Gitlab_log_parser


class Gitlab_job_object:
    def __init__(self, job: ProjectJob):
        self.__job = job

    def extract_raw_log(self) -> Union[str, bytes]:
        try:
            job_log = bytes(self.__job.trace())
        except exceptions.ConnectionError:
            return str('Error. Perhaps, it is a connection problem.')
        return job_log

    @property
    def id(self) -> int:
        return self.__job.id

    def parse_log_file(self) -> str:
        raw_log = self.extract_raw_log()
        if isinstance(raw_log, bytes):
            if not raw_log:
                return 'There are nothing.'
            return raw_log.decode('utf-8')
        elif isinstance(raw_log, str):
            return raw_log
        #return raw_log.decode('cp1251')

    def filter(self, substring: str, lines_up: int, lines_down: int) -> str:
        gitlab_log_parser = Gitlab_log_parser(self.parse_log_file())
        if lines_up == 0 and lines_down == 0:
            return gitlab_log_parser.simple_filter(substring)
        else:
            return gitlab_log_parser.wide_filter(substring, lines_up, lines_down)
