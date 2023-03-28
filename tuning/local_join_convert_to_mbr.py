import os


def main():
    print ('Convert wkt records to records of MBRs')

    # File paths
    master_file = 'local_join/roads_us_indexed_160_wkt/roads_160.grid'
    # master_file = 'data/inputs/local_join_indexed_datasets/roads_us_indexed_160_wkt/roads_160.grid'
    indexed_path = 'datasets/sjml/local_join/roads_us_indexed_160.wkt'
    converted_path = 'datasets/sjml/local_join/roads_us_indexed_160.converted'

    # Read the master file
    f = open(master_file)

    line = f.readline()
    line = f.readline()

    while line:
        data = line.split('\t')
        partition_name = data[1]
        print (partition_name)

        cmd = 'beast-0.9.5-RC2/bin/beast --master local[*] cat {}/{} {}/{} \'iformat:wkt(0)\' \'oformat:envelope(0,1,2,3)\' -overwrite'.format(indexed_path, partition_name, converted_path, partition_name)
        print (cmd)
        os.system(cmd)

        line = f.readline()

    f.close()


if __name__ == '__main__':
    main()
