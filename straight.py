import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title of the app
st.title('Straight Lines')

# Create a dropdown box for selecting the operation
operation = st.selectbox("Select an operation:", ["Calculate Slope", "Check Relationship", "Calculate Distance"])

# Get input coefficients for the first line
st.subheader('Enter the coefficients for the first line:')
a1 = st.number_input('Enter the value for a1:', value=1.0, format='%f')
b1 = st.number_input('Enter the value for b1:', value=1.0, format='%f')
c1 = st.number_input('Enter the value for c1:', value=1.0, format='%f')

# Calculate the corresponding y values for the first line
x = np.linspace(-10, 10, 400)
y1 = (-a1 * x - c1) / b1

# Create a new figure using plt.subplots
fig, ax = plt.subplots()

# Plot the first line
ax.plot(x, y1, label='Line 1', linestyle='-', marker='o')

if operation == "Calculate Slope":
    # Calculate and display the slope of the first line
    slope1 = -a1 / b1
    st.write(f"Slope of Line 1: {slope1}")

elif operation == "Check Relationship":
    # Get input coefficients for the second line
    st.subheader('Enter the coefficients for the second line:')
    a2 = st.number_input('Enter the value for a2:', value=1.0, format='%f')
    b2 = st.number_input('Enter the value for b2:', value=1.0, format='%f')
    c2 = st.number_input('Enter the value for c2:', value=1.0, format='%f')

    # Calculate the corresponding y values for the second line
    y2 = (-a2 * x - c2) / b2

    # Plot the second line
    ax.plot(x, y2, label='Line 2', linestyle='-', marker='o')

    # Check relationship between lines
    slope1 = -a1 / b1
    slope2 = -a2 / b2

    if slope1 == slope2:
        st.write("Lines are parallel.")
    elif slope1 * slope2 == -1:
        st.write("Lines are perpendicular.")
    else:
        st.write("Lines intersect.")

elif operation == "Calculate Distance":
    # Get input coefficients for the second line
    st.subheader('Enter the coefficients for the second line:')
    a2 = st.number_input('Enter the value for a2:', value=1.0, format='%f')
    b2 = st.number_input('Enter the value for b2:', value=1.0, format='%f')
    c2 = st.number_input('Enter the value for c2:', value=1.0, format='%f')

    # Calculate the distance between the two lines
    distance = abs(c2 - c1) / np.sqrt(a1**2 + b1**2)
    st.write(f"Distance between lines: {distance}")

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot')
ax.grid(True)
ax.legend()

# Show the plot
st.pyplot(fig)

# Close the figure
plt.close(fig)
