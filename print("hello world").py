import streamlit as st

# 1. Set up the page title and description
st.title("🧮 Simple Python Calculator")
st.write("Enter two numbers and select an operation to see the result.")

# 2. Create input fields for numbers
# We use number_input to ensure the user enters valid numbers
num1 = st.number_input(label="Enter first number", value=0.0)
num2 = st.number_input(label="Enter second number", value=0.0)

# 3. Create a dropdown menu for the operation
operation = st.selectbox(
    "Select Operation",
        ("Add", "Subtract", "Multiply", "Divide")
        )

        # 4. Perform the calculation when the user clicks the button
        if st.button("Calculate"):
            result = 0
                if operation == "Add":
                        result = num1 + num2
                            elif operation == "Subtract":
                                    result = num1 - num2
                                        elif operation == "Multiply":
                                                result = num1 * num2
                                                    elif operation == "Divide":
                                                            if num2 != 0:
                                                                        result = num1 / num2
                                                                                else:
                                                                                            st.error("Error: Division by zero is not allowed.")
                                                                                                        result = None

                                                                                                            # 5. Display the result
                                                                                                                if result is not None:
                                                                                                                        st.success(f"The result is: **{result}**")

                                                                                                                        # Optional: Add a footer
                                                                                                                        st.markdown("---")
                                                                                                                        st.caption("Built with Python and Streamlit")
                                                                                                                        