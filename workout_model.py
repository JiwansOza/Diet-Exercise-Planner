import pandas as pd

# Load the workout dataset
df_exercise_data = pd.read_csv('exercise_data.csv')

# Recommend exercise based on age and activity level from exercise_data.csv
def recommend_exercise(age, activity_level):
    # Convert activity level to match dataset format (capitalize first letter)
    activity_level = activity_level.capitalize()

    # Find the age_category that matches the input age
    filtered_exercise = df_exercise_data[
        (df_exercise_data['age_category'] == age) &  # Ensure exact match on age_category
        (df_exercise_data['activity'] == activity_level)
    ]
    
    if not filtered_exercise.empty:  # Check if the DataFrame is not empty
        # Get unique exercises and convert to list
        exercises = filtered_exercise['exercise'].unique().tolist()  # Use unique() and convert to list
        return exercises
    else:
        return []  # Return an empty list for no exercises
