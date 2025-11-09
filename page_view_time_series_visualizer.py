import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv")

print(df.head())

input("Press Enter to exit...")
# Clean the data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]
print(df.head())
print(df.shape) 

# Draw line plot
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['value'], color='red')
plt.title('Daily freeCodeCamp Forum Page Views 2016–2019')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.show()

# Add columns for year and month
df['year'] = pd.to_datetime(df['date']).dt.year
df['month'] = pd.to_datetime(df['date']).dt.month
# Create a new DataFrame for monthly average
df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
# Draw the bar plot
df_bar.plot(kind='bar', figsize=(10, 6))
plt.title('Average Daily Page Views per Month')
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.legend(title='Month', loc='upper left')
plt.show()
input("Press Enter to exist...")

# Prepare data for box plots
df_box = df.copy()
df_box['date'] = pd.to_datetime(df_box['date'])
df_box['year'] = df_box['date'].dt.year
df_box['month'] = df_box['date'].dt.strftime('%b')

# Draw box plots (using Seaborn)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
axes[0].set_title('Year-wise Box Plot (Trend)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Page Views')

sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
            order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
axes[1].set_title('Month-wise Box Plot (Seasonality)')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Page Views')

plt.show()
input("Press Enter to exist...")


