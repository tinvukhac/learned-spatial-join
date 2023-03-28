import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main():
    print ('Train and test local join model')
    features = ['Record Count_x',
               'Data Size_x',
               'xmin_x',
               'ymin_x',
               'xmax_x',
               'ymax_x',
               'avg_x_x',
               'avg_y_x',
               'avg_area_x',
               'Record Count_y',
               'Data Size_y',
               'xmin_y',
               'ymin_y',
               'xmax_y',
               'ymax_y',
               'avg_x_y',
               'avg_y_y',
               'avg_area_y',
               'intersection_percentage_1',
               'intersection_percentage_2',
               'intersection_percentage_1_x',
               'intersection_percentage_2_x',
               'intersection_percentage_1_y',
               'intersection_percentage_2_y',
               'intersection_area',
               'jaccard_similarity',
               'jaccard_similarity_x',
               'jaccard_similarity_y']

    features = ['Record Count_x',
                'Data Size_x',
                'xmin_x',
                'ymin_x',
                'xmax_x',
                'ymax_x',
                'avg_x_x',
                'avg_y_x',
                'avg_area_x',
                'Record Count_y',
                'Data Size_y',
                'xmin_y',
                'ymin_y',
                'xmax_y',
                'ymax_y',
                'avg_x_y',
                'avg_y_y',
                'avg_area_y',
                'intersection_percentage_1',
                'intersection_percentage_2',
                'intersection_area',
                'jaccard_similarity']

    label = ['plane_x_is_better']

    columns = []
    for f in features:
        columns.append(f)

    for l in label:
        columns.append(l)

    df = pd.read_csv('../data/outputs/join_results_local_xy_training_data.csv', sep='\t', header=0)
    df = df[columns]
    features_df = df[features]
    label_df = df[label]

    df_min_max_scaled = features_df.copy()

    # apply normalization techniques
    # Asymetric normalization
    for column in df_min_max_scaled.columns:
        df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (
                    df_min_max_scaled[column].max() - df_min_max_scaled[column].min())

    df = df_min_max_scaled
    df[label] = label_df[label]

    print (df)

    train, test = train_test_split(df, test_size=0.2, random_state=90)
    X_train, y_train, X_test, y_test = train[features], train[label], test[features], test[label]


    smote = SMOTE(random_state=14)
    X_train, y_train = smote.fit_resample(X_train, y_train)
    X_test, y_test = smote.fit_resample(X_test, y_test)

    print(y_train.value_counts())
    print(y_test.value_counts())

    clf = RandomForestClassifier(max_depth=2, random_state=41)
    clf.fit(X_train, y_train)

    y_predict = clf.predict(X_test)
    print ('Accuracy score: {}'.format(accuracy_score(y_test, y_predict)))

    for name, important in zip(features, clf.feature_importances_):
        print ('{}\t{}'.format(name, important))


if __name__ == '__main__':
    main()
