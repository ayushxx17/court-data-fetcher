#  Sales Data Analysis Project

This project analyzes a sample sales dataset using Python, Pandas, Matplotlib, and Seaborn to generate insights and visualizations. It is part of my internship task to strengthen my data analysis skills.

##  Dataset

The dataset used is a CSV file named `sales_data.csv` with the following columns:

- `Date` – The date of the sale  
- `Product` – Name of the product sold  
- `Units Sold` – Number of units sold  
- `Price` – Price per unit  

##  Objectives

- Perform basic data exploration  
- Handle null/missing values  
- Calculate total sales  
- Visualize sales performance per product  
- (Optional) Analyze sales trends over time  

##  Tools & Libraries Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code (Jupyter Extension)

##  Key Visualizations

- 📌 Bar chart: Total Sales per Product  
- 📌 Bar chart: Units Sold per Product  
- 📌 Line chart: Sales Over Time (if dates are available)

##  How to Run

1. Clone the repository  
2. Open `sales_analysis.ipynb` in Jupyter Notebook or VS Code  
3. Make sure `sales_data.csv` is in the same folder  
4. Run all cells step-by-step

##  Sample Code Snippet

```python
# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_csv('sales_data.csv')

# Step 3: Basic Visualization
df['Total Sales'] = df['Units Sold'] * df['Price']
plt.bar(df['Product'], df['Total Sales'])
plt.title("Total Sales per Product")
plt.show()
