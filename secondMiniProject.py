import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calc_mean_erp(trial_points_file, ecog_data_file):
    # Add column names to the trial points file if missing
    data = pd.read_csv(trial_points_file, header=None)  # Load trial points data without header
    data.columns = ['starting_point', 'peak_point', 'finger']  # Assign appropriate column names
    data.to_csv(trial_points_file, index=False)  # Save the updated trial points data with column names

    # Load the trial points CSV and ensure data type for relevant columns is integer
    trial_points = pd.read_csv(trial_points_file)  # Load trial points data from CSV file
    # Converts the 'starting_point' column to numeric values. If a value cannot be converted, it is replaced with NaN.
    trial_points['starting_point'] = pd.to_numeric(trial_points['starting_point'], errors='coerce')  
    # Converts the 'peak_point' column to numeric values. Non-numeric values are replaced with NaN.
    trial_points['peak_point'] = pd.to_numeric(trial_points['peak_point'], errors='coerce')  
    # Converts the 'finger' column to numeric values. Non-numeric values are replaced with NaN.
    trial_points['finger'] = pd.to_numeric(trial_points['finger'], errors='coerce')  
    # Drops rows where any of the specified columns ('starting_point', 'peak_point', 'finger') have NaN values.
    trial_points = trial_points.dropna(subset=['starting_point', 'peak_point', 'finger'])  
    # Converts the columns 'starting_point', 'peak_point', and 'finger' to integer type after ensuring no NaN values remain.
    trial_points = trial_points.astype({'starting_point': 'int', 'peak_point': 'int', 'finger': 'int'})  

    # Load the ECOG data as a NumPy array
    ecog_data = pd.read_csv(ecog_data_file, header=None).to_numpy().flatten()  # Load brain data as a flat NumPy array
    
    # Define constants for the time window
    pre_start = 200  # Define the time window: 200 ms before the starting point
    post_start = 1000  # Define the time window: 1000 ms after the starting point
    window_length = pre_start + post_start + 1  # Total number of samples in the time window (1201)
    
    # Initialize storage for averaging ERPs per finger
    fingers_erp = {finger: [] for finger in range(1, 6)}  # Dictionary to store trials for each finger (1-5)
    
    # Extract signals around each event and group by finger
    for i, row in trial_points.iterrows():  # Iterate through each trial in the trial_points data
        start_idx = row['starting_point']  # Get the starting point of the movement
        finger = row['finger']  # Get the finger identifier (1-5)
        # Ensure the indices are within bounds
        if start_idx - pre_start >= 0 and start_idx + post_start < len(ecog_data):  # Check if the segment is within the valid range
            segment = ecog_data[start_idx - pre_start: start_idx + post_start + 1]  # Extract the segment of brain data
            fingers_erp[finger].append(segment)  # Append the segment to the corresponding finger's list
    
    # Calculate the mean ERP for each finger
    fingers_erp_mean = np.zeros((5, window_length))  # Initialize a matrix to store the mean ERP for each finger
    for finger in range(1, 6):  # Iterate through each finger (1-5)
        if fingers_erp[finger]:  # Check if there are trials for the current finger
            mean_erp = np.mean(fingers_erp[finger], axis=0)  # Compute the mean across trials for the current finger
            fingers_erp_mean[finger - 1] = mean_erp  # Store the mean ERP in the output matrix
    # Define custom colors for each finger

    colors = ['#f7a1a1', '#ffcfdf', '#a2d2ff', '#c6f1d6', '#ffc3a0'] # List of colors for fingers 1-5
    # Plot the averaged brain response for each finger
    time_vector = np.linspace(-200, 1000, window_length)  # Create a time vector in milliseconds
    plt.figure(figsize=(12, 8))  # Initialize a figure for plotting
    for i, finger in enumerate(range(1, 6)):  # Iterate through each finger to plot the corresponding ERP
        plt.plot(time_vector, fingers_erp_mean[i], label=f'Finger {finger}', color=colors[i])  # Use a specific color for each finger
    plt.xlabel('Time (ms)')  # Label the x-axis as time in milliseconds
    plt.ylabel('Amplitude')  # Label the y-axis as amplitude
    plt.title('Event-Related Potential (ERP) for Each Finger')  # Set the plot title
    plt.legend()  # Display a legend for the plot
    plt.grid(True)  # Enable a grid for better visualization
    plt.show()  # Display the plot
    
    return fingers_erp_mean  # Return the matrix of mean ERPs for each finger

# Usage
trial_points_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\events_file_ordered.csv"  # Path to the trial points file
ecog_data_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\brain_data_channel_one.csv"  # Path to the ECOG data file
# Call the function to compute and plot the ERPs
fingers_erp_mean = calc_mean_erp(trial_points_file, ecog_data_file)  # Calculate and plot the mean ERPs
