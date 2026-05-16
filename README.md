# Underwriter Assist
A tool to assist Underwriters in making loan approval decisions quickly and within a set standard. 

## Live Demo

## Live Demo
[Try It](https://underwriter-assist.streamlit.app/)
### Purpose

To build a tool that predicts whether a borrower will default on their loan, and calculates the expected loss to the bank. 

This is for the underwriter at a "Buy Here Pay Here" dealership. 

***Tools***

- DBeaver to manipulate the data
- Postgres SQL to store the data
- Visual Studio Code IDE and Jupyter Notebook to write the code and this report

*** Skills Learned: ***
- Project Management
- Planning
- Python Programming Language
- SQL
- XG Boost
- Statistical Analysis
- Feature Engineering
- Data Storage
- Data Cleaning
- Model Training
- Prediction
- Business Recommendation

### Methodology
***Phase 1:*** 
- Download Lending Club data, load into SQL Database.
- Explore data with SQL queries.

***Phase 2:***
- Using SQL queries, clean the dataset, create temporary tables with necessary features by way of feature engineering. 
- Export Enhanced Dataset to Python Pandas.

***Phase 3:***
- Perform Correlation Analysis.
- Train/Test split the data and train the model.
- Use balanced Logistic Regression.
- Evaluate model performance for accuracy, precision, recall and confusion matrix.
- Retrain with XGBoost and compare with Logistic Regression for accuracy, precision, recall, and confusion matrix.
- Use GridSearchCV set for maximum recall to see if I can boost accuracy and to what percentage, and if it is worth the trade-off.
- Make my recommendation based on findings. 

***Phase 4:***
- Build the expected loss function.
- Build a prediction function that returns a prediction, expected loss, and a recommendation.

***Phase 5:***
- Compile final Jupyter Notebook. 
- Write executive summary.
- Final recommendation with supporting visualizations.

***Phase 6:***
- Build the Streamlit app.
- Test it locally.
- Deploy it on Streamlit

***Deliverables***
- SQL database with cleaned Lending Club data.
- Jupyter notebook with full analysis.
- Trained model that predicts the probability of default.
- Expected loss calculator.


## Reasoning

- Logistic Regression to allow the banking institution to be able to explain in detail why a customer was rejected while XGBoost would yield more accurate results, it is ambiguous to explain.
- PostgreSQL data and DBeaver interface for easier cleaning and manipulation of such a large dataset. 
- Use OptimalBinning on the total_il_high_credit_limit because varying credit limit is important in determining default rate, and the amount of unknown is significant enough to warrant its own column. This prompts me to one-hot encode this column, and OptimalBinning allows me to reduce the number of columns it would generate.
- Use GridSearchCV focused on recall to see how it compares to being balanced and if the trade-off is worth it. 
- Kept rows with unknown emp_length because it was a significant category showing 27% default rate vs 20% for known employment. 
- Rows where dti = 'nan' were dropped because these were zero-income applicants who somehow got loans, indicating fraud or error. 
- Using Steamlit for its ease of use and rapid development of data applications in pure Python, as I lack frontend expertise.
 
## Data

[Lending Club dataset on Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)


## Limitations of the Data

The data is limited because it is not up-to-date or dynamic, so it does not constantly learn or self-correct, and as the economy and human behavior evolve, the machine can become obsolete. 

That being said, given the volume of historical data, these predictions should serve as a useful tool for the underwriter to make the final decision. 

## Future Roadmap

- Add Loan-to-Value Calculation
- Build Credit Soft Pull pipeline
- Populate customer fields with soft pull data
- Docker Deployment
