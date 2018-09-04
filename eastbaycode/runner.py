import subprocess
from subprocess import Popen, PIPE
import sys

def runcode(code, inputs):
    # create program.py but concat the stub.py the submission from user
    with open('program.py', 'w') as the_file:
        the_file.write(code)
        the_file.write("\n\n")
        with open('stub.py', 'r') as the_stub:
            line = the_stub.read()
            the_file.write(line)
    process = subprocess.run(['python3', 'program.py'],
                            input="ted\n".encode('utf-8'),
                            stdout=PIPE)

    output = process.stdout.decode('utf-8')

    print(output)
    return output
