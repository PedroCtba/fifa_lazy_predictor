# Import whats necessary
import streamlit as st
import pandas as pd
from PIL import Image
import time

# Read data
data = pd.read_pickle("data/points.pkl")

# Read icon
icon = Image.open("icons/versus.png")

# Make header container
header = st.container()

# Make comparison container's
team_1_container, X, team_2_container = st.columns(3)

# Write the header
with header:
    st.title("Seja bem-vindo comparador fifa!\n ~ Power by Dhauz")
    st.markdown("")

# Make the comparison section
with team_1_container:
    st.markdown("")
    st.markdown("")

    # Select the team_1
    team_1 = st.selectbox(label="Time 1:", options=data.index)

with team_2_container:
    st.markdown("")
    st.markdown("")

    # Select the team_2
    team_2 = st.selectbox(label="Time 2:", options=data.index)

with X:
    # Show icon
    st.image(icon)

    # Get p1, and 2p2
    p1 = data.loc[team_1][0]
    p2 = data.loc[team_2][0]
    
    # Calculate We
    we = 1/(10**(((-1)*(p1-p2))/600)+1)

# Show odd's of victory
team_1_container.metric(f"Chance vitória:", f"{int(we.round(2) * 100)}%")
team_2_container.metric(f"Chance vitória:", f"{int((1 - we).round(2) * 100)}%")

# Center odd's fo win from both teams
st.markdown('''
<style>
/*center metric label*/
[data-testid="stMetricLabel"] > div:nth-child(1) {
    justify-content: center;
}

/*center metric value*/
[data-testid="stMetricValue"] > div:nth-child(1) {
    justify-content: center;
}
</style>
''', unsafe_allow_html=True)
