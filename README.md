<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>

This code takes narratives as inputs and generates internal and external scores as outputs. We  use a fine-tuned language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions are aggregated to obtain internal and external content estimates for each narrative. The colab notebook makes it easy to apply this approach to your own data!


Expected setup:
 - your.csv file with narratives is located on your google drive (.xlsx files not currently accepted, so please convert to .csv)
 - .csv file includes three columns called 'participantID', 'prompt', and 'text'.
 - narratives, which are stored in 'text' are transcribed with lots of punctuation, or are written from participants.
 - there are no unmatched qoutes (") in the narratives. Our sentence splitting algorithm may have problems with unmatched qoutes.

  
Feel free to reach out to ruben_vangenugten@g.harvard.edu with questions.


Future changes
- [ ] Add test to check if the input data is in the correct format
- [ ] Add test to check if data is properly punctuated




