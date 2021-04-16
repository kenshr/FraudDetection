# FraudDetection

# Background

The goal is to build an application that can leverage machine learning to screen events for potential fraud monitoring.

# Pipeline

The raw data was in Json format, which was processed by a Class object for ease of use and automation of the data-cleaning process.  

# Work-Flow

As a group we started wtih CRISP-DM process and iterated through making the pre-process pipeline, EDA, and modeling processes more robust in every round. 

# Scoring Metrics

We chose to emphasize recall as our scoring metric because the penalty of not catching a fraud event is worse than false flagging a non-fraud account. Fortunately for us our model predicts new data well on both precision and recall around 99%.

# Validation

We split our data into training and test data after pre-processing, and used cross-validation to test how well our model performed on training data and then tested on data to determine model performance.  

# Model Optimization

Using CRISP-DM process we were able to identify data-leakage in location based features and remove them clearing the way for the features that best captured new data. Outside of iteratively making our data better with more thorough pre-processing we used multiple grid searches for all of our modeling approaches and settled on a very optimized random forest model. 


# Final Product
We deployed the final product to AWS and succesfully screened new events for fraud monitoring.

# Further Steps
Test NLP and ensemble models for efficacy.
Building a deployable product end-to-end for fraud detection.
