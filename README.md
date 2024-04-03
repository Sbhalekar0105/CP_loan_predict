# 🏦 Loan Prediction
[![Kaggle](https://img.shields.io/badge/-Kaggle-blue?logo=kaggle)](https://www.kaggle.com/)
[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Keras Tuner](https://img.shields.io/badge/-Keras%20Tuner-FF6F00?logo=keras&logoColor=white)](https://keras-team.github.io/keras-tuner/)
[![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![imblearn](https://img.shields.io/badge/-imblearn-F1C40F)](https://imbalanced-learn.org/stable/)
[![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B)](https://www.streamlit.io/)


## Table of Contents
 - [Installation](#installation)
 - [Deployement on Streamlit](#deployement-on-streamlit)
 - [Directory Tree](#directory-tree)
 - [Bug / Feature Request](#bug--feature-request)
 - [Future scope of project](#future-scope)
## Installation

This project is written in Python 3.10.10. If you don't have Python installed, you can download it from the [official website](https://www.python.org/downloads/). If you have an older version of Python, you can upgrade it using the pip package manager, which should be already installed if you have Python 2 >=2.7.9 or Python 3 >=3.4 on your system.
To install the required packages and libraries, you can use pip and the provided requirements.txt file. First, clone this repository to your local machine using the following command:
```
git clone https://github.com/Sajid030/Lending-Club-Loan-Prediction.git
```
Once you have cloned the repository, navigate to the project directory and run the following command in your terminal or command prompt:
```bash
pip install -r requirements.txt
```
This will install all the necessary packages and libraries needed to run the project.

## Deployement on Streamlit
1. Create an account on Streamlit Sharing.
2. Fork this repository to your GitHub account.
3. Log in to Streamlit Sharing and create a new app.
4. Connect your GitHub account to Streamlit Sharing and select this repository.
5. Set the following configuration variables in the Streamlit Sharing dashboard:
```
[server]
headless = true
port = $PORT
enableCORS = false
```
6. Click on "Deploy app" to deploy the app on Streamlit Sharing.

## Directory Tree

```
├── model
│   ├── dataset.pkl
│   ├── my_model.h5
├── app.py
├── loan_prediction.ipynb
├── requirements.txt
```
## Future Scope

- Improving the model performance by trying different machine learning algorithms or hyperparameter tuning.
- Adding more features to the dataset, which could potentially improve the accuracy of the model.
- Deploying the model on a cloud platform like AWS, GCP or Azure for more scalable and reliable use.
- Integrating the model with other financial data sources to make more accurate predictions and provide better insights.
- Using natural language processing techniques to analyze borrower comments or reviews to identify any potential risks or fraud.
