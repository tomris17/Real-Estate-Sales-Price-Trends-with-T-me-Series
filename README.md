# Real Estate Sales & Price Trends

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-blueviolet.svg)](https://seaborn.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository analyzes historical real estate sales data over time to uncover housing market trends and price fluctuations[cite: 18].

---

## Project Workflow
1. **Data Loading & Preprocessing**: Reading historical real estate records from `raw_sales.csv`, parsing date sold strings into datetime objects, and sorting chronologically[cite: 18].
2. **Monthly Resampling**: Aggregating historical sales by month end (`ME`) to compute average monthly property prices[cite: 18].
3. **Exploratory Data Analysis & Visualization**: Plotting monthly price trends over time and evaluating price distributions across property types using box plots with Seaborn and Matplotlib[cite: 18].
4. **Web Application**: Interactive user deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/real-estate-trends.git](https://github.com/YOUR_USERNAME/real-estate-trends.git)
   cd real-estate-trends
