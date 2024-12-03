<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>

<br />
This code takes narratives as inputs and generates internal and external scores as outputs. We  use a fine-tuned language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions are aggregated to obtain internal and external content estimates for each narrative. The colab notebook makes it easy to apply this approach to your own data!

<br />
<br />


Instructions for use:
  - Login to google drive and create a folder in My Drive called 'automated_autobiographical_interview_scoring'. Place your data (called data.csv) in this folder. 
  - Click on the file 'automated_autobiographical_interview_scoring_shared.ipynb' here on github.
  - Once this document opens, click on the following button at the top:
    <br />
    ![image](https://user-images.githubusercontent.com/43548396/149639845-ef10888e-0090-45c1-9062-bc6fbe09a18e.png)
    <br />
   - To run the code, click 'runtime' -> 'run all' in your menu bar. Results should appear in the same folder as your data once the code is done running! 

<br />
<br />


Expected data characteristics:
 - Your data are stored as a .csv file (.xlsx files not currently accepted, so please convert to .csv)
 - The .csv file that contains your narratives is located on your google drive.
 - Your .csv file includes three columns called 'participantID', 'prompt', and 'text'. These columns contain your participant IDs, the names or numbers of the prompts the participants saw, and the responses. 
 - Data should be in long format.
 - Your narratives, which are stored in the 'text' column, were written by participants or have been transcribed with lots of punctuation. The model will work poorly without punctuation.
 - Your narratives do not have any unmatched qoutes. Our sentence splitting algorithm may have problems with unmatched qoutes. In our paper, we did not preprocess data to ensure we had only matched qoutes; however, for maximum accuracy, this is recommended. An example of matched qoutes in a narrative is: he thought 'wow, this is so nice' Afterwards they went to the park. An example of unmatched qoutes is: he thought 'wow, this is so nice Afterwards they went to the park. 

<br />
<br />

Feel free to reach out to r.vangenugten@northeastern.edu with questions. Ongoing work is expanding this project with more performant language models and subcategory scoring, amongst other aims.

<br />
<br />

Future changes
- [ ] Add test to check if the input data is in the correct format
- [ ] Allow .xlsx files
- [ ] Add test to check if data is properly punctuated



