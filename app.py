import streamlit as st

# Set page configuration
st.set_page_config(page_title="Agent Natalia", layout="centered")

# Title and subtitle
st.title("🌟 Meet Agent Natalia")
st.subheader("Your Signature Experience Curator for Weddings and Events")

# Agent Natalia's profile
with st.container():
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Person_Icon.png/600px-Person_Icon.png", width=150)  # Placeholder avatar
    st.markdown("""
    **Agent Natalia** is the visionary behind your unforgettable moments. She is responsible for:

    - 🎯 **Setting the overall brand strategy** that aligns with elegance, authenticity, and excellence.
    - 🤝 **Cultivating relationships** with clients and trusted vendors to ensure seamless collaboration.
    - 💍 **Delivering heartfelt ceremonies** and expertly **coordinating events** with grace and precision.
    - 🏆 **Ensuring the highest quality of service** in every wedding and event experience.

    Agent Natalia is more than a planner—she's your partner in creating extraordinary memories.
    """)

# Optional: Contact or Call-to-Action
st.markdown("---")
st.markdown("✨ Ready to create a once-in-a-lifetime event? [Book a Consultation](#) or Contact Agent Natalia today!")

# Optional footer
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 Your Brand Name | Crafted with care by Agent Natalia</p>", unsafe_allow_html=True)
