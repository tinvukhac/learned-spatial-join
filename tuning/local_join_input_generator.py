import pandas as pd
from shapely.geometry import Polygon
import shapely.wkt


def intersection(geom1, geom2):
    return geom1.intersects(geom2)


def main():
    print('Local join in x and y axis')

    df1 = pd.read_csv('masters/roads_160.grid', header=0, sep='\t', encoding='utf-8')
    df2 = pd.read_csv('masters/linear_water_160.grid', header=0, sep='\t', encoding='utf-8')

    df1['geom'] = df1['Geometry'].apply(shapely.wkt.loads)
    df2['geom'] = df2['Geometry'].apply(shapely.wkt.loads)

    df1['File Name'] = df1['File Name'].apply(lambda x: 'local_join/roads_us_indexed_160_wkt/{}'.format(x))
    df2['File Name'] = df2['File Name'].apply(lambda x: 'local_join/linear_water_indexed_160_wkt/{}'.format(x))

    df1['key'] = '1'
    df2['key'] = '1'

    df3 = pd.merge(df1, df2, on='key').drop('key', 1)

    df3['intersection'] = df3.apply(lambda x: intersection(x['geom_x'], x['geom_y']), axis=1)

    df3 = df3.loc[df3['intersection']]

    df4 = df3[['File Name_x', 'File Name_y', 'geom_x', 'geom_y']]
    df4.insert(0, 'JoinID', range(len(df4)))

    df4.to_csv('potential_partitions.csv', sep='\t', encoding='utf8', index=None, header=None)


if __name__ == '__main__':
    main()
