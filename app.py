# import streamlit as st
# import random
# import emoji

# # Custom Styling
# custom_css = """
# <style>
# body {
#     font-family: 'Inter', sans-serif;
#     background-color: #eef2f3;
#     margin: 0;
#     padding: 0;
# }

# .navbar {
#     font-size: 22px;
#     font-weight: bold;
#     position: fixed;
#     top: 0;
#     width: 100%;
#     background: #2c3e50;
#     color: white;
#     padding: 15px;
#     text-align: center;
#     left: 0;
#     z-index: 1000;
# }

# .footer {
#     background: #2c3e50;
#     color: white;
#     padding: 15px 0;
#     text-align: center;
#     font-size: 16px;
#     width: 100%;
#     position: fixed;
#     bottom: 0;
#     left: 0;
#     z-index: 1000;
# }

# .stApp {
#     padding-top: 70px;
#     padding-bottom: 70px;
# }

# .quote-box {
#     font-size: 20px;
#     font-weight: bold;
#     animation: fadeIn 1s ease-in-out;
#     background: #d1ecf1;
#     padding: 20px;
#     border-radius: 10px;
#     text-align: center;
#     color: #0c5460;
# }

# .challenge-text {
#     border-radius: 10px;
#     text-align: center;
#     font-size: 18px;
#     font-weight: 500;
#     color: #856404;
#     background: #fff3cd;
#     padding: 15px;
#     margin-top: 10px;
# }
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)
# st.markdown("<div class='navbar'>🚀 Mindset Booster</div>", unsafe_allow_html=True)

# # Session State Management
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# # Inspirational Quotes
# quotes = [
#     emoji.emojize("💡 Every setback is a setup for a comeback!"),
#     emoji.emojize("💪 Strength grows in moments of challenge."),
#     emoji.emojize("🚀 The only limit is the one you refuse to push through."),
#     emoji.emojize("📖 Learning never stops, keep growing!"),
#     emoji.emojize("🔥 Failure is proof you're pushing beyond comfort zones."),  
#     emoji.emojize("🌟 Your journey is unique—embrace it!"),  
#     emoji.emojize("🏋‍♂ Break limits, build resilience!"),  
#     emoji.emojize("🎯 Small efforts compound into big victories."),  
#     emoji.emojize("⏳ Persistence is the key to progress."),  
#     emoji.emojize("🛠 Shift your thoughts, shape your world!"),  
#     emoji.emojize("💭 Dream it, plan it, achieve it."),  
#     emoji.emojize("⚡ Energy follows intention—focus wisely!"),  
#     emoji.emojize("🏆 Small daily wins lead to lifelong success."),  
#     emoji.emojize("🛤 Progress is a journey, not a race."),  
#     emoji.emojize("🧠 A strong mind builds an unstoppable life."),  
#     emoji.emojize("🔄 Mistakes are stepping stones, not stop signs."),  
# ]

# # Growth Challenges
# challenges = [
#     "Write down a lesson you learned today.",
#     "Challenge yourself to try something new.",
#     "Share a piece of encouragement with someone.",
#     "Reflect on a recent challenge and your response to it.",
#     "Spend 10 minutes reading something inspiring.",
#     "Identify one habit to improve and take a step today.",
#     "Express gratitude by writing down three things you appreciate.",
#     "Turn a mistake into a learning opportunity today.",
#     "Go a whole day focusing on positive solutions.",
#     "Push yourself outside your comfort zone today!",
# ]

# # Home Page
# if st.session_state.page == "home":
#     st.title("Mindset Booster Challenge")
#     name = st.text_input("Enter your name:")
#     email = st.text_input("Enter your email:")

#     if st.button("🚀 Start the Challenge"):
#         if name and email:
#             st.session_state.name = name
#             st.session_state.email = email
#             st.session_state.page = "welcome"
#             st.rerun()
#         else:
#             st.warning("Please provide both your name and email.")

# # Welcome Page
# elif st.session_state.page == "welcome":
#     st.header(f"🚀 Welcome, {st.session_state.name}!")
#     st.write("Get ready to fuel your mindset with daily motivation and challenges.")

#     if st.button("🎯 Get Your Inspiration", key="get_quote"):
#         st.session_state.page = "challenge"
#         st.session_state.quote = random.choice(quotes)
#         st.session_state.daily_challenge = random.choice(challenges)
#         st.rerun()

#     st.markdown(
#         """
#         <div class='challenge-text'>
#         Click "Get Your Inspiration" to receive a motivational quote and a challenge for today. 
#         Push yourself, stay focused, and make progress! 💡💪🚀
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # Challenge Page
# elif st.session_state.page == "challenge":
#     st.header("💡 Daily Motivation")
#     st.markdown(f"<p class='quote-box'>{st.session_state.quote}</p>", unsafe_allow_html=True)

#     st.subheader("🎯 Today's Challenge")
#     st.markdown(f"<p class='challenge-text'>{st.session_state.daily_challenge}</p>", unsafe_allow_html=True)

#     reflection = st.text_area("📝 Reflect on today's challenge:")

#     if reflection:
#         st.success("🌟 Keep pushing forward—progress is yours!")

#     if st.button("🏠 Back to Home"):
#         st.session_state.page = "home"
#         st.rerun()

# # Footer
# st.markdown("<div class='footer'>📧 Contact: support@mindsetbooster.com | 🌍 www.mindsetbooster.com</div>", unsafe_allow_html=True)

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
