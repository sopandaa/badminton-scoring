import streamlit as st
from game_logic import BadmintonGame
import pandas as pd
import plotly.express as px

# Initialize the game in session state to persist data between interactions
if 'game' not in st.session_state:
    st.session_state.game = BadmintonGame()

game = st.session_state.game

# --- Page Title ---
st.title("🏸 Badminton Scoring System")

# --- Player Names Input ---
player_a = st.text_input("Player A Name", "Player A")
player_b = st.text_input("Player B Name", "Player B")

# --- Display Current Scores with Colors ---
st.markdown(f"**Current Game:** {game.current_game} of 3")
st.markdown(f"<span style='color:red;font-size:20px;'>{player_a}: {game.score_a}</span> | "
            f"<span style='color:blue;font-size:20px;'>{player_b}: {game.score_b}</span>", 
            unsafe_allow_html=True)

# --- Display Games Won ---
st.markdown(f"**Games Won:** {player_a}: {game.games_won_a} | {player_b}: {game.games_won_b}")

# --- Bar Chart for Current Score ---
score_data = pd.DataFrame({
    "Player": [player_a, player_b],
    "Score": [game.score_a, game.score_b]
})
fig = px.bar(score_data, x="Player", y="Score", color="Player",
             color_discrete_map={player_a: "red", player_b: "blue"},
             title="Current Game Score")
st.plotly_chart(fig, use_container_width=True)

# --- Match Logic with Buttons ---
if not game.match_winner():
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"+1 {player_a}"):
            game.add_point("A")
    with col2:
        if st.button(f"+1 {player_b}"):
            game.add_point("B")
else:
    winner_name = player_a if game.games_won_a == 2 else player_b
    st.success(f"🎉 Match Winner: {winner_name}")
    if st.button("🔄 Reset Match"):
        st.session_state.game = BadmintonGame()
