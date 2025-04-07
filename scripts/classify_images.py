#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Grisha Lala
# DATE CREATED: 11.11.24                              
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. 

# Imports classifier function for using CNN to classify images 
from classifier import classifier 
import os

def classify_images(images_dir, results_dic, model):
    for key, value in results_dic.items():  # Using .items() to get key-value pairs
        # Check if the file is an image by its extension
        if key.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Construct the image path using os.path.join to avoid issues with slashes
            image_path = os.path.join(images_dir, key)

            # Classify the image and get the label
            model_label = classifier(image_path, model)

            # Process the classifier label
            model_label = model_label.lower().strip()

            # Get the true label from results_dic
            truth = value[0]

            # Compare the classifier label to the true label
            if truth in model_label:
                value.extend([model_label, 1])  # 1 indicates a match
            else:
                value.extend([model_label, 0])  # 0 indicates no match
        else:
            print(f"Skipping non-image file: {key}")
            # Ensure skipped files have a consistent structure to avoid index errors
            value.extend(["", 0])

    # Debugging output to confirm structure
    print("Contents of results_dic after classification:")
    for key, value in results_dic.items():
        print(f"{key}: {value}")

"""
Creates classifier labels with classifier function, compares pet labels to 
the classifier labels, and adds the classifier label and the comparison of 
the labels to the results dictionary using the extend function. This function 
uses the classifier() function from classifier.py.

Parameters: 
 images_dir - The (full) path to the folder of images to be classified (string)
 results_dic - Dictionary with 'key' as image filename and 'value' as a List:
               index 0 = pet image label (string)
               NEW - index 1 = classifier label (string)
               NEW - index 2 = 1/0 (int), where 1 = match, 0 = no match
 model - Indicates which CNN model architecture to use (string: 'resnet', 
         'alexnet', 'vgg')
Returns:
 None - results_dic is a mutable data type, so no return needed.
"""
