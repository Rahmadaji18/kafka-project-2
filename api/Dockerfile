FROM python:3.8-slim
RUN pip install flask joblib
COPY api.py /api/api.py
WORKDIR /api
CMD ["python", "api.py"]
