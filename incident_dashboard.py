
import streamlit as st   # Streamlit → build web dashboard
import pandas as pd      # Pandas → data handling
import matplotlib.pyplot as plt   # Matplotlib → charts
import seaborn as sns    # Seaborn → heatmap

# -----------------------------
# Page Configuration (UI setup)
# -----------------------------
st.set_page_config(page_title="Incident Dashboard", layout="wide")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Incident Analysis Dashboard")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("cleaned_incidents.csv")

# Convert date columns to datetime
df["Created_Date"] = pd.to_datetime(df["Created_Date"])
df["Resolved_Date"] = pd.to_datetime(df["Resolved_Date"])

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📋 Dataset Preview")
st.write(df.head())

# -----------------------------
# Filters Section
# -----------------------------
st.subheader("🎛 Filters")

# Category filter (FIXED: Category not category)
category = st.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].dropna().unique())
)

# Priority filter
priority = st.selectbox(
    "Select Priority",
    ["All"] + list(df["Priority"].dropna().unique())
)

# Apply filters
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if priority != "All":
    filtered_df = filtered_df[filtered_df["Priority"] == priority]

# -----------------------------
# Key Metrics
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

total_incidents = len(filtered_df)

sla_met = (filtered_df["SLA_Status"] == "Met").mean() * 100
if pd.isna(sla_met):
    sla_met = 0

avg_time = filtered_df["Resolution_Time"].mean()
if pd.isna(avg_time):
    avg_time = 0

with col1:
    st.metric("Total Incidents", total_incidents)

with col2:
    st.metric("SLA Met %", f"{sla_met:.2f}%")

with col3:
    st.metric("Avg Resolution (days)", f"{avg_time:.2f}")

# -----------------------------
# Incident Trend
# -----------------------------
st.subheader("📈 Incident Trend")

trend = filtered_df.groupby(filtered_df["Created_Date"].dt.date).size()

fig1, ax1 = plt.subplots()
trend.plot(ax=ax1)

ax1.set_xlabel("Date")
ax1.set_ylabel("Number of Incidents")
ax1.set_title("Incidents Over Time")

st.pyplot(fig1)

# -----------------------------
# SLA Distribution (Pie Chart)
# -----------------------------
st.subheader("🟢 SLA Distribution")

sla_counts = filtered_df["SLA_Status"].value_counts()

fig2, ax2 = plt.subplots()
sla_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)

ax2.set_title("SLA Distribution")
ax2.set_ylabel("")

st.pyplot(fig2)

# -----------------------------
# Priority & Category Charts (Side-by-side)
# -----------------------------
st.subheader("📊 Analysis Charts")

col1, col2 = st.columns(2)

# Priority Chart
priority_counts = filtered_df["Priority"].value_counts()

fig3, ax3 = plt.subplots()
priority_counts.plot(kind="bar", ax=ax3)

ax3.set_title("Incidents by Priority")
ax3.tick_params(axis='x', rotation=45)

with col1:
    st.pyplot(fig3)

# Category Chart
cat_counts = filtered_df["Category"].value_counts().head(10)

fig4, ax4 = plt.subplots()
cat_counts.plot(kind="bar", ax=ax4)

ax4.set_title("Top Categories")
ax4.tick_params(axis='x', rotation=45)

with col2:
    st.pyplot(fig4)

# -----------------------------
# Priority vs SLA Heatmap
# -----------------------------
st.subheader("🔥 Priority vs SLA Analysis")

pivot = pd.crosstab(filtered_df["Priority"], filtered_df["SLA_Status"])

st.write(pivot)

fig5, ax5 = plt.subplots()
sns.heatmap(pivot, annot=True, fmt="d", cmap="coolwarm", ax=ax5)

st.pyplot(fig5)

# -----------------------------
# Insights Section
# -----------------------------
st.subheader("📊 Insights")

st.write(f"Total Incidents: {total_incidents}")
st.write(f"SLA Met Percentage: {sla_met:.2f}%")
st.write(f"Average Resolution Time: {avg_time:.2f} days")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.write("✅ Built using Streamlit | Incident Analysis Dashboard")
