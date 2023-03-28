import pandas as pd


def extract_raw_data(input_file, output_file):
    f = open(input_file)
    output_f = open(output_file, 'w')

    line = f.readline()

    while line:
        data = line.strip().split(':')
        output_f.writelines('{}\n'.format(data[4]))

        line = f.readline()

    output_f.close()
    f.close()


def extract_sorted_data(input_file, output_file):
    df = pd.read_csv(input_file, names=['id', 'dataset1', 'dataset2', 'pbsm_multiplier', 'total_time', 'mbr_tests', 'refinement_cost', 'result_size'], sep=',')
    # print(df)
    min_df = df.groupby('id')['mbr_tests'].min()
    min_df.to_csv('join_results_larger_medium_datasets_data_sorted_min.csv', sep=',')

    join_df = pd.merge(df, min_df, on='id')
    join_df.to_csv('join_results_larger_medium_datasets_data_sorted_merged.csv', index=None, sep=',')

    min_multiplier_df = join_df.loc[join_df['mbr_tests_x'] == join_df['mbr_tests_y']]
    min_multiplier_df = min_multiplier_df.drop(['mbr_tests_y'], axis=1)
    min_multiplier_df.rename(columns={'mbr_tests_x': 'mbr_tests'})
    min_multiplier_df.to_csv('join_results_larger_medium_datasets_training_data.csv', index=None, sep=',')

    uniform_df = min_multiplier_df['uniform' in min_multiplier_df['dataset1']]
    uniform_df.to_csv('join_results_larger_medium_datasets_training_data_uniform.csv', index=None, sep=',')


def main():
    print('Extract join result')
    # extract_raw_data('join_results_larger_medium_datasets.csv', 'join_results_larger_medium_datasets_data.csv')
    # extract_sorted_data('join_results_larger_medium_datasets_data.csv', 'join_results_larger_medium_datasets_data_sorted.csv')

    # extract_raw_data('pbsm_multiplier_dynamic_larger_medium_datasets_join_result_data.log', 'join_results_larger_medium_datasets_data.csv')
    extract_sorted_data('join_results_larger_medium_datasets_data.csv',
                        'join_results_larger_medium_datasets_data_sorted.csv')


if __name__ == '__main__':
    main()
