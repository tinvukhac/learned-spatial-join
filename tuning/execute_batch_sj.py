import os


def main():
    print('Execute batch sj')

    os.system('mkdir -p pbsm_multiplier_logs_big_medium_bit')

    f = open('join_pairs_pbsm_multiplier_big_medium_bit.csv')

    line = f.readline()

    while line:
        data = line.strip().split(',')
        query_id, dataset1, dataset2, pbsm_multiplier = data[0], data[1], data[2], data[3]

        cmd = 'beast-0.9.4-SNAPSHOT/bin/beast sj {} {} method:pbsm pbsmmultiplier:{} \'iformat:envelope(0,1,2,3)\' sjworkload:160k separator:, output:false -overwrite &> pbsm_multiplier_logs_big_medium_bit/{}.log'.format(dataset1, dataset2, pbsm_multiplier, query_id)
        print(cmd)
        os.system(cmd)

        line = f.readline()


if __name__ == '__main__':
    main()
