import json
import csv


def read_json_to_dict(file_path):
    """
    read a json file and convert to python3 dictionary
    :param file_path: json file path
    :return: the associated dictionary
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error in reading json file: ", e)
        return None


def string2dict(string):
    """
    convert a string to a dictionary
    :param string: input string
    :return: the associated dictionary
    """
    try:
        return json.loads(string)
    except Exception as e:
        print("Error in converting string to dictionary: ", e)
        return None


def save_2d_list_to_csv(input_list, file_path):
    """
    save a 2d list to a csv file, should be able to handle any data type
    :param input_list: the input list
    :param file_path: the csv file path
    :return: None
    """
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(input_list)
    except Exception as e:
        print("Error in saving 2d list to csv file: ", e)


def read_csv_to_2d_list(file_path):
    """
    read a csv file and convert to a 2d list
    :param file_path: csv file path
    :return: the associated 2d list
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except Exception as e:
        print("Error in reading csv file: ", e)
        return None


def save_dictionary_to_json(input_dict, file_path):
    """
    save a dictionary to a json file, use human-readable indent for better readability
    :param input_dict: the input dictionary
    :param file_path: the json file path
    :return: None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(input_dict, file, indent=4)
    except Exception as e:
        print("Error in saving dictionary to json file: ", e)


def binary_classification_result_evaluation(true_labels, predicted_labels):
    """
    evaluate the binary classification results
    :param true_labels: the true labels, with 0 as negative and 1 as positive
    :param predicted_labels: the predicted labels, with 0 as negative and 1 as positive
    :return: the evaluation results, including accuracy, precision, recall, f1 score
    """
    if len(true_labels) != len(predicted_labels):
        return None

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for i in range(len(true_labels)):
        if true_labels[i] == 1:
            if predicted_labels[i] == 1:
                true_positive += 1
            else:
                false_negative += 1
        else:
            if predicted_labels[i] == 1:
                false_positive += 1
            else:
                true_negative += 1

    accuracy = (true_positive + true_negative) / len(true_labels)
    precision = true_positive / (true_positive + false_positive) if true_positive + false_positive != 0 else 0
    recall = true_positive / (true_positive + false_negative) if true_positive + false_negative != 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


def convert_2dlist_to_string(input_list):
    """
    convert a 2d list to a string, the element in the list can be string (with space or comma) or numbers, separate column with ; and row with ##\n
    :param input_list: the input 2d list
    :return: the associated string
    """
    result = ""
    for row in input_list:
        result += ";".join([str(item) for item in row]) + "##\n"
    return result



