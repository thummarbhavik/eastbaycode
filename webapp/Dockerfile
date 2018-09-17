FROM python:3.6-slim
WORKDIR /webapp
ADD . /webapp
RUN pip install --trusted-host pypi.python.org -r requirements.txt 
CMD ["./startup"]
