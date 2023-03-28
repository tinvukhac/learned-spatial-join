from os.path import exists


def get_result_size(lines):
    matched_lines = [line for line in lines if "Join result size is" in line]
    data = matched_lines[0].strip().split()

    return data[8]


def get_mbr_test(lines):
    matched_lines = [line for line in lines if "Total number of MBR tests" in line]
    data = matched_lines[0].strip().split()

    return data[10]


def get_refinement_cost(lines):
    matched_lines = [line for line in lines if "Total number of MBR tests" in line]
    data = matched_lines[0].strip().split()

    return data[17]


def get_total_time(lines):
    matched_lines = [line for line in lines if "The operation sj finished in" in line]
    data = matched_lines[0].strip().split()
    print(data)

    return data[9]


def get_split_time(lines):
    matched_lines = [line for line in lines if "GeometryQuadSplitter.splitRDD finished after" in line]
    data = matched_lines[0].strip().split()

    return data[7]


def run1():
    f = open('join_pairs_pbsm_multiplier_big_medium_bit2.csv')
    output_f = open('join_results_pbsm_multiplier_big_medium_bit.csv', 'w')

    output_f.writelines('ID,dataset1,dataset2,pbsm_multiplier,total_time,mbr_tests,refinement_cost,result_size\n')

    line = f.readline()

    while line:
        data = line.strip().split(',')
        query_id = data[0]
        print(query_id)
        log_f = open('pbsm_multiplier_logs_big_medium_bit/{}.log'.format(query_id))
        lines = log_f.readlines()

        result_size, mbr_tests, refinement_cost, total_time = get_result_size(lines), get_mbr_test(
            lines), get_refinement_cost(lines), get_total_time(lines)

        output_f.writelines(
            '{},{},{},{},{}\n'.format(line.strip(), total_time, mbr_tests, refinement_cost, result_size))

        line = f.readline()

    f.close()
    output_f.close()


def run2():
    output_f = open('join_results_quad_split_simplified.csv', 'w')

    log_dir = 'quad_split_logs_simplified'

    # datasets1 = ['TIGER2017_COUNTY.csv', 'TIGER2018_COUSUB.csv']
    # datasets1 = ['TIGER2017_COUNTY.csv']
    datasets1 = ['TIGER2017_COUNTY_simplified_0.001.csv',
                 'TIGER2017_COUNTY_simplified_1.0E-4.csv',
                 'TIGER2017_COUNTY_simplified_1.0E-5.csv',
                 'TIGER2017_COUNTY_simplified_5.0E-4.csv',
                 'TIGER2017_COUNTY_simplified_5.0E-5.csv',
                 'TIGER2018_COUSUB_simplified_0.001.csv',
                 'TIGER2018_COUSUB_simplified_1.0E-4.csv',
                 'TIGER2018_COUSUB_simplified_1.0E-5.csv',
                 'TIGER2018_COUSUB_simplified_5.0E-4.csv',
                 'TIGER2018_COUSUB_simplified_5.0E-5.csv']
    # datasets2 = ['part-{0:05d}.csv'.format(x) for x in range(1, 11)]
    datasets2 = ['Tweets.wkt']
    # datasets2 = ['TIGER2018_COUSUB.csv']

    output_f.writelines('dataset1,dataset2,quad_split1,quadsplitthreshold,total_time,mbr_tests,refinement_cost,result_size\n')

    for ds1 in datasets1:
        for ds2 in datasets2:
            quad_split1 = 'true'
            for quadsplitthreshold in ['10', '50', '100']:
                log_file = '{}/sj_{}_{}_{}_{}.log'.format(log_dir, ds1, ds2, quad_split1, quadsplitthreshold)
                log_f = open(log_file)
                lines = log_f.readlines()

                result_size, mbr_tests, refinement_cost, total_time = get_result_size(lines), get_mbr_test(
                    lines), get_refinement_cost(lines), get_total_time(lines)

                # output_f.writelines(
                #     '{},Tweets.wkt/{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time, mbr_tests, refinement_cost, result_size))
                output_f.writelines(
                    '{},{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time,
                                                                  mbr_tests, refinement_cost, result_size))

            quad_split1 = 'false'
            quadsplitthreshold = 1000
            log_file = '{}/sj_{}_{}_{}_{}.log'.format(log_dir, ds1, ds2, quad_split1, quadsplitthreshold)
            log_f = open(log_file)
            lines = log_f.readlines()

            result_size, mbr_tests, refinement_cost, total_time = get_result_size(lines), get_mbr_test(
                lines), get_refinement_cost(lines), get_total_time(lines)

            # output_f.writelines(
            #     '{},Tweets.wkt/{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time,
            #                                                   mbr_tests, refinement_cost, result_size))
            output_f.writelines(
                '{},{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time,
                                                              mbr_tests, refinement_cost, result_size))

    output_f.close()


