# ⚙️ Distributed Job Scheduler — Queue-Based Async Task Processing System

A lightweight distributed job scheduler built using Python and FastAPI, designed to process tasks asynchronously using a queue-based architecture with worker threads, retry mechanisms, and fault tolerance.

---

## 🚀 Features

* 🔹 Asynchronous job processing using worker threads
* 🔹 Queue-based architecture for decoupled task execution
* 🔹 Retry mechanism with configurable limits
* 🔹 Fault-tolerant design (handles failures gracefully)
* 🔹 Concurrent job execution using worker pool
* 🔹 Lightweight and easily extendable to distributed systems

---

## 🏗️ Tech Stack

* **Backend:** Python (FastAPI)
* **Queue:** In-memory queue (Queue module)
* **Concurrency:** Threading (worker pool)
* **Server:** Uvicorn

---

## 🧠 System Design Overview

* Clients submit jobs via REST API
* Jobs are pushed into a centralized queue
* Worker threads continuously poll the queue
* Each job is:

  * Processed asynchronously
  * Retried on failure (up to max retries)
* Decoupled architecture ensures scalability and fault isolation

---

## 📡 API Endpoints

### 🔹 Submit Job

POST `/submit`

**Request Body:**

```json id="8r4k7o"
{
  "task": "send_email"
}
```

**Response:**

```json id="4h3j9d"
{
  "status": "Job submitted",
  "job": {
    "task": "send_email"
  }
}
```

---

## ⚡ How It Works

1. Client sends a job request
2. Job is added to the queue
3. Worker thread picks up the job
4. Job execution simulated (can be extended to real tasks)
5. If failure occurs:

   * Job is retried up to 3 times
6. Logs track job lifecycle (processing, retry, success, failure)

---

## ⚡ Performance

* Handles concurrent job execution using worker pool
* Efficient asynchronous processing with minimal blocking
* Supports retry logic for improved reliability
* Tested locally with multiple queued jobs

---

## ▶️ Running Locally

### 1. Clone the repository

```bash id="z71x2a"
git clone https://github.com/anirudh2781998/job-scheduler.git
cd job-scheduler
```

### 2. Install dependencies

```bash id="o4r6cw"
pip install -r requirements.txt
```

### 3. Run the server

```bash id="0v7r8l"
uvicorn app:app --reload
```

Server will start at:

```id="e9q5sn"
http://localhost:8000
```

---

## 🧪 Testing the Scheduler

Submit a job using curl:

```bash id="h8k3pw"
curl -X POST http://localhost:8000/submit \
-H "Content-Type: application/json" \
-d '{"task":"process_data"}'
```

Check logs in terminal to observe:

* Job processing
* Retry attempts
* Success/failure states

---

## 📂 Project Structure

```id="k9d2mf"
job-scheduler/
│── app.py
│── worker.py
│── job_queue.py
│── requirements.txt
│── README.md
```

---

## 🔒 Future Improvements

* Redis / RabbitMQ for distributed queue
* Persistent job storage (PostgreSQL)
* Task prioritization (priority queue)
* Scheduled jobs (cron-like system)
* Monitoring dashboard (job status tracking)
* Horizontal scaling with multiple worker nodes

---

## 👨‍💻 Author

**Anirudh Pandey**

* GitHub: https://github.com/anirudh2781998
* Email: [pandeyanirudh92@gmail.com](mailto:pandeyanirudh92@gmail.com)

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub!
