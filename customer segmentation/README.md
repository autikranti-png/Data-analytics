Customer Segmentation Project
📌 Project Overview

This project focuses on Customer Segmentation using Machine Learning and K-Means Clustering.

The main objective is to segment customers into different groups based on their demographic characteristics, purchasing behavior, spending patterns, engagement, and preferences.

Customer segmentation helps businesses understand different types of customers and develop targeted marketing strategies, personalized offers, customer retention plans, and better business decisions.

🎯 Objectives

The major objectives of this project are:

Analyze customer demographics and purchasing behavior.
Perform data cleaning and preprocessing.
Explore customer characteristics using EDA.
Select relevant features for segmentation.
Standardize numerical features.
Determine a suitable number of customer clusters.
Apply K-Means Clustering.
Evaluate clustering using the Elbow Method and Silhouette Score.
Visualize customer segments using PCA.
Analyze the characteristics of each customer segment.
Generate actionable business insights.
📊 Dataset

The project uses a synthetic dataset containing 1,000 customer records.

Dataset Features
Feature	Description
CustomerID	Unique customer identifier
Age	Customer age
Gender	Customer gender
AnnualIncome	Annual customer income
SpendingScore	Customer spending score
PurchaseFrequency	Number/frequency of purchases
AvgPurchaseAmount	Average purchase amount
TotalPurchaseValue	Total purchase value
OnlinePurchasePercentage	Percentage of online purchases
RecencyDays	Days since recent purchase
PreferredCategory	Customer's preferred product category
Location	Customer location
MembershipLevel	Customer membership level
DiscountUsagePercentage	Percentage of purchases using discounts
SatisfactionScore	Customer satisfaction score
🛠️ Technologies Used
Python
Jupyter Notebook
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Machine Learning Techniques
StandardScaler
K-Means Clustering
Elbow Method
Silhouette Score
Principal Component Analysis (PCA)
📁 Project Structure
Customer-Segmentation/
│
├── customer_segmentation_1000.csv
│
├── customer_segmentation_project.ipynb
│
├── customer_segmentation_with_clusters.csv
│
└── README.md
🔄 Project Workflow
Dataset
   ↓
Data Loading
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Feature Scaling
   ↓
Elbow Method
   ↓
Silhouette Score
   ↓
K-Means Clustering
   ↓
PCA Visualization
   ↓
Cluster Profiling
   ↓
Business Insights
🔍 Project Steps
1. Data Loading

The dataset is loaded using Pandas.

df = pd.read_csv("customer_segmentation_1000.csv")

The dataset contains 1,000 customer records.

2. Data Cleaning

The dataset is checked for:

Missing values
Duplicate records
Incorrect data types
Unnecessary data

Duplicate records are removed and missing values are handled where required.

3. Exploratory Data Analysis

EDA is performed to understand customer behavior.

The project analyzes:

Age distribution
Income distribution
Spending score
Gender distribution
Preferred product categories
Membership levels
Correlation between numerical variables

Various graphs and a correlation heatmap are used for visualization.

4. Feature Selection

The following features are used for clustering:

features = [
    "Age",
    "AnnualIncome",
    "SpendingScore",
    "PurchaseFrequency",
    "AvgPurchaseAmount",
    "TotalPurchaseValue",
    "OnlinePurchasePercentage",
    "RecencyDays",
    "DiscountUsagePercentage",
    "SatisfactionScore"
]

These features represent customer demographics and purchasing behavior.

5. Feature Scaling

Since the selected features have different ranges, StandardScaler is used.

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

Scaling prevents features with larger numerical values from dominating the clustering process.

🤖 6. K-Means Clustering

K-Means clustering is used to divide customers into groups with similar characteristics.

from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

The project uses 4 customer clusters for the final segmentation.

📈 7. Elbow Method

The Elbow Method is used to determine a suitable number of clusters.

inertia = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    inertia.append(kmeans.inertia_)

The resulting elbow graph helps identify a suitable value of K.

📊 8. Silhouette Score

The Silhouette Score is used to evaluate cluster separation.

from sklearn.metrics import silhouette_score

score = silhouette_score(
    X_scaled,
    df["Cluster"]
)

print("Silhouette Score:", score)

A higher silhouette score generally indicates better-defined clusters.

📉 9. PCA Visualization

Because the clustering uses multiple features, Principal Component Analysis (PCA) is used to visualize the customer groups in two dimensions.

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

