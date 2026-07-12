# Data Quality Report

## Missing Values
True.csv:
- No missing values detected.
Fake.csv:
- No missing values detected.
### Duplicate Records
True.csv:
- 206 duplicate records found.
- Duplicate records removed.
Fake.csv:
- 3 duplicate records found.
- Duplicate records removed.

## Dataset Balance

True articles: 21211

Fake articles: 23478

Observation:
The dataset is reasonably balanced and no balancing technique is required.

## Data Types
title      object
text       object
subject    object
date       object
label      int64

## Data Leakage Check

Title:
- Useful feature. It contains the headline of the article.

Text:
- Useful feature. It contains the complete news content.

Subject:
- Investigated but may introduce data leakage, so it may be excluded.

Date:
- Excluded because publication date does not directly determine whether news is fake or real.




note-We do  need techniques like Data Balance:

Oversampling
Undersampling
SMOTE

at this stage.