def run3():
    output_f = open('join_results_quad_split_split_time_values.csv', 'w')

    log_dir = 'quad_split_logs_split_time'

    datasets1 = ['TIGER2017_COUNTY.csv', 'TIGER2018_COUSUB.csv']
    datasets2 = ['part-{0:05d}.csv'.format(x) for x in range(1, 11)]
    datasets2 = ['Tweets.wkt']

    output_f.writelines(
        'dataset1,dataset2,quad_split1,quadsplitthreshold,total_time,mbr_tests,refinement_cost,result_size,split_time\n')

    for ds1 in datasets1:
        for ds2 in datasets2:
            quad_split1 = 'true'
            for quadsplitthreshold in ['100', '500', '1000']:
                log_file = '{}/sj_{}_{}_{}_{}.log'.format(log_dir, ds1, ds2, quad_split1, quadsplitthreshold)
                log_f = open(log_file)
                lines = log_f.readlines()

                result_size, mbr_tests, refinement_cost, total_time, split_time = get_result_size(lines), get_mbr_test(
                    lines), get_refinement_cost(lines), get_total_time(lines), get_split_time(lines)

                # output_f.writelines(
                #     '{},Tweets.wkt/{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time, mbr_tests, refinement_cost, result_size))
                output_f.writelines(
                    '{},{},{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time,
                                                       mbr_tests, refinement_cost, result_size, split_time))

            quad_split1 = 'false'
            quadsplitthreshold = 1000
            split_time = 0
            log_file = '{}/sj_{}_{}_{}_{}.log'.format(log_dir, ds1, ds2, quad_split1, quadsplitthreshold)
            log_f = open(log_file)
            lines = log_f.readlines()

            result_size, mbr_tests, refinement_cost, total_time = get_result_size(lines), get_mbr_test(
                lines), get_refinement_cost(lines), get_total_time(lines)

            output_f.writelines(
                '{},{},{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quadsplitthreshold, total_time,
                                                              mbr_tests, refinement_cost, result_size, split_time))

    output_f.close()


def get_num_features(lines):
    matched_lines = [line for line in lines if '"num_features" :' in line]
    data = matched_lines[0].strip().split()
    return int(data[2].replace(',', ''))


def get_num_points(lines):
    matched_lines = [line for line in lines if '"num_points" :' in line]
    data = matched_lines[0].strip().split()
    return int(data[2].replace(',', ''))


def run4():
    print('Extract summary of datasets')

    output_f = open('datasets_summary.csv', 'w')
    output_f.writelines('dataset,num_features,num_points,avg_segments\n')

    datasets = ['TIGER2017_COUNTY_simplified_0.001.csv',
                'TIGER2017_COUNTY_simplified_1.0E-4.csv',
                'TIGER2017_COUNTY_simplified_1.0E-5.csv',
                'TIGER2017_COUNTY_simplified_5.0E-4.csv',
                'TIGER2017_COUNTY_simplified_5.0E-5.csv',
                'TIGER2018_COUSUB_simplified_0.001.csv',
                'TIGER2018_COUSUB_simplified_1.0E-4.csv',
                'TIGER2018_COUSUB_simplified_1.0E-5.csv',
                'TIGER2018_COUSUB_simplified_5.0E-4.csv',
                'TIGER2018_COUSUB_simplified_5.0E-5.csv']

    for d in datasets:
        log_file = 'summary/{}.summary'.format(d)
        f = open(log_file)
        lines = f.readlines()
        num_features, num_points = get_num_features(lines), get_num_points(lines)
        output_f.writelines('{},{},{},{}\n'.format(d, num_features, num_points, num_points / num_features))


    output_f.close()


