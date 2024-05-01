import streamlit as st
import requests
import pandas as pd

def convert_currency(amount, from_currency, to_currency):
    # Make an API request to get the conversion rate
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['rates'][to_currency]

    # Convert the amount
    converted_amount = amount * conversion_rate
    return converted_amount

def main():
    st.title("Currency Converter")
    #st.image("moneywings.png", use_column_width=False, width=100)
    st.write("")

    st.write("This is a simple currency converter that uses the exchange rate API from exchangerate-api.com. You can convert between USD, EUR, GBP, JPY, AUD, CAD, CHF, CNH, HKD, and NZD.")
    
    amount = st.number_input("Enter amount to convert", min_value=0.01, value=1.0, step=1.0)
    from_currency = st.selectbox("From currency", ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNH", "HKD", "NZD"], index=1)
    to_currency = st.selectbox("To currency", ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNH", "HKD", "NZD"], index=0)

    # Convert the currency
    converted_amount = convert_currency(amount, from_currency, to_currency)

    # Display the result
    st.write(f"{amount} {from_currency} = {converted_amount} {to_currency}")

    st.markdown("---")

    # Create a line chart to visualize the conversion rates
    st.header("Conversion Rates Chart")
    st.write("Here is a line chart showing the conversion rates:")
    chart_data = {'Currency': [from_currency, to_currency], 'Amount': [amount, converted_amount]}
    chart_df = pd.DataFrame(chart_data)
    st.line_chart(chart_df.set_index('Currency'))

    st.write("")
    st.write("")
    st.write("Made with ❤️ by [Nick Balatos](https://github.com/NickBalatos)")
    st.write("")
    st.write("")
if __name__ == "__main__":
    main()