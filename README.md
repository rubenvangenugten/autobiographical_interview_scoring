<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>


We fine-tuned an existing language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions can be aggregated to obtain internal and external content estimates for each narrative. This colab notebook makes it easy to apply this approach to your own data!

Expected setup:
 - .csv file with narratives located in your google drive
 - .csv file has at least three columns called 'participantID', 'prompt', and 'text'. If you wnat to use this without modifying code, it is important to use this exact spelling of these column names.
 - 

  



Future changes
- [ ] Add test to check if the input data is in the format necessary for the code
- [ ] Add test to check if data is properly punctuated




