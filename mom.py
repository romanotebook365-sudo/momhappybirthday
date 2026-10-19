import streamlit as st

st.set_page_config(page_title="С днём рождения, мама!", page_icon="🌸", layout="centered")

# --- СТИЛЬ ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    }
    h1, h2, h3 {
        color: white !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 50px;
        padding: 15px 30px;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0 4px 10px rgba(255, 107, 107, 0.4);
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ee5a24;
        color: white;
    }
    .poem, .wish, .secret, .facts {
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 20px;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #333;
        margin-top: 20px;
    }
    .highlight {
        color: #ff6b6b;
        font-weight: bold;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .heart {
        display: inline-block;
        animation: pulse 1.5s infinite;
        font-size: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("С днём рождения, мама! 🌸")
st.markdown('<div style="text-align: center; font-size: 3rem;"><span class="heart">❤️</span></div>', unsafe_allow_html=True)

# --- СЧЁТЧИК ---
st.markdown(
    """
    <div style="text-align: center; color: white; font-size: 1.2rem; margin-bottom: 20px;">
    Ты — мама уже <b>15 лет и 5 месяцев</b>.<br>
    Спасибо за каждый день!
    </div>
    """,
    unsafe_allow_html=True
)

# --- КНОПКИ ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Стих"):
        st.session_state.show_poem = not st.session_state.get("show_poem", False)
with col2:
    if st.button("Пожелания"):
        st.session_state.show_wish = not st.session_state.get("show_wish", False)
with col3:
    if st.button("Секрет"):
        st.session_state.show_secret = not st.session_state.get("show_secret", False)
with col4:
    if st.button("Факты"):
        st.session_state.show_facts = not st.session_state.get("show_facts", False)

# --- СТИХ ---
if st.session_state.get("show_poem", False):
    st.markdown(
        """
        <div class="poem">
        <p>Кому обязан я всем, что имею?</p>
        <p>Кто научил меня всему?</p>
        <p>Как быть умнее и добрее,</p>
        <p>Тому свой стих сейчас прочту.</p>
        <br>
        <p>Я с днём рождения поздравляю</p>
        <p>И с гордостью готов сказать,</p>
        <p>Что лучше мамы нету в мире!</p>
        <p>Вот что готов я пожелать:</p>
        <br>
        <p>Любви, удачи и здоровья,</p>
        <p>Чтоб сбылись все твои мечты,</p>
        <p>Чтобы желания исполнялись,</p>
        <p>Всё то, что загадаешь ты.</p>
        <br>
        <p>Чтоб радовалась ты побольше,</p>
        <p>Ведь жизнь для этого нужна.</p>
        <p>Тебя люблю я очень-очень,</p>
        <p>Ты очень для меня важна.</p>
        <br>
        <p class="highlight">С днём рождения, мамочка моя!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- ПОЖЕЛАНИЯ ---
if st.session_state.get("show_wish", False):
    st.markdown(
        """
        <div class="wish">
        <p>С днём рождения, мамуля.</p>
        <p>Желаю тебе здоровья, счастья, любви, удачи и долгих лет жизни.</p>
        <p>Я тебя очень уважаю и люблю.</p>
        <p class="highlight">Ты лучшая! Правда!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- СЕКРЕТ ---
if st.session_state.get("show_secret", False):
    st.markdown(
        """
        <div class="secret">
        <p>Мама, я тебя очень сильно люблю.</p>
        <p>Ты — самый важный человек в моей жизни.</p>
        <p>Спасибо, что ты есть. 💖</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()
# --- ФАКТЫ ---
if st.session_state.get("show_facts", False):
    st.markdown(
        """
        <div class="facts">
        <p>✨ Ты — врач. Ты спасаешь жизни каждый день.</p>
        <p>✨ Ты — мама, которая вырастила меня.</p>
        <p>✨ Ты — человек, который никогда не сдаётся.</p>
        <p class="highlight">И я горжусь тобой. 💖</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- ПОДВАЛ ---
st.markdown(
    """
    <div style="text-align: center; color: white; margin-top: 40px; font-size: 1rem;">
    С любовью, Рома. 💖
    </div>
    """,
    unsafe_allow_html=True
)
