<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>

<br />
This code takes narratives as inputs and generates internal and external scores as outputs. We  use a fine-tuned language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions are aggregated to obtain internal and external content estimates for each narrative. The colab notebook makes it easy to apply this approach to your own data!

<br />
<br />

Expected data:
 - Your data are stored as a .csv file (.xlsx files not currently accepted, so please convert to .csv)
 - The .csv file that contains your narratives is located on your google drive.
 - Your .csv file includes three columns called 'participantID', 'prompt', and 'text'. These columns contain your participant IDs, the names or numbers of the prompts the participants saw, and the responses. 
 - Data should be in long format.
 - Your narratives, which are stored in the 'text' column, were written by participants or have been transcribed with lots of punctuation.
 - Your narraties do not have any unmatched qoutes. Our sentence splitting algorithm may have problems with unmatched qoutes. In our paper, we did not preprocess data to ensure we had only matched qoutes; however, for maximum accuracy, this is recommended. An example of matched qoutes in a narrative is: he thought 'wow, this is so nice' Afterwards they went to the park. An example of unmatched qoutes is: he thought 'wow, this is so nice Afterwards they went to the park. 

<br />
<br />

Instructions for use:
  - Open the colab notebook
  - Allow colab access to google drive so that you can point it to the file location
  - Provide data file location. Provide location where you want the results stored.
  - Click 'runtime' -> 'run all' in your menu bar 

<br />
<br />

Future changes
- [ ] Add test to check if the input data is in the correct format
- [ ] Allow .xlsx files
- [ ] Add test to check if data is properly punctuated

<br />
<br /> 
Feel free to reach out to ruben_vangenugten@g.harvard.edu with questions.



