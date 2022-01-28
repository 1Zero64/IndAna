# python3 DataPreparation.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Ann-Kathrin Jauk
# Runs parts of or whole project
# ===========================================================================================

import DataProcessing.DataExploration as exploration
import DataProcessing.DataMerge as merge

def runSystem(articleId, date, processStep="all"):
    '''
    Function to run parts of or whole system

    :param articleId: (int)
            articleId of article to examine
    :param date: (datetime64)
            date from where to forecast
    :param processStep: (str)
            Process step until which to run process, default: merge;
            there are: explore, merge, (FUTURE) analyze, evaluate, visualize and all
    '''

    if processStep == "explore":
        print("Starting Data Exploration")
        exploration.explore()
        print("Finish of Data Exploration")
        print("======================================================================")

    if processStep == "merge":
        print("Starting Data Merge")
        print(merge.mergeData())
        print("Finish of Data Merge")
        print("======================================================================")

    if processStep == "analyze":
        print("Data Analysis")
        print("Finish of Data Analysis")
        # integrate ML Modelling in future
        print("======================================================================")

    if processStep == "evaluate":
        print("Data Evaluation")
        # integrate ML evaluation in future
        print("Finish of Data evaluation")
        print("======================================================================")

    if processStep == "visualize":
        print("Result Visualization")
        # integrate Result Visualization in future
        print("Finish of Result Visualization")
        print("======================================================================")

    if processStep == "all":
        print("Starting Data Exploration")
        exploration.explore()
        print("Finish of Data Exploration")
        print("======================================================================")
        print("Starting Data Merge")
        print(merge.mergeData())
        print("Finish of Data Merge")
        print("======================================================================")
        print("Data Analysis")
        print("Finish of Data Analysis")
        # integrate ML in future
        print("======================================================================")
        print("Data Evaluation")
        # integrate ML evaluation in future
        print("Finish of Data evaluation")
        print("======================================================================")
        print("Result Visualization")
        # integrate Result Visualization in future
        print("Finish of Result Visualization")
        print("======================================================================")