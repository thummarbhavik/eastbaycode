from rundocker import build_and_run_submit
from encode import Encoder
import json
import requests

# Runner method

def runner(job):
    print(job)
    print(job['code'])
    # CHeck Whether need to convert inot dict or not
    #job = dict(job)
    a = job['code']
    print(a)
    result = build_and_run_submit(job)
    print(result)
    url = 'https://eastbaycode_webapp_1:5000/runner_done'
    data = {'msg':result, 
            'sid':job['session_id']}
    #result = json.dumps(result)
    # here instead of passing result as a data, we are passing with json so that on it's resolving the problem when you have to transfer dictionary of dictionary. 
    r = requests.post(url = url, json = result, verify = False)
    print('Task Completed: ',r)
    #if result['result'] == 'compiler_error':
    #    print(result['error']['msg'])
    #    print(result['error']['text'])
    #    for i in range(result['error']['offset']-1):
    #        print(" ",end="")
    #    print("^")
