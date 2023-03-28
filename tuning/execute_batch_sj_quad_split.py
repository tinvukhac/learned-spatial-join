import os


def run1():
    log_dir = 'quad_split_logs'
    os.system('mkdir -p {}'.format(log_dir))

    datasets = ['uniform_001',
                'uniform_002',
                'diagonal_001',
                'diagonal_002',
                'gaussian_001',
                'gaussian_002']

    datasets = ['TIGER2017_COUNTY_large', 'TIGER2018_COUSUB_large']

    n = len(datasets)
    for i in range(n):
        for j in range(i + 1, n):
            ds1, ds2 = datasets[i], datasets[j]

            for quad_split1 in ['true', 'false']:
                for quad_split2 in ['true', 'false']:
                    if quad_split1 != 'false' or quad_split2 != 'false':
                        for quadsplitthreshold in ['100', '500', '1000']:
                            cmd = 'beast-0.9.4-SNAPSHOT/bin/beast sj datasets/sjml/quad_split/{} datasets/sjml/quad_split/{} method:pbsm quadsplit1:{} quadsplit2:{} quadsplitthreshold:{} \'iformat:wkt(0)\' output:false -overwrite &> {}/sj_{}_{}_{}_{}_{}.log'.format(
                                ds1, ds2, quad_split1, quad_split2, quadsplitthreshold, log_dir, ds1, ds2, quad_split1,
                                quad_split2, quadsplitthreshold)

                            'iformat[0]:wkt(0) iformat[1]:wkt(0)'
                            print(cmd)
                            os.system(cmd)
                    else:
                        quadsplitthreshold = 100
                        cmd = 'beast-0.9.4-SNAPSHOT/bin/beast sj datasets/sjml/quad_split/{} datasets/sjml/quad_split/{} method:pbsm quadsplit1:{} quadsplit2:{} quadsplitthreshold:{} \'iformat:wkt(0)\' output:false -overwrite &> {}/sj_{}_{}_{}_{}_{}.log'.format(
                            ds1, ds2, quad_split1, quad_split2, quadsplitthreshold, log_dir, ds1, ds2, quad_split1,
                            quad_split2, quadsplitthreshold)

                        'iformat[0]:wkt(0) iformat[1]:wkt(0)'
                        print(cmd)
                        os.system(cmd)


def run2():
    log_dir = 'quad_split_logs'
    os.system('mkdir -p {}'.format(log_dir))

    datasets1_prefix = 'datasets/sjml/quad_split'
    datasets2_prefix = 'datasets/sjml/quad_split'
    # datasets2_prefix = 'datasets/sjml/quad_split'

    # datasets1 = ['TIGER2017_COUNTY.csv', 'TIGER2018_COUSUB.csv']
    # datasets1 = ['TIGER2017_COUNTY.csv']
    datasets1 = ['TIGER2017_COUNTY_large']
    # datasets1 = ['TIGER2017_COUNTY_simplified_0.001.csv',
    #              'TIGER2017_COUNTY_simplified_1.0E-4.csv',
    #              'TIGER2017_COUNTY_simplified_1.0E-5.csv',
    #              'TIGER2017_COUNTY_simplified_5.0E-4.csv',
    #              'TIGER2017_COUNTY_simplified_5.0E-5.csv',
    #              'TIGER2018_COUSUB_simplified_0.001.csv',
    #              'TIGER2018_COUSUB_simplified_1.0E-4.csv',
    #              'TIGER2018_COUSUB_simplified_1.0E-5.csv',
    #              'TIGER2018_COUSUB_simplified_5.0E-4.csv',
    #              'TIGER2018_COUSUB_simplified_5.0E-5.csv']
    # datasets2 = ['part-{0:05d}.csv'.format(x) for x in range(1, 11)]
    # datasets2 = ['Tweets.wkt']
    datasets2 = ['TIGER2018_COUSUB_large']
    # datasets2 = ['part-{0:05d}.csv'.format(x) for x in range(1, 3)]

    for ds1 in datasets1:
        for ds2 in datasets2:
            quad_split1 = 'true'
            for quadsplitthreshold in ['10', '50', '100']: # for quadsplitthreshold in ['100', '500', '1000']:
                cmd = 'beast-0.9.4-SNAPSHOT/bin/beast sj {}/{} {}/{} \'iformat[0]:wkt(0)\' \'iformat[1]:wkt(0)\' method:pbsm pbsmmultiplier:1000 quadsplit1:{} quadsplit2:false quadsplitthreshold:{} output:false &> {}/sj_{}_{}_{}_{}.log'.format(
                    datasets1_prefix, ds1, datasets2_prefix, ds2, quad_split1, quadsplitthreshold, log_dir, ds1, ds2,
                    quad_split1, quadsplitthreshold)
                print(cmd)
                os.system(cmd)

            quad_split1 = 'false'
            quadsplitthreshold = 1000
            cmd = 'beast-0.9.4-SNAPSHOT/bin/beast sj {}/{} {}/{} \'iformat[0]:wkt(0)\' \'iformat[1]:wkt(0)\' method:pbsm pbsmmultiplier:1000 quadsplit1:{} quadsplit2:false quadsplitthreshold:{} output:false &> {}/sj_{}_{}_{}_{}.log'.format(
                datasets1_prefix, ds1, datasets2_prefix, ds2, quad_split1, quadsplitthreshold, log_dir, ds1, ds2,
                quad_split1, quadsplitthreshold)
            print(cmd)
            os.system(cmd)


def run3():
    log_dir = 'quad_split_logs_local'
    os.system('mkdir -p {}'.format(log_dir))

    datasets = ['TIGER2017_COUNTY_simplified_0.001.wkt',
                'TIGER2017_COUNTY_simplified_5.0E-4.wkt',
                'TIGER2017_COUNTY_simplified_1.0E-4.wkt',
                'TIGER2017_COUNTY_simplified_5.0E-5.wkt',
                'TIGER2017_COUNTY_simplified_1.0E-5.wkt']

    counts = [100, 200, 300]

    for count in counts:
        for dataset in datasets:
            cmd = 'beast-0.9.4-SNAPSHOT/bin/beast --jars beast-examples-0.9.4-SNAPSHOT.jar --class edu.ucr.cs.bdlab.beastExamples.Benchmark quad_split/simplified/{} {} &> {}/sj_{}_{}.log'.format(dataset, count, log_dir, dataset, count)
            print(cmd)
            os.system(cmd)


def main():
    print('Batch SJ')
    run3()


if __name__ == '__main__':
    main()
