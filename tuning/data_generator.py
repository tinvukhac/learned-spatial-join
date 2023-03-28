
def main():
    print('Generate join pairs')

    f = open('join_pairs_pbsm_multiplier_larger_medium_datasets.csv', 'w')

    # bits = range(1, 11)
    # dias = range(1, 11)

    # bits = [1, 2]
    # dias = [1]

    pbsm_multipliers = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000, 100000]
    pbsm_multipliers = [1, 10, 100, 1000, 10000, 100000]
    pbsm_multipliers = [1]
    # pbsm_multipliers = [1, 2, 5, 10, 20, 35, 50, 75, 100, 125, 150, 200, 500]

    datasets = []

    distributions = ['bit', 'diagonal', 'gaussian', 'uniform', 'parcel']

    for d in distributions:
        for i in range(1, 11):
            bit_dataset = 'datasets/sjml/larger_medium_datasets/%s_%03d.csv' % (d, i)
            datasets.append(bit_dataset)

    # for b in bits:
    #     bit_dataset = 'datasets/sjml/bit_datasets/bit_00{}.csv'.format(b)
    #     datasets.append(bit_dataset)

    # for d in dias:
    #     dia_dataset = 'datasets/sjml/medium_datasets/diagonal_00{}.csv'.format(d)
    #     datasets.append(dia_dataset)

    print(datasets)
    count = 0
    for i in range(len(datasets)):
        for j in range(i + 1, len(datasets)):
            for p in pbsm_multipliers:
                count += 1
                print('{} - {}'.format(datasets[i], datasets[j]))
                f.writelines('{},{},{},{}\n'.format(count, datasets[i], datasets[j], p))

    f.close()


if __name__ == '__main__':
    main()