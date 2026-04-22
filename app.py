from fastapi import FastAPI
from queue import job_queue, Job
from worker import start_worker

app = FastAPI()

# start workers
start_worker(job_queue, num_workers=2)

@app.post("/submit")
def submit_job(data: dict):
    job = Job(data)
    job_queue.put(job)
    return {"status": "Job submitted", "job": data}