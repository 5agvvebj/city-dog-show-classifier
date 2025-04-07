#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py

# PROGRAMMER: Grisha Lala
# DATE CREATED: 11-11-24
# REVISED DATE: 
# PURPOSE: Create a function `calculates_results_stats` that calculates the
#          statistics of the results of the program run using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#          The statistics that are calculated will be counts and percentages.

def calculates_results_stats(results_dic):
    results_stats_dic = dict()

    # Sets all counters to initial values of zero
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Process through the results dictionary
    for value in results_dic.values():  # Iterate over dictionary values
        if value[2] == 1:
            results_stats_dic['n_match'] += 1
        if value[3] == 1 and value[2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        if value[3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if value[4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            if value[4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculates run statistics (counts & percentages)
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

    # Calculates % correct for matches
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0

    # Calculates % correct dogs if there are any dog images
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
        results_stats_dic['pct_correct_breed'] = 0.0

    # Calculates % correct not-a-dog images if there are any non-dog images
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic
