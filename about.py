import streamlit as st

def show_about():
    st.title("📖 About Ramadan Mubarak App")
    st.markdown(
    """
    <style>
    .custom-text {
        font-size: 22px; /* Font size bara kar diya */
        font-weight: bold;
    }
    .custom-link {
        font-size: 20px;
        font-weight: bold;
        color: blue;
        text-decoration: none;
    }
    .custom-link:hover {
        color: darkblue;
        text-decoration: underline;
    }
    </style>
    
    <p class="custom-text">
        I'm Laiba, and I'm excited to introduce my Ramadan Mubarak app, thoughtfully designed to enrich your spiritual journey during the holy month of Ramadan. 
        This app features Azkar from the revered book <strong>Ibadat Ramadan Mubarak</strong> by <strong>Baba Jani Sarkar</strong>, which are recited <strong> Namaz-e-Isha after</strong> throughout Ramadan.
    </p>

    <p class="custom-text">
        <strong>Baba Jani Sarkar</strong>, an esteemed spiritual guide, hosts daily live sermons where he recites the Quran with Tafseer (detailed explanations). 
        You can tune in to these live sessions on his YouTube channel:
    </p>

    <p>
        <a class="custom-link" href="https://youtube.com/@babajanisarkar?si=NmqCsAikCK34k21D" target="_blank">
            📺 Visit Baba Jani Sarkar's YouTube Channel
        </a>
    </p>

    <p class="custom-text">
        This app is crafted to bring you closer to the teachings of <strong>Baba Jani Sarkar</strong> and help you make the most of this blessed month with Allah's blessings.
    </p>
    """,
    unsafe_allow_html=True
)

    
    st.subheader("🌟 Features:")
    st.markdown("- 📅 Sehri & Iftar Timings (Auto-updating based on city)")
    st.markdown("- 📿 Azkar for all 5 prayers")
    st.markdown("- 📖 Hadith Sharif ")
    st.markdown("- 🕌 Ashra Duas displayed based on the Ramadan day")
    
    st.subheader("💡 How to Use:")
    st.write("Simply select your desired option from the sidebar to navigate between Home, Azkar, Hadith Sharif, and About.")
    
    st.info("Developed with ❤️ for Ramadan.")
