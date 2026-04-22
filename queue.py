from queue import Queue

job_queue = Queue()

class Job:
    def __init__(self, data, retries=0):
        self.data = data
        self.retries = retries
        self.max_retries = 3

    def can_retry(self):
        return self.retries < self.max_retries

    def increment_retry(self):
        self.retries += 1