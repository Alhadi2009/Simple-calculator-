import streamlit as st



# 1. Title and Description
st.title("🙂 Simple Calculator")
st.write("Did you know that calculators are actually very reliable friends?")
st.write("because you can always COUNT on them")

# 2. Input Section
# We use columns to make it look nicer side-by-side
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# 3. Operation Selection
operation = st.selectbox(
    "Select Operation",
    ("Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)")
)

# 4. Calculation Logic
if st.button("Calculate"):
    result = 0
    
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (*)":
        result = num1 * num2
    elif operation == "Divide (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero is not allowed.")
            result = None

    # 5. Display Result
    if result is not None:
        st.success(f"The result is: {result}")
        # --- Footer Section ---
st.markdown("---") # This adds a horizontal line to separate the content
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Made by <b>Al Hadi 😎</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

