
# Diet & Exercise Recommendation System 🍽🏋

A personalized web-based application designed to recommend diet and exercise plans tailored to an individual's BMI, activity level, and weight goals. Built using **Streamlit** and powered by machine learning for calorie prediction.

---

## 🏗️ Features

- **BMI & Health Status Analysis**: Calculates BMI and categorizes health status (Underweight, Healthy, Overweight, Obese).
- **Personalized Calorie Distribution**: Recommends daily calorie intake based on Basal Metabolic Rate (BMR) and activity level.
- **Meal Recommendations**:
  - Suggests multiple meal options (breakfast, lunch, dinner) tailored to user preferences (Veg/Non-veg).
  - Provides detailed recipes for selected meals.
- **Exercise Plan**:
  - Offers exercises based on age and activity level.
  - Includes categories like Resistance, Yoga, and Aerobic with detailed descriptions.
- **Interactive UI**: Modern, user-friendly interface with visually appealing BMI results and calorie distribution.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for building the web application.
- **Pandas**: For data manipulation and analysis.
- **Machine Learning Model**: Predicts calorie values for meals using macros (Carbs, Fat, Protein, Fiber).

---

## 📦 Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your_username/diet-exercise-recommendation.git
    cd diet-exercise-recommendation
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download Datasets**:
   - Place the required CSV files (`meal.csv`, `recipe.csv`) in the project directory.

5. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

---

## 🖼️ Screenshots

### Home Page

<img width="1440" alt="Screenshot 2024-11-22 at 8 01 33 PM" src="https://github.com/user-attachments/assets/ed335cb9-196b-4f26-aecf-3d5788654b85">


### Personalized Results


<img width="1440" alt="Screenshot 2024-11-22 at 8 00 35 PM" src="https://github.com/user-attachments/assets/9ce83ef9-7796-4742-b25e-ca74488def9e">

---

## 📊 File Structure

```
diet-exercise-recommendation/
│
├── app.py                   # Main Streamlit application
├── diet_model.py            # Machine learning model for calorie prediction
├── meal.csv                 # Dataset with meal details
├── recipe.csv               # Dataset with meal recipes
├── requirements.txt         # Python dependencies
├── README.md                # Project README
└── images/                  # Screenshots and additional assets
```

---

## 🎯 Future Enhancements

- Add support for more exercises and meal types.
- Enable user login and profile customization.
- Integrate additional dietary preferences (e.g., vegan, gluten-free).
- Add export functionality to download personalized plans.

---

## 🖇️ Contributing

Contributions are welcome! Feel free to fork the repository and create a pull request with your improvements or new features.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- **Streamlit** for providing a robust and simple framework.
- **Pandas** for seamless data handling.
- **Community** for inspiration and open datasets.
