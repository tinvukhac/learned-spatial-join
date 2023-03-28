import os
# import pandas as pd


def main():
    print('Execute batch SJ - XY')

    # df = pd.read_csv('join_pairs_real.csv', header=0, sep=',', encoding='utf8')
    # df['dataset1'] = df['dataset1'].apply(lambda x: x.replace('real/', ''))
    # df['dataset2'] = df['dataset2'].apply(lambda x: x.replace('real/', ''))
    # df = df[['dataset1', 'dataset2']].head(10)
    # df.to_csv('join_pairs_real_xy.csv', header=None, index=None, sep=',', encoding='utf8')

    log_file = 'plane_sweep_xy_logs'
    os.system('mkdir {}'.format(log_file))

    f = open('join_pairs_real_xy.csv')
    lines = f.readlines()

    i = 0
    for line in lines:
        i += 1
        data = line.strip().split(',')
        ds1, ds2 = data[0], data[1]

        # cmd1 = 'beast-0.9.5-RC2/bin/beast sj datasets/sjml/real_datasets/{} datasets/sjml/real_datasets/{} method:pbsm \'iformat:envelope(0,1,2,3)\' separator:, output:false &> {}/x_{}_{}_{}.log'.format(
        #     ds1, ds2, log_file, i, ds1, ds2)
        # print(cmd1)
        # os.system(cmd1)

        cmd2 = 'beast-0.9.5-RC2-y/bin/beast sj datasets/sjml/real_datasets/{} datasets/sjml/real_datasets/{} method:pbsm \'iformat:envelope(0,1,2,3)\' separator:, output:false &> {}/y_{}_{}_{}.log'.format(
            ds1, ds2, log_file, i, ds1, ds2)
        print(cmd2)
        os.system(cmd2)


if __name__ == '__main__':
    main()
