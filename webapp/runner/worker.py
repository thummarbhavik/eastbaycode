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
    data = {'msg':result}
    r = requests.post(url = url, data = data, verify = False)
    print('Task Completed: ',r)
    #if result['result'] == 'compiler_error':
    #    print(result['error']['msg'])
    #    print(result['error']['text'])
    #    for i in range(result['error']['offset']-1):
    #        print(" ",end="")
    #    print("^")