df["PCA1"] = X_pca[:, 0]
df["PCA2"] = X_pca[:, 1]

The resulting scatter plot provides a visual representation of the customer segments.

👥 Customer Segments

The clusters can be interpreted based on their average income, spending score, purchase frequency, total purchase value, recency, and satisfaction.

Typical segment interpretations include:

💎 High-Value Customers

Characteristics may include:

Higher spending
Higher purchase frequency
Higher total purchase value
Strong customer engagement

Business strategy:
Provide loyalty rewards, personalized recommendations, premium offers, and exclusive benefits.

🌱 Potential / Affluent Customers

These customers may have relatively strong income or purchasing capacity but may have opportunities for increased engagement.

Business strategy:

Promote premium products
Personalized recommendations
Cross-selling
Membership upgrades
🔄 Regular Customers

These customers show moderate purchasing behavior.

Business strategy:

Product bundles
Reward points
Cross-selling
Personalized discounts
Encourage repeat purchases
⚠️ Low-Engagement Customers

These customers may show lower spending, lower purchase frequency, or higher recency.

Business strategy:

Re-engagement campaigns
Personalized offers
Limited-time promotions
Customer feedback surveys
Retention campaigns

Note: The exact interpretation of each cluster should be based on the cluster-profile table generated by the notebook.

💼 Business Applications

Customer segmentation can help businesses with:

🎯 Targeted Marketing

Different customer groups can receive different marketing campaigns.

🛍️ Personalized Recommendations

Products can be recommended according to customer preferences and purchasing behavior.

❤️ Customer Retention

Low-engagement customers can be identified and targeted with retention campaigns.

💰 Revenue Growth

High-value customers can be prioritized for loyalty programs and premium services.

📢 Promotional Campaigns

Discounts can be targeted toward customer groups that are more likely to respond.

📊 Visualizations Included

The project includes:

Customer Age Distribution
Annual Income Distribution
Spending Score Distribution
Gender Distribution
Preferred Category Distribution
Membership Distribution
Correlation Heatmap
Elbow Method Graph
Silhouette Score Graph
Cluster Size Graph
PCA Cluster Visualization
Income by Cluster
Spending Score by Cluster
Purchase Frequency by Cluster
📂 Output Files
Input Dataset
customer_segmentation_1000.csv

Contains the original 1,000 customer records.

Jupyter Notebook
customer_segmentation_project.ipynb

Contains the complete Python analysis and machine learning workflow.

Final Dataset
customer_segmentation_with_clusters.csv

Contains the original customer information along with:

Cluster
PCA1
PCA2
CustomerSegment
🚀 How to Run the Project
Step 1: Install Python

Make sure Python is installed on your computer.

Step 2: Install Required Libraries

Open Command Prompt or Anaconda Prompt:

pip install pandas numpy matplotlib seaborn scikit-learn jupyter
Step 3: Open Jupyter Notebook
jupyter notebook
Step 4: Open the Notebook

Open:

customer_segmentation_project.ipynb
Step 5: Keep the CSV in the Same Folder

Make sure:

customer_segmentation_1000.csv

is in the same directory as the notebook.

Step 6: Run the Cells

Run the notebook cells from top to bottom.

📌 Key Learning Outcomes

Through this project, I learned how to:

Work with customer datasets
Perform data preprocessing
Conduct exploratory data analysis
Select useful ML features
Apply feature scaling
Implement K-Means clustering
Determine the number of clusters
Evaluate clustering performance
Use PCA for visualization
Interpret customer segments
Convert machine learning results into business insights
🔮 Future Enhancements

The project can be further improved by:

Using real-world customer transaction data
Comparing K-Means with DBSCAN and Hierarchical Clustering
Building an interactive Power BI dashboard
Adding customer lifetime value analysis
Implementing RFM analysis
Creating automated customer recommendations
Deploying the segmentation model as a web application
👩‍💻 Author

Kranti Auti

Project

Customer Segmentation using K-Means Clustering

Internship

Thiranex – Skill Development & Future Tech

⭐ Conclusion

This project demonstrates how Machine Learning can be used to segment customers based on their behavior and demographics. By applying K-Means clustering, customers can be grouped into meaningful segments, allowing businesses to better understand their customers and create targeted marketing, personalized offers, retention strategies, and improved customer experiences.