def run5():
    output_f = open('join_results_quad_split_large_files_3.csv', 'w')

    log_dir = 'quad_split_logs_large_batch_3'

    output_f.writelines(
        'dataset1,dataset2,quad_split1,quad_split2,quadsplitthreshold,total_time,mbr_tests,refinement_cost,result_size\n')

    datasets = ['TIGER2017_COUNTY_large', 'TIGER2018_COUSUB_large']

    n = len(datasets)
    for i in range(n):
        for j in range(i + 1, n):
            ds1, ds2 = datasets[i], datasets[j]

            for quad_split1 in ['true', 'false']:
                for quad_split2 in ['true', 'false']:
                    if quad_split1 != 'false' or quad_split2 != 'false':
                        for quadsplitthreshold in ['100', '500', '1000']:
                            log_file = '{}/sj_{}_{}_{}_{}_{}.log'.format(log_dir, ds1, ds2, quad_split1, quad_split2,
                                                                      quadsplitthreshold)
                            log_f = open(log_file)
                            lines = log_f.readlines()

                            result_size, mbr_tests, refinement_cost, total_time = get_result_size(lines), get_mbr_test(
                                lines), get_refinement_cost(lines), get_total_time(lines)

                            output_f.writelines(
                                '{},{},{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quad_split2, quadsplitthreshold,
                                                                      total_time,
                                                                      mbr_tests, refinement_cost, result_size))
                    else:
                        quadsplitthreshold = 100
                        log_file = '{}/sj_{}_{}_{}_{}_{}.log'.format(log_dir, ds1, ds2, quad_split1, quad_split2,
                                                                     quadsplitthreshold)
                        log_f = open(log_file)
                        lines = log_f.readlines()

                        result_size, mbr_tests, refinement_cost, total_time = get_result_size(lines), get_mbr_test(
                            lines), get_refinement_cost(lines), get_total_time(lines)

                        output_f.writelines(
                            '{},{},{},{},{},{},{},{},{}\n'.format(ds1, ds2, quad_split1, quad_split2, quadsplitthreshold,
                                                                  total_time,
                                                                  mbr_tests, refinement_cost, result_size))

    output_f.close()


def run6():
    output_f = open('join_results_quad_split_local.csv', 'w')
    output_f.writelines('num_points,dataset,time\n')

    log_dir = 'quad_split_logs_local'
    datasets = ['TIGER2017_COUNTY_simplified_0.001.wkt',
                'TIGER2017_COUNTY_simplified_5.0E-4.wkt',
                'TIGER2017_COUNTY_simplified_1.0E-4.wkt',
                'TIGER2017_COUNTY_simplified_5.0E-5.wkt',
                'TIGER2017_COUNTY_simplified_1.0E-5.wkt']
    counts = [100, 200, 300]

    for count in counts:
        for dataset in datasets:
            log_file = '{}/sj_{}_{}.log'.format(log_dir, dataset, count)
            f = open(log_file)
            lines = f.readlines()
            matched_lines = [line for line in lines if 'durationAll' in line]
            data = matched_lines[0].strip().split('=')
            output_f.writelines('{},{},{}\n'.format(count, dataset, data[1].strip()))

    output_f.close()


def run7():
    print('Extract log - Plane Sweep')
    log_file = 'plane_sweep_xy_logs'

    output_f = open('join_results_real_xy.csv', 'w')
    output_f.writelines('dataset1,dataset2,time_x,time_y,mbr_tests_x,mbr_tests_y\n')

    f = open('join_pairs_real_xy.csv')
    lines = f.readlines()

    i = 0
    for line in lines:
        i += 1
        print((i))
        if i == 6:
            break
        data = line.strip().split(',')
        ds1, ds2 = data[0].strip(), data[1].strip()

        log_file_x = open('{}/x_{}_{}_{}.log'.format(log_file, i, ds1, ds2))
        lines_x = log_file_x.readlines()
        total_time_x, mbr_tests_x = get_total_time(lines_x), get_mbr_test(lines_x)

        log_file_y = open('{}/y_{}_{}_{}.log'.format(log_file, i, ds1, ds2))
        lines_y = log_file_y.readlines()
        total_time_y, mbr_tests_y = get_total_time(lines_y), get_mbr_test(lines_y)

        output_f.writelines('{},{},{},{},{},{}\n'.format(ds1, ds2, total_time_x, total_time_y, mbr_tests_x, mbr_tests_y))

    f.close()
    output_f.close()


def run8():
    print('Extract log - Plane Sweep')
    log_path = 'local_join/logs_160'

    output_f = open('join_results_local_xy.csv', 'w')
    output_f.writelines('dataset1,dataset2,plane_sweep_x,plane_sweep_y,result_size\n')

    f = open('potential_partitions.csv')

    line = f.readline()

    while line:
        data = line.strip().split()

        log_file = '{}/{}.log'.format(log_path, data[0])
        if exists(log_file):
            print (log_file)
            log_f = open(log_file)
            lines = log_f.readlines()
            matched_lines = [line for line in lines if 'PlaneSweepX' in line]
            log_data = matched_lines[0].strip().split(':')
            log_data = log_data[1].strip().split(',')
            duration_x, result_size = log_data[0], log_data[1]
            matched_lines = [line for line in lines if 'PlaneSweepY' in line]
            log_data = matched_lines[0].strip().split(':')
            log_data = log_data[1].strip().split(',')
            duration_y = log_data[0]

            output_f.writelines('{},{},{},{},{}\n'.format(data[1], data[2], duration_x, duration_y, result_size))

            log_f.close()

        line = f.readline()

    output_f.close()
    f.close()


def main():
    print('Extract log data')
    run8()


if __name__ == '__main__':
    main()
