import streamlit as st

# Initialize session state for the game progression
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Step 1: Introduction
st.text('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/[Raghul G Art] 
*******************************************************************************''')

st.write("Welcome to Treasure Island. \nYour mission is to find the treasure.")

# Step 2: Crossroad decision (only proceed if the game is not over)
if not st.session_state.game_over and st.session_state.step >= 1:
    direction = st.selectbox("You are at a crossroad. Where do you want to go?", ["", "Left", "Right"], key='direction')
    
    if direction == "Left" and st.session_state.step == 1:
        st.session_state.step = 2
    elif direction == "Right" and st.session_state.step == 1:
        st.write("You fall into a river. Game Over.")
        st.session_state.game_over = True  # End the game

# Step 3: Lake decision (only proceed if the game is not over and player chose "Left")
if not st.session_state.game_over and st.session_state.step >= 2:
    waitrswim = st.selectbox('You have come to the lake. There is an island in the middle of the lake. What do you want to do?', ["", "Wait for a boat", "Swim across"], key='waitrswim')

    if waitrswim == "Wait for a boat" and st.session_state.step == 2:
        st.session_state.step = 3
    elif waitrswim == "Swim across" and st.session_state.step == 2:
        st.write("Attacked by trout. Game Over.")
        st.session_state.game_over = True  # End the game

# Step 4: Door decision (only proceed if the game is not over and player chose "Wait for a boat")
if not st.session_state.game_over and st.session_state.step >= 3:
    door = st.selectbox("You arrive safely at the island. Which color door do you want to open?", ["", "Red", "Blue", "Yellow"], key='door')
    
    if door == "Red":
        st.write("Burned by fire. Game Over.")
        st.session_state.game_over = True  # End the game
    elif door == "Blue":
        st.write("Eaten by beasts. Game Over.")
        st.session_state.game_over = True  # End the game
    elif door == "Yellow":
        st.write("Yayy! You Win!")
        st.session_state.game_over = True  # End the game
