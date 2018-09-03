import subprocess
from subprocess import Popen, PIPE
import sys

def runcode(code, inputs):
    # create program.py
    with open('program.py', 'w') as the_file:
        the_file.write(code)
        the_file.write("\n\n")
        with open('stub.py', 'r') as the_stub:
            line = the_stub.read()
            the_file.write(line)

    process = subprocess.run(['python3', 'program.py'], input="ted\n".encode('utf-8'),
            stdout=PIPE)
    # stdout, stderr = process.communicate(input="ted\n")
    #process.stdin.write("ted\n")
    #process.stdin.close()
    # while process.returncode is None:
    #     i = sys.stdin.read(1)
    #     if i == '':
    #         process.stdin.close()
    #         break
    #     process.stdin.write(i)
    #     process.poll()
    # while process.returncode is None:
    #     process.poll()
    output = process.stdout.decode('utf-8')
    print(output)
    return output
