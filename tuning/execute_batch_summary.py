import os


def main():
    print('Batch summary')

    log_dir = 'larger_medium_datasets_filenames_summary'
    os.system('mkdir -p {}'.format(log_dir))

    input_f = open('larger_medium_datasets_filenames.csv')

    filenames = input_f.readlines()

    for filename in filenames:
        cmd = 'beast-0.9.4-SNAPSHOT/bin/beast summary datasets/sjml/larger_medium_datasets/{} \'iformat:envelope(0,1,2,3)\' separator:, &> {}/{}.log'.format(filename.strip(), log_dir, filename.strip())
        print(cmd)
        os.system(cmd)


if __name__ == '__main__':
    main()
