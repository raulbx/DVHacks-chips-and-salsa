Chips and Salsa
===================================================

Contributers
------------
Dylan Chatterjee  
Manlo Ngai  
Rahul Bhaskar  
Tony Lew  

Introduction
------------

Code Structure and basic instructions
-------------------------------------

Looking at the data
-------------------

The training data contains a row per comment, with an id, the text of the comment, and 6 different labels that we'll try to predict.


Max_df

When building the vocabulary, it ignores terms that have a document frequency strictly higher than the given threshold. This could be used to exclude terms that are too frequent and are unlikely to help predict the label. For example, by analyzing reviews on the movie Lion King, the term 'Lion' might appear in 90% of the reviews (documents), in which case, we could consider establishing Max_df=0.89
