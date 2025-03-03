import streamlit as st

# 🔹 Extended Conversion Factors Dictionary
CONVERSION_FACTORS = {
    "Length": {
        "meters": 1, "feet": 3.28084, "inches": 39.3701, "kilometers": 0.001,
        "miles": 0.000621371, "yards": 1.09361, "centimeters": 100, "millimeters": 1000,
        "nautical_miles": 0.000539957, "micrometers": 1e6
    },
    "Weight": {
        "kilograms": 1, "pounds": 2.20462, "ounces": 35.274, "grams": 1000,
        "milligrams": 1e6, "stones": 0.157473, "metric_tons": 0.001
    },
    "Volume": {
        "liters": 1, "gallons": 0.264172, "milliliters": 1000, "cubic_meters": 0.001,
        "cubic_centimeters": 1000, "cups": 4.16667, "pints": 2.11338
    },
    "Time": {
        "seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400,
        "milliseconds": 1000, "microseconds": 1e6, "weeks": 1/604800,
        "months": 1/2.628e6, "years": 1/3.154e7
    },
    "Speed": {
        "meters_per_second": 1, "kilometers_per_hour": 3.6, "miles_per_hour": 2.23694,
        "knots": 1.94384, "feet_per_second": 3.28084
    },
    "Energy": {
        "joules": 1, "kilojoules": 0.001, "calories": 0.239006, "kilocalories": 0.000239006,
        "watt_hours": 0.000277778, "electronvolts": 6.242e18
    },
    "Area": {
        "square_meters": 1, "square_kilometers": 1e-6, "square_miles": 3.861e-7,
        "square_yards": 1.19599, "square_feet": 10.7639, "acres": 0.000247105,
        "hectares": 0.0001
    },
    "Data Storage": {
        "bits": 1, "bytes": 0.125, "kilobytes": 0.000125, "megabytes": 1.25e-7,
        "gigabytes": 1.25e-10, "terabytes": 1.25e-13, "petabytes": 1.25e-16
    }
}

# 🔹 Categories & Units
CATEGORIES = {category: list(units.keys()) for category, units in CONVERSION_FACTORS.items()}
CATEGORIES["Temperature"] = ["celsius", "fahrenheit", "kelvin"]  # Handled separately

# 🔹 Temperature Conversion Function
def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
        ("celsius", "kelvin"): lambda x: x + 273.15,
        ("kelvin", "celsius"): lambda x: x - 273.15,
        ("fahrenheit", "kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("kelvin", "fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

# 🔹 General Unit Conversion Function
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    try:
        base_value = value / CONVERSION_FACTORS[category][from_unit]  # Convert to base unit
        return base_value * CONVERSION_FACTORS[category][to_unit]  # Convert to target unit
    except KeyError:
        st.error(f"⚠️ Unsupported conversion from {from_unit} to {to_unit} in {category}.")
        return None

# 🔹 Streamlit Unit Converter UI
def unit_converter():
    st.markdown("""
        <h1 style="text-align: center;">📏 Universal Unit Converter</h1>
        <p style="text-align: center;">Easily convert between different measurement units in multiple categories.</p>
        <hr style="border: 1px solid #ccc;">
    """, unsafe_allow_html=True)

    category = st.selectbox("📂 Select Category", list(CATEGORIES.keys()))

    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("🔄 From", CATEGORIES[category])
    to_unit = col2.selectbox("🎯 To", [u for u in CATEGORIES[category] if u != from_unit])

    value = st.number_input("🔢 Enter Value", min_value=0.0, value=1.0, step=0.1)

    if st.button("Convert 🔄"):
        result = convert_units(value, from_unit, to_unit, category)
        if result is not None:
            st.success(f"✅ {value} {from_unit} = **{result:.4f} {to_unit}** 🎯")

    # 🔹 Closing Message
    st.markdown("""
        <hr style="border: 1px solid #ccc;">
        <p style="text-align: center;">
        🌟 <b>Make calculations easy!</b> Use this tool for quick and precise conversions anytime. 🚀
        </p>
    """, unsafe_allow_html=True)

unit_converter()
