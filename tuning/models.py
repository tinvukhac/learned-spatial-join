import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error, mean_squared_error


def main():
    print('Train and test PBSM-Multiplier tuning model')

    training_df = pd.read_csv('training_data_larger_medium_datasets.csv', header=0, sep=',')

    features = ['size_x', 'num_features_x', 'num_points_x', 'avg_area_x', 'avg_sidelength_1_x', 'avg_sidelength_2_x', 'e0_x' , 'e2_x',
                'size_y', 'num_features_y', 'num_points_y', 'avg_area_y', 'avg_sidelength_1_y', 'avg_sidelength_2_y', 'e0_y', 'e2_y']
    label = ['pbsm_multiplier_best']

    train_data, test_data = train_test_split(training_df, test_size=0.20, random_state=41)

    X_train = pd.DataFrame.to_numpy(train_data[features])
    y_train = pd.DataFrame.to_numpy(train_data[label])
    X_test = pd.DataFrame.to_numpy(test_data[features])
    y_test = pd.DataFrame.to_numpy(test_data[label])

    reg_model = RandomForestRegressor(max_depth=8, random_state=11)
    model = reg_model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    y_test = y_test.flatten()
    print(y_test.shape)
    print(y_pred.shape)
    # print(np.array(y_test.flatten()))

    # test_df = pd.DataFrame()
    # test_df['y_test'] = 'a'
    # test_df['y_pred'] = y_pred
    # test_df.to_csv('test_df.csv')

    output_f = open('test.csv', 'w')
    output_f.writelines('y_test,y_pred\n')
    for a, b in zip(y_test, y_pred):
        output_f.writelines('{},{}\n'.format(a, b))
    output_f.close()

    mae = mean_absolute_error(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print('{},{},{}'.format(mae, mape, mse))

    # Baseline
    y_pred_100 = [100] * len(y_pred)
    mae = mean_absolute_error(y_test, y_pred_100)
    mape = mean_absolute_percentage_error(y_test, y_pred_100)
    mse = mean_squared_error(y_test, y_pred_100)

    print('{},{},{}'.format(mae, mape, mse))

    training_df = pd.read_csv('training_data_larger_medium_datasets.csv', header=0, sep=',')
    y_100 = training_df['mbr_tests_100']
    y_best = training_df['mbr_tests_best']

    output_f = open('test_100.csv', 'w')
    output_f.writelines('mbr_tests_best,mbr_tests_100\n')
    for a, b in zip(y_best, y_100):
        output_f.writelines('{},{}\n'.format(a, b))
    output_f.close()

    mae = mean_absolute_error(y_best, y_100)
    mape = mean_absolute_percentage_error(y_best, y_100)
    mse = mean_squared_error(y_best, y_100)

    print('{},{},{}'.format(mae, mape, mse))


if __name__ == '__main__':
    main()
