# Employee Attrition Prediction and Retention Analysis
A data science project to analyze employee attrition and build a logistic regression model that predicts whether an employee will leave the organization based on certain features. The project is deployed as an interactive Streamlit web app.

## 1. Problem Statement
Employee attrition, or turnover, is a major challenge for organizations. Losing skilled employees negatively impacts company productivity, employee morale, and financial performance. Therefore, it is important to identify the key factors that influence attrition and predict which employees are at risk of leaving. This project aims to:
- Understand factors contributing to employee attrition.
- Build a predictive machine learning model to forecast attrition risk.

## 2. Objective
- Perform Exploratory Data Analysis (EDA) and visualize trends in employee attrition.
- Identify important features impacting employee retention.
- Build a Logistic Regression model to predict whether an employee will leave.
- Deploy the model using Streamlit to make it accessible through a web interface.

## 3. Tools & Technologies Used
### Programming Language:
- Python 3.11
### Python Libraries:
- pandas : for data loading and preprocessing
- matplotlib & seaborn : for data visualization
- sklearn : for model building and evaluation
- pickle : for saving the model
- streamlit : for building the web app
### Platforms & Services:
- Kaggle : dataset source
- Jupyter Notebook : data exploration and model building
- Git : version control
- GitHub : source code hosting
- Streamlit Cloud : web app deployment
- Git Bash : terminal for git commands

## 4.Processes Uses
### Data Collection:
- The dataset used in this project was sourced from Kaggle - HR Analytics, which contains features like employee satisfaction level, salary, promotion status, and more.
   <a href="https://www.kaggle.com/datasets/giripujar/hr-analytics" target="_blank">HR Analytics Dataset on Kaggle</a>
###  Data Cleaning and Exploration:
- Checked for missing or null values using:data.isnull().sum()
- Verified data types and value distributions.
- No major cleaning was required as the dataset was well-structured.
### Exploratory Data Analysis (EDA) and Visualization:
- The purpose of EDA was to understand which features significantly contribute to employee attrition. The target variable in this analysis is left, which indicates whether an employee left the company (1) or stayed (0).
- Boxplots were plotted for features like satisfaction_level, average_montly_hours, and time_spend_company against left to visualize how distributions differ between employees who stayed vs. those who left.
- Histplots and Countplots were used to compare frequency of different categorical or numerical values grouped by attrition.
![Average Monthly Hours vs Attrition](https://github.com/user-attachments/assets/50c594ec-6e5e-44c1-810d-6ef5b50faae8)
![Department-wise Attrition](https://github.com/user-attachments/assets/5ca6e6d9-87ff-4d71-8c74-4c5972251231)
![Promotion in Last 5 Years vs Attrition](https://github.com/user-attachments/assets/33138e54-fd41-443e-bf27-3e800333ec1e)
![Salary Level vs Attrition](https://github.com/user-attachments/assets/e106355e-fcb7-43ec-b8e9-4de6329ed37d)
![Satisfaction Level vs Attrition](https://github.com/user-attachments/assets/b942492a-3208-475c-856c-3626d31cdbe3)
![Time Spent at Company vs Attrition](https://github.com/user-attachments/assets/637de84a-c1ed-43e3-a86b-cb5a0875aec5)
### Feature Selection:
- Based on EDA and correlation, the following features were selected:
  - satisfaction_level
  - average_monthly_hours
  - salary
  - promotion_last_5years
  - time_spend_company
- These variables showed noticeable influence on whether an employee left the organization.
### Encoding Categorical Variables:
- Salary is a categorical variable (low, medium, high), so we applied one-hot encoding.
- Avoided the dummy variable trap by dropping one column (high).
### Train-Test Split:
- The data was split into training and testing sets using an 80-20 ratio.
### Model Building (Logistic Regression):
- A logistic regression model was trained on the selected features.
### Model Evaluation:
- Evaluated model performance using:
  - Confusion Matrix
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- Visualized the confusion matrix using Seaborn heatmap.
![Confusion_matrix](https://github.com/user-attachments/assets/0c879d28-788d-4380-a371-70365b685249)
### Model Saving (Pickle):
- Saved the trained model for deployment.
### Streamlit App Development:
- Created an app.py file using Streamlit to build an interactive UI.
- Took user inputs via sliders/dropdowns.
- Loaded the .pkl model.
- Displayed prediction output dynamically.
### Deployment:
- Generated requirements.txt with: pip freeze > requirements.txt
- Used Git for version control:
    - git init
    - git add .
    - git commit -m "Initial commit"
    - git remote add origin <repo_url>
    - git push -u origin main
- Hosted the app on Streamlit Cloud by linking the GitHub repository.
- Final live project accessible via Streamlit link.

## Final Output
#### Interactive Streamlit App
![employee retention prediction](https://github.com/user-attachments/assets/fb278f77-d5ff-4315-bb07-831357388227)
<a href="https://linu-1234-employee-retention-app-app-plsrlw.streamlit.app/">Try the app</a>
<a href="https://github.com/Linu-1234/employee-retention-app">View project on Github</a>

## Conclusion
- This project demonstrates how data science techniques can be applied to real-world HR problems. By analyzing key factors like satisfaction level, salary, promotions, and time spent in the company, we were able to create a model that helps in predicting employee attrition. The project is presented as a user-friendly web app that can be extended or integrated into larger HR analytics systems.


