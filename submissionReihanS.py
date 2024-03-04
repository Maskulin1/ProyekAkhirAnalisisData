import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')


# Function to create rental trends over time
def create_rentals_over_time(df):
    df['dteday'] = pd.to_datetime(df['dteday'])
    monthly_df = df.resample('ME', on='dteday').sum()
    return monthly_df

# Function to aggregate bike rentals based on seasonal data framework
def aggregate_by_season(df):
    season_agg = df.groupby("season_x").agg({
        "instant_x": "nunique",
        "cnt_x": ["max", "min"]
    })
    return season_agg


# Function to aggregate bike rentals based on monthly data framework
def aggregate_by_month(df):
    monthly_agg = df.groupby("mnth_x").agg({
        "instant_x": "nunique",
        "cnt_x": ["max", "min"]
    })
    return monthly_agg


# Function to aggregate bike rentals based on daily data framework
def aggregate_by_day(df):
    weekday_agg = df.groupby("weekday_x").agg({
        "instant_x": "nunique",
        "cnt_x": ["max", "min"]
    })
    return weekday_agg


# Function to aggregate bike rentals based on hourly data framework
def aggregate_by_hour(df):
    hourly_agg = df.groupby("hr").agg({
        "instant_y": "nunique",
        "cnt_y": ["max", "min"]
    })
    return hourly_agg


# Load CSV files
all_df = pd.read_csv("all_data.csv")
datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

with st.sidebar:
    # Adding header
    st.header("Dashboard Rent Bike", divider='red')
    # Adding logo
    st.image(
        "https://st4.depositphotos.com/4881653/19685/v/1600/depositphotos_196857636-stock-illustration-bike-rental-bicycle-sign-for.jpg")
    st.subheader("by Reihan Septyawan")

# Create Dataframes
rents_over_time_df = create_rentals_over_time(all_df)
byseason_df = aggregate_by_season(all_df)
bymonth_df = aggregate_by_month(all_df)
byday_df = aggregate_by_day(all_df)
byhour_df = aggregate_by_hour(all_df)

# Visualization of Bike Rentals Over Time (Aggregated by Month)
st.subheader("Bike Rentals Over Time")
plt.figure(figsize=(10, 6))
plt.plot(rents_over_time_df.index, rents_over_time_df['cnt_x'], color='#6499E9')
plt.xlabel('Month')
plt.ylabel('Number of Bike Rentals')
plt.title('Bike Rentals Over Time (Aggregated by Month)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Visualization of Bike Rentals by Season
st.subheader('Bike Rentals by Season')
plt.figure(figsize=(10, 6))
x = byseason_df.index
y_max = byseason_df[('cnt_x', 'max')]
y_min = byseason_df[('cnt_x', 'min')]
plt.bar(x, y_max, label='Max Rentals', color='#6499E9')
plt.bar(x, y_min, label='Min Rentals', color='orange')
season_labels = ['Season 1', 'Season 2', 'Season 3', 'Season 4']
plt.xticks(x, season_labels)
plt.xlabel('Season')
plt.ylabel('Number of Bike Rentals')
plt.title('Max and Min Bike Rentals by Season')
plt.legend()
for i, (max_val, min_val) in enumerate(zip(y_max, y_min)):
    plt.text(i + 1, max_val, str(max_val), ha='center', va='bottom', fontweight='bold')
    plt.text(i + 1, min_val, str(min_val), ha='center', va='bottom', fontweight='bold')
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Visualization of Bike Rentals by Month
st.subheader("Bike Rentals by Month")
plt.figure(figsize=(10, 6))
x = bymonth_df.index
y_max = bymonth_df[('cnt_x', 'max')]
y_min = bymonth_df[('cnt_x', 'min')]
plt.bar(x, y_max, label='Max Rentals', color='#6499E9')
plt.bar(x, y_min, label='Min Rentals', color='orange')
plt.xlabel('Month')
plt.ylabel('Number of Bike Rentals')
plt.title('Max and Min Bike Rentals per Month')
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(x, month_labels)
plt.legend()
for i, (max_val, min_val) in enumerate(zip(y_max, y_min)):
    plt.text(i + 1, max_val, str(max_val), ha='center', va='bottom', fontweight='bold')
    plt.text(i + 1, min_val, str(min_val), ha='center', va='bottom', fontweight='bold')
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Visualization of Bike Rentals by Day of the Week
st.subheader('Bike Rentals by Day of the Week')
plt.figure(figsize=(10, 6))
x = byday_df.index
y_max = byday_df[('cnt_x', 'max')]
y_min = byday_df[('cnt_x', 'min')]
plt.bar(x, y_max, label='Max Rentals', color='#6499E9')
plt.bar(x, y_min, label='Min Rentals', color='orange')
plt.xlabel('Day')
plt.ylabel('Number of Bike Rentals')
plt.title('Max and Min Bike Rentals by Day')
plt.xticks(rotation=0)
plt.legend()
for i, (max_val, min_val) in enumerate(zip(y_max, y_min)):
    plt.text(i, max_val, str(max_val), ha='center', va='bottom', fontweight='bold')
    plt.text(i, min_val, str(min_val), ha='center', va='bottom', fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Visualization of Bike Rentals by Hour
st.subheader('Bike Rentals by Hour')
plt.figure(figsize=(10, 6))
x = byhour_df.index
y_max = byhour_df[('cnt_y', 'max')]
y_min = byhour_df[('cnt_y', 'min')]
plt.bar(x, y_max, label='Max Rentals', color='#6499E9')
plt.bar(x, y_min, label='Min Rentals', color='orange')
plt.xlabel('Hour')
plt.ylabel('Number of Bike Rentals')
plt.title('Max and Min Bike Rentals per Hour')
hour_labels = [str(i) for i in x]
plt.xticks(x, hour_labels)
plt.legend()

for i, (max_val, min_val) in enumerate(zip(y_max, y_min)):
    plt.text(i, max_val, str(max_val), ha='center', va='bottom', fontweight='bold')
    plt.text(i, min_val, str(min_val), ha='center', va='bottom', fontweight='bold')
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)
