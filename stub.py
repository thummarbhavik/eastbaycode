def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    with open("output.txt", "w") as out_file:
        while True:
            try:
                line = next(lines)
                # s = stringToString(line);
                ret = sayHello(line)
                out = str(ret);
                print(out)
                out_file.write(out)
            except StopIteration:
                break

if __name__ == '__main__':
    main()
