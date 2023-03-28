import os


def main():
    print('Summary a list of files')

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
        cmd = 'beast-0.9.4-SNAPSHOT/bin/beast summary datasets/sjml/quad_split/{} \'iformat:wkt(0)\' &> quad_split/summary/{}.summary'.format(d, d)
        print(cmd)
        os.system(cmd)


if __name__ == '__main__':
    main()
