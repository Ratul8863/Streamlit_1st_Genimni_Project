import io
import streamlit as st
from api_calling import genarate_note, genarate_audio, genarate_quiz
from PIL import Image

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NoteVision AI",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #080c14;
    color: #e2e8f0;
}

.stApp {
    background: #080c14;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(0,200,255,0.07), transparent),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(120,0,255,0.05), transparent);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0d1322 !important;
    border-right: 1px solid rgba(0,200,255,0.12);
}
[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #00c8ff;
    font-family: 'Space Mono', monospace;
    letter-spacing: 0.05em;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    border: 1px dashed rgba(0,200,255,0.3) !important;
    border-radius: 12px;
    background: rgba(0,200,255,0.03) !important;
    transition: border-color 0.3s;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(0,200,255,0.6) !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: #0d1322 !important;
    border: 1px solid rgba(0,200,255,0.25) !important;
    color: #e2e8f0 !important;
    border-radius: 8px;
}

/* ── Primary button ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #00c8ff 0%, #7000ff 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em !important;
    padding: 0.6rem 1.4rem !important;
    width: 100%;
    transition: opacity 0.2s, transform 0.15s !important;
    box-shadow: 0 0 18px rgba(0,200,255,0.25);
}
.stButton > button[kind="primary"]:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* ── Alert / success / error / warning ── */
.stAlert {
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] {
    color: #00c8ff !important;
}

/* ── Containers / cards ── */
[data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlock"] {
    background: rgba(13,19,34,0.7);
    border: 1px solid rgba(0,200,255,0.1);
    border-radius: 14px;
    padding: 1.4rem;
    backdrop-filter: blur(8px);
}

/* ── Subheaders ── */
h3 {
    color: #00c8ff !important;
    font-family: 'Space Mono', monospace !important;
    letter-spacing: 0.04em !important;
    font-size: 1rem !important;
}

/* ── Markdown text ── */
.stMarkdown p, .stMarkdown li {
    color: #b8c8d8;
    line-height: 1.75;
    font-size: 0.97rem;
}
.stMarkdown strong {
    color: #00c8ff;
}

/* ── Audio player ── */
audio {
    width: 100%;
    border-radius: 8px;
    filter: hue-rotate(160deg) saturate(1.5);
}

/* ── Divider ── */
hr {
    border-color: rgba(0,200,255,0.12) !important;
}

