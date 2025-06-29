# Machine Learning Model : Predict Delay of Shipment Probability

This project aims to analyze delivery performance in the logistics sector to identify factors that that can contribute to delay in shipment. Using the available logistics dataset, the data will be cleaned, processed, and used to build a machine learning model that predicts the delivery delays. The prediction results are expected to help the operations team improve delivery planning and assist management in formulating strategies to reduce delays and increase overall logistics efficiency.


## Repository Outline
```
1. README.md - Explanation of the project overview
2. ML_Model_Training_Evaluation.ipynb - Notebook that contains data loading, feature engineering, modelling, hyperparramter tunning, and model saving
3. Model_Inference.ipynb - Notebook that contains model inference from best modeling that have been analyzed from the 2nd Repository
4. url.txt - Text that contains URL of dataset and URL of model deployment
5. dataset_logistics - Dataset that being used for this analysis
6. model_fix.pkl - Model saving from analysis that being used for machine learning prediction
7. /deployment - Folder containing Python code and requirements for Model Deployment to Huggingface

```

## Problem Background
The logistics sector is an important sector that contributes to ensuring the supply chain will run smoothly, especially in industries that depend on delivery such as retail, manufacturing, and healthcare. In practice, operational problems are still often encountered that indirectly affect the delivery process, therefore it is necessary to analyze what factors contribute to delivery time. The "Logistics and supply chain dataset" dataset provides a comprehensive picture of what factors affect delivery time.

As a data scientist team from the "NCT Logistics" Company, a 3rd party logistics company that has a vision to always maintain the delivery of goods safely and on time, this analysis is important to predict what important factors need to be considered to maintain on time delivery and reduce delays. By conducting this analysis, the main parties involved; data teamn, operational team, and top level management, are expected to gain insight into minimizing factors that contribute to delays so as to increase business efficiency.


## Project Output

The output of this project is an Machine Learning that can predict delay probability of shipment. Model that is used in this machine learning is the best model that already being evaluated in the analysis, which is using Boosting + Tunning. To use the machine learning, users have to access the machine learning model on a link which the model are being deployed to the website (we use HuggingFace). Users have to input factors/features that contribute to delay of shipment and after that the model will give prediction of delay probability. 


## Data

The dataset provides a comprehensive collection of logistics and supply chain operations from Kaggle. In this dataset, it contains 26 columns and 32.065 rows. There are no missing values on the dataset. 22 columns are features columns and 4 columns are target. In this analysis, will be choosen 1 target which is delay prediction.


## Method

This analysis we divide 2 steps, which is pre processing and modelling. 
1. For pre processing, we use pipeline that contains Feature Scaling
2. For modeling we use 5 models in Machine Learning from Scikit-Learn. Here are 5 models that being used: KNeighborRegressor, SVR, Decision Tree, Random Forest, and Boosting. From 5 models, will be choosen 1 models for Hyperparamter tunning


## Stacks

Tools used for this analysis are VS Code, Streamlit, and HuggingFace. Additional library that being used are pandas, numpy, scipy, matplotlib, seaborn, scikit-learn, statsmodels, and pickle for model saving.


## Reference

- [Raw dataset link](https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset)
- [Model Deployment](https://huggingface.co/spaces/wandanisrina/milestoneproject2)
- [Project Repository](https://github.com/wandanisrina/ML-Predict-Delay-of-Shipment-Probability.git) (**Must read**)
