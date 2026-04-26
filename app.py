import streamlit as st
import streamlit.components.v1 as components
import os
import time
import io
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

st.set_page_config(page_title="Bridesmaid Proposal", page_icon="💍", layout="centered")

# --------------------------
# SESSION STATE
# --------------------------

if "page" not in st.session_state:
    st.session_state.page = "invite"

if "no_moves" not in st.session_state:
    st.session_state.no_moves = 0

if "current_name" not in st.session_state:
    st.session_state.current_name = None

if "response_type" not in st.session_state:
    st.session_state.response_type = None

audio = None

# --------------------------
# STYLING
# --------------------------

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@500&family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">

<style>

[data-testid="stAppViewContainer"]{
    background-color:#ffe4ec;
}

/* FORCE ALL GENERAL TEXT TO BLACK */
html, body, [class*="css"]  {
    color: #000000 !important;
    font-family:'Poppins', sans-serif;
}

/* MAIN HEADERS STAY PINK */
.title{
    font-family:'Great Vibes', cursive;
    text-align:center;
    font-size:64px;
    color:#d63384 !important;
}

.subtitle{
    font-family:'Playfair Display', serif;
    text-align:center;
    font-size:28px;
    color:#d63384 !important;
}

/* NORMAL MESSAGE TEXT */
.message{
    text-align:center;
    font-size:20px;
    color:#000000 !important;
    font-family:'Poppins', sans-serif;
}

/* INPUT LABELS */
label, .stTextInput label, .stTextArea label{
    color:#000000 !important;
    font-weight:500;
}

/* INPUT BOXES */
input, textarea{
    border-radius:12px !important;
    border:2px solid #f4a7c5 !important;
    padding:10px !important;
    color:#000000 !important;
    background-color:#fff8fb !important;
}

/* BUTTONS */
button{
    height:60px;
    font-size:20px !important;
    border-radius:14px !important;
}

/* STREAMLIT GENERATED TEXT */
p, span, div, h1, h2, h3, h4, h5, h6 {
    color:#000000 !important;
}

/* SUCCESS INFO WARNING TEXT */
.stSuccess, .stInfo, .stWarning, .stError{
    color:#000000 !important;
}

