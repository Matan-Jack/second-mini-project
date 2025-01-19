# Second Mini Project: Event-Related Potentials (ERP)

## Project Objective:
Analyze brain signals (ECOG data) to compute the average Event-Related Potential (ERP) for finger movements. The ERP reflects brain activity before, during, and after specific finger movements.

### Workflow:
1. **Load and Clean Data:**
   - Load the `trial_points` file (events) and `ecog_data` file (brain signals).
   - Ensure proper column names and data types (`int` for trial points).
   - Handle invalid or missing data.

2. **Data Segmentation:**
   - Extract brain signals for each event using a time window:
     - 200 ms before the starting point.
     - 1 ms at the starting point.
     - 1000 ms after the starting point.
   - Group data by finger identifier.

3. **Compute Mean ERPs:**
   - For each finger, calculate the mean signal across all trials (length: 1201).
   - Organize the mean signals into a 5x1201 matrix (`fingers_erp_mean`).

4. **Visualization:**
   - Plot ERPs for all fingers using distinct colors.
   - Display a time series (-200 ms to +1000 ms).
     ![image](https://github.com/user-attachments/assets/3292e25c-42b2-4f20-a4db-f205afd8657c)
     
### Running the Project:
## To run the project follow these commands:
All commands should be run under the project root/working directory:

```bash
# Install Virtualenv - a tool to set up your Python environments
pip install virtualenv

# Create a virtual environment (serves only this project):
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# (venv) should appear as a prefix to all commands; run the next command after activating venv

# Update venv's Python package installer (pip) to its latest version
python.exe -m pip install --upgrade pip

# Install project's packages (Everything needed to run the project)
pip install pandas numpy matplotlib

## Running the Project:
1. Place the trial points file (`events_file_ordered.csv`) and ECOG data file (`brain_data_channel_one.csv`) in the working directory.
2. Update the file paths in the script:
   trial_points_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\events_file_ordered.csv"
   ecog_data_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\brain_data_channel_one.csv"
3. Run the script to compute and visualize the ERPs:
   ## Visualization Output:
   The script will generate a plot displaying the average ERP for each finger movement over time, with distinct colors for each finger.
   ```