/* ── Hero title ── */
.hero-title {
    font-family: 'Space Mono', monospace;
    font-size: clamp(2rem, 5vw, 3.2rem);
    font-weight: 700;
    letter-spacing: -0.01em;
    background: linear-gradient(90deg, #00c8ff 0%, #a78bfa 60%, #ff6ec7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    margin-bottom: 0;
}
.hero-sub {
    color: #5a7a9a;
    font-size: 0.95rem;
    letter-spacing: 0.06em;
    margin-top: 0.3rem;
    font-family: 'Space Mono', monospace;
}
.badge {
    display: inline-block;
    background: rgba(0,200,255,0.1);
    border: 1px solid rgba(0,200,255,0.25);
    color: #00c8ff;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    margin-bottom: 1rem;
}
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    color: #00c8ff;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
    opacity: 0.8;
}
.glow-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    background: #00c8ff;
    border-radius: 50%;
    box-shadow: 0 0 8px 3px rgba(0,200,255,0.6);
    margin-right: 8px;
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="section-label">⚡ NoteVision AI</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("**📸 Upload Notes**")
    images = st.file_uploader(
        "Drop up to 3 images of your notes",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    P_image = []
    if images:
        for img in images:
            P_image.append(Image.open(img))

        if len(images) > 3:
            st.error("⚠️ Max 3 images allowed.")
        else:
            st.success(f"✅ {len(images)} image(s) ready")
            cols = st.columns(len(images))
            for i, img in enumerate(images):
                with cols[i]:
                    st.image(img, use_container_width=True)
    else:
        st.caption("No images uploaded yet.")

    st.markdown("---")
    st.markdown("**🎯 Difficulty Level**")
    selected = st.selectbox(
        "Note complexity",
        ("Easy Notes", "Medium Notes", "Hard Notes"),
        index=None,
        placeholder="Choose level...",
        label_visibility="collapsed",
    )

    if selected:
        level_emoji = {"Easy Notes": "🟢", "Medium Notes": "🟡", "Hard Notes": "🔴"}
        st.success(f"{level_emoji.get(selected, '📝')} {selected} selected")
    else:
        st.warning("Select a difficulty level")

    st.markdown("---")
    pressed = st.button("✦ Generate Note", type="primary")

# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown('<div class="badge">✦ AI-POWERED STUDY TOOL</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Turn Photos<br>Into Smart Notes.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">// upload · summarize · quiz · listen</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Quick feature pills
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="background:rgba(0,200,255,0.06);border:1px solid rgba(0,200,255,0.15);
    border-radius:12px;padding:1rem;text-align:center;">
    <div style="font-size:1.5rem">📝</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.75rem;color:#00c8ff;margin-top:0.4rem;letter-spacing:0.08em">TEXT NOTES</div>
    <div style="color:#5a7a9a;font-size:0.8rem;margin-top:0.3rem">Key topics extracted instantly</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="background:rgba(120,0,255,0.06);border:1px solid rgba(120,0,255,0.2);
    border-radius:12px;padding:1rem;text-align:center;">
    <div style="font-size:1.5rem">🔊</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.75rem;color:#a78bfa;margin-top:0.4rem;letter-spacing:0.08em">AUDIO NOTES</div>
    <div style="color:#5a7a9a;font-size:0.8rem;margin-top:0.3rem">Listen while you study</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="background:rgba(255,110,199,0.06);border:1px solid rgba(255,110,199,0.2);
    border-radius:12px;padding:1rem;text-align:center;">
    <div style="font-size:1.5rem">🧩</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.75rem;color:#ff6ec7;margin-top:0.4rem;letter-spacing:0.08em">QUIZ MODE</div>
    <div style="color:#5a7a9a;font-size:0.8rem;margin-top:0.3rem">Test your understanding</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# ── Helper: beautiful error card ──────────────────────────────────────────────
def show_error_card(icon: str, title: str, message: str, hint: str = ""):
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(255,60,60,0.06) 0%, rgba(255,100,0,0.04) 100%);
        border: 1px solid rgba(255,80,80,0.25);
        border-left: 4px solid #ff4444;
        border-radius: 14px;
        padding: 1.5rem 1.8rem;
        margin: 0.5rem 0;
    ">
        <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.6rem;">
            <span style="font-size:1.8rem">{icon}</span>
            <span style="font-family:'Space Mono',monospace;color:#ff6b6b;font-size:1rem;font-weight:700;letter-spacing:0.05em">{title}</span>
        </div>
        <div style="color:#c0a0a0;font-size:0.9rem;line-height:1.6;">{message}</div>
        {"<div style='margin-top:0.8rem;padding:0.6rem 1rem;background:rgba(255,255,255,0.04);border-radius:8px;color:#888;font-family:Space Mono,monospace;font-size:0.78rem;letter-spacing:0.05em;'>" + hint + "</div>" if hint else ""}
    </div>
    """, unsafe_allow_html=True)


# ── Output section ────────────────────────────────────────────────────────────
if pressed:
    if not images:
        st.error("📂 Please upload at least one image first.")
    elif not selected:
        st.error("🎯 Please select a difficulty level.")
    elif len(images) > 3:
        st.error("⚠️ Please upload no more than 3 images.")
    else:
        # ── Text Note ──
        with st.container(border=True):
            st.markdown('<div class="section-label"><span class="glow-dot"></span>Text Note</div>', unsafe_allow_html=True)
            try:
                with st.spinner("ℹ️ Extracting key topics..."):
                    note = genarate_note(P_image)
                st.markdown(note)
            except Exception as e:
                err = str(e)
                note = None
                if "quota" in err.lower() or "free-tier" in err.lower():
                    show_error_card(
                        "⚡", "QUOTA EXCEEDED",
                        "You've hit the Gemini free-tier limit. The API allows only a limited number of requests per minute/day on the free plan.",
                        "💡 Wait ~30 seconds and try again — or upgrade at ai.google.dev"
                    )
                else:
                    show_error_card("❌", "NOTE GENERATION FAILED", f"Something went wrong: {err}")

        if note:
            st.markdown("<br>", unsafe_allow_html=True)

            # ── Audio Note ──
            with st.container(border=True):
                st.markdown('<div class="section-label"><span style="display:inline-block;width:8px;height:8px;background:#a78bfa;border-radius:50%;box-shadow:0 0 8px 3px rgba(167,139,250,0.6);margin-right:8px;vertical-align:middle;"></span>Audio Note</div>', unsafe_allow_html=True)
                try:
                    with st.spinner("🔊 Generating audio..."):
                        clean_note = note
                        for ch in ["\n", "-", ":", "#", "*", "**"]:
                            clean_note = clean_note.replace(ch, " ")
                        audio = genarate_audio(clean_note)
                    st.audio(audio)
                except Exception as e:
                    show_error_card("🔇", "AUDIO FAILED", f"Could not generate audio: {str(e)}")

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Quiz ──
            with st.container(border=True):
                st.markdown('<div class="section-label"><span style="display:inline-block;width:8px;height:8px;background:#ff6ec7;border-radius:50%;box-shadow:0 0 8px 3px rgba(255,110,199,0.6);margin-right:8px;vertical-align:middle;"></span>Quiz Mode</div>', unsafe_allow_html=True)
                try:
                    with st.spinner("🧩 Building your quiz..."):
                        quiz = genarate_quiz(P_image)
                    st.markdown(quiz)
                except Exception as e:
                    err = str(e)
                    if "quota" in err.lower() or "free-tier" in err.lower():
                        show_error_card(
                            "⚡", "QUOTA EXCEEDED",
                            "Quota hit again while generating the quiz. The API has per-minute limits on the free tier.",
                            "💡 Wait a moment, then regenerate. Only the quiz failed — your notes above are safe."
                        )
                    else:
                        show_error_card("❌", "QUIZ GENERATION FAILED", f"Something went wrong: {err}")

else:
    # Empty state
    st.markdown("""
    <div style="text-align:center;padding:3rem 1rem;border:1px dashed rgba(0,200,255,0.12);
    border-radius:16px;background:rgba(0,200,255,0.02);">
        <div style="font-size:3rem;margin-bottom:1rem">ℹ️</div>
        <div style="font-family:'Space Mono',monospace;color:#00c8ff;font-size:0.85rem;letter-spacing:0.1em">AWAITING INPUT</div>
        <div style="color:#3a5a7a;margin-top:0.5rem;font-size:0.88rem">Upload your notes and hit <strong style="color:#5a8a9a">Generate Note</strong> to begin.</div>
    </div>
    """, unsafe_allow_html=True)