import numpy as np
import matplotlib.pyplot as plt


def infer_ASL(filepath, model_name):
    total_inf_time = 0
    total = 0
    correct = 0
    n_classes = 33

    false_detections = 0
    miss_class = 0
    matrix = np.zeros((n_classes, n_classes))

    class_names = ['0', '1', '2', '3', '4', '5', '6',
                   '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'X', 'Y', 'None']

    last_line_desc = False

    with open(filepath) as f:
        for line in f:

            if 'Enter Image Path' in line:
                contained_copy = False
                if ' copy.jpg' in line:
                    line = line.replace(' copy', '')
                    contained_copy= True

                if last_line_desc and true_class_index == -1:  # input had no sign, model detected no sign
                    correct += 1
                    total += 1
                elif last_line_desc:  # input had sign, model detected no sign
                    total += 1

                last_line_desc = True
                words = line.split(' ')
                if len(words) < 6:
                    break
                image_filepath = words[3]
                rate = words[6]
                total_inf_time += float(rate)

                if contained_copy:
                    text_file_path = image_filepath.replace('.jpg:', ' copy.txt')
                else:
                    text_file_path = image_filepath.replace('jpg:', 'txt')

                with open(text_file_path) as f2:
                    true_class_index = -1
                    for line2 in f2:
                        true_class_index = int(line2.split(' ')[0])

                        if true_class_index > 13:
                            true_class_index -= 3

                        break

            elif '%' in line:
                if not last_line_desc:
                    continue
                last_line_desc = False
                line = str(line.replace(':', ''))
                line = str(line.replace('%', ''))
                numbers = line.split(' ')
                predicted_class = numbers[0]

                class_index = class_names.index(predicted_class)

                if class_index == true_class_index:
                    correct += 1
                elif true_class_index == -1:
                    false_detections += 1
                else:
                    miss_class += 1

                total += 1

                matrix[class_index, true_class_index] += 1

    precision = correct / total

    # remove unused classes
    matrix = np.delete(matrix, n_classes - 2, 0)
    matrix = np.delete(matrix, n_classes - 3, 0)
    matrix = np.delete(matrix, n_classes - 2, 1)
    matrix = np.delete(matrix, n_classes - 3, 1)

    labels = ['0 / O', '1 / Z', '2 / V', '3', '4', '5', '6 / W',
                   '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'H', 'I', 'J', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'X', 'Y', 'None']


    rp = total / total_inf_time

    print('Model:', model_name, 'mAP:', precision, 'total inference time:', total_inf_time, 'rate of prediction:', rp, 'fps')
    print('Detected with no sign present:', false_detections, 'misclassifications:', miss_class, 'total:', total)
    fig, ax = plt.subplots()
    ax.set_xlabel('Ground truth classes')
    ax.set_ylabel('Predicted classes')
    ax.set_title(f'ASL Class confusion matrix for {model_name}')
    ax.set_yticks(list(range(len(labels))))
    ax.set_yticklabels(labels, fontsize=6)
    ax.set_xticks(list(range(len(labels))))
    ax.set_xticklabels(labels, rotation=90, fontsize=6)

    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.savefig(f"results/ConfusionMatrix_{model_name}.png")


def infer_ISL(filepath, model_name):
    total_inf_time = 0
    total = 0
    correct = 0
    n_classes = 36
    matrix = np.zeros((n_classes, n_classes))

    class_names = ['1', '2', '3', '4', '5', '6',
                   '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'None']

    last_line_desc = False

    with open(filepath) as f:
        for line in f:

            if 'Enter Image Path' in line:
                contained_copy = False
                if ' copy.jpg' in line:
                    line = line.replace(' copy', '')
                    contained_copy= True

                if last_line_desc and true_class_index == -1:  # input had no sign, model detected no sign
                    correct += 1
                    total += 1
                elif last_line_desc:  # input had sign, model detected no sign
                    total += 1

                last_line_desc = True
                words = line.split(' ')
                if len(words) < 6:
                    break
                image_filepath = words[3]
                rate = words[6]
                total_inf_time += float(rate)

                if contained_copy:
                    text_file_path = image_filepath.replace('.jpg:', ' copy.txt')
                else:
                    text_file_path = image_filepath.replace('jpg:', 'txt')

                with open(text_file_path) as f2:
                    true_class_index = -1
                    for line2 in f2:
                        true_class_index = int(line2.split(' ')[0])
                        break

            elif '%' in line:
                if not last_line_desc:
                    continue
                last_line_desc = False
                line = str(line.replace(':', ''))
                line = str(line.replace('%', ''))
                numbers = line.split(' ')
                predicted_class = numbers[0]

                class_index = class_names.index(predicted_class)

                if class_index == true_class_index:
                    correct += 1

                total += 1

                matrix[class_index, true_class_index] += 1

    precision = correct / total

    # remove unused classes
    matrix = np.delete(matrix, n_classes - 2, 0)
    matrix = np.delete(matrix, n_classes - 3, 0)
    matrix = np.delete(matrix, n_classes - 2, 1)
    matrix = np.delete(matrix, n_classes - 3, 1)


    rp = total / total_inf_time

    print('Model:', model_name, 'mAP:', precision, 'total inference time:', total_inf_time, 'rate of prediction:', rp, 'fps')
    fig, ax = plt.subplots()
    ax.set_xlabel('Ground truth classes')
    ax.set_ylabel('Predicted classes')
    ax.set_title(f'ISL Class confusion matrix for {model_name}')
    ax.set_yticks(list(range(len(class_names))))
    ax.set_yticklabels(class_names, fontsize=6)
    ax.set_xticks(list(range(len(class_names))))
    ax.set_xticklabels(class_names, rotation=90, fontsize=6)

    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.savefig(f"results/ConfusionMatrix_{model_name}.png")


if __name__ == "__main__":
    #model_names = ['YOLOv3-Tiny_CPU', 'YOLOv4-Tiny_CPU']
    #model_results = ['results/Yolov3-Tiny_test_cpu_results.txt',
    #                 'results/Yolov4-Tiny_test_cpu_results.txt']

    model_names = ['YOLOv4-ISL']
    model_results = [ 'results/Yolov4-isl_test_results.txt']

    for index, model_name in enumerate(model_names):
        infer_ISL(model_results[index], model_name)
