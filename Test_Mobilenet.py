import io
import os
import datetime

import scipy.misc
import numpy as np
import six
import time
import glob
from IPython.display import display
import multiprocessing

from six import BytesIO
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

import tensorflow as tf
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

import timeit
import functools


def load_image_into_numpy_array(path):
  """Load an image from file into a numpy array.

  Puts image into numpy array to feed into tensorflow graph.
  Note that by convention we put it into a numpy array with shape
  (height, width, channels), where channels=3 for RGB.

  Args:
    path: a file path (this can be local or on colossus)

  Returns:
    uint8 numpy array with shape (img_height, img_width, 3)
  """
  img_data = tf.io.gfile.GFile(path, 'rb').read()
  image = Image.open(BytesIO(img_data))
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis,...]

    # Run inference
    model_fn = model.signatures['serving_default']
    start_time = datetime.datetime.now()

    output_dict = model_fn(input_tensor)
    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time).total_seconds()

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy()
                 for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections

    # detection_classes should be ints.
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    return output_dict, execution_time


def infer():
    os.chdir('models/research/object_detection')
    output_directory = 'inference_graph'
    labelmap_path = 'ASL_data/classes.pbtxt'
    category_index = label_map_util.create_category_index_from_labelmap(labelmap_path, use_display_name=True)

    class_names = [entry['name'] for entry in list(category_index.values())]
    n_classes = len(class_names)

    tf.keras.backend.clear_session()
    model = tf.saved_model.load(f'{output_directory}/saved_model')

    conf_threshold = 0.5
    total_inf_time = 0
    total = 0
    correct = 0

    matrix = np.zeros((n_classes, n_classes))

    with open('ASL_data/test.txt') as f:
        for line in f:
            image_path = str(line.rstrip())
            text_file_path = image_path.replace('jpg', 'txt')
            true_class_index = -1  # nothing
            with open(text_file_path) as f2:
                for line2 in f2:
                    true_class_index = int(line2.split(' ')[0])
                    break

            image_np = load_image_into_numpy_array(image_path)
            output_dict, inf_time = run_inference_for_single_image(model, image_np)
            vis_util.visualize_boxes_and_labels_on_image_array(
              image_np,
              output_dict['detection_boxes'],
              output_dict['detection_classes'],
              output_dict['detection_scores'],
              category_index,
              instance_masks=output_dict.get('detection_masks_reframed', None),
              use_normalized_coordinates=True,
              line_thickness=8)
            total_inf_time += inf_time

            class_index = output_dict['detection_classes'][0] - 1

            conf = output_dict['detection_scores'][0]
            if conf < conf_threshold:
                class_index = -1  # nothing

            if class_index > 13:
                class_index -= 3

            if true_class_index > 13:
                true_class_index -= 3

            if class_index == true_class_index:
                correct += 1

            total += 1

            matrix[class_index, true_class_index] += 1

    precision = correct / total

    # remove unused classes
    matrix = np.delete(matrix, n_classes-2, 0)
    matrix = np.delete(matrix, n_classes-3, 0)
    matrix = np.delete(matrix, n_classes-2, 1)
    matrix = np.delete(matrix, n_classes-3, 1)

    new_class_names = []

    for name in class_names:
        if name != 'del' and name != 'space' and name != 'nothing':
            if name == '0':
                new_class_names.append('0 / O')
            elif name == '2':
                new_class_names.append('2 / V')
            elif name == '6':
                new_class_names.append('6 / W')
            elif name == '1':
                new_class_names.append('1 / Z')
            else:
                new_class_names.append(name)

    new_class_names.append('None')

    rp = total / total_inf_time

    print('mAP:', precision, 'total inference time:', total_inf_time, 'rate of prediction:', rp,'fps')
    fig, ax = plt.subplots()
    ax.set_xlabel('Ground truth classes')
    ax.set_ylabel('Predicted classes')
    ax.set_title('Class confusion matrix for SSD MobileNet')
    ax.set_yticks(list(range(n_classes-2)))
    ax.set_yticklabels(new_class_names, fontsize=6)
    ax.set_xticks(list(range(n_classes-2)))
    ax.set_xticklabels(new_class_names, rotation=90, fontsize=6)

    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.savefig("../../../test.png")


if __name__ == "__main__":

    p = multiprocessing.Process(target=infer)
    p.start()
    p.join()
