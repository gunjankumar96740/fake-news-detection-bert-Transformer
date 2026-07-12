# Fake News Detection Project

## Business Problem
Fake news can have serious consequences for individuals, businesses, and society. It can spread misinformation, create public panic, influence decisions, and increase social division. In financial markets, fake news can affect investor behavior and cause unnecessary volatility. A fake news detection system can help users identify potentially misleading information and make more informed decisions.

## Stakeholders
- Police
- Journalist
- Civilian
- Businessman
- Fact Checker
- Investor

## ML Problem Definition
This is a binary classification problem. The objective is to classify a news article as either Fake or Real. The model will use information from the news article, such as the title and text content, as input. The expected output is a prediction indicating whether the article is fake or real.


## Dataset Overview
### True 
- No. of rows=21417
- No. of columns=4
### Fake
- No. of rows=23503
- No. of Columns=4
### Columns
### Title
- The title column contains the headline of the news article.
### Text
- The text column contains the full content of the news article.
### Subject
- The subject column contains the category or topic of the news article.
### Date
- The date column indicates when the news article was published.
### Initial Observations
- The dataset contains news articles.
- This is about the fake news whether real.

## Risk
1. Some time our news classifies goes into wrong predictions.
2. Incorrect predictions may lead to financial losses or poor decision-making.
3. Maybe our training labeling is not proper.
4. News will be different from data on which we have trained earlier.

## Assumptions
1. Our data is based on the real life Data.
2. All the data has correct labels.
3. The data which we have is matching with correct columns.
4. The dataset contains sufficient information to learn patterns useful for fake news detection.

## Project And Roadmap
1. Understanding the Business Problem
2. Business Scale / Stakeholders
3. Collecting Data
4. Data Understanding
5. Data Preprocessing
6. Splitting the Data
7. Training the Model
8. Testing the Model
9. Model Evaluation
10. Model Deployment


