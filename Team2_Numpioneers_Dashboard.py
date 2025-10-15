import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import streamlit as st
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        .stApp {
            background-color: white;
            color: black;
        }
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: black !important;
        }
        .stMarkdown, .stSubheader, .stHeader, .stText {
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


patients_file="patients_cleaned_file.csv"
demographics_file="demographics_cleaned.csv"


final_df=pd.read_csv(patients_file, parse_dates=["DateTime"],dtype={"Patient_ID":"string"})
demographics=pd.read_csv(demographics_file,dtype={"Patient_ID": "string","Gender":"string","Race":"string"}) 

# -------------------------
# Title
# -------------------------


st.markdown("<h1 style='text-align: center; color: black'>Type 1 Diabetes Analysis</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='color: black;'>Descriptive Analysis</h2>", unsafe_allow_html=True)



# -------------------------
# Percentage of male and female
# -------------------------

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Gender Distribution")
        fig1, ax1 = plt.subplots(figsize=(2,2))
        gender_percentages = demographics['Gender'].value_counts(normalize=True) * 100
        labels = gender_percentages.index.tolist()
        sizes = gender_percentages.values
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                startangle=90, colors=['skyblue','lightcoral'], explode=(0.1,0), radius=1.2,textprops={'fontsize': 5}        
)
        ax1.axis('equal')
        plt.tight_layout()
        st.pyplot(fig1, use_container_width=True)
        st.markdown("This chart shows the proportion of male and female patients. "
                    "Males make up the majority, while females represent a smaller fraction.")


#---------------------------------------
# --- Boxplot (Heart Rate by Patient) ---
#---------------------------------------


with col2:
    with st.container(border=True):
        st.subheader("Heart Rate Distribution by Patients")
        fig2, ax2 = plt.subplots(figsize=(10,10))
        df_split_time = final_df['DateTime'].dt.strftime('%Y-%m-%d')
        Heart_Rate = final_df.groupby(['Patient_ID', df_split_time])['Heart Rate(BPM)'].mean().reset_index()
        sns.boxplot(x="Patient_ID", y="Heart Rate(BPM)", data=Heart_Rate, ax=ax2, color="green")
        ax2.set_xlabel("Patient ID")
        ax2.set_ylabel("Heart Rate (BPM)")
        ax2.tick_params(axis="x", rotation=45)
        plt.tight_layout()
        st.pyplot(fig2, use_container_width=True)
        st.markdown("This boxplot illustrates heart rate variability across patients. "
                    "Some patients have consistently higher average heart rates, "
                    "while others show wider variation.")
    
# -------------------------
# Time windows where glucose spikes are more frequent,and how do they relate to carb input
# -------------------------

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("Glucose spikes vs Carb intake by Hour of Day")
        
        # 1. Extract hour of day
        final_df["Hour"] = final_df["DateTime"].dt.hour
        
        # 2. Define glucose spike (threshold >180)
        final_df["Glucose_Spike"] = (final_df["Glucose(mg/dL)"] > 180).astype(int)
        
        # 3. Aggregate by hour: % spikes and avg carbs
        time_summary = final_df.groupby("Hour").agg(
            Spike_Freq=("Glucose_Spike", "mean"),   # proportion of readings that are spikes
            Avg_Carb=("Carb Intake (grams)", "mean")
        ).reset_index()
        
        # Convert spike frequency to %
        time_summary["Spike_Freq(%)"] = (time_summary["Spike_Freq"] * 100).round(2)
        
        # Optional: show data
        #st.dataframe(time_summary)
        
        # 4. Plot spikes and carb intake across hours
        fig, ax1 = plt.subplots(figsize=(12,11))
        
        # Bar plot for carb intake
        sns.barplot(x="Hour", y="Avg_Carb", data=time_summary, color="skyblue", ax=ax1, alpha=0.6)
        ax1.set_ylabel("Average Carb Intake (grams)", color="blue")
        
        # Line plot for spike frequency
        ax2 = ax1.twinx()
        sns.lineplot(x="Hour", y="Spike_Freq(%)", data=time_summary, color="red", marker="o", ax=ax2)
        ax2.set_ylabel("Spike Frequency (%)", color="red")
        
        # Show in Streamlit
        st.pyplot(fig, use_container_width=True)
        st.markdown("When analyzed by hour, the highest spike frequency (26%) occurred in the evening (7–9 PM), which coincides with higher carb intake from dinner.Moderate spikes were also seen after breakfast (8–10 AM) and lunch (12–1 PM), aligning with mealtime carb intake.The lowest spike frequency (15%) was in mid-afternoon (2–3 PM), when carb intake is minimal")

