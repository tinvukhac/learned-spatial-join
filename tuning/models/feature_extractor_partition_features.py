import pandas as pd


def main():
    print ('Extract feature for single input of local join')

    df1 = pd.read_csv('../data/inputs/local_join_indexed_datasets/linear_water_indexed_160_wkt/linear_water_160.grid', sep='\t', header=0)
    df2 = pd.read_csv('../data/inputs/local_join_indexed_datasets/linear_water_indexed_160_wkt/density.csv', sep='\t', header=0)
    df = pd.merge(df1, df2, on='ID')
    df.to_csv('../data/inputs/local_join_indexed_datasets/linear_water_indexed_160_wkt/linear_water_indexed_160_partition_features.tsv', sep='\t', header=True, index=None)

    df3 = pd.read_csv('../data/inputs/local_join_indexed_datasets/roads_us_indexed_160_wkt/roads_160.grid', sep='\t', header=0)
    df4 = pd.read_csv('../data/inputs/local_join_indexed_datasets/roads_us_indexed_160_wkt/density.csv', sep='\t', header=0)
    df = pd.merge(df3, df4, on='ID')
    df.to_csv('../data/inputs/local_join_indexed_datasets/roads_us_indexed_160_wkt/roads_us_indexed_160_partition_features.tsv', sep='\t', header=True, index=None)


if __name__ == '__main__':
    main()
