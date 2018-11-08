import docker
import redis
import time
import json
import ast
from encode import *
from shutil import copyfile
import os


def connection():
    conn = redis.Redis(host="eastbaycode_redis_1", port=6379, db=0)
    return conn

def build_and_run_submit(job):
    # create inputs and code files in docker2 directory
    result = {}
    result['session_id'] = job['session_id']
    result['submission_id'] = job['submission_id']
    encoder = Encoder(job['prototype'])

    # compile the code
    try:
        code_obj = compile(job['code'], 'code', 'exec')
    # catch a syntax error
    except SyntaxError as e:
        # return the error
        result['result'] = "compiler_error"
        compile_result={}
        compile_result['msg']= e
        compile_result['text']=e.text.strip()
        compile_result['offset']=e.offset
        compile_result['lineno'] = e.lineno
        result['error'] = compile_result
        return result


    code = encoder.make_program(job)
    path_to_submission = os.path.dirname(os.path.abspath(__file__)) + '/docker2/submission.py'

    with open(path_to_submission, 'w') as program:
        program.write(code)
    path_to_encode =  os.path.dirname(os.path.abspath(__file__)) 
    copyfile(path_to_encode + '/encode.py', path_to_encode + '/docker2/encode.py')


    client = docker.from_env()
    #handles=client.containers.run("ubuntu:latest","./bbt train sol.py input.json output.json")

    path_to_docker2 =  os.path.dirname(os.path.abspath(__file__)) + '/docker2'
    handles=client.images.build(path=path_to_docker2,tag="latest")
    # print(handles)


    handles=client.containers.run("latest:latest", volumes = { "eastbaycode_output":{"bind": "/code/output", "mode": "rw"}})
    #outputs = handles.decode('utf-8')
    #print(outputs)
    with open(path_to_docker2 + '/output/output.txt') as f:
        outputs = json.load(f)
    if os.path.exists(path_to_docker2 + "/output.txt"):
        os.remove(path_to_docker2 + "/output.txt")
    #print('from bind',outputs)
    #outputs = ast.literal_eval(outputs)
    result['outputs'] = outputs
    outputs_last_index = len(outputs) - 1
    if len(outputs) != len(job['inputs']) or outputs[outputs_last_index]['stderr'] != 'ok':
        result['result'] = 'runtime_error'
        return result
    result['result'] = 'ok'
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

def main():
    while True:
        job = get_a_job(qname = "work")
        if job:
            job = json.loads(job)
            result = build_and_run_submit(job)
            send_result(qname="result", msg=result)
        else:
            time.sleep(10)
            print("No jobs anymore")


if __name__ == "__main__":
    main()
