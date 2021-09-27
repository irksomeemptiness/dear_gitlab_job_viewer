from os import environ
from gitlab.v4.objects import ProjectJob
import dearpygui.dearpygui as dpg


class Gitlab_job_object:
    def __init__(self, job: ProjectJob):
        self.__job = job

    def extract_raw_log(self) -> bytes:
        return bytes(self.__job.trace())

    @property
    def id(self) -> int:
        return self.__job.id

    def parse_log_file(self) -> str:
        raw_log: bytes = self.extract_raw_log()
        if not raw_log:
            return 'There are nothing.'
        return raw_log.decode('utf-8')
        #return raw_log.decode('cp1251')

    def filter(self, substring: str, lines_up: int, lines_down: int) -> str:
        if lines_up == 0 and lines_down == 0:
            result_string: str = ''
            full_text = self.parse_log_file().splitlines()
            for string in full_text:
                if substring in string:
                    result_string += f'\n{string}'
            final_string = '\n'.join((f'TOTAL MATCHES: {len(result_string)}', result_string))
            return final_string
        else:
            return self.__wide_filter(substring, lines_up, lines_down)

    def __wide_filter(self, substring: str, up: int, down: int) -> str:
        result_string: str = ''
        total_matches: int = 0
        full_text = self.parse_log_file().splitlines()
        if not full_text:
            return 'No logs'
        if environ.get("DEBUG"):
            print(len(full_text))
        for match_index, string in enumerate(full_text):
            if substring in string:
                total_matches += 1
                above_match: int = match_index - int(up)
                below_match: int = match_index + int(down)
                result_string += f'\n\n---------------------\n MATCH: string index {match_index}\n---------------------'
                while above_match <= below_match:
                    if above_match == len(full_text):
                        final_string = '\n'.join((f'TOTAL MATCHES: {total_matches}', result_string))
                        return final_string
                    if above_match == match_index:
                        #result_string += '\n' + f'\033[2;31;43m {full_text[match_index]} \033[0;0m'
                        result_string += f'\n________________________________________________\n' \
                                         f'{full_text[match_index]}' \
                                         f'\n ________________________________________________\n'
                        above_match += 1
                    result_string += f'\n{full_text[above_match]}'
                    above_match += 1

        print(f'total_matches - {total_matches}')
        if result_string:
            final_string = '\n'.join((f'TOTAL MATCHES: {total_matches}', result_string))
            return final_string
        else:
            return 'No matches'
