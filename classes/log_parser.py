from typing import List
import logging


class Gitlab_log_parser:
    def __init__(self, log_data: str):
        self.log_data = log_data

    def simple_filter(self, substring: str) -> str:
        total_matches: int = 0
        result_list: List[str] = []
        full_text = self.log_data.splitlines()
        for string in full_text:
            if substring in string:
                total_matches += 1
                result_list.append(string)
        if substring == '':
            final_string = '\n'.join(result_list)
        else:
            result_string = '\n'.join(result_list)
            final_string = f'TOTAL MATCHES: {total_matches}\n{result_string}'
        return final_string

    def wide_filter(self, substring: str, up: int, down: int) -> str:
        if up == 0 and down == 0:
            raise ValueError('Incorrect value of strings above and below.')
        result_string: str = ''
        total_matches: int = 0
        full_text = self.log_data.splitlines()
        logging.debug(f'Full text and length = {len(full_text)-1}')
        if not full_text:
            return 'No logs'
        for match_index, string in enumerate(full_text):
            if substring in string:
                total_matches += 1
                above_match: int = match_index - int(up)
                below_match: int = match_index + int(down)
                # Cut too long bellow index. There is a fix about the length of the list and index from which it starts
                if below_match >= len(full_text)-1:
                    below_match = len(full_text)-1
                logging.debug(f'match from: {above_match}, to: {below_match} string: {string}')
                result_string += (f'\n\n--------------------'
                                  f'\nMATCH: string index {match_index+1}'
                                  f'\n--------------------')
                # the loop collects strings above and below the exact match
                while above_match <= below_match:
                    if above_match == match_index:
                        result_string += (f'\n------------------------------------------------\n'
                                          f'-> {full_text[match_index]}'
                                          f'\n------------------------------------------------')
                    else:
                        logging.debug(full_text[above_match])
                        result_string += f'\n{full_text[above_match]}'
                    # we don't increase match for kind of situations where the message at the end of the file
                    # makes it looks nice and tidy :3
                    if above_match != len(full_text):
                        above_match += 1

        if result_string:
            final_string = f'TOTAL MATCHES: {total_matches}{result_string}'
            return final_string
        else:
            return 'No matches'
