# Myntra-Sales-Analysis

# Data Analytics Project: Sales and Profit Analysis

## Overview
This project performs a comprehensive data analysis on sales and profit data. It explores the relationships between sales, profit, quantity, and shipping cost, and provides insights on customer behavior, product performance, and regional sales. The analysis is aimed at uncovering patterns in sales performance, identifying high-value customers, and providing recommendations for optimizing business operations.

## Dataset Description
The dataset contains the following columns:
- **Order ID**: Unique identifier for each order.
- **Order Date**: The date when the order was placed.
- **Ship Date**: The date when the order was shipped.
- **Ship Mode**: The shipping method used (e.g., Standard, Expedited).
- **Customer ID**: Unique identifier for each customer.
- **Customer Name**: Name of the customer.
- **Segment**: Customer segment (e.g., Consumer, Corporate).
- **City**: City where the customer is located.
- **State**: State where the customer is located.
- **Country**: Country of the customer.
- **Postal Code**: Postal code of the customer.
- **Market**: Geographical market.
- **Region**: Region where the customer is located.
- **Product ID**: Unique identifier for each product.
- **Category**: Product category (e.g., Furniture, Technology).
- **Sub-Category**: Product sub-category.
- **Product Name**: Name of the product.
- **Sales**: Total sales amount for the order.
- **Quantity**: Quantity of the product sold.
- **Discount**: Discount applied on the product.
- **Profit**: Profit generated from the product.
- **Shipping Cost**: Cost of shipping the product.
- **Order Priority**: Priority level of the order (e.g., High, Low).

## Key Analysis Performed
1. **Data Cleaning**: 
   - Missing values handling.
   - Data type correction for numeric and date columns.
   - Removal of duplicate entries.

2. **Exploratory Data Analysis (EDA)**:
   - Descriptive statistics (mean, median, standard deviation).
   - Correlation analysis between sales, quantity, profit, and shipping cost.

3. **Data Visualization**:
   - Scatter plot: Sales vs Profit.
   - Bar charts: Sales by Region, Ship Mode, and Category.
   - Line plot: Monthly sales trends.
   - Customer segmentation: High-value customers by sales and profit.

4. **Profitability Analysis**:
   - Profit margin analysis by product category.
   - Top 10 most profitable products.

5. **Shipping Cost vs Profit Analysis**:
   - Boxplot to show the relationship between shipping cost and profit.

## Requirements

To run the analysis, ensure the following libraries are installed:

- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical computing.
- **matplotlib**: Data visualization.
- **seaborn**: Advanced data visualization.

You can install the required libraries using `pip`:

```bash
pip install pandas numpy matplotlib seaborn
