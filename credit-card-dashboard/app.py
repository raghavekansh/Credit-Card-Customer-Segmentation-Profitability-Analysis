
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(page_title="Credit Card Portfolio Analytics", 
                   page_icon="💳", 
                   layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("credit_card_analytics_complete.csv")
    return df

df = load_data()

# Title and description
st.title("💳 Credit Card Portfolio Analytics Dashboard")
st.markdown("### Business Intelligence Unit - Customer Segmentation & Profitability Analysis")
st.markdown("---")

# Executive Summary Metrics (Top Row)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Customers", f"{len(df):,}")
    
with col2:
    churn_rate = (df['Attrition_Flag'] == 'Attrited Customer').sum() / len(df) * 100
    st.metric("Churn Rate", f"{churn_rate:.2f}%", delta="-2.3%", delta_color="inverse")
    
with col3:
    total_revenue = df['Total_Revenue'].sum()
    st.metric("Total Revenue", f"${total_revenue/1e6:.2f}M")
    
with col4:
    total_profit = df['Net_Profit'].sum()
    st.metric("Net Profit", f"${total_profit/1e6:.2f}M")
    
with col5:
    avg_clv = df['Customer_Lifetime_Value'].mean()
    st.metric("Avg CLV", f"${avg_clv:.0f}")

st.markdown("---")

# Create tabs for different views
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "🎯 Segmentation", "💰 Profitability", "⚠️ Churn Analysis", "🔍 Deep Dive"])

