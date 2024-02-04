import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Read accelerometer data from a CSV file
data = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\Acc-Data\\Acc Data\\accelerometer_data.csv")
print(data.head())

# Define a color map for line plots
color_map = {
    "accel_x": "darkcyan",
    "accel_y": "green",
    "accel_z": "blue",
}

# Create a line plot of acceleration data over time
fig = px.line(data, x="Date", 
              y=["accel_x", "accel_y", "accel_z"], 
              title="Plotting of Acceleration data over the complete Time Period", color_discrete_map=color_map)
fig.update_layout(
    plot_bgcolor="lightblue",  # Specify the desired background color
    paper_bgcolor="lightgray"   # Specify the color of the paper or canvas
)

fig.show()

# Extract hour of the day and day of the week from the timestamps
data["hour_of_Day"] = pd.to_datetime(data["Time"]).dt.hour
data["day_of_week"] = pd.to_datetime(data["Date"]).dt.day_name()

# Define the order of the days of the week
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create a pivot table for average acceleration by hour of day and day of week
agg_data = data.pivot_table(index="hour_of_Day", columns="day_of_week", 
                            values=["accel_x", "accel_y", "accel_z"], 
                            aggfunc="mean")

# Create a heatmap using Plotly Graph Objects
fig = go.Figure(go.Heatmap(x=agg_data.columns.levels[1], 
                           y=agg_data.index, 
                           z=agg_data.values,
                           xgap=1, ygap=1, 
                           colorscale="Viridis", 
                           colorbar=dict(title="Average Acceleration")))
fig.update_layout(title="Average Acceleration by Hour of Day and Day of Week")
fig.show()

# Calculate the magnitude of acceleration using NumPy
data['acceleration_mag'] = np.linalg.norm(data[['accel_x', 'accel_y', 'accel_z']], axis=1)

# Create a scatter plot of acceleration magnitude over time
fig = px.scatter(data, x='Time', 
                 y='acceleration_mag', 
                 title='Magnitude of Acceleration over time')
fig.show()

# Create a 3D scatter plot of acceleration data
fig = px.scatter_3d(data, x='accel_x', 
                    y='accel_y', 
                    z='accel_z', 
                    title='Acceleration in 3D space')
fig.show()

# Create a histogram of acceleration magnitude
fig = px.histogram(data, 
                   x='acceleration_mag', 
                   nbins=50, title='Acceleration magnitude histogram')
fig.show()
