import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
#import dataseet
    st.subheader("Dataset of WN Logistics Shipment From 2021 - 2024")
    df = pd.read_csv('dataset.csv')
    st.dataframe (df)

#eda 1
    st.subheader("A. Total Shipment Based on Month From 2021 - 2024")

    total_shipment = df.groupby('month_shipment').size()
    total_shipment

    x = total_shipment.index.astype(str)
    y = total_shipment.values

    fig = plt.figure(figsize=(15,6))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.title('Total Shipment Based on Month From 2021 - 2024')
    plt.xlabel('Month-Year')
    plt.ylabel('Total Shipment')
    plt.tight_layout()
    st.pyplot(fig)
    
    st.caption("From analysis above, we can see the average of total shipments are above 600 shipments per months. " \
                    "we can see on February for each year, the total shipment was decrease compare to other months. " \
                    "This can be caused by the number of days in February only 28 days and 29 days on 2024 (leap year).")

#eda 2
    st.subheader("B. Shipment Delay Trend From 2021 - 2024")

    delay_avg = df.groupby('month_shipment')['delay_probability'].mean()
    fig = plt.figure(figsize=(15, 7))
    delay_avg.plot(kind='line', marker='o')
    plt.title('Average Delay Probability Trend per Month From 2021 - 2024')
    plt.xlabel('Month-Year')
    plt.ylabel('Average Delay Probability')
    plt.ylim(0, 1)
    plt.grid(True)
    plt.tight_layout()

    st.pyplot(fig)
    
    st.caption("From analysis above, we can see the trend of shipment delay from 2021-2024 is showing a stable performance. " \
                    "The average range of delay probablity from 2021-2024 is 0.6 - 0.8 (Moderate-High Risk). Compare from previous years, the delay trend in 2024 is showing lower probability. " \
                    "Through this analysis, the company aim to decrease the delay by reaching the delay probability to 0 (Low Risk).")
    
#eda 3
    st.subheader("C. Proportion of Each Delay Category")
    counts_delay = df['delay_category'].value_counts()

    fig = plt.figure(figsize=(7,7))
    counts_delay.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Proportion of Delay Categories')
    plt.ylabel('') 

    st.pyplot(fig)
    
    st.caption("From analysis above, we can see the company still have High Risk as the highest for Delay probability from all shipments count for 61.5%. " \
                "The low risk still hold the lowest percentage for 17.6% and moderate risk still hold the lowest percentage for 20.9% .")
    


#eda 4
    st.subheader("D. Delay Category Counts by Year")
    delay_trend = df.groupby('year')['delay_category'].value_counts().reset_index(name='count')
    fig = plt.figure(figsize=(10,6))
    ax = sns.barplot(x='year', y='count', hue='delay_category', data=delay_trend)
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)
    plt.title('Delay Category Counts by Year')
    plt.ylabel('Count')

    st.pyplot(fig)
    
    st.caption("From this visualization, it shows the number of High Risk delay is decreasing and the number of Low Risk delay is increasing gradually. " \
                "This trend shows a good progress for the company. " \
                "Hopefully, the trend for High Risk can keep decreasing and Low Risk can keep increasing on the following years. " \
                "The percentage of shipment delay is expected to decrease up to 5% in the next year.")

#eda 5
    st.subheader("E. Weather Severity & Delay Probability per Month")

    weather_trend = df.groupby(['month'])[['weather_condition_severity', 'delay_probability']].median().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weather_trend['month'], weather_trend['weather_condition_severity'], marker='o', label='Weather Severity', color='skyblue')
    ax.plot(weather_trend['month'], weather_trend['delay_probability'], marker='s', label='Delay Probability', color='tomato')

    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    ax.set_title('Weather Severity & Delay Probability per Month')
    ax.set_xticks(range(1, 13))
    ax.set_ylim(0.3, 1)
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    st.pyplot(fig)

    st.caption("Both the weather severity and delay probability show relatively stable trends throughout the year, indicating no significant seasonal spikes affecting the delay. " \
                "However, during Q3 (June to September), there is a noticeable fluctuation in weather severity. " \
                "Hopefully, the trend for High Risk can keep decreasing and Low Risk can keep increasing on the following years. " \
                "Interestingly, despite the weather severity fluctuating in Q3, the delay probability remains relatively stable, suggesting that delays are not solely driven by weather severity." \
                "Eventhough so, operational mitigation strategies can be prepared when entering Q3 period.")
