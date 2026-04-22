import time
import random
import threading
from queue import Empty
from queue import Queue
from queue import Job  # import from your queue.py

def worker(job_queue: Queue):
    while True:
        try:
            job = job_queue.get(timeout=1)

            print(f"[WORKER] Processing job: {job.data}")
            time.sleep(2)

            # simulate failure randomly
            if random.choice([True, False]):
                raise Exception("Random failure")

            print(f"[SUCCESS] Completed job: {job.data}")

        except Empty:
            continue

        except Exception as e:
            print(f"[ERROR] {e} | Job: {job.data}")

            if job.can_retry():
                job.increment_retry()
                print(f"[RETRY] Retrying job ({job.retries})")
                job_queue.put(job)
            else:
                print(f"[FAILED] Job permanently failed: {job.data}")

        finally:
            job_queue.task_done()


def start_worker(job_queue: Queue, num_workers=2):
    for _ in range(num_workers):
        thread = threading.Thread(target=worker, args=(job_queue,), daemon=True)
        thread.start()