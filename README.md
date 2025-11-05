# Credit-Card-Customer-Segmentation-Profitability-Analysis

🧩 Project Overview

This project focuses on **analyzing credit card customer data** to uncover patterns in customer behavior, segment customers for targeted marketing, and predict churn risk using **machine learning**.  
It combines **RFM segmentation, profitability analysis, clustering, and predictive modeling** to deliver actionable business insights.

## 🗂️ Dataset
**Source:** Kaggle – Credit Card Customers Dataset  
**Records:** 10,127 customers  
**Fields:** Demographics, income, card type, credit limit, transaction amount & frequency, inactivity, churn flag, etc.
## Dataset Information
- **Rows:** 10,127  
- **Columns:** 21  
- **Key Features:**
  - `Customer_Age`, `Gender`, `Income_Category`, `Card_Category`
  - `Total_Trans_Amt`, `Total_Trans_Ct`, `Credit_Limit`, `Avg_Utilization_Ratio`
  - `Attrition_Flag` (Target Variable → “Existing” or “Attrited”)
---

## ⚙️ Methodology Overview
| Stage | Description |
|--------|-------------|
| **1. Data Cleaning** | Verified dataset integrity — no missing or duplicate values. |
| **2. EDA (Exploratory Analysis)** | Analyzed demographics, card category, income, churn distribution. |
| **3. Behavioral Analysis** | Compared transaction behavior and credit utilization between existing vs attrited customers. |
| **4. Feature Engineering** | Created **Engagement Score**, `Avg_Transaction_Value`, and % utilization metrics. |
| **5. RFM Segmentation** | Built Recency–Frequency–Monetary scores (1–4 scale) → 9 business segments. |
| **6. Profitability Modeling** | Revenue = 1.5% of transaction spend; Cost = servicing + capital charge. |
| **7. Churn & Retention Analytics** | Computed churn by segment and identified at-risk cohorts. |
| **8. K-Means Clustering (Advanced Layer)** | Clustered customers (K=5, silhouette=0.20) → “Premium High-Value”, “Growing Mid-Tier”, etc. |

---

## 📊 Key Insights & Visuals

### 1️⃣ Portfolio Overview
- 16.1% attrition rate; majority are Blue cardholders.  
- Income group **< ₹40K** dominates base (~34%).  
- Gender distribution nearly balanced (53% F, 47% M).

### 2️⃣ Transaction Behavior
- Attrited customers show lower transaction counts, credit limits, and utilization ratios.  
- Transaction count (`Total_Trans_Ct`) has **0.81 correlation** with revenue.

### 3️⃣ Segmentation Summary (RFM-Based)
| Segment | % of Customers | Key Traits |
|----------|----------------|-------------|
| **Need Attention** | 19.2% | Moderate engagement, 24% churn |
| **Potential Loyalists** | 18.8% | Stable, profitable mid-tier |
| **Loyal Customers** | 11.8% | High value, low churn |
| **At Risk** | 11.7% | Declining engagement, watchlist |
| **Champions** | 4.1% | Most profitable, highest engagement |
| **Lost / Hibernating** | ~22% combined | Very low ROI |
| **Cannot Lose Them** | 1.3% | High churn (72%), urgent focus |

---
## 🤖 Predictive Modeling – Churn Propensity

| Metric | Score |
|---------|--------|
| **Accuracy** | 95% |
| **ROC-AUC** | 0.93 |
| **Precision (Churn)** | 0.88 |
| **Recall (Churn)** | 0.84 |

**Top Predictors of Churn:**
1. Lower Engagement Score  
2. Fewer Transactions  
3. High Months Inactive  
4. Low Credit Utilization

## 💰 Profitability Analysis
| Segment | Avg. Transaction Amt | Total Revenue ($) | Churn % |
|----------|---------------------|------------------|---------|
| Loyal Customers | 10,183 | **12.2M** | 2.1 |
| Potential Loyalists | 4,444 | **8.4M** | 2.4 |
| At Risk | 4,754 | **5.6M** | 6.1 |
| Need Attention | 2,633 | **5.1M** | 24.0 |
| Champions | 10,558 | **4.4M** | 0.2 |
| Hibernating | 3,053 | 3.4M | 39.3 |
| New Customers | 2,471 | 2.6M | 9.6 |
| Lost | 1,589 | 1.8M | 32.0 |
| Cannot Lose Them | 6,454 | 0.86M | **72.4** |

🔹 **Top 35% of customers drive >75% of revenue.**  
🔹 “Need Attention” and “Hibernating” are **high-risk but recoverable** segments.  
🔹 “Cannot Lose Them” have high credit limits but minimal engagement → targeted recovery needed.

---

## 🔬 K-Means Cluster Analysis
**Optimal K = 5 (Silhouette ≈ 0.20)**  
Clusters were named as follows:

| Cluster | Size | Avg Engagement | Churn % | Label |
|----------|------|----------------|----------|--------|
| 3 & 4 | 3,800 | 83–92 | 3–6 | **Premium High-Value** |
| 2 | 2,127 | 39 | 12 | **Growing Mid-Tier** |
| 0 | 2,767 | 38 | 35 | **Standard Active** |
| 1 | 1,434 | 36 | 15 | **Low Engagement** |

---

## 🧭 Business Recommendations
| Segment | Suggested Action | Objective |
|----------|------------------|------------|
| **Champions / Loyal** | Offer tier upgrades, co-branded cards | Strengthen loyalty |
| **Potential Loyalists** | Cross-sell EMI/auto-debit | Increase spend frequency |
| **Need Attention** | Personalized reactivation offers | Prevent churn |
| **Hibernating / Lost** | Digital-only outreach | Cost efficiency |
| **Cannot Lose Them** | High-touch retention via RM calls | Recover profitability |

---

## 📈 Business Impact
- Enables **targeted retention** focusing on 40% of customers who drive 85% profit.  
- Potential **profitability lift of 10–15%** through optimized customer engagement.  
- Framework can be directly used by BIU for portfolio monitoring.

---

## 🧰 Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn

---










