# import streamlit as st
# import requests


# st.title("🔄 Universal Converter")
# st.write("Convert **Units & Currencies** easily! Select a category and get instant results.")

# CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/"
# #  Define supported currencies with their respective countries
# CURRENCIES = ["USD", "EUR", "GBP", "INR", "JPY", "PKR", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
#              "AED", "SGD", "HKD", "MYR", "THB", "KRW", "SAR", "ZAR", "BRL", "MXN", "RUB", "TRY",
#              "IDR", "NOK", "DKK", "PLN", "ILS", "PHP", "CZK"]

# # Dictionary mapping currencies to their country names
# CURRENCY_COUNTRIES = {
#     "USD": "United States Dollar",
#     "EUR": "Euro",
#     "GBP": "British Pound Sterling",
#     "INR": "Indian Rupee",
#     "JPY": "Japanese Yen",
#     "PKR": "Pakistani Rupee",
#     "AUD": "Australian Dollar",
#     "CAD": "Canadian Dollar",
#     "CHF": "Swiss Franc",
#     "CNY": "Chinese Yuan",
#     "SEK": "Swedish Krona",
#     "NZD": "New Zealand Dollar",
#     "AED": "United Arab Emirates Dirham",
#     "SGD": "Singapore Dollar",
#     "HKD": "Hong Kong Dollar",
#     "MYR": "Malaysian Ringgit",
#     "THB": "Thai Baht",
#     "KRW": "South Korean Won",
#     "SAR": "Saudi Riyal",
#     "ZAR": "South African Rand",
#     "BRL": "Brazilian Real",
#     "MXN": "Mexican Peso",
#     "RUB": "Russian Ruble",
#     "TRY": "Turkish Lira",
#     "IDR": "Indonesian Rupiah",
#     "NOK": "Norwegian Krone",
#     "DKK": "Danish Krone",
#     "PLN": "Polish Złoty",
#     "ILS": "Israeli Shekel",
#     "PHP": "Philippine Peso",
#     "CZK": "Czech Koruna"
# }


# def get_conversion_rate(base_currency, target_currency):
#     """Fetch currency conversion rates from API"""
#     try:
#         response = requests.get(f"{CURRENCY_API_URL}{base_currency}")
#         if response.status_code == 200:
#             return response.json()["rates"].get(target_currency)
#         st.error("Failed to fetch conversion rates. Please try again later.")
#         return None
#     except requests.RequestException as e:
#         st.error(f"API request failed: {str(e)}")
#         return None
    
    
# def currency_converter():
#     """Currency Converter UI"""
#     st.header("💰 Currency Converter")
#     amount = st.number_input("Enter Amount", min_value=0.01, value=1.0)
    
#     # Update currency selection to show country names
#     base_currency = st.selectbox("From Currency", 
#                                CURRENCIES,
#                                format_func=lambda x: f"{x} - {CURRENCY_COUNTRIES[x]}")
#     target_currency = st.selectbox("To Currency", 
#                                  [c for c in CURRENCIES if c != base_currency],
#                                  format_func=lambda x: f"{x} - {CURRENCY_COUNTRIES[x]}")

#     if st.button("Convert"):
#         conversion_rate = get_conversion_rate(base_currency, target_currency)
#         if conversion_rate:
#             converted_amount = amount * conversion_rate
#             st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
# currency_converter()
import streamlit as st
import requests

# 🔹 API Endpoint
CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/"

# 🔹 Define Supported Currencies
CURRENCIES = ["USD", "EUR", "GBP", "INR", "JPY", "PKR", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
             "AED", "SGD", "HKD", "MYR", "THB", "KRW", "SAR", "ZAR", "BRL", "MXN", "RUB", "TRY",
             "IDR", "NOK", "DKK", "PLN", "ILS", "PHP", "CZK"]

CURRENCY_COUNTRIES = {
    "USD": "United States Dollar", "EUR": "Euro", "GBP": "British Pound Sterling", "INR": "Indian Rupee",
    "JPY": "Japanese Yen", "PKR": "Pakistani Rupee", "AUD": "Australian Dollar", "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc", "CNY": "Chinese Yuan", "SEK": "Swedish Krona", "NZD": "New Zealand Dollar",
    "AED": "United Arab Emirates Dirham", "SGD": "Singapore Dollar", "HKD": "Hong Kong Dollar",
    "MYR": "Malaysian Ringgit", "THB": "Thai Baht", "KRW": "South Korean Won", "SAR": "Saudi Riyal",
    "ZAR": "South African Rand", "BRL": "Brazilian Real", "MXN": "Mexican Peso", "RUB": "Russian Ruble",
    "TRY": "Turkish Lira", "IDR": "Indonesian Rupiah", "NOK": "Norwegian Krone", "DKK": "Danish Krone",
    "PLN": "Polish Złoty", "ILS": "Israeli Shekel", "PHP": "Philippine Peso", "CZK": "Czech Koruna"
}

# 🔹 Function to Fetch Currency Exchange Rates
def get_conversion_rate(base_currency, target_currency):
    try:
        response = requests.get(f"{CURRENCY_API_URL}{base_currency}")
        if response.status_code == 200:
            return response.json()["rates"].get(target_currency)
        st.error("⚠️ Unable to fetch conversion rates. Please try again later.")
        return None
    except requests.RequestException:
        st.error("⚠️ Network error! Please check your internet connection.")
        return None

# 🔹 Streamlit Currency Converter UI
def currency_converter():
    # 👉 Professional Header
    st.markdown("""
        <h1 style="text-align: center; color: #2E86C1;">💰 Currency Converter</h1>
        <p style="text-align: center; font-size: 18px;">Easily convert between international currencies in real-time.</p>
        <hr style="border: 1px solid #ccc;">
    """, unsafe_allow_html=True)

    # 👉 User Input Fields
    col1, col2 = st.columns(2)
    amount = st.number_input("💵 Enter Amount", min_value=0.01, value=1.0, step=0.01)
    
    base_currency = col1.selectbox("🌍 From Currency", 
                               CURRENCIES, format_func=lambda x: f"{x} - {CURRENCY_COUNTRIES[x]}")
    target_currency = col2.selectbox("🔄 To Currency", 
                                 [c for c in CURRENCIES if c != base_currency],
                                 format_func=lambda x: f"{x} - {CURRENCY_COUNTRIES[x]}")

    # 👉 Convert Button
    if st.button("🔄 Convert Now"):
        conversion_rate = get_conversion_rate(base_currency, target_currency)
        if conversion_rate:
            converted_amount = amount * conversion_rate
            st.success(f"✅ {amount} {base_currency} is equal to **{converted_amount:.2f} {target_currency}** 💵")
            st.markdown(f"""
                <p style="text-align: center; font-size: 16px;">
                Current exchange rates are dynamic and may vary. Always verify rates before major transactions. 📊
                </p>
            """, unsafe_allow_html=True)
        else:
            st.error("⚠️ Conversion failed! Please check your currency selection and try again.")

    # 👉 Closing Message
    st.markdown("""
        <hr style="border: 1px solid #ccc;">
        <p style="text-align: center; font-size: 16px;">
        🎯 <b>Stay ahead in the financial world!</b> Use this tool to make informed currency conversions and manage your international transactions smartly. 🚀
        </p>
    """, unsafe_allow_html=True)

# Run the Converter
currency_converter()
