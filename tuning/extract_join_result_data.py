import sys


def main(args):
    print('Extract join result')
    input_f = open(args[0])
    output_f = open(args[1], 'w')

    line = input_f.readline()

    while line:
        if 'join-result' in line:
            output_f.writelines('{}\n'.format(line.strip()))

        line = input_f.readline()

    output_f.close()
    input_f.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