with col4:
    with st.container(border=True):
        st.subheader("Sleep Duration Distribution by Glucose Control")
        merged_df = pd.merge(final_df, demographics, on='Patient_ID', how ='left')

        merged_df['glucose_control'] = np.where(merged_df['Glucose(mg/dL)'] > 180, 'Poor', 'Good')

        # Count number of samples per group
        counts = merged_df['glucose_control'].value_counts()
        print(counts)
        # Data
        labels = ['Good', 'Poor']
        counts = [242954, 66438]
        
        # Setup
        fig4 = plt.figure(figsize=(8,2))
        ax4 = fig4.add_subplot(111, projection='3d')
        
        x = np.arange(len(labels))  # x locations
        y = np.zeros(len(labels))   # single row (y=0)
        
        # Bar plot
        ax4.bar3d(x, y, np.zeros(len(labels)), 0.5, 0.5, counts, color=['#66c2a5','#fc8d62'])
        
        # Labels with reduced font size
        ax4.set_xticks(x)
        ax4.set_xticklabels(labels, fontsize=4)   # 👈 smaller x-axis labels
        ax4.set_ylabel("Category", fontsize=4)    # 👈 smaller y label
        ax4.set_zlabel("Count", fontsize=4)       # 👈 smaller z label

        # Reduce tick label sizes on all axes
        ax4.tick_params(axis='x', labelsize=4)
        ax4.tick_params(axis='y', labelsize=4)
        ax4.tick_params(axis='z', labelsize=4)

        st.pyplot(fig4, use_container_width=True)

        st.markdown(
            "Sleep deprivation is known to impair glucose metabolism and increase insulin resistance. "
            "If your data shows that patients with elevated glucose levels consistently sleep less, "
            "this could justify recommending longer sleep durations as part of their diabetes management plan."
        )

# -------------------------
# Charts Row 2 (side by side)
# -------------------------
col5, col6= st.columns(2)

with col5:
    with st.container(border=True):
        st.subheader("Mean Glucose Levels Across Heart Rate Groups")
        df_merged = pd.merge(final_df, demographics, on='Patient_ID', how='left')

        # Define bins & labels
        hr_bins = [0, 60, 80, 100, 120, 140, 200]
        hr_labels = ['<60','60-80','81-100','101-120','121-140','140+']
        df_merged['HR_Group'] = pd.cut(
            df_merged['Heart Rate(BPM)'], 
            bins=hr_bins, 
            labels=hr_labels, 
            right=False
        )

        # Aggregate mean glucose per HR group
        df_hr_glucose = df_merged.groupby('HR_Group')['Glucose(mg/dL)'].mean().reset_index()

        # Color palette
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

        # Create figure
        fig5, ax5 = plt.subplots(figsize=(9,7))

        # Line plot
        sns.lineplot(
            x='HR_Group', 
            y='Glucose(mg/dL)', 
            data=df_hr_glucose, 
            marker='o',
            color="black",    # base line in black
            linewidth=2,
            ax=ax5
        )

        # Add big colored points
        for i, val in enumerate(df_hr_glucose['Glucose(mg/dL)']):
            ax5.scatter(
                df_hr_glucose['HR_Group'][i], 
                val, 
                s=150, 
                color=colors[i], 
                alpha=0.9,
                edgecolor="black"
            )

        # Labels and title
        #ax5.set_title("Mean Glucose Levels Across Heart Rate Groups", fontsize=16, fontweight='bold', color="black")
        ax5.set_xlabel("Heart Rate Group (BPM)", fontsize=12, color="black")
        ax5.set_ylabel("Mean Glucose (mg/dL)", fontsize=12, color="black")
        ax5.grid(True, linestyle='--', alpha=0.5)

        # Show in Streamlit
        st.pyplot(fig5, use_container_width=True)
        st.markdown("Heart rate reflects physical activity and physiological stress, both affecting glucose Identifying heart rate ranges linked to stable glucose helps guide exercise, stress management, and monitoring")

       # st.dataframe(df_hr_glucose.describe(include='all'))


with col6:
    with st.container(border=True):
        st.subheader("Mean Glucose Levels by Age Group")

        # Group patients by age and calculate mean glucose
        df_age_glucose = df_merged.groupby(['Patient_ID', 'Age'])['Glucose(mg/dL)'].mean().reset_index()

        # Bin ages
        age_bins = [0, 30, 50, 65, 100]
        age_labels = ['<30', '30-50', '51-65', '65+']
        df_age_glucose['Age_Group'] = pd.cut(
            df_age_glucose['Age'], 
            bins=age_bins, 
            labels=age_labels, 
            right=False
        )

        # Show summary statistics in Streamlit
        #st.markdown("**Summary Statistics by Age Group**")
        #st.dataframe(df_age_glucose.groupby('Age_Group')['Glucose(mg/dL)'].describe())

        # Visualization
        fig6, ax6 = plt.subplots(figsize=(8,6))
        sns.boxplot(
            x='Age_Group', 
            y='Glucose(mg/dL)', 
            data=df_age_glucose, 
            palette='Set2',
            ax=ax6
        )

        #ax6.set_title("Mean Glucose Levels by Age Group", fontsize=14, fontweight="bold", color="black")
        ax6.set_ylabel("Mean Glucose (mg/dL)", fontsize=12, color="black")
        ax6.set_xlabel("Age Group", fontsize=12, color="black")
        ax6.grid(True, linestyle="--", alpha=0.5)

        # Show in Streamlit
        st.pyplot(fig6, use_container_width=True)

        # Explanation
        st.markdown(
            "This chart shows how **average glucose levels vary by age group**. "
            "The boxplots represent distribution per group, with potential outliers visible."
        )



