Objective-
The objective of this task is to develop a Linear Regression model using Python to predict house prices based on key features such as house size, number of rooms, and location. The task demonstrates data preprocessing, model training, and prediction using standard machine learning practices.

Dataset-
The dataset (house_prices.csv) contains the following columns:
Size_sqft – Size of the house in square feet
Rooms – Number of rooms
Location – Type of area (Rural, Suburban, Urban)
Price – House price in INR
Tools and Libraries Used
Python
Pandas
Scikit-learn
Methodology

Data Loading- The dataset was loaded using Pandas.
Initial inspection was performed to understand the structure and values.

Data Preprocessing-
The categorical Location feature was converted into numerical values:
Rural → 0
Suburban → 1
Urban → 2

The dataset was split into:
Features (X): Size_sqft, Rooms, Location
Target (y): Price

Model Training-A Linear Regression model from Scikit-learn was used.The model was trained using the processed feature set.

Prediction-House prices were predicted for the existing dataset. A comparison between actual and predicted prices was generated. The model was also used to predict the price of a new house with the following attributes:
Size: 1300 sqft
Rooms: 3
Location: Urban

Results and Observations-
The model successfully learned the relationship between house features and price.
House size and number of rooms show a strong influence on pricing.
Urban properties tend to have higher prices compared to rural and suburban areas.
The predicted price for the new house was approximately INR 6.3 million, which aligns with the dataset trends.

Folder Structure-
task2_linear_regression/
│
├── data/
│   └── house_prices.csv
│
├── model.ipynb
└── README.md

Conclusion-This task demonstrates a complete beginner-level machine learning workflow, including data preprocessing, model training, and prediction. The Linear Regression model provides reasonable predictions and serves as a foundational example of supervised learning in Python.

Version Control-All work related to this task has been committed and pushed to GitHub following standard version control practices.