import streamlit as st
import json
import requests 
from streamlit_lottie import st_lottie

st.set_page_config(
        page_title="HELLO",
        page_icon=":rocket:",
        
    )

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_github = load_lottiefile("assets/animations/Github.json") 
lottie_linkedin = load_lottiefile("assets/animations/Linkedin.json") 
lottie_twitter = load_lottiefile("assets/animations/Twitter.json") 
lottie_instagram = load_lottiefile("assets/animations/Instagram.json") 
lottie_laptop = load_lottiefile("assets/animations/laptop.json")

# lottie_laptop = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_fYpwnrZX8W.json")

with st.container():
    st.title("Hey there :wave:, I'm *Shahnawaz*")
    st.subheader("A software developer with a passion for learning!")
    st.write("I'm currently exploring exciting new technologies such as AR, VR, Flutter, and Unity3D. While I'm not yet an expert in these areas, I'm enthusiastic about learning and pushing the boundaries of what's possible. I've started a few small projects in these areas and can't wait to see where my journey takes me. Check out my portfolio to see some of my early work, and let's connect if you're interested in collaborating on something innovative and fun!")

# Social
with st.container():
    left_column, right_column = st.columns([1,2])
    with left_column:
        st.header("Lets Connect")
        l_c_1,r_c_1 = st.columns([1,2])
        with st.container():
            with l_c_1:
                st_lottie(
                    lottie_github,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low", # medium ; high
                    # renderer="svg", # canvas
                    height=70,
                    width=70,
                    key=None,
                )
            with r_c_1:   
                st.write("#### [Github](https://github.com/shahnawazdev)")
        l_c_2,r_c_2 = st.columns([1,2])
        with st.container():
            with l_c_2:
                st_lottie(
                    lottie_linkedin,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low", # medium ; high
                    # renderer="svg", # canvas
                    height=70,
                    width=70,
                    key=None,
                )
            with r_c_2:   
                st.write("#### [Linkedin](https://www.linkedin.com/in/shahnawazdev)")
        l_c_2,r_c_2 = st.columns([1,2])
        with st.container():
            with l_c_2:
                st_lottie(
                    lottie_twitter,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low", # medium ; high
                    # renderer="svg", # canvas
                    height=70,
                    width=70,
                    key=None,
                )
            with r_c_2:   
                st.write("#### [Twitter](https://twitter.com/shahnawazdev)")    
        l_c_2,r_c_2 = st.columns([1,2])
        with st.container():
            with l_c_2:
                st_lottie(
                    lottie_instagram,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low", # medium ; high
                    # renderer="svg", # canvas
                    height=70,
                    width=70,
                    key=None,
                )
            with r_c_2:   
                st.write("#### [Instagram](https://instagram.com/shahnawaz_dev)")    
       

    with right_column:
        # st.image("image.png")
        st_lottie(
            lottie_laptop,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            # renderer="svg", # canvas
            height="none",
            width="none",
            key=None,
        )
st.markdown("---")


# PROJECTS
st.title("Projects") 

p1,p2 = st.columns(2)

with p1:
    with st.container():    
        st.image("assets/icons/todo_icon.png",width=200)
        st.subheader("To Do")
        st.write("A simple ToDo App")
        st.write("[Source Code](https://github.com/ShahnawazDev/ToDo)")
with p2:
    with st.container():
        st.image("assets/icons/fitbook_icon.png",width=200)
        st.subheader("FitBook")
        st.write("Fitness Tracker App")
        st.write("[Source Code](https://github.com/ShahnawazDev/FitBook)")
# with p1:
#     with st.container():    
#         st.image("assets/icons/todo_icon.png",width=200)
#         st.subheader("To Do App")
#         st.write("A simple ToDo App")
#         st.write("[Source Code](https://github.com/ShahnawazDev/ToDo)")
# with p2:
#     with st.container():    
#         st.image("assets/icons/todo_icon.png",width=200)
#         st.subheader("To Do App")
#         st.write("A simple ToDo App")
#         st.write("[Source Code](https://github.com/ShahnawazDev/ToDo)")


# Project 1
with st.container():
    st.image("assets/icons/todo_icon.png", width=200, caption="Project 1 - ToDo App Icon")
    st.subheader("To Do")
    st.image(["assets/icons/todo_icon.png", "assets/icons/todo_icon.png"], width=200,use_column_width=True)
    st.video("https://www.youtube.com/watch?v=your_project1_demo_video_id")
    st.write("A simple ToDo App")
    st.write("[Source Code](https://github.com/ShahnawazDev/ToDo)")

# Project 2
with st.container():
    st.image("assets/icons/todo_icon.png", width=200, caption="Project 2 - FitBook Icon")
    st.subheader("FitBook")
    st.image(["assets/icons/todo_icon.png", "assets/icons/todo_icon.png"], width=200, caption="Project 2 - Screenshots")
    st.video("https://www.youtube.com/watch?v=your_project2_demo_video_id")
    st.write("Fitness Tracker App")
    st.write("[Source Code](https://github.com/ShahnawazDev/FitBook)")


# Contact Form
st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/8da309eeef68c9b48d32c71560a22c1d" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")