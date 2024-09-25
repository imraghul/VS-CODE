import streamlit as st

# Display the game banner
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

# Introduction
st.write("Welcome to Treasure Island. \nYour mission is to find the treasure.")

# First choice: Crossroad
direction = st.selectbox("You are at a crossroad. Where do you want to go?", ["Left", "Right"])

if direction == "Left":
    # Second choice: Lake
    waitrswim = st.selectbox('You have come to the lake. There is an island in the middle of the lake. What do you want to do?', ['Wait for a boat', 'Swim across'])
    
    if waitrswim == 'Wait for a boat':
        # Third choice: Door
        door = st.selectbox("You arrive safely at the island. Which color door do you want to open?", ["Red", "Blue", "Yellow"])
        
        if door == "Red":
            st.write("Burned by fire. Game Over.")
        elif door == "Blue":
            st.write("Eaten by beasts. Game Over.")
        elif door == "Yellow":
            st.write("Yayy! You Win!")
        else:
            st.write("Wrong input. Game Over.")
            
    elif waitrswim == 'Swim across':
        st.write("Attacked by trout. Game Over.")

elif direction == "Right":
    st.write("You fall into a river. Game Over.")
else:
    st.write("Wrong input. Game Over.")
