import streamlit as st
st.title("BRUNCH WITH SR")


st.image("C:/Users/yourusername/Downloads/cafe.png", width=700) 


st.write("""
In a fast-paced world where everyone is rushing somewhere,
Brunch with SR is a pause.

A place where coffee stays warm,
stories flow slowly,
and conversations with seniors remind us of values, laughter, and life lessons.

Whether you're waiting for your ride,
or just need a moment of comfort —
this café welcomes you.
""")

st.subheader("Why are you here today?")

purpose = st.radio(
    "Select one:",
    ("Waiting for someone ☕",
     "Listening to senior stories 🧓",
     "Having a quiet coffee break 📖",
     "Hanging out with friends 🧑‍🤝‍🧑")
)

st.write(f"You chose: **{purpose}**")

st.subheader("☕ Our Coffee Corner")

coffee = st.radio(
    "Choose your coffee:",
    (
        "Indian Filter Coffee (strong & comforting)",
        "Milk Coffee (home-style)",
        "Cold Coffee (sweet & creamy)",
        "Chocolate Coffee (for a cozy mood)"
    )
)
st.write(f"You selected: **{coffee}**")

st.subheader("🍕 Comfort Food Menu")

food = st.multiselect(
    "What would you like to eat?",
    [
        "Cheese Pizza",
        "White Sauce Pasta",
        "Red Sauce Pasta",
        "Garlic Bread",
        "French Fries",
        "Chocolate Cake",
        "Brownie"
    ]
)
st.write("You chose:")
for item in food:
    st.write(f"- {item}")

st.subheader("🧓 Today's Senior Story")

st.subheader("📝 Share a Story with a Senior")

with st.form("story_form"):
    name = st.text_input("Your Name (optional)")
    relation = st.text_input("Who is this senior to you?")
    story = st.text_area("Write your story here")
    mood = st.radio("Mood of the story", ["Funny", "Emotional", "Inspiring", "Nostalgic"])
    submit = st.form_submit_button("Share Story")

if submit:
    st.success("Thank you for sharing your story 💛")


if submit:
    with open("stories.txt", "a", encoding="utf-8") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Relation: {relation}\n")
        f.write(f"Mood: {mood}\n")
        f.write(f"Story: {story}\n")
        f.write("-" * 40 + "\n")


st.subheader("💬 A Quote from a Senior")

st.write("""
"In our time, friendships were built on long walks,
shared tea, and listening more than speaking."

— A retired army officer
""")

st.write("💛 At Brunch with SR, every cup of coffee comes with a story.")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}
</style>
        
""", unsafe_allow_html=True)
st.markdown("""
<style>
body {
    background: rgba(255,182,193,0.5);
}
</style>
""", unsafe_allow_html=True)




# You must be in the same folder as the file "cafe.png" for the image to load correctly.
# cd "C:\Users\yourusername\Downloads"
# python -m streamlit run cafe.py
st.write("Visit us again for more stories and warm moments!") 