/* ADMIN HEADINGS */
h3, h4 {
    color:#d63384 !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# INVITATION PAGE
# --------------------------

if st.session_state.page == "invite":

    st.markdown('<div class="title">You Are Invited 💌</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="message">
    My Nikkah and Traditional Wedding Ceremony will take place on  
    <br><br>
    <b>23rd & 24th October 2026</b>
    <br><br>
    I am using this opportunity to invite you to be part of something very special to me.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Next 💕"):
        st.session_state.page = "proposal"
        st.rerun()

    st.stop()

# --------------------------
# FRIEND DATA
# --------------------------

friends = {

    "Hamidat":{"role":"Maid of Honour","allow_no":False},
    "Aaisha":{"role":"Maid of Honour","allow_no":False},

    "Hafsat":{"role":"Bridesmaid","allow_no":False},
    "Ayobayonle":{"role":"Bridesmaid","allow_no":False},

    "Ifeoluwa":{"role":"Bridesmaid","allow_no":True},
    "Omotola":{"role":"Bridesmaid","allow_no":True},
    "Dolapo":{"role":"Bridesmaid","allow_no":False},
    "Ayanfe":{"role":"Bridesmaid","allow_no":False},
    "Busayo":{"role":"Bridesmaid","allow_no":False},
    "Samiat":{"role":"Bridesmaid","allow_no":True,},
    "Fathia":{"role":"Bridesmaid","allow_no":False},
    "Zainab":{"role":"Bridesmaid","allow_no":True},
    "Azizat":{"role":"Bridesmaid","allow_no":False},
    "Abbi":{"role":"Bridesmaid","allow_no":True},
    "Victoria":{"role":"Bridesmaid","allow_no":True},
    "Halima":{"role":"Bridesmaid","allow_no":True},
    "Apako":{"role":"Bridesmaid","allow_no":False},
    "Rofiat":{"role":"Bridesmaid","allow_no":False},
    "Praise":{"role":"Bridesmaid","allow_no":True},
    "Fathias":{"role":"Bridesmaid","allow_no":True},
    "Lero":{"role":"Bridesmaid","allow_no":True},
    "Darla":{"role":"Bridesmaid","allow_no":True},
    "Ruyina":{"role":"Bridesmaid","allow_no":True}
}

# --------------------------
# PROPOSAL PAGE
# --------------------------

if st.session_state.page == "proposal":

    st.markdown('<div class="title">A Little Surprise</div>', unsafe_allow_html=True)
    st.markdown('<div class="message">I have something special I would love to ask you.</div>', unsafe_allow_html=True)

    name = st.text_input("Enter your name")

    if name:

        name = name.strip().title()

        if name != st.session_state.current_name:
            st.session_state.no_moves = 0

        st.session_state.current_name = name

        if name in friends:

            friend = friends[name]
            folder = f"photos/{name.lower()}"

            if os.path.exists(folder):

                st.markdown("### A few memories of us 💕")

                files = sorted(os.listdir(folder))

                cols = st.columns(3)

                for i, file in enumerate(files):

                    path = os.path.join(folder,file)

                    col = cols[i % 3]

                    with col:

                        if file.lower().endswith(("jpg","jpeg","png")):
                            st.image(path, use_container_width=True)

                        elif file.lower().endswith(("mp4","mov")):
                            st.video(path)

            st.markdown(f'<div class="subtitle">{name}, you are so special to me.</div>', unsafe_allow_html=True)

            st.markdown(
            '<div class="message">Our friendship means so much to me and I cannot imagine such an important moment without you beside me.</div>',
            unsafe_allow_html=True)

            if friend["role"] == "Maid of Honour":
                st.markdown('<div class="subtitle">Will you be my Maid of Honour?</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="subtitle">Will you be my Bridesmaid?</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            # YES BUTTON
            with col1:

                if st.button("Yes 💕"):

                    with open("responses_log.csv","a",encoding="utf-8") as f:
                        f.write(f"{st.session_state.current_name},YES\n")

                    st.success("Yay! I'm so happy you'll be spending the day with me on such an important day 💕")
                    st.balloons()

                    time.sleep(3)

                    st.session_state.response_type = "yes"
                    st.session_state.page = "message"
                    st.rerun()

            # NO BUTTON
            with col2:

                if friend["allow_no"]:

                    if st.button("No 😅"):

                        with open("responses_log.csv","a",encoding="utf-8") as f:
                            f.write(f"{st.session_state.current_name},NO\n")

                        st.info("That is completely okay. I understand and I still appreciate you so much.")

                        time.sleep(2)

                        st.session_state.response_type = "no"
                        st.session_state.page = "thankyou"
                        st.rerun()

                else:

                    if st.session_state.no_moves < 3:

                        if st.button("No 😅"):
                            st.session_state.no_moves += 1
                            st.warning("Hmm... that answer seems incorrect. Try again 😄")

                    else:

                        if st.button("No 😅"):
                            st.error("That answer seems incorrect. Please refresh the page and try again.")

        else:
            st.error("Sorry, I couldn't find your name.")

# --------------------------
# MESSAGE PAGE
# --------------------------

if st.session_state.page == "message":

    st.markdown("### Leave me a message 💌")

    message = st.text_area("Your message")

    if st.button("Send Message"):

        if message.strip():

            with open("responses.csv", "a", encoding="utf-8") as f:
                f.write(f"{st.session_state.current_name},{message}\n")

            st.success("Your message has been sent successfully 💕")
            time.sleep(2)

            st.session_state.page = "thankyou"
            st.rerun()

        else:
            st.error("Please write a message before sending.")

# --------------------------
# THANK YOU PAGE
# --------------------------

if st.session_state.page == "thankyou":

    st.markdown('<div class="title">Thank You 💖</div>', unsafe_allow_html=True)

    if st.session_state.response_type == "yes":

        st.markdown("""
        <div class="message">
        Your message means the world to me.<br><br>
        Thank you for saying yes — I truly cannot wait to share this beautiful journey with you.<br>
        Having you beside me on such an important day means so much to me.
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="message">
        Thank you for taking the time to respond.<br><br>
        I completely understand and truly appreciate your honesty.<br>
        Our friendship still means so much to me.
        </div>
        """, unsafe_allow_html=True)

    if os.path.exists("bride.jpg"):
        st.image("bride.jpg", use_container_width=True)

# --------------------------
# ADMIN VIEW
# --------------------------

st.markdown("---")
st.markdown("### Admin")

# Track admin login
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

password = st.text_input("Enter admin password", type="password")

# Check password
if password and not st.session_state.admin_logged_in:

    if password == ADMIN_PASSWORD:
        st.session_state.admin_logged_in = True
        st.success("Admin access granted")

    else:
        st.error("Incorrect password")

# Admin panel
if st.session_state.admin_logged_in:

    # --------------------------
    # YES / NO RESPONSES
    # --------------------------

    st.markdown("#### Yes / No Responses")

    if os.path.exists("responses_log.csv"):

        with open("responses_log.csv", "r", encoding="utf-8") as f:
            responses = f.readlines()

        yes_list = []
        no_list = []

        for r in responses:

            try:
                name, ans = r.strip().split(",")

                if ans == "YES":
                    yes_list.append(name)

                elif ans == "NO":
                    no_list.append(name)

            except:
                pass

        st.markdown("**People who said YES:**")

        if yes_list:
            for n in yes_list:
                st.write(f"💍 {n}")
        else:
            st.write("None yet")

        st.markdown("**People who said NO:**")

        if no_list:
            for n in no_list:
                st.write(f"😅 {n}")
        else:
            st.write("None yet")

    else:
        st.info("No responses yet.")

    # --------------------------
    # WRITTEN MESSAGES
    # --------------------------

    st.markdown("#### Written Messages")

    if os.path.exists("responses.csv"):

        with open("responses.csv", "r", encoding="utf-8") as f:
            messages = f.readlines()

        if messages:
            for m in messages:
                st.write(m.strip())
        else:
            st.info("No written messages yet.")

    else:
        st.info("No written messages yet.")

    # --------------------------
    # VOICE NOTES
    # --------------------------

    st.markdown("#### Voice Notes")

    voice_folder = "voice_notes"

    if os.path.exists(voice_folder):

        files = sorted(os.listdir(voice_folder))

        wav_files = [f for f in files if f.endswith(".wav")]

        if wav_files:

            for file in wav_files:

                path = os.path.join(voice_folder, file)

                st.write(f"🎤 {file}")

                with open(path, "rb") as audio_file:
                    st.audio(audio_file.read(), format="audio/wav")

        else:
            st.info("No voice notes yet.")

    else:
        st.info("No voice notes yet.")