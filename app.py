import streamlit as st
import random
import emoji
import re

# Custom Styling
custom_css = """
<style>
body {
    font-family: 'Inter', sans-serif;
    background-color: #eef2f3;
    margin: 0;
    padding: 0;
    color: black;
}

.navbar {
    font-size: 22px;
    font-weight: bold;
    position: fixed;
    top: 0;
    width: 100%;
    background: #2c3e50;
    color: white;
    padding: 15px;
    text-align: center;
    left: 0;
    z-index: 1000;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.footer {
    background: #2c3e50;
    color: white;
    padding: 15px 0;
    text-align: center;
    font-size: 16px;
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 1000;
}

.stApp {
    padding-top: 70px;
    padding-bottom: 70px;
}

.quote-box {
    font-size: 22px;
    font-weight: bold;
    animation: fadeIn 1s ease-in-out;
    background: #d1ecf1;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: #0c5460;
    border: 2px solid #17a2b8;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

.challenge-text {
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    font-weight: 500;
    color: #856404;
    background: #fff3cd;
    padding: 15px;
    margin-top: 10px;
    border: 2px solid #ffbf00;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<div class='navbar'>🚀 Mindset Booster</div>", unsafe_allow_html=True)

# Session State Management
if "page" not in st.session_state:
    st.session_state.page = "home"

# Email Validation
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

# Inspirational Quotes
quotes = [
    emoji.emojize("💡 Every setback is a setup for a comeback!"),
    emoji.emojize("💪 Strength grows in moments of challenge."),
    emoji.emojize("🚀 The only limit is the one you refuse to push through."),
]

# Growth Challenges
challenges = [
    "Write down a lesson you learned today.",
    "Challenge yourself to try something new.",
    "Share a piece of encouragement with someone.",
]

# Home Page
if st.session_state.page == "home":
    st.title("Mindset Booster Challenge")
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")

    if st.button("🚀 Start the Challenge"):
        if name and is_valid_email(email):
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.page = "welcome"
            st.rerun()
        else:
            st.warning("Please provide a valid name and email.")

# Welcome Page
elif st.session_state.page == "welcome":
    st.header(f"🚀 Welcome, {st.session_state.name}!")
    st.write("Get ready to fuel your mindset with daily motivation and challenges.")

    if st.button("🎯 Get Your Inspiration", key="get_quote"):
        st.session_state.page = "challenge"
        st.session_state.quote = random.choice(quotes)
        st.session_state.daily_challenge = random.choice(challenges)
        st.rerun()

    st.markdown(
        """
        <div class='challenge-text'>
        Click "Get Your Inspiration" to receive a motivational quote and a challenge for today. 
        Push yourself, stay focused, and make progress! 💡💪🚀
        </div>
        """,
        unsafe_allow_html=True
    )

# Challenge Page
elif st.session_state.page == "challenge":
    st.header("💡 Daily Motivation")
    st.markdown(f"<p class='quote-box'>{st.session_state.quote}</p>", unsafe_allow_html=True)

    st.subheader("🎯 Today's Challenge")
    st.markdown(f"<p class='challenge-text'>{st.session_state.daily_challenge}</p>", unsafe_allow_html=True)

    reflection = st.text_area("📝 Reflect on today's challenge:")

    if reflection:
        st.success("🌟 Keep pushing forward—progress is yours!")

        # LinkedIn Share Link
        share_text = f"I've completed today's mindset challenge: {st.session_state.daily_challenge}! 💡🚀 #MindsetBooster"
        linkedin_url = f"https://www.linkedin.com/shareArticle?mini=true&url=https://www.mindsetbooster.com&title=Mindset%20Booster&summary={share_text}"
        st.markdown(f"[🔗 Share on LinkedIn]({linkedin_url})", unsafe_allow_html=True)

    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# Footer
st.markdown("<div class='footer'>📧 Contact: naghmanaasif85@gmail.com | 🌍 https://www.linkedin.com/in/naghmana-asif</div>", unsafe_allow_html=True)
