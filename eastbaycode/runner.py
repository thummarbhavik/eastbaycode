def runcode(code, inputs):
    # create program.py
    with open('program.py', 'w') as the_file:
        the_file.write(code)
        the_file.write("\n\n")
        with open('stub.py', 'r') as the_stub:
            line = the_stub.read()
            the_file.write(line)

    return "Your file"
