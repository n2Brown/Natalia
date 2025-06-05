import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Agent Natalia | Wedding & Event Strategy",
    page_icon="💍",
    layout="centered"
)

# Title and subtitle
st.title("💫 Meet Agent Natalia")
st.subheader("Chief Experience Architect | Wedding & Event Specialist")

# Introduction
st.markdown("""
**Agent Natalia** is the heart of your unforgettable event experience.  
She leads with vision, strategy, and poise to ensure every celebration reflects excellence and intention.
""")

# Section: Core Responsibilities
st.header("🎯 Core Responsibilities")

st.markdown("""
- 🧭 **Setting the overall brand strategy** for impactful and memorable events.
- 🤝 **Bridging the gap between clients and vendors**, ensuring seamless communication and aligned expectations.
- 📝 **Developing personalized ceremony scripts and detailed event plans** tailored to each client’s vision.
- 💍 **Officiating ceremonies and leading event coordination**, turning ambitions into reality.
- ❤️ **Building and nurturing lasting client relationships** with trust and support.
- 📈 **Overseeing strategic marketing content** to attract qualified leads.
- 📊 **Managing the booking pipeline and optimizing conversion rates** for sustainable growth.
""")

# Section: Closing
st.header("💼 Service Model")

st.markdown("""
Agent Natalia offers services à la carte or through custom packages tailored to your needs.  
Whether guiding a couple through their vows or orchestrating the entire flow of an event,  
**every moment is curated with purpose, passion, and professionalism.**
""")

# Optional: Contact button or booking CTA
if st.button("📅 Book a Consultation"):
    st.success("Redirecting to scheduling page... (This would link to your real booking tool)")

 # Optional: Add a footer or contact information section.
    st.markdown("---")
    st.markdown(
        """
        For inquiries regarding wedding and event services, please connect with Agent Natalia.
        """
    )
    
