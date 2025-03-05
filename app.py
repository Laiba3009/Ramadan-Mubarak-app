import streamlit as st
from prayer_timings import get_prayer_timings
from hadith import get_hadith  # ✅ Hadith import kiya
from azkar import get_azkar
import base64

# ✅ Function to encode image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

# ✅ Function to set background image
def set_bg_image():
    image_path = "img.jpg"  # ✅ Ensure the image exists
    base64_image = get_base64_image(image_path)

    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .title {{
        color: #1E90FF;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }}
    .dua-text {{
        color: #008000;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }}
    .info-box {{
        background: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 10px;
    }}
    .azkar-box {{
        font-size: 22px;
        font-weight: bold;
        color: #4B0082;
        background: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# ✅ Call function to set background
set_bg_image()

# ✅ Initialize session state
def initialize_session_state():
    if "day_number" not in st.session_state:
        st.session_state.day_number = 1

initialize_session_state()

# ✅ Function to display title with logo
def display_title_with_logo():
    logo_path = "image.jpg"  # Apni image ka path yahan daalain
    base64_logo = get_base64_image(logo_path)

    title_with_logo = f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; flex-wrap: wrap;">
        <h1 style="color: #12239E; margin: 0; text-align: center; flex-grow: 1;">🌙 Ramadan Mubarak</h1>
        <img src="data:image/jpg;base64,{base64_logo}" 
             style="width: 50px; height: 50px; border-radius: 50%; margin-left: 10px;">
    </div>
    """
    st.markdown(title_with_logo, unsafe_allow_html=True)

# ✅ Call function to display title with logo
display_title_with_logo()




# Sidebar Navigation
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("### Choose an option:")
page = st.sidebar.radio("", ["Home", "Hadis Sharif", "About"])

if page == "Home":
    st.subheader("🌍 Select your city:")
    cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta", "Multan"]
    city = st.selectbox("", cities)
    timings = get_prayer_timings(city)
    if timings:
        st.success(f"📍 **City:** {city}")
        st.success(f"🌅 **Sehri Time:** {timings['Fajr']} AM")
        st.success(f"🌇 **Iftar Time:** {timings['Maghrib']} PM")
    else:
        st.error("⚠️ Error fetching data. Please try again.") 

    # ✅ Fetch and display Azkar
    st.markdown(
        '<h3 style="color: #12239E;">📜 Select a Ramadan Day to View Azkar</h3>', 
        unsafe_allow_html=True
    )

    selected_day = st.radio("📆 Choose a day:", [f"Day {i}" for i in range(1, 31)], horizontal=True)
    st.session_state.day_number = int(selected_day.split()[1])

    if 1 <= st.session_state.day_number <= 10:
        dua = """
        📿 پہلے عشرے کی دعا  
        <h2 style='text-align:center; color:#008000;'>حَى يَا قَيُّومُ بِرَحْمَتِكَ اَسْتَغِيثُ</h2>
        <p style='text-align:center; color:#A80000; font-size:20px;'>اے زندہ رہنے والے، اے کائنات کو تھامنے والے! تیری رحمت کے وسیلے سے تجھ سے فریاد کرتا ہوں۔</p>
        """
    elif 11 <= st.session_state.day_number <= 20:
        dua = """
        **📿 دوسرے عشرے کی دعا**  
        <h2 style='text-align:center; color:#008000;'>اَسْتَغْفِرُ اللّٰهَ رَبِّيْ مِنْ كُلِّ ذَنْبٍ وَّأَتُوْبُ إِلَيْهِ</h2>
        <p style='text-align:center; font-size:20px;'>میں اللہ سے اپنے تمام گناہوں کی بخشش مانگتا ہوں اور اس کی طرف رجوع کرتا ہوں۔</p>
        """
    else:
        dua = """
        📿 تیسرے عشرے کی دعا 
        <h2 style='text-align:center; color:#008000;'>اَللّٰهُمَّ أَجِرْنِيْ مِنَ النَّارِ</h2>
        <p style='text-align:center ;color:#A80000 font-size:20px;'>اے اللہ! مجھے جہنم کی آگ سے بچا لے۔</p>
        """
    st.markdown(f'<div class="dua-text">{dua}</div>', unsafe_allow_html=True)


    st.subheader(Azkar for  Day 📿)
    azkar = get_azkar(st.session_state.day_number)
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="azkar-box">📿 Fajr: {azkar["Fajr"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="azkar-box">📿 Zohar: {azkar["Zohar"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="azkar-box">📿 Asar: {azkar["Asar"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="azkar-box">📿 Maghrib: {azkar["Maghrib"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="azkar-box">📿 Isha: {azkar["Isha"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">', unsafe_allow_html=True)




elif page == "Hadis Sharif":
    st.title("📖 Hadis Sharif")
    hadiths = get_hadith()
    for hadith in hadiths:
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.8); padding: 15px; border-radius: 10px; margin: 15px 0;">
            <h3 style="text-align: right; color: #4B0082;">📜 {hadith['Arabic']}</h3>
            <p style="font-size: 20px; color: #333;">📝 {hadith['Urdu']}</p>
            <p style="font-size: 18px; font-weight: bold; color: #008000;">📖 {hadith['Reference']}</p>
        </div>
        """, unsafe_allow_html=True)
    st.sidebar.info("Created by Laiba for Ramadan.❤️")

elif page == "About":
    import about
    about.show_about()
    st.sidebar.info("Created by Laiba for Ramadan.❤️")
