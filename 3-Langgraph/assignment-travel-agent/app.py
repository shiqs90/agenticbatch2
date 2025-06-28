import streamlit as st
from datetime import date

# Assume your TravelAgent class is in a file named `agent.py`
# from agent import TravelAgent 

# --- Mock TravelAgent for demonstration ---
# (Replace this with your actual agent import)
class TravelAgent:
    def plan_trip(self, destination, start_date, end_date, interests, home_currency):
        # Simulate a delay to show the spinner
        import time
        time.sleep(5) 
        
        # This is where your actual agent logic would run
        # and return the full, formatted plan.
        return f"""
        **Your Awesome Trip Plan for {destination}!**

        *   **Dates:** {start_date} to {end_date}
        *   **Interests:** {interests}
        *   **Home Currency:** {home_currency}
        
        ... (Full weather, itinerary, and cost breakdown would go here) ...
        """
# ---------------------------------------------

# --- UI Layout ---

st.set_page_config(page_title="AI Travel Agent", layout="centered")
st.title("✈️ AI Travel Agent & Expense Planner")
st.write("Fill in the details below to get your personalized travel plan!")

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("📍 Destination (e.g., Paris, France)")
    start_date = st.date_input("🗓️ Start Date", min_value=date.today())

with col2:
    home_currency = st.selectbox("💵 Your Home Currency", ["USD", "EUR", "GBP", "INR"])
    end_date = st.date_input("🗓️ End Date", min_value=start_date)

interests = st.text_area("✨ Your Interests (e.g., history, foodie, hiking)")

# The button to trigger the agent
if st.button("Generate My Travel Plan", type="primary"):
    if not destination or not interests:
        st.error("Please fill in all the required fields!")
    else:
        # Show a "loading" spinner while the agent is working
        with st.spinner("🤖 Your AI agent is crafting the perfect trip..."):
            # Initialize and run your agent
            # agent = TravelAgent() # Uncomment when using your real agent
            # complete_plan = agent.plan_trip(destination, start_date, end_date, interests, home_currency)
            
            # Using the mock agent for this example
            agent = TravelAgent()
            complete_plan = agent.plan_trip(destination, start_date, end_date, interests, home_currency)

        # Display the final plan
        st.success("Here is your complete travel plan!")
        st.markdown(complete_plan)