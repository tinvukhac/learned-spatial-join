import glob
import pandas as pd


def read_tsv_dir(dir_path):
    glued_data = pd.DataFrame()
    for file_name in glob.glob(dir_path + '/*.csv'):
        x = pd.read_csv(file_name, sep='\t', usecols=range(4), header=None)
        glued_data = pd.concat([glued_data, x], axis=0)

    glued_data.columns = ['x1', 'y1', 'x2', 'y2']
    return glued_data


def main():
    print ('Extract features of single partitions')
    master_file = '../data/inputs/local_join_indexed_datasets/linear_water_indexed_160_wkt/linear_water_160.grid'
    converted_mbr_path = '../data/inputs/local_join_indexed_datasets/linear_water_indexed_160.converted'

    # Read the master file
    f = open(master_file)
    output_f = open('../data/inputs/local_join_indexed_datasets/linear_water_indexed_160_wkt/density.csv', 'w')
    output_f.writelines('ID\tavg_x\tavg_y\tavg_area\n')

    line = f.readline()
    line = f.readline()

    while line:
        data = line.split('\t')
        partition_id, partition_name = data[0], data[1]

        tsv_path = '{}/{}'.format(converted_mbr_path, partition_name)
        df = read_tsv_dir(tsv_path)
        print (partition_id)
        df['x'] = df.apply(lambda x: abs(x['x2'] - x['x1']), axis=1)
        df['y'] = df.apply(lambda x: abs(x['y2'] - x['y1']), axis=1)
        df['area'] = df.apply(lambda x: abs(x['x2'] - x['x1']) * abs(x['y2'] - x['y1']), axis=1)
        output_f.writelines('{}\t{}\t{}\t{}\n'.format(partition_id, df['x'].mean(), df['y'].mean(), df['area'].mean()))

        line = f.readline()

    output_f.close()
    f.close()


if __name__ == '__main__':
    main()
