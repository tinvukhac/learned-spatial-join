def main():
    print('Extract log - Plane Sweep')
    log_file = 'plane_sweep_xy_logs'

    f = open('join_pairs_real_xy.csv')
    lines = f.readlines()

    i = 0
    for line in lines:
        i += 1
        data = line.strip().split(',')
        ds1, ds2 = data[0], data[1]

        log_file_x = '{}/x_{}_{}_{}.log'.format(log_file, i, ds1, ds2)
        log_file_x = '{}/y_{}_{}_{}.log'.format(log_file, i, ds1, ds2)


if __name__ == '__main__':
    main()
