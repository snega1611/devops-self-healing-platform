from flask import Flask
import threading
import time

app = Flask(__name__)

memory_hog = []

@app.route("/")
def home():
    return {
        "project": "AI-Assisted Self-Healing Kubernetes Platform",
        "status": "running"
    }

@app.route("/health")
def health():
    return {
        "status": "Healthy"
    }

@app.route("/cpu-load")
def cpu_load():

    def burn_cpu():
        end_time = time.time() + 60

        while time.time() < end_time:
            x = 0
            for i in range(100000):
                x += i * i

    threading.Thread(target=burn_cpu).start()

    return {
        "message": "CPU load started for 60 seconds"
    }

@app.route("/memory-load")
def memory_load():

    global memory_hog

    memory_hog.append("A" * 10_000_000)

    return {
        "message": "Memory allocation increased"
    }
    
@app.route("/break-health")
def break_health():
    global health_status
    health_status = False
    return {"message": "Health check broken"}


health_status = True

@app.route("/health")
def health():

    if not health_status:
        return {"status": "failed"}, 500

    return {"status": "healthy"}

@app.route("/crash")
def crash():
    import os
    os._exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)