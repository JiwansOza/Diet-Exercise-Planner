import streamlit as st
import pandas as pd
from diet_model import predict_calories

# Exercise details dictionary with descriptions and exercises
exercise_details = {
    "Resistance": {
        "description": "💪 Resistance training improves muscle strength using weights, bands, or body weight.",
        "exercises": ["🏋 Squats", "💪 Push-Ups", "🏋 Dumbbell Rows"]
    },
    "Yoga": {
        "description": "🧘‍♀️ Yoga enhances flexibility, balance, and relaxation through postures and breathing.",
        "exercises": ["🧘‍♀️ Downward Dog", "🧘‍♂️ Warrior I", "🧘‍♀️ Tree Pose"]
    },
    "Aerobic": {
        "description": "🏃 Aerobic exercises elevate heart rate and improve cardiovascular health.",
        "exercises": ["🏃 Jumping Jacks", "🏃‍♂️ High Knees", "🏃‍♀️ Burpees"]
    }
}

# Load datasets
df_meal = pd.read_csv('meal.csv')
df_recipe = pd.read_csv('recipe.csv', on_bad_lines='skip')  # Load recipe dataset, skip bad lines

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Healthy"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return bmi, status

# Calculate BMR based on the Mifflin-St Jeor equation
def calculate_bmr(weight, height, age, gender):
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

# Calculate daily calorie needs based on activity level and weight loss plan
def calculate_daily_calories(weight, activity_level, plan):
    if activity_level == 'Low':
        base_calories = weight * 24
    elif activity_level == 'Medium':
        base_calories = weight * 30
    else:
        base_calories = weight * 35
    
    if plan == 'Lose weight':
        daily_calories = base_calories - 500
    elif plan == 'Gain weight':
        daily_calories = base_calories + 500
    else:
        daily_calories = base_calories

    return daily_calories

# Function to balance calories across meals
def distribute_calories(total_calories):
    breakfast_calories = total_calories * 0.3
    lunch_calories = total_calories * 0.4
    dinner_calories = total_calories * 0.3

    return breakfast_calories, lunch_calories, dinner_calories

# Function to pick multiple meals based on calorie target and user preference
def pick_multiple_meals(meal_type, target_calories, diet_preference, num_meals=3):
    filtered_meals = df_meal[(df_meal[meal_type] == 1) & (df_meal[diet_preference] == 1)]
    filtered_meals['predicted_calories'] = filtered_meals.apply(
        lambda row: predict_calories(row['Carbs'], row['Fat'], row['Protein'], row['Fiber']),
        axis=1
    )
    
    selected_meals = filtered_meals.iloc[(filtered_meals['predicted_calories'] - target_calories).abs().argsort()[:num_meals]]
    
    return selected_meals

# Function to get recipe for a meal
def get_recipe(meal_name):
    recipe = df_recipe[df_recipe['Recipe Name'] == meal_name]['Ingredients'].values
    if len(recipe) > 0:
        return recipe[0]
    else:
        return "No recipe available."

# Function to recommend exercises based on age and activity level
def recommend_exercise(age, activity_level):
    # Determine exercise category based on activity level
    if activity_level == 'Low':
        exercise_category = "Yoga"
    elif activity_level == 'Medium':
        exercise_category = "Aerobic"
    else:
        exercise_category = "Resistance"
    
    # Lookup exercises for this category
    exercises = exercise_details.get(exercise_category, {}).get('exercises', [])
    return exercise_category, exercises

# Main Streamlit app interface
st.set_page_config(page_title="Diet & Exercise Recommendation 💪", page_icon="🍽", layout="wide")

st.title("Diet 🍽 & Exercise 🏋 Recommendation System")
st.markdown("### Your personalized meal and workout plan awaits! Let's get started!")
st.markdown("💡 *Tip: Consistency is key to achieving your fitness goals!*")

# Add an image initially if not already hidden
if 'image_shown' not in st.session_state or not st.session_state.image_shown:
    st.image("image.jpg", caption="Your personalized health plan", use_container_width=True)

