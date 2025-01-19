<p align="center">
  <a href="https://academic.oup.com/brain/advance-article-abstract/doi/10.1093/brain/awae417/7950911?redirectedFrom=fulltext&login=false">
      <img width="20%" src="https://img.freepik.com/premium-photo/brain-logo-icon-human-brain-icon-creative-simple-mind-symbol-vector-illustration_1162225-51928.jpg?w=740" alt="Brianlytics" />
      <h1 align="center">Brianlytics</h1>
  </a>
</p>

## Project Documentation:
The project analyzes Event-Related Potentials (ERP) from brain data to compute the average response for specific finger movements. Below is the workflow:

1. **Load and Clean Data:**
   - Load trial event points and ECOG data.
   - Ensure column names and data types are valid.
   - Handle missing or invalid data.

2. **Data Segmentation:**
   - Define a time window around movement events.
   - Extract and group signals by finger identifier.

3. **Compute Mean ERPs:**
   - Average the signals for each finger.
   - Store and visualize the results.

4. **Visualization:**
   - Plot ERPs for each finger with unique colors:
     ![image](https://github.com/user-attachments/assets/3292e25c-42b2-4f20-a4db-f205afd8657c)

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
   ```python
   trial_points_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\events_file_ordered.csv"
   ecog_data_file = r"C:\Users\matan\Downloads\mini_project_2_data\mini_project_2_data\brain_data_channel_one.csv"
   ```
3. Run the script to compute and visualize the ERPs:

## Visualization Output:
- The script will generate a plot displaying the average ERP for each finger movement over time, with distinct colors for each finger.

