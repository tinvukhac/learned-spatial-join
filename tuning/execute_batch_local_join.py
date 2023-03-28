import os


def main():
    print ('Execute batch local join')

    logs = 'local_join/logs_160'
    os.system('mkdir -p {}'.format(logs))

    f = open('potential_partitions.csv')

    line = f.readline()

    while line:
        data = line.strip().split()
        cmd = 'beast-0.9.5-RC2-y/bin/beast --jars beast-examples-0.9.5-RC2.jar --class edu.ucr.cs.bdlab.beastExamples.BenchmarkLocalPlaneSweep {} {} &> {}/{}.log'.format(data[1], data[2], logs, data[0])
        print (cmd)
        os.system(cmd)

        line = f.readline()


if __name__ == '__main__':
    main()