# Input form for user data
st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input('🧑 Enter your age', min_value=1, help="Your age in years.")
weight = st.sidebar.number_input('⚖️ Enter your weight (kg)', min_value=1, help="Your weight in kilograms.")
height = st.sidebar.number_input('📏 Enter your height (cm)', min_value=1, help="Your height in centimeters.")
gender = st.sidebar.selectbox('👤 Select your gender', ['Male', 'Female'], help="Choose your gender.")
activity_level = st.sidebar.selectbox('🏃‍♂️ Activity level', ['Low', 'Medium', 'High'], help="Your activity level.")
weight_loss_plan = st.sidebar.selectbox('⚖️ Weight management plan', ['Maintain weight', 'Lose weight', 'Gain weight'], help="Choose your weight management plan.")
diet_preference = st.sidebar.selectbox('🥗 Diet preference', ['Veg', 'Non-veg'], help="Select your dietary preference.")

# Generate button
if st.sidebar.button('Generate Plan ✅'):
    # Hide the image after first button click
    if 'image_shown' not in st.session_state:
        st.session_state.image_shown = True

    st.markdown("---")
    with st.spinner('🔄 Generating your personalized plan...'):
        # Calculate BMI and health status with styling
        bmi, status = calculate_bmi(weight, height)
        st.markdown(f"""
            <style>
                .bmi-status {{ font-size: 20px; font-weight: bold; color: #2e8b57; }}
                .bmi-value {{ font-size: 18px; color: #3e8e41; }}
                .status-value {{ font-size: 18px; color: #ff6347; }}
            </style>
            <div class="bmi-status">
                <span class="bmi-value">BMI: {bmi:.2f}</span> 
                <span class="status-value">Status: {status}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Calculate total daily calories needed
        daily_calories = calculate_daily_calories(weight, activity_level, weight_loss_plan)
        st.write(f"**Total Daily Calories**: {daily_calories:.2f} kcal")
        
        # Calculate BMR and show it
        bmr = calculate_bmr(weight, height, age, gender)
        st.write(f"**Basal Metabolic Rate (BMR)**: {bmr:.2f} kcal/day")
        
        # Distribute calories across meals
        breakfast_calories, lunch_calories, dinner_calories = distribute_calories(daily_calories)
        
        # Meal recommendations
        st.subheader("🍽 **Meal Plan**")
        col1, col2, col3 = st.columns(3)
        
        # Breakfast
        with col1:
            st.write("🥞 **Breakfast**")
            breakfast_meals = pick_multiple_meals('Breakfast', breakfast_calories, diet_preference)
            for idx, meal in breakfast_meals.iterrows():
                with st.expander(f"{meal['Meals']} - {meal['predicted_calories']:.2f} kcal"):
                    st.write(f"🍴 Recipe: {get_recipe(meal['Meals'])}")
        
        # Lunch
        with col2:
            st.write("🍲 **Lunch**")
            lunch_meals = pick_multiple_meals('Lunch', lunch_calories, diet_preference)
            for idx, meal in lunch_meals.iterrows():
                with st.expander(f"{meal['Meals']} - {meal['predicted_calories']:.2f} kcal"):
                    st.write(f"🍴 Recipe: {get_recipe(meal['Meals'])}")
        
        # Dinner
        with col3:
            st.write("🍛 **Dinner**")
            dinner_meals = pick_multiple_meals('Dinner', dinner_calories, diet_preference)
            for idx, meal in dinner_meals.iterrows():
                with st.expander(f"{meal['Meals']} - {meal['predicted_calories']:.2f} kcal"):
                    st.write(f"🍴 Recipe: {get_recipe(meal['Meals'])}")
        
        # Exercise Recommendations
        st.subheader("🏋 Exercise Plan")
        exercise_category, exercises = recommend_exercise(age, activity_level)
        st.write(f"💪 **Recommended Exercise Category**: {exercise_category}")
        for exercise in exercises:
            st.write(exercise)
