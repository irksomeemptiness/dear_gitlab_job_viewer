import gitlab


class Gitlab_job_object:
    def __init__(self, job: object):
        self.job = job

    def extract_raw_log(self):
        return self.job.trace()

    def get_id(self):
        return self.job.id

    def parse_log_file(self):
        raw_log = self.extract_raw_log()
        return raw_log.decode('utf-8')



