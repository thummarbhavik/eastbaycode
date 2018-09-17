import docker
import redis
import time
import json

time.sleep(10)
def connection():
    conn = redis.Redis(host="eastbaycode_redis_1", port=6379, db=0)
    return conn

def build_and_run_submit(code, inputs):
    # create inputs and code files in docker2 directory
    with open('/code/docker2/input.json', 'w') as input:
        json.dump(inputs, input)
    with open('/code/docker2/sol.py', 'w') as program:
        program.write(code)

    client = docker.from_env()
    #handles=client.containers.run("ubuntu:latest","./bbt train sol.py input.json output.json")
    handles=client.images.build(path="/code/docker2",tag="latest")
    # print(handles)
    handles=client.containers.run("latest:latest")
    result = handles.decode('utf-8')
    # print(handles)
    #input("fdfgbbgfgb")
    return result

def get_a_job(qname):
    conn = connection()
    result = conn.lpop(qname)
    if result != None:
        result = result.decode('utf-8')
        return result

def send_result(qname, msg):
    conn = connection()
    conn.rpush(qname, msg)

while True:
    job = get_a_job(qname = "work")
    if job:
        job = json.loads(job) 
        result = build_and_run_submit(code=job['code'], inputs=job['inputs'])
        send_result(qname="result", msg=result)
    else:
        time.sleep(10)
        print("No jobs anymore")
