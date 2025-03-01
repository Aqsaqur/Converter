import streamlit as st
from pint import UnitRegistry

ureg= UnitRegistry()
st.title("Google Unit Converter")

categories = {"Length" : ["meter", "kilometer", "inch", "foot", "yard", "mile"],
              "Mass" : ["kilogram", "gram", "pound", "ounce", "stone"],
              "Speed" : ["meter per second", "kilometer per hour", "mile per hour"],
              "Temperature" : ["celsius", "fahrenheit", "kelvin"],
              "Time" : ["second", "minute", "hour", "day", "week", "month", "year"]}

category = st.selectbox("Select a category", list(categories.keys()))

from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])

value = st.number_input("Enter a value", min_value=0.0, step=0.1)

if st.button("Convert"):
    try: 
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                results = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                results = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                results = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                results = value + 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                results = (value -32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                results = (value - 273.15) * 5/9 + 32
            else:
               results = value
        else:
             results = (value * ureg( from_unit).to(to_unit).magnitude)
        st.success(f"{value} {from_unit} = {results}")
    except Exception as e:
      st.error(f"Error: {e}")

