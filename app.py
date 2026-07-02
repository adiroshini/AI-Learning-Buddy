import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model=genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Learning Buddy",page_icon="🎓",layout="centered")

st.markdown('''
<style>

.stApp{
    background:#FAF7FF;
}

.block-container{
    padding-top:3rem;
    padding-bottom:3rem;
    padding-left:4rem;
    padding-right:4rem;
}

.main-title{
    text-align:center;
    color:#6D28D9;
    font-size:46px;
    font-weight:700;
    margin-bottom:0px;
}

.sub{
    text-align:center;
    color:#6B7280;
    font-size:18px;
    margin-top:6px;
    margin-bottom:35px;
}

.box{
    background:white;
    padding:22px 28px;
    border-radius:18px;
    border:1px solid #E9D5FF;
    box-shadow:0 8px 18px rgba(0,0,0,.08);
    margin-bottom:30px;
}

.footer{
    text-align:center;
    color:#6B7280;
    font-size:14px;
    margin-top:40px;
}

.stTextInput{
    margin-bottom:28px;
}

.stSelectbox{
    margin-bottom:28px;
}

.stButton{
    margin-top:10px;
    margin-bottom:35px;
}

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#8B5CF6,#A855F7);
    color:white;
    border:none;
    border-radius:14px;
    padding:14px;
    font-size:18px;
    font-weight:600;
    transition:.3s;
    box-shadow:0 8px 18px rgba(139,92,246,.25);
}

.stButton>button:hover{
    background:linear-gradient(90deg,#7C3AED,#9333EA);
    transform:translateY(-2px);
}

.stTextInput input{
    border-radius:14px;
    border:2px solid #E9D5FF;
    padding:10px;
}

.stTextInput input:focus{
    border:2px solid #8B5CF6;
    box-shadow:0 0 12px rgba(139,92,246,.20);
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:14px;
    border:2px solid #E9D5FF;
}

</style>
''',unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 AI Learning Buddy</div>',unsafe_allow_html=True)
st.markdown('<div class="sub">Learn Smarter with AI ✨</div>',unsafe_allow_html=True)

st.markdown("""
<div class="box">
<h3>✨ Welcome to AI Learning Buddy</h3>

<p>
Your personal AI tutor that helps you understand concepts,
solve doubts, practice quizzes, and learn smarter.
</p>
</div>
""", unsafe_allow_html=True)

topic=st.text_input("📚 Enter a Topic")
option=st.selectbox("🎯 Choose Activity",["📖 Explain Concept","🌍 Real-Life Example","📝 Generate Quiz","💬 Ask Anything"])

def prompt_builder(topic,opt):
    if "Explain" in opt:
        return f'''You are Rosh, an AI Learning Buddy.
Explain "{topic}" simply.
Use easy English.
Give one analogy.
Give one real-life example.
End with 3 key points.'''
    elif "Real-Life" in opt:
        return f'''You are Rosh.
Give a practical real-life example of "{topic}".
Explain how and why it is useful.'''
    elif "Quiz" in opt:
        return f'''Create 5 MCQs on "{topic}".
Each should have 4 options, answer and explanation.'''
    return f'''You are Rosh, an AI Learning Buddy.
Answer clearly:
{topic}'''

if st.button("🟣 Generate Response", use_container_width=True):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("✨ Thinking..."):
            res = model.generate_content(prompt_builder(topic, option))

        st.success("Response Generated Successfully!")

        st.markdown("### 🤖 Your AI Learning Buddy Says...")

        with st.container(border=True):
            st.markdown(res.text)

st.markdown(
    '<div class="footer"><hr>💜 Built by <b>Roshini Adi</b><br>Infosys Springboard AI Empower(H)ER</div>',
    unsafe_allow_html=True
)
