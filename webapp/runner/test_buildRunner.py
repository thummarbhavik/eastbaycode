from rundocker import build_and_run_submit

def test_answer():
    protos = [
          {
              "name": "SayHello",
              "type": "string",
              "args": [{"name": "who", "type": "string"}]
          }]
    code = """def SayHello(who):
    return "hello " + who
        """
    job = {'code': code,
           'inputs':['"Hien"','"Paul"'],
           'prototype':protos[0]}
    output = {'outputs': [{'input': '"Hien"', 'answer': '"hello Hien"', 'stdout': '', 'stderr': 'ok'}, {'input': '"Paul"', 'answer': '"hello Paul"', 'stdout': '', 'stderr': 'ok'}], 'result': 'ok'}
    assert build_and_run_submit(job) == output
    assert 3==3
