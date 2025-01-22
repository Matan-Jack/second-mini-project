import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calc_mean_erp(trial_points, ecog_data):
   # Add column names to the trial points file if missing
    data = pd.read_csv(trial_points, header=None, names=['starting_point', 'peak_point', 'finger'])
    # Ensure data type is integers, drop rows with invalid data
    trial_points_int = (data.apply(pd.to_numeric, errors='coerce').dropna().astype(int))
    # Save cleaned data back to the CSV
    trial_points_int.to_csv(trial_points, index=False)

    # Load the ECOG data as a NumPy array
    ecog_data = pd.read_csv(ecog_data, header=None).to_numpy(dtype=np.float64).flatten()

    # Define constants for the time window
    pre_start = 200
    post_start = 1000
    window_length = pre_start + post_start + 1

    # Initialize storage for averaging ERPs per finger
    fingers_erp = {finger: [] for finger in range(1, 6)}

    # Extract signals around each event and group by finger
    for _, row in trial_points_int.iterrows():
        start_idx = row['starting_point']
        finger = row['finger']

        if start_idx - pre_start >= 0 and start_idx + post_start < len(ecog_data):
            segment = ecog_data[start_idx - pre_start: start_idx + post_start + 1]
            fingers_erp[finger].append(segment)

    # Calculate the mean ERP for each finger
    fingers_erp_mean_matrix = np.zeros((5, window_length), dtype=np.float64)
    for finger in range(1, 6):
        if fingers_erp[finger]:
            fingers_erp_mean_matrix[finger - 1, :] = np.mean(np.array(fingers_erp[finger], dtype=np.float64), axis=0)

    # Convert the mean ERP matrix to a DataFrame with numeric index names
    fingers_erp_mean = pd.DataFrame(fingers_erp_mean_matrix, index=[str(finger) for finger in range(1, 6)], columns=np.arange(window_length))

    # Plot the averaged brain response for each finger
    colors = ['#f7a1a1', '#ffcfdf', '#a2d2ff', '#c6f1d6', '#ffc3a0']
    time_vector = np.linspace(-pre_start, post_start, window_length)  # Time vector for plotting
    plt.figure(figsize=(12, 8))
    for i, finger in enumerate(range(1, 6)):
        plt.plot(time_vector, fingers_erp_mean.loc[str(finger)], label=f'Finger {finger}', color=colors[i])
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.title('Event-Related Potential (ERP) for Each Finger')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(fingers_erp_mean)

    # Return the transposed DataFrame with the name fingers_erp_mean
    return fingers_erp_mean

# Usage
trial_points = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\events_file_ordered.csv"
ecog_data_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\brain_data_channel_one.csv"
fingers_erp_mean = calc_mean_erp(trial_points, ecog_data_file)