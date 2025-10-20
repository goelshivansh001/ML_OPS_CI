import streamlit as st

# ---------- Page configuration ----------
st.set_page_config(page_title="🧮 Streamlit Calculator", layout="centered")

# ---------- Title ----------
st.title("🧮 Simple Streamlit Calculator")

st.write("Perform basic arithmetic operations easily using Streamlit!")

# ---------- Input section ----------
st.header("Enter your numbers:")
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# ---------- Operation selection ----------
operation = st.radio(
    "Choose operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (^)")
)

# ---------- Calculate ----------
st.header("Result:")
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                result = None
            else:
                result = num1 / num2
        elif operation == "Power (^)":
            result = num1 ** num2
        else:
            result = None

        if result is not None:
            st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error occurred: {e}")

# ---------- Reset option ----------
if st.button("Reset"):
    st.experimental_rerun()

# ---------- Footer ----------
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
