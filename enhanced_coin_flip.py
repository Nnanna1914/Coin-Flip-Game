import random
import streamlit as st

# Title and Introduction
st.title("Enhanced Flip a Coin Game")
st.write("""
Welcome to the **Enhanced Flip a Coin Game!** 🎲
- Enter the number of flips you'd like to simulate.
- View detailed logs of each flip.
- Track the statistics (total heads/tails and percentages).
- Reset the game at any time.
""")

# Initialize session state for persistent data
if "flip_history" not in st.session_state:
    st.session_state.flip_history = []

# Function to flip the coin
def flip_coin():
    return "Heads" if random.random() >= 0.5 else "Tails"

# Number of flips input
num_flips = st.number_input("Enter the number of flips:", min_value=1, max_value=100, value=1)

# Flip Coin Button
if st.button("Flip Coin"):
    for _ in range(num_flips):
        result = flip_coin()
        st.session_state.flip_history.append(result)
        st.write(f"Flip {len(st.session_state.flip_history)}: **{result}**")

# Display Flip History
if st.session_state.flip_history:
    st.subheader("Flip History")
    st.write(st.session_state.flip_history)

    # Calculate statistics
    heads_count = st.session_state.flip_history.count("Heads")
    tails_count = st.session_state.flip_history.count("Tails")
    total_flips = len(st.session_state.flip_history)
    heads_percentage = (heads_count / total_flips) * 100
    tails_percentage = (tails_count / total_flips) * 100

    # Display statistics
    st.subheader("Statistics")
    st.write(f"Total Flips: {total_flips}")
    st.write(f"**Heads:** {heads_count} ({heads_percentage:.2f}%)")
    st.write(f"**Tails:** {tails_count} ({tails_percentage:.2f}%)")

# Reset Game Button
if st.button("Reset Game"):
    st.session_state.flip_history = []
    st.write("Game reset successfully! Start flipping again.")

# Footer
st.write("---")
st.write("Built with ❤️ using [Streamlit](https://streamlit.io)")
