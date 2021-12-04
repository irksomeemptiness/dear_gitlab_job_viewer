import unittest
from classes.log_parser import Gitlab_log_parser
from unit.responses import Responses


class TestLogParcer(unittest.TestCase):
    def test_simple_filter_without_substring(self):
        gitlab_log_input = 'WARNING: test123\nWARNING: test123\nERROR: test123\nERROR: test123\nERROR: test123'
        log_object = Gitlab_log_parser(log_data=gitlab_log_input)
        final_string = log_object.simple_filter(substring='')
        self.assertEqual(final_string, gitlab_log_input)

    def test_simple_filter_with_substring(self):
        gitlab_log_input = 'WARNING: test123\nWARNING: test123\nERROR: test123\nERROR: test123\nERROR: test123'
        log_object = Gitlab_log_parser(log_data=gitlab_log_input)
        final_string = log_object.simple_filter(substring='ERROR')
        expected = f'TOTAL MATCHES: 3\nERROR: test123\nERROR: test123\nERROR: test123'
        self.assertEqual(final_string, expected)

    def test_wide_filter_without_substring_up_and_down_zero(self):
        gitlab_log_input = 'WARNING: test123\nWARNING: test123\nERROR: test123\nERROR: test123\nERROR: test123'
        log_object = Gitlab_log_parser(log_data=gitlab_log_input)
        self.assertRaises(ValueError, log_object.wide_filter, substring='ERROR', up=0, down=0)

    def test_wide_filter_without_substring_up_and_down_1(self):
        gitlab_log_input = Responses.input1
        log_object = Gitlab_log_parser(log_data=gitlab_log_input)
        final_string = log_object.wide_filter(substring='ERROR', up=2, down=2)
        print(final_string)
        expected = Responses.response1
        self.assertEqual(final_string, expected)

    def test_wide_filter_without_substring_up_and_down_2(self):
        gitlab_log_input = Responses.input2
        log_object = Gitlab_log_parser(log_data=gitlab_log_input)
        final_string = log_object.wide_filter(substring='ERROR', up=2, down=2)
        print(final_string)
        expected = Responses.response2
        self.assertEqual(final_string, expected)


if __name__ == '__main__':
    unittest.main()
