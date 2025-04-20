# Unit Convertor Streamlit Python Project -2

import streamlit as st

# Function to Convert Length
def convert_length(value, conversion_choice):
    if conversion_choice == "Kilometers to Miles":
        return f"{value} km is {value * 0.621371:.2f} miles"
    elif conversion_choice == "Miles to Kilometers":
        return f"{value} miles is {value * 1.60934:.2f} km"

# Function to Convert Weight
def convert_weight(value, conversion_choice):
    if conversion_choice == "Kilograms to Pounds":
        return f"{value} kg is {value * 2.20462:.2f} pounds"
    elif conversion_choice == "Pounds to Kilograms":
        return f"{value} pounds is {value * 0.453592:.2f} kg"

# Function to Convert Temperature
def convert_temperature(value, conversion_choice):
    if conversion_choice == "Celsius to Fahrenheit":
        return f"{value}°C is {(value * 9/5) + 32:.2f}°F"
    elif conversion_choice == "Fahrenheit to Celsius":
        return f"{value}°F is {(value - 32) * 5/9:.2f}°C"

# Main Function for the App
def main():
    # Displaying title and subheading
    st.title("Unit Converter")
    st.subheader("Convert Length, Weight, and Temperature")

    # Conversion Type Selection
    option = st.selectbox("Select Conversion Type", ["Length Converter", "Weight Converter", "Temperature Converter"])

    if option == "Length Converter":
        choice = st.radio("Choose Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
        value = st.number_input("Enter Value (e.g., 10)", min_value=0.0, format="%.2f")
        if st.button("🔄 Convert"):
            result = convert_length(value, choice)
            st.success(result)

    elif option == "Weight Converter":
        choice = st.radio("Choose Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
        value = st.number_input("Enter Value (e.g., 5)", min_value=0.0, format="%.2f")
        if st.button("🔄 Convert"):
            result = convert_weight(value, choice)
            st.success(result)

    elif option == "Temperature Converter":
        choice = st.radio("Choose Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        value = st.number_input("Enter Value (e.g., 25)", format="%.2f")
        if st.button("🔄 Convert"):
            result = convert_temperature(value, choice)
            st.success(result)

# Run the main function
if __name__ == "__main__":
    main()
