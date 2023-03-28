import json


def main():
    print('Extract dataset features')

    input_f = open('larger_medium_datasets_filenames.csv')
    output_f = open('larger_medium_datasets_summary_features.csv', 'w')

    line = input_f.readline()

    while line:
        filename = line.strip()
        file_path = 'larger_medium_datasets_filenames_summary_log/larger_medium_datasets_filenames_summary{}.log'.format(filename)
        f = open(file_path)
        content = f.readlines()

        json_str = ''
        for i in range(len(content)):
            line_content = content[i]
            if 'scheduler.DAGScheduler: Job 1 finished: first at GeometricSummary.scala:85' in line_content:
                for j in range(1, 11):
                    json_str += content[i+j].strip()

        json_data = json.loads(json_str)

        output_f.writelines('{},{},{},{},{},{},{}\n'.format(filename, json_data['size'], json_data['num_features'], json_data['num_points'], json_data['avg_area'], json_data['avg_sidelength'][0], json_data['avg_sidelength'][1]))

        line = input_f.readline()


if __name__ == '__main__':
    main()
