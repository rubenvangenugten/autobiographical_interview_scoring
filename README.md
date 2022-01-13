<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>


We fine-tuned an existing language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions can be aggregated to obtain internal and external content estimates for each narrative. This colab notebook makes it easy to apply this approach to your own data!

Expected setup:
 - your.csv file with narratives is located on your google drive
 - .csv file includes three columns called 'participantID', 'prompt', and 'text'.
 - narratives, which are stored in 'text' are transcribed with lots of punctuation, or are written from participants.
 - there are no unmatched qoutes (") in the narratives. Our sentence splitting algorithm may have problems with unmatched qoutes.

  
Feel free to reach out to ruben_vangenugten@g.harvard.edu with questions.


Future changes
- [ ] Add test to check if the input data is in the format necessary for the code
- [ ] Add test to check if data is properly punctuated




