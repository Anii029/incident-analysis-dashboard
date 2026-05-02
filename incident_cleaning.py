import pandas as pd

# Load dataset
df = pd.read_csv("incident_event_log.csv")

print("Original shape:", df.shape)

# -----------------------------
# Select important columns
# -----------------------------
df = df[[
    "number",
    "opened_at",
    "resolved_at",
    "closed_at",
    "priority",
    "category",
    "assignment_group",
    "made_sla"
]]

# -----------------------------
# Remove duplicates (one row per incident)
# -----------------------------
df = df.drop_duplicates(subset="number", keep="last")

print("After removing duplicates:", df.shape)

# -----------------------------
# Rename columns
# -----------------------------
df.rename(columns={
    "number": "Incident_ID",
    "opened_at": "Created_Date",
    "resolved_at": "Resolved_Date",
    "assignment_group": "Assigned_To",
    "made_sla": "SLA_Status"
}, inplace=True)

# -----------------------------
# Convert dates (IMPORTANT)
# -----------------------------
df["Created_Date"] = pd.to_datetime(df["Created_Date"], dayfirst=True, errors="coerce")
df["Resolved_Date"] = pd.to_datetime(df["Resolved_Date"], dayfirst=True, errors="coerce")

# -----------------------------
# Create Resolution Time
# -----------------------------
df["Resolution_Time"] = (df["Resolved_Date"] - df["Created_Date"]).dt.days

# -----------------------------
# Clean SLA column
# -----------------------------
df["SLA_Status"] = df["SLA_Status"].map({
    True: "Met",
    False: "Breached"
})

# -----------------------------
# Handle missing values
# -----------------------------
df["Category"] = df["category"].fillna("Other")
df["Priority"] = df["priority"].fillna("Medium")

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv("cleaned_incidents.csv", index=False)

print("✅ Cleaned dataset saved as cleaned_incidents.csv")