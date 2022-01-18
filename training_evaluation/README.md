- automated_internal_external_scoring_CV_clean.ipynb was used to train with leave-one-dataset out crossvalidation. This code saves the model and predictions on leftout data for  each CV fold
- plots_clean.py was used to take the predictions on the left-out sets and make the plots in the paper.
- synthetic_data_training_repeat.csv is a synthetic dataset that you can use to run the code in this folder. It is intended to illustrate the format that the training and evaluation data is in. It is not intended to train a meaningful model. The  dataset consists of 3 memories, copied multiple times to work. We provide synthetic data because data used for actually training our model cannot be shared.



