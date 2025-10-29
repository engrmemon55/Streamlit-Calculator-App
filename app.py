import streamlit as st

# --- Streamlit page setup ---
st.set_page_config(page_title="🧮 Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")
st.write("A basic calculator built with Streamlit in Python.")

# --- Input fields ---
num1 = st.number_input("Enter first number", step=1.0, format="%.5f")
operation = st.selectbox("Select operation", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"])
num2 = st.number_input("Enter second number", step=1.0, format="%.5f")

# --- Perform calculation ---
result = None
if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (×)":
            result = num1 * num2
        elif operation == "Divide (÷)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("❌ Cannot divide by zero!")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# --- Display result ---
if result is not None:
    st.success(f"✅ Result: {result}")
