import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Meter By Harmain Bashir", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin:auto;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    return feedback  # Return feedback list

# Password input field
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

# Button working
if st.button("Check Strength"):
    if password:
        feedback = check_password_strength(password)  # Get feedback from function

        # Show feedback if available
        if feedback:
            with st.expander("🔍 **Improve your password**"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Please enter a password first!")  # Show warning if password is empty

