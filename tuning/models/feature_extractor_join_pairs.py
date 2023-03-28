import pandas as pd
import shapely.wkt


def compute_intersection_area(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    return intersection.area


def compute_intersection_percentage_1(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    return compute_intersection_area(Geometry1, Geometry2) / geom1.area


def compute_intersection_percentage_2(Geometry1, Geometry2):
    geom2 = shapely.wkt.loads(Geometry2)
    return compute_intersection_area(Geometry1, Geometry2) / geom2.area


def compute_intersection_percentage_1_x(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    intersection_x = intersection.bounds[2] - intersection.bounds[0]
    geom1_x = geom1.bounds[2] - geom1.bounds[0]
    return intersection_x / geom1_x


def compute_intersection_percentage_2_x(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    intersection_x = intersection.bounds[2] - intersection.bounds[0]
    geom2_x = geom2.bounds[2] - geom2.bounds[0]
    return intersection_x / geom2_x


def compute_intersection_percentage_1_y(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    intersection_y = intersection.bounds[3] - intersection.bounds[1]
    geom1_y = geom1.bounds[3] - geom1.bounds[1]
    return intersection_y / geom1_y


def compute_intersection_percentage_2_y(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    intersection_y = intersection.bounds[3] - intersection.bounds[1]
    geom2_y = geom2.bounds[3] - geom2.bounds[1]
    return intersection_y / geom2_y


def compute_jaccard_similarity(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    union = geom1.union(geom2)
    return intersection.area / union.area


def compute_jaccard_similarity_x(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    union = geom1.union(geom2)
    intersection_x = intersection.bounds[2] - intersection.bounds[0]
    union_x = union.bounds[2] - union.bounds[0]
    return intersection_x / union_x


def compute_jaccard_similarity_y(Geometry1, Geometry2):
    geom1 = shapely.wkt.loads(Geometry1)
    geom2 = shapely.wkt.loads(Geometry2)
    intersection = geom1.intersection(geom2)
    union = geom1.union(geom2)
    intersection_y = intersection.bounds[3] - intersection.bounds[1]
    union_y = union.bounds[3] - union.bounds[1]
    return intersection_y / union_y


def main():
    print ('Extract join pair features')

    df1 = pd.read_csv('../data/inputs/local_join_indexed_datasets/roads_us_indexed_160_wkt/roads_us_indexed_160_partition_features.tsv', sep='\t', header=0)
    df1['dataset1'] = df1['File Name'].apply(lambda x: 'local_join/roads_us_indexed_160_wkt/{}'.format(x))
    df1.drop(['ID', 'File Name', 'NonEmpty Count', 'NumPoints', 'Sum_x', 'Sum_y'], axis=1, inplace=True)
    df2 = pd.read_csv('../data/inputs/local_join_indexed_datasets/linear_water_indexed_160_wkt/linear_water_indexed_160_partition_features.tsv', sep='\t', header=0)
    df2['dataset2'] = df2['File Name'].apply(lambda x: 'local_join/linear_water_indexed_160_wkt/{}'.format(x))
    df2.drop(['ID', 'File Name', 'NonEmpty Count', 'NumPoints', 'Sum_x', 'Sum_y'], axis=1, inplace=True)
    df_join_pairs = pd.read_csv('../data/outputs/join_results_local_xy.csv', sep=',', header=0)

    df = pd.merge(df_join_pairs, df1, on='dataset1')
    df = pd.merge(df, df2, on='dataset2')
    df['intersection_area'] = df.apply(lambda x: compute_intersection_area(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['intersection_percentage_1'] = df.apply(lambda x: compute_intersection_percentage_1(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['intersection_percentage_2'] = df.apply(lambda x: compute_intersection_percentage_2(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['intersection_percentage_1_x'] = df.apply(lambda x: compute_intersection_percentage_1_x(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['intersection_percentage_2_x'] = df.apply(lambda x: compute_intersection_percentage_2_x(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['intersection_percentage_1_y'] = df.apply(lambda x: compute_intersection_percentage_1_y(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['intersection_percentage_2_y'] = df.apply(lambda x: compute_intersection_percentage_2_y(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['jaccard_similarity'] = df.apply(lambda x: compute_jaccard_similarity(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['jaccard_similarity_x'] = df.apply(lambda x: compute_jaccard_similarity_x(x['Geometry_x'], x['Geometry_y']), axis=1)
    df['jaccard_similarity_y'] = df.apply(lambda x: compute_jaccard_similarity_y(x['Geometry_x'], x['Geometry_y']), axis=1)

    df['plane_x_is_better'] = df.apply(lambda x: 1 if float(x['plane_sweep_x']) < float(x['plane_sweep_y']) else 0, axis=1)

    df.drop(['Geometry_x', 'Geometry_y'], axis=1, inplace=True)

    df.to_csv('../data/outputs/join_results_local_xy_training_data.csv', sep='\t', header=True, index=None)
    print (df)


if __name__ == '__main__':
    main()
