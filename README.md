<h1 align="center">Automated Scoring of Autobiographical Interview Narratives </h1>

This code takes narratives as inputs and generates internal and external scores as outputs. We  use a fine-tuned language model (distilBERT) to identify the amount of internal and external content in each sentence. These predictions are aggregated to obtain internal and external content estimates for each narrative. The colab notebook makes it easy to apply this approach to your own data!

<br />
<br />

Expected setup:
 - the .csv file that contains your narratives is located on your google drive. (.xlsx files not currently accepted, so please convert to .csv)
 - .csv file includes three columns called 'participantID', 'prompt', and 'text'. 
 - Data are in [long/narrow format](https://en.wikipedia.org/wiki/Wide_and_narrow_data). This means that row 1 contains data from participant 1, prompt 1, and the corresponding response. Row 2 contains data from participant 1, prompt 2, and the corresponding response. And so on.
 - narratives, which are stored in the 'text' column, were written by participants or have been transcribed with lots of punctuation.
 - there are no unmatched qoutes (") in the narratives. Our sentence splitting algorithm may have problems with unmatched qoutes.

<br />
<br />

Future changes
- [ ] Add test to check if the input data is in the correct format
- [ ] Add test to check if data is properly punctuated

<br />
<br /> 
Feel free to reach out to ruben_vangenugten@g.harvard.edu with questions.



