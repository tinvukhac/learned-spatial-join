from classification_model import ClassificationModel
from utils import spatial_quality_extractor


def main():
    print('Main 2')

    # spatial_quality_extractor.extract_partitions_features_from_master_file('data/temp/osm2015_roads_master.rsgrove')

    model = ClassificationModel('clf_random_forest')
    # model.train('data/train_and_test_all_features_split/train_join_results_combined_v3.csv', 'best_algorithm', 'trained_models/model_best_algorithm_1219.h5')
    mae, mape, mse, msle = model.test('data/train_and_test_all_features_split/test_join_results_real_datasets_large.csv', 'best_algorithm', 'trained_models/model_best_algorithm_1219.h5')
    print('{}, {}, {}, {}'.format(mae, mape, mse, msle))


if __name__ == '__main__':
    main()
