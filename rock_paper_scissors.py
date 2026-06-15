import streamlit as st
import random

st.title("🎮 Rock Paper Scissors")

choices = ["Rock", "Paper", "Scissors"]

player = st.radio(
    "Choose your move:",
    choices,
    horizontal=True
)

if st.button("Play"):
    computer = random.choice(choices)

    st.write("### You chose:", player)
    st.write("### Computer chose:", computer)

    if player == computer:
        st.success("🤝 It's a Tie!")
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        st.balloons()
        st.success("🎉 You Win!")
    else:
        st.error("😢 Computer Wins!")