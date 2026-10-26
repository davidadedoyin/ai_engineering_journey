# Week 20: Deployment and monitoring

## Analogy

A model is only valuable when it can be served reliably. Deployment is like putting a service into production so real users can use it.

## Mon: why deployment matters

Deployment means moving an app from your laptop to a server or container environment where it can run continuously.

In AI work, deployment includes:
- creating an API service
- keeping the runtime environment stable
- exposing a health check
- monitoring usage and errors

## Tue: containers and Docker

A Dockerfile tells the system how to build an image.

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Docker makes your app easier to run consistently across machines.

## Wed: health checks and readiness

A health endpoint tells you whether the service is alive and ready to accept traffic.

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

This is a basic but important deployment check.

## Thu: logs and monitoring

Logs help you answer:
- Did the service start?
- Did a request fail?
- Is latency increasing?
- Are we seeing errors in production?

## Friday challenge

Create a small FastAPI service with a `/health` route and a `/metrics` route showing a simple count.

## Saturday project

Package the final app or a deployment-ready service in `projects/month11_deployment_ready_service/`.

## Did it stick? Repeat checklist

- I can explain what deployment means in practice.
- I can explain what Docker does for a service.
- I can describe why `/health` is important.
- I can explain why monitoring and logs matter after launch.
