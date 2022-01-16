<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>

<br />
This code takes narratives as inputs and generates internal and external scores as outputs. We  use a fine-tuned language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions are aggregated to obtain internal and external content estimates for each narrative. The colab notebook makes it easy to apply this approach to your own data!

<br />
<br />

Expected data characteristics:
 - Your data are stored as a .csv file (.xlsx files not currently accepted, so please convert to .csv)
 - The .csv file that contains your narratives is located on your google drive.
 - Your .csv file includes three columns called 'participantID', 'prompt', and 'text'. These columns contain your participant IDs, the names or numbers of the prompts the participants saw, and the responses. 
 - Data should be in long format.
 - Your narratives, which are stored in the 'text' column, were written by participants or have been transcribed with lots of punctuation. The model will work poorly without punctuation.
 - Your narraties do not have any unmatched qoutes. Our sentence splitting algorithm may have problems with unmatched qoutes. In our paper, we did not preprocess data to ensure we had only matched qoutes; however, for maximum accuracy, this is recommended. An example of matched qoutes in a narrative is: he thought 'wow, this is so nice' Afterwards they went to the park. An example of unmatched qoutes is: he thought 'wow, this is so nice Afterwards they went to the park. 

<br />
<br />

Instructions for use:
  - Login to google drive on your computer. Create a folder with your data (you can use example_data.csv provided here if you would like an example).
  - Click on the file 'automated_autobiographical_interview_scoring_shared.ipynb' here on github.
  - Once this document opens, click on the following button at the top:
    <br />
    ![image](https://user-images.githubusercontent.com/43548396/149639845-ef10888e-0090-45c1-9062-bc6fbe09a18e.png)
    <br />
  - After the above step launches google colab in your browser, click on the following button at the top:
    <br />
    ![image](https://user-images.githubusercontent.com/43548396/149639889-361a3787-b5d1-439f-bb81-399dc367b515.png)
    <br />
  - You now have the notebook saved in your google drive! Follow the instructions in the notebook so that the code can find your data, and hit 'run all'!

<br />
<br />

Future changes
- [ ] Add test to check if the input data is in the correct format
- [ ] Allow .xlsx files
- [ ] Add test to check if data is properly punctuated

<br />
<br /> 
Feel free to reach out to ruben_vangenugten@g.harvard.edu with questions.



