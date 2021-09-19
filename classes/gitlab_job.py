from os import environ
from dataclasses import dataclass


@dataclass(frozen=True)
class Gitlab_job:
    job: object

    def __str__(self):
        return f'{self.job.id} {self.job.status} {self.job.name} {self.job.duration}'


class Gitlab_job_object:
    def __init__(self, job: Gitlab_job):
        self.job = job

    def extract_raw_log(self):
        return self.job.trace()

    def get_id(self):
        return self.job.id

    def parse_log_file(self):
        raw_log = self.extract_raw_log()
        if not raw_log:
            return 'There are nothing.'
        return raw_log.decode('utf-8')
        #return raw_log.decode('cp1251')

    def filter(self, substring: str):
        result_string: str = ''
        full_text = self.parse_log_file().splitlines()
        for string in full_text:
            if substring in string:
                result_string += '\n' + string
        return result_string

    def wide_filter(self, substring: str, up: int, down: int):
        result_string: str = ''
        full_text = self.parse_log_file().splitlines()
        if not full_text:
            return 'No logs'
        if environ.get("DEBUG"):
            print(len(full_text))
        for match_index, string in enumerate(full_text):
            if substring in string:
                #print(match_index)
                above_match: int = match_index - int(up)
                below_match: int = match_index + int(down)
                result_string += f'\n\n---------------------\n MATCH: string index {match_index}\n---------------------'
                while above_match <= below_match:
                    if above_match == len(full_text):
                        return result_string
                    if above_match == match_index:
                        #result_string += '\n' + f'\033[2;31;43m {full_text[match_index]} \033[0;0m'
                        result_string += '\n________________________________________________\n' + \
                                         f'{full_text[match_index]}\n' \
                                         + '________________________________________________\n'
                        above_match += 1
                    result_string += '\n' + full_text[above_match]
                    above_match += 1

        if result_string:
            return result_string
        else:
            return 'No matches'
