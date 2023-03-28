import pandas as pd


def main():
    print('Extract training data')

    join_df_100 = pd.read_csv('join_results_larger_medium_datasets_data_sorted_merged.csv', header=0, sep=',')
    join_df_100 = join_df_100.loc[join_df_100['pbsm_multiplier'] == 100]
    join_df_100.to_csv('join_results_larger_medium_datasets_data_sorted_merged_100.csv', sep=',', index=None)

    join_df = pd.read_csv('join_results_larger_medium_datasets_training_data.csv', header=0, sep=',')
    features_df = pd.read_csv('larger_medium_datasets_features.csv', header=0, sep=',')
    features_df['filename'] = features_df['filename'].apply(lambda f: 'datasets/sjml/larger_medium_datasets/{}'.format(f))

    training_df = pd.merge(join_df, features_df, left_on='dataset1', right_on='filename')
    training_df = training_df.drop(columns=['filename'])
    training_df = pd.merge(training_df, features_df, left_on='dataset2', right_on='filename')
    training_df = training_df.drop(columns=['id', 'total_time', 'refinement_cost', 'result_size', 'filename'])

    training_df = pd.merge(training_df, join_df_100, left_on=['dataset1', 'dataset2'], right_on=['dataset1', 'dataset2'])
    training_df = training_df.drop(columns=['id', 'total_time', 'refinement_cost', 'result_size', 'mbr_tests_y'])

    training_df['pbsm_multiplier_best'] = training_df['pbsm_multiplier_x']
    training_df['mbr_tests_best'] = training_df['mbr_tests_x_x']
    training_df['pbsm_multiplier_100'] = training_df['pbsm_multiplier_y']
    training_df['mbr_tests_100'] = training_df['mbr_tests_x_y']

    training_df = training_df.drop(columns=['pbsm_multiplier_y', 'mbr_tests_x_y', 'pbsm_multiplier_x', 'mbr_tests_x_x'])

    training_df.to_csv('training_data_larger_medium_datasets.csv', sep=',', index=None)


if __name__ == '__main__':
    main()
