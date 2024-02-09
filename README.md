# User Behavior Analysis for Detecting Unauthorized Access

## Overview

### Problem Statement
Unauthorized access to user accounts and sensitive information poses a significant security threat to organizations. Detecting and preventing unauthorized access is crucial for maintaining data security and integrity.

### Solution
In this project, we aim to detect unauthorized access by analyzing user behavior patterns using machine learning techniques. We leverage a dataset from Kaggle, preprocess the data, and train a machine learning model to classify user behavior as normal or suspicious/attack.

## Process

1. **Dataset Selection**: We chose the dataset from Kaggle, provided by Mohamed Saleh, which contains user behavior data.

2. **Data Preprocessing**: We performed data preprocessing tasks such as handling missing values, encoding categorical variables, scaling numerical features, and splitting the data into training and testing sets.

3. **Feature Engineering**: We extracted relevant features from the dataset to represent user behavior patterns effectively. This included feature selection, transformation, and creation of new features based on domain knowledge.

4. **Model Training**: We trained machine learning models using the preprocessed data to predict whether a user behavior is normal or suspicious/attack. We experimented with various algorithms such as decision trees, random forests, logistic regression, etc., and evaluated their performance using appropriate metrics.

5. **Model Evaluation**: We evaluated the trained models on the test dataset to assess their performance in detecting unauthorized access. We analyzed metrics such as accuracy, precision, recall, F1-score, and ROC-AUC to measure the model's effectiveness.

6. **Deployment**: We deployed the trained model in a production environment for real-time detection of unauthorized access. The model continuously analyzes user behavior data and alerts administrators whenever suspicious activity is detected.

## Dataset
- **Dataset Name**: User Behavior Dataset
- **Dataset Source**: [Kaggle - Mohamed Saleh](https://www.kaggle.com/datasets/mohamedsaleh123/datasets123)
- **Description**: The dataset contains user behavior data collected from various sources, including login/logout activities, file access events, network connections, etc. It includes features such as user ID, timestamp, activity type, IP address, etc.


## Usage

1. **Clone the Repository**: Clone the project repository to your local machine.

2. **Install Dependencies**: Install the required Python libraries specified in the `requirements.txt` file using pip.

    ```bash
    pip install -r requirements.txt
    ```

3. **Explore Notebooks**: Explore the Jupyter notebooks in the `notebooks/` directory to understand the data exploration, preprocessing, model training, and evaluation processes.

4. **Run Scripts**: Use the Python scripts in the `src/` directory to perform data preprocessing, model training, and evaluation tasks.

5. **Deploy Model**: Deploy the trained model in production environment for the real-time detection of unauthorized access.

## Contributors

-Prince Kumar
-Piyush Kumar
-Hemant Singh
-Vaibhav Singh

##Google Colab Link 

(https://colab.research.google.com/drive/1kS9fCwBEgAygPv1WmJxQijU6IH_XXESC?usp=sharing)

