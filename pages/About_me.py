import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Overthinking Out Loud",
    page_icon='📝'
)

img = Image.open('./image/Jam.png')

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(img, width=230)

with col2:
    st.title('Jamaica Valdez')
    st.write('Currently Studying in SNSU main campus, a BSCpE Sudent')

st.write("\n")
st.subheader("Five Facts About Me", anchor=False)
"""
Hi, I’m Jamaica! I’m a soft-hearted and caring person who loves finding beauty in life’s little moments. While I sometimes struggle with anger, I’ve learned to channel those emotions into my passions, turning challenges into creativity and growth.

Nature is my happy place 🌱—whether it’s hiking through lush trails or camping under the stars, being surrounded by greenery makes me feel alive. When words fail, I express myself through painting and sketching 🎨, pouring my heart into every stroke.

On the volleyball court, I thrive as a dedicated player, bringing energy, teamwork, and a sense of fun to every game. Off the court, my love for matcha adds a calming ritual to my day, and my coffee enthusiasm ☕ ensures I never miss out on the perfect cappuccino (especially with latte art!).

I’m also a bookworm 📚 who loves getting lost in stories with fierce female leads and epic adventures. Singing is another passion of mine, a way I share joy with myself and others. And, as a hopeless romantic 💕, I can’t resist a good rom-com, writing heartfelt poetry, or cherishing those magical, movie-like moments in life.

For me, life is all about embracing passions, connecting with others, and finding inspiration in every step of the journey. 🌟
"""

st.sidebar.success("Select pages above")