with tab1:
    st.header("Portfolio Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Customer Segment Distribution
        segment_dist = df['Customer_Segment'].value_counts()
        fig = px.pie(values=segment_dist.values, 
                     names=segment_dist.index,
                     title='Customer Segment Distribution',
                     hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Profitability Tier Distribution
        tier_dist = df['Profitability_Tier'].value_counts()
        fig = px.bar(x=tier_dist.index, y=tier_dist.values,
                     title='Profitability Tier Distribution',
                     labels={'x': 'Tier', 'y': 'Customer Count'})
        fig.update_traces(marker_color='#3498db')
        st.plotly_chart(fig, use_container_width=True)
    
    # Transaction behavior
    st.subheader("Transaction Behavior by Attrition Status")
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.box(df, x='Attrition_Flag', y='Total_Trans_Amt',
                     title='Transaction Amount Distribution',
                     color='Attrition_Flag')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(df, x='Attrition_Flag', y='Total_Trans_Ct',
                     title='Transaction Count Distribution',
                     color='Attrition_Flag')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Customer Segmentation Analysis")
    
    # Segment metrics
    segment_metrics = df.groupby('Customer_Segment').agg({
        'CLIENTNUM': 'count',
        'Total_Trans_Amt': 'mean',
        'Customer_Lifetime_Value': 'mean',
        'Net_Profit': 'mean',
        'Engagement_Score': 'mean'
    }).round(2)
    segment_metrics.columns = ['Count', 'Avg Trans Amt', 'Avg CLV', 'Avg Net Profit', 'Avg Engagement']
    
    st.dataframe(segment_metrics.sort_values('Avg CLV', ascending=False), use_container_width=True)
    
    # Revenue by segment
    st.subheader("Revenue Contribution by Segment")
    segment_revenue = df.groupby('Customer_Segment')['Total_Revenue'].sum().sort_values(ascending=False)
    fig = go.Figure(go.Bar(
        x=segment_revenue.index,
        y=segment_revenue.values,
        marker=dict(color=segment_revenue.values, colorscale='Viridis', showscale=True)
    ))
    fig.update_layout(title='Total Revenue by Customer Segment',
                      xaxis_title='Segment', yaxis_title='Revenue ($)')
    st.plotly_chart(fig, use_container_width=True)
    
    # RFM Analysis
    col1, col2 = st.columns(2)
    with col1:
        fig = px.scatter(df, x='F_Score', y='M_Score', color='R_Score',
                         title='RFM Score Distribution',
                         labels={'F_Score': 'Frequency', 'M_Score': 'Monetary', 'R_Score': 'Recency'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.histogram(df, x='RFM_Score', nbins=30,
                          title='RFM Score Distribution',
                          labels={'RFM_Score': 'RFM Score'})
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Profitability Analysis")
    
    # CLV Distribution
    st.subheader("Customer Lifetime Value Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        clv_by_segment = df.groupby('Customer_Segment')['Customer_Lifetime_Value'].mean().sort_values(ascending=False)
        fig = go.Figure(go.Bar(
            x=clv_by_segment.index,
            y=clv_by_segment.values,
            marker=dict(color='#2ecc71')
        ))
        fig.update_layout(title='Average CLV by Segment', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(df, x='Profitability_Tier', y='Customer_Lifetime_Value',
                     title='CLV Distribution by Tier',
                     color='Profitability_Tier')
        st.plotly_chart(fig, use_container_width=True)
    
    # Profit margin analysis
    st.subheader("Profitability Metrics by Segment")
    profit_metrics = df.groupby('Customer_Segment').agg({
        'Total_Revenue': 'sum',
        'Total_Cost': 'sum',
        'Net_Profit': 'sum',
        'ROI_%': 'mean'
    }).round(0)
    st.dataframe(profit_metrics.sort_values('Net_Profit', ascending=False), use_container_width=True)
    
    # ROI visualization
    fig = px.bar(profit_metrics.reset_index(), x='Customer_Segment', y='ROI_%',
                 title='Average ROI by Customer Segment',
                 labels={'ROI_%': 'ROI (%)', 'Customer_Segment': 'Segment'})
    fig.update_traces(marker_color='#9b59b6')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Churn Analysis & Risk Assessment")
    
    # Churn rate by segment
    churn_by_segment = df.groupby('Customer_Segment')['Attrition_Flag'].apply(
        lambda x: (x == 'Attrited Customer').sum() / len(x) * 100
    ).sort_values(ascending=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure(go.Bar(
            x=churn_by_segment.index,
            y=churn_by_segment.values,
            marker=dict(color=churn_by_segment.values, colorscale='Reds', showscale=True)
        ))
        fig.update_layout(title='Churn Rate by Segment (%)', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Value matrix
        value_matrix_dist = df['Value_Matrix'].value_counts()
        fig = px.pie(values=value_matrix_dist.values,
                     names=value_matrix_dist.index,
                     title='Customer Value Matrix',
                     hole=0.3)
        st.plotly_chart(fig, use_container_width=True)
    
    # High-risk customers
    st.subheader("High-Risk Segment Details")
    high_risk = df[df['Customer_Segment'].isin(['Cannot Lose Them', 'Hibernating', 'At Risk', 'Lost'])]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("High-Risk Customers", f"{len(high_risk):,}")
    with col2:
        st.metric("At-Risk Revenue", f"${high_risk['Total_Revenue'].sum()/1e6:.2f}M")
    with col3:
        st.metric("Potential Loss", f"${high_risk[high_risk['Attrition_Flag']=='Attrited Customer']['Net_Profit'].sum()/1e6:.2f}M")

with tab5:
    st.header("Deep Dive Analysis")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_segment = st.multiselect("Select Segment", 
                                         options=df['Customer_Segment'].unique(),
                                         default=df['Customer_Segment'].unique()[:3])
    
    with col2:
        selected_tier = st.multiselect("Select Profitability Tier",
                                      options=df['Profitability_Tier'].unique(),
                                      default=df['Profitability_Tier'].unique())
    
    with col3:
        attrition_filter = st.selectbox("Attrition Status",
                                       options=['All', 'Existing Customer', 'Attrited Customer'])
    
    # Filter data
    filtered_df = df.copy()
    if selected_segment:
        filtered_df = filtered_df[filtered_df['Customer_Segment'].isin(selected_segment)]
    if selected_tier:
        filtered_df = filtered_df[filtered_df['Profitability_Tier'].isin(selected_tier)]
    if attrition_filter != 'All':
        filtered_df = filtered_df[filtered_df['Attrition_Flag'] == attrition_filter]
    
    st.subheader(f"Filtered Data: {len(filtered_df):,} customers")
    
    # Scatter plot: CLV vs Transaction Amount
    fig = px.scatter(filtered_df, 
                     x='Total_Trans_Amt', 
                     y='Customer_Lifetime_Value',
                     color='Customer_Segment',
                     size='Credit_Limit',
                     hover_data=['Profitability_Tier', 'Engagement_Score'],
                     title='CLV vs Transaction Amount',
                     labels={'Total_Trans_Amt': 'Total Transaction Amount ($)',
                            'Customer_Lifetime_Value': 'CLV ($)'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed table
    st.subheader("Customer Details")
    display_cols = ['CLIENTNUM', 'Customer_Segment', 'Total_Trans_Amt', 'Customer_Lifetime_Value',
                   'Net_Profit', 'Profitability_Tier', 'Attrition_Flag']
    st.dataframe(filtered_df[display_cols].head(100), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Credit Card Portfolio Analytics Dashboard** | Developed for Axis Bank BIU | Powered by Python & Streamlit")
