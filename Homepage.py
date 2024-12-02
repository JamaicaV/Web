import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def load_html_template():
    with open("layout.html", "r") as file:
        return file.read()

st.set_page_config(page_title="My Personal Blog", layout="wide", page_icon="📝")

img = Image.open('./image/das.jpg')

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{img_to_base64(img)}" width="800"/>
    </div>
    """, unsafe_allow_html=True
)

st.markdown('---')

# Blog post data
blog_posts = [
    {
        "title": "The Importance of Self-Care",
        "date": "November 24, 2024",
        "content": "Self-care isn't just about relaxation—it's about maintaining your mental and physical health to function at your best. In this post, I dive into the importance of taking time for yourself and how it helps you grow.",
        "url": "#"
    },
    {
        "title": "How to Manage Time Effectively",
        "date": "November 20, 2024",
        "content": "Time management is crucial in achieving balance in life. In this post, I share practical tips to help you manage your time effectively, boost productivity, and prioritize what's most important.",
        "url": "#"
    },
    {
        "title": "Embracing the Power of Failure",
        "date": "November 18, 2024",
        "content": "Failure can be a stepping stone to success. In this post, I talk about how embracing failure can lead to growth and how learning from mistakes makes you stronger.",
        "url": "#"
    }
]

header_footer_html = load_html_template()
st.markdown(header_footer_html, unsafe_allow_html=True)

st.write("### Latest Blog Posts")

for post in blog_posts:
    st.markdown(f"#### [{post['title']}]({post['url']})")
    st.write(f"**{post['date']}**")
    st.write(post["content"])
    st.markdown("---")

st.markdown(
    """
    <div class="footer">
        <p>&copy; 2024 My Personal Blog. All Rights Reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.success("Select pages above")