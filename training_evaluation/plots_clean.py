#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:59:30 2021

@author: Ruben van Genugten
"""

import os 
import scipy
import re
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir("/Users/Ruben/Desktop/Automated_AI_scoring/autoscore_memories_python/autoscore_memories/plots")

#### generate fake data for plotting expected results

x = np.linspace(start=0, stop=10, num=100)
y = np.linspace(start=0, stop=10, num=100)
z = np.linspace(start=0, stop=0, num=100)


positive_EffectArray= np.array([x,y]).T
positive_EffectDf = pd.DataFrame(positive_EffectArray, columns = ['x','y'])

null_EffectArray= np.array([x,z]).T
null_EffectDf = pd.DataFrame(null_EffectArray, columns = ['x','z'])

#### now, start plotting target model performance

fig, axs = plt.subplots(ncols=2, nrows = 2,figsize=(15,9))

sns.regplot(x='x', y='y', data=positive_EffectDf, ax=axs[0,0], scatter = False, ci = None ) \
    .set_title('Correct Internal Content Classification', fontsize = 16, pad = 12)
axs[0,0].set_xlabel('Predicted Internal Content', fontsize = 14)
axs[0,0].set_ylabel('Internal Details', fontsize = 14)
axs[0,0].set(xticklabels=[]) 
axs[0,0].set(yticklabels=[]) 

sns.regplot(x='x', y='y', data=positive_EffectDf, ax=axs[0,1], scatter = False, ci = None ) \
    .set_title('Correct External Content Classification', fontsize = 16, pad = 12)
axs[0,1].set_xlabel('Predicted External Content', fontsize = 14)
axs[0,1].set_ylabel('External Details', fontsize = 14)
axs[0,1].set(xticklabels=[]) 
axs[0,1].set(yticklabels=[]) 

sns.regplot(x='x', y='z', data=null_EffectDf, ax=axs[1,0], scatter = False, ci = None ) \
    .set_title('Not Misclassifying Internal Content as External', fontsize = 16, pad = 12)
axs[1,0].set_xlabel('Internal Details', fontsize = 14)
axs[1,0].set_ylabel('Predicted External Content', fontsize = 14)
axs[1,0].set(xticklabels=[]) 
axs[1,0].set(yticklabels=[]) 

sns.regplot(x='x', y='z', data=null_EffectDf, ax=axs[1,1], scatter = False, ci = None ) \
    .set_title('Not Misclassifying External Content as Internal', fontsize = 16, pad = 12)
axs[1,1].set_xlabel('External Details', fontsize = 14)
axs[1,1].set_ylabel('Predicted Internal Content', fontsize = 14)
axs[1,1].set(xticklabels=[]) 
axs[1,1].set(yticklabels=[]) 

fig.tight_layout(pad=5.0)
fig.suptitle("Target Model Performance", fontsize = 20)

fig.savefig('target_results.png', dpi = 600)



### now define a function to do this automatically for each testing set
# takes in the data to plot, the name of the test set (so that we know what to name file),
# and a dictionary from which to choose titles of plots
# It will write out the plots and return the four relevant correlation values


def generateResultPlots(plottingDf, TestSetName, title_Dict):
    
    fig, axs = plt.subplots(ncols=2, nrows = 2,figsize=(15,9))
    
    
    ### first plot: how well internal ocntent is identified
    r_a, p_a = scipy.stats.pearsonr(plottingDf.numInt_sentence, grouped.numInt_preds)
    r_a_round = round(r_a, 2)
    p_a_round = round(p_a, 3)
    
    if p_a_round == 0.0:
       p_a_round = 'p < .001'
    else:
       p_a_round = 'p = {}'.format(p_a_round)

    sns.regplot(x="numInt_preds", y="numInt_sentence", data=plottingDf, ax=axs[0,0], scatter = True ) \
        .set_title('Internal Content Classification r = {}, {}'.format(r_a_round,p_a_round), fontsize = 16, pad = 12)
    axs[0,0].set_xlabel('Predicted Internal Content', fontsize = 14)
    axs[0,0].set_ylabel('Internal Details', fontsize = 14)
    axs[0,0].set(xticklabels=[]) 
    axs[0,0].set(yticklabels=[]) 
    
    ### second plot: how well external content is identified

    r_b, p_b = scipy.stats.pearsonr(grouped.numExt_sentence, grouped.numExt_preds)
    r_b_round = round(r_b, 2)
    p_b_round = round(p_b, 3)
    
    if p_b_round == 0.0:
       p_b_round = 'p < .001'
    else:
       p_b_round = 'p = {}'.format(p_b_round)
    
    sns.regplot(x="numExt_preds", y="numExt_sentence", data=plottingDf, ax=axs[0,1], scatter = True) \
        .set_title('External Content Classification r={}, {}'.format(r_b_round,p_b_round), fontsize = 16, pad = 12)
    axs[0,1].set_xlabel('Predicted External Content', fontsize = 14)
    axs[0,1].set_ylabel('External Details', fontsize = 14)
    axs[0,1].set(xticklabels=[]) 
    axs[0,1].set(yticklabels=[]) 
    
    
    ### third plot: misclassifying internal content as external
    
    r_c, p_c = scipy.stats.pearsonr(grouped.numExt_preds, grouped.numInt_sentence)
    r_c_round = round(r_c, 2)
    p_c_round = round(p_c, 3)
    
    if p_c_round == 0.0:
       p_c_round = 'p < .001'
    else:
       p_c_round = 'p = {}'.format(p_c_round)
    
    sns.regplot(x="numExt_preds", y="numInt_sentence", data=plottingDf, ax=axs[1,0], scatter = True) \
        .set_title('Classifying Internal Content as External r={}, {}'.format(r_c_round,p_c_round), fontsize = 16, pad = 12)
    axs[1,0].set_xlabel('Internal Details', fontsize = 14)
    axs[1,0].set_ylabel('Predicted External Content', fontsize = 14)
    axs[1,0].set(xticklabels=[]) 
    axs[1,0].set(yticklabels=[]) 
    
    
    ### fourth plot: misclassifying external content as internal

    
    r_d, p_d = scipy.stats.pearsonr(grouped.numInt_preds, grouped.numExt_sentence)
    r_d_round = round(r_d, 2)
    p_d_round = round(p_d, 3)
    
    if p_d_round == 0.0:
       p_d_round = 'p < .001'
    else:
       p_d_round = 'p = {}'.format(p_d_round)
       
    sns.regplot(x="numInt_preds", y="numExt_sentence", data=plottingDf, ax=axs[1,1], scatter = True) \
        .set_title('Classifying External Content as Internal r={}, {}'.format(r_d_round,p_d_round), fontsize = 16, pad = 12)
    axs[1,1].set_xlabel('External Details', fontsize = 14)
    axs[1,1].set_ylabel('Predicted Internal Content', fontsize = 14)
    axs[1,1].set(xticklabels=[]) 
    axs[1,1].set(yticklabels=[]) 
    
    fig.tight_layout(pad=5.0)
    
    top_title = "Automated Scoring Performance: {}".format(title_Dict[TestSetName]) 
    fig.suptitle(top_title, fontsize = 20, y = 1.0)
    

    save_fig_title = TestSetName + ' results.png'
    fig.savefig(save_fig_title, dpi = 600)
    return([r_a,r_b,r_c, r_d])




# create dataframe of labels for top title
titleLabelDict ={
    "Perspective": "Autobiographical Memory Task (King et al., 2021)",
    "OpinionOpinion": "Opinion Task (Williams & Sheldon, in prep)",
    "OpinionMemory": "Autobiographical Memory Task (Williams & Sheldon, in prep)",
    "OpinionDescription": "Picture Descrition Task (Williams & Sheldon, in prep)",
    "CW": "Creative Writing Task (van Genugten et al., 2021)",
    "DevittOlder Adult Episodic Simulation": "Older Adult Episodic Simulation (Devitt & Schacter, 2018; 2019)",
    "DevittYoung Adult Episodic Simulation": "Young Adult Episodic Simulation (Devitt & Schacter, 2018; 2019)",
    "MuMem": "Autobiographical Memory Task (Sheldon et al.,2020)",
    }


# after each iteration of train-on-all-but-one-dataset, the predictions
# for the left out dataset are written out.
# so, read in each of those datasets.
# each of these datsets is still in the one-sentence-per-row format.
# so sum up predictions and scores for each combination of participant & prompt (e.g.
# participant 1, prompt 1; participant 1, prompt 2)

currentWD = os.getcwd()
allFiles = os.listdir('colabData_CVTraining/data')

allFiles.remove('.DS_Store')

# create empty correlation dataframe to fill in


corr_table = []

for file in allFiles:    
    pattern = "testData_(.*?)_CVTraining.csv"
    substring = re.search(pattern, file).group(1)
    
    filePath = currentWD + '/' + 'colabData_CVTraining/data/' + file
    testData = pd.read_csv(filePath)
    
    # if the test dataset contains only one task (e.g. just memories from YA),
    # go ahead and create a plot with that data. If it contains more than one task,
    # make a seperate set of plots for each task.
    
    if testData.task.unique().size ==1:
        test_subset = testData.loc[:,["participantID","Interview", "numInt_preds", "numInt_sentence", "numTotal_sentence", "numExt_preds" ,"numExt_sentence", 'sentenceWordCount']]
        grouped = test_subset.groupby(by = ["participantID", "Interview"]).sum()
        newRowInCorrTable = [substring, ''] + generateResultPlots(grouped, substring, titleLabelDict)
        corr_table.append(newRowInCorrTable)
        
    else:
        # now look through different tasks, for each, write out.
        for task in testData.task.unique():
            testData2 = testData[testData.task == task]
            test_subset = testData2.loc[:,["participantID","Interview", "numInt_preds", "numInt_sentence", "numTotal_sentence", "numExt_preds" ,"numExt_sentence", 'sentenceWordCount']]
            grouped = test_subset.groupby(by = ["participantID", "Interview"]).sum()
            name_subtask = substring + task
            newRowInCorrTable = [substring, name_subtask] + generateResultPlots(grouped, name_subtask, titleLabelDict)
            corr_table.append(newRowInCorrTable)



##  write out correlations/results dataframes

corr_df = pd.DataFrame(corr_table, columns=['Dataset','Task','r_a', 'r_b', 'r_c', 'r_d'])

corr_df.to_csv('CV_Model_Performance_R_Unrounded.csv')


corr_df_square = pd.DataFrame(corr_table, columns=['Dataset','Task','r2_a', 'r2_b', 'r2_c', 'r2_d'])
corr_df_square.loc[:,'r2_a'] =  round(corr_df_square.loc[:,'r2_a'] **2, 2)
corr_df_square.loc[:,'r2_b'] =  round(corr_df_square.loc[:,'r2_b'] **2, 2)
corr_df_square.loc[:,'r2_c'] =  round(corr_df_square.loc[:,'r2_c'] **2, 2)
corr_df_square.loc[:,'r2_d'] =  round(corr_df_square.loc[:,'r2_d'] **2, 2)

corr_df_square.to_csv('CV_Model_Performance_R2.csv')


corr_df.loc[:,'r_a'] =  round(corr_df.loc[:,'r_a'], 2)
corr_df.loc[:,'r_b'] =  round(corr_df.loc[:,'r_b'], 2)
corr_df.loc[:,'r_c'] =  round(corr_df.loc[:,'r_c'], 2)
corr_df.loc[:,'r2d'] =  round(corr_df.loc[:,'r_d'], 2)

corr_df.to_csv('CV_Model_Performance_R.csv')



