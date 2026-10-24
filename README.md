Customer Churn Prediction | Machine Learning

A Machine Learning project that predicts customer churn based on customer-related features, with an interactive Gradio interface and a FastAPI prediction API.

Project Overview

Customer churn is an important challenge for businesses seeking to understand customer behavior and improve retention. This project explores how classification models can help predict whether a customer is likely to leave a service.

The project covers data exploration, preprocessing, model training and evaluation, saving the trained model, and building interfaces for interactive predictions.

Project Objectives

- Explore customer data through Exploratory Data Analysis (EDA).
- Prepare and preprocess data for Machine Learning.
- Train and evaluate classification models.
- Compare predictive performance using appropriate evaluation metrics.
- Save the trained model using Pickle.
- Build an interactive user interface with Gradio.
- Develop a REST API using FastAPI for predictions.

Technologies Used

- Python
- Pandas & NumPy — Data manipulation
- Matplotlib & Seaborn — Data visualization
- Scikit-learn — Preprocessing, classification, and model evaluation
- Pickle — Model serialization
- Gradio — Interactive user interface
- FastAPI — REST API development
- Jupyter Notebook — Analysis and model experimentation

Dataset and Features

The dataset contains customer-related information used to predict churn.

Features include:

- "age"
- "monthly_charges"
- "tenure_months"
- "support_calls"
- "satisfaction_score"
- "total_spent"

Target variable: "churn"

- "0" — Customer stays
- "1" — Customer churns

The dataset used in the notebook contains 600 records and 7 columns.

Machine Learning Workflow

1. Data loading and inspection.
2. Exploratory Data Analysis (EDA).
3. Data cleaning and preprocessing.
4. Feature and target separation.
5. Train-test splitting.
6. Feature scaling where required.
7. Classification model training and evaluation.
8. Saving the trained model as a Pickle file.
9. Creating an interactive Gradio interface.
10. Developing a FastAPI endpoint for customer churn predictions.

Models and Evaluation

The notebook explores classification models, including Logistic Regression and Random Forest.

Model performance is evaluated using metrics such as:

- Accuracy
- Precision
- Recall
- F1-score

The recorded Logistic Regression experiment achieved 87.5% accuracy on the test set.

These results reflect the current experiment and do not guarantee the same performance on new, unseen customer data.

Interactive Interface

The project includes a Gradio interface designed to let users enter customer features and obtain a churn prediction.

The interface provides a more accessible way to experiment with the trained model without interacting directly with the notebook code.

API

The project also includes a FastAPI application intended to expose the model through a REST API.

The API implementation should be tested to ensure that input validation, feature ordering, and preprocessing are consistent with the model's training workflow.

Repository Structure

customer_churn-/
├── customer_churn_.ipynb
├── main.py
├── model.pkl
└── README.md

Additional interface or dependency files can be listed here if included in the repository.

Future Improvements

- Integrate preprocessing and prediction into a consistent Scikit-learn Pipeline.
- Validate predictions using unseen data and additional evaluation metrics.
- Test the Gradio interface and FastAPI endpoints.
- Improve API input validation and error handling.
- Deploy the interface or API to a public hosting platform.

Author

Menna Waleed
Statistics and Data Science Graduate

Interested in Machine Learning, Data Analytics, and Data Science.

Project Repository:
https://github.com/menna-waleed/customer_churn-

GitHub (https://github.com/menna-waleed/customer_churn-)
GitHub - menna-waleed/customer_churn-
Contribute to menna-waleed/custo
