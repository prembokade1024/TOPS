import seaborn as sns
import matplotlib.pyplot as plt

# TASK 1: Pairplot on 'tips' dataset
print("--- TASK 1: Tips Dataset Pairplot ---")
# Load the built-in 'tips' dataset
df_tips = sns.load_dataset('tips')

# Create a pairplot to visualize relationships between all numeric variables
sns.pairplot(df_tips)

plt.show()
plt.close()

# TASK 2: Heatmap on 'flights' dataset
print("--- TASK 2: Flights Dataset Heatmap ---")
# Load the built-in 'flights' dataset
df_flights = sns.load_dataset('flights')

# Use pivot_table to reshape the data for the heatmap
flights_pivot = df_flights.pivot_table(index='month', columns='year', values='passengers')

plt.figure(figsize=(10, 8))
# Create the heatmap, annot=True displays the passenger counts in each cell
sns.heatmap(flights_pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Airline Passengers: Months vs Years")

plt.show()
plt.close()


# TASK 3: Relplot on 'fmri' dataset
print("--- TASK 3: FMRI Dataset Relplot ---")
# Load the built-in 'fmri' dataset
df_fmri = sns.load_dataset('fmri')

# Create a relplot (relational plot) set to kind='line' to show signal over time
sns.relplot(data=df_fmri, x="timepoint", y="signal", hue="event", kind="line")
plt.title("FMRI Signal Changes Over Time by Event")

plt.show()
plt.close()

# TASK 4: Catplot on 'titanic' dataset
print("--- TASK 4: Titanic Dataset Catplot ---")
# Load the built-in 'titanic' dataset
df_titanic = sns.load_dataset('titanic')

# Create a catplot (categorical plot) set to kind='bar' 
# By default, Seaborn calculates the mean and draws a 95% confidence interval line
sns.catplot(data=df_titanic, x="class", y="survived", kind="bar", palette="muted")
plt.title("Titanic Survival Rate by Passenger Class")

plt.show()
plt.close()

# TASK 5: Jointplot on 'penguins' dataset
print("--- TASK 5: Penguins Dataset Jointplot ---")
# Load the built-in 'penguins' dataset
df_penguins = sns.load_dataset('penguins')

# Create a jointplot with kind='reg' to add a regression line and scatter plot
sns.jointplot(data=df_penguins, x="bill_length_mm", y="flipper_length_mm", kind="reg", color="teal")

plt.show()
plt.close()