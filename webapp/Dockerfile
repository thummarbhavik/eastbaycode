FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt 
ENV NAME env
CMD ["python", "ebc.py"]
