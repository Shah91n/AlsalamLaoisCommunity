from datetime import datetime
import streamlit as st
from utils.handlers import fetch_prayer_times, handle_manual_refresh, get_next_prayer, get_time_until, get_hijri_time
from content.contact import display_contact_form
from content.activity import display_activities
from content.gallery import display_image_gallery
import os
from utils.style import load_custom_css

# ------------------------ß--------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------------------------------
st.set_page_config(
	page_title="Laois Muslim Community",
	layout="wide",
	initial_sidebar_state="expanded",
	page_icon="🕌",
)

# CALL THE CSS LOADER
load_custom_css()

# get prayer times
prayer_times = fetch_prayer_times()

st.markdown("<h1 style='text-align: center;'>Co Laoise Muslim Community Foundation</h1>", unsafe_allow_html=True)

# Path to your background image
main_image_path = os.path.join(os.getcwd(), 'images', 'main_image.png')
	
st.markdown("<div style='text-align: center;'>مؤسسة غير ربحية تعني بالحفاظ على الهوية الإسلامية والدمج الإيجابي للمسلمين في المجتمع الأيرلندي</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>A non-profit organisation concerned with preserving Islamic identity and the positive integration of Muslims into Irish society.</div>", unsafe_allow_html=True)

# Divider for better visual separation
st.markdown("---")

# Main prayers section
st.markdown("<h2 style='text-align: center;'>Prayer Times</h2>", unsafe_allow_html=True)

cols = st.columns(5)
prayer_data = [
    ("Fajr", prayer_times.get('Fajr', 'N/A')),
    ("Dhuhr", prayer_times.get('Dhuhr', 'N/A')),
    ("Asr", prayer_times.get('Asr', 'N/A')),
    ("Maghrib", prayer_times.get('Maghrib', 'N/A')),
    ("Isha", prayer_times.get('Isha', 'N/A'))
]

for i, (name, time) in enumerate(prayer_data):
    with cols[i]:
        st.markdown(f"""
            <div class="prayer-card">
                <div class="prayer-time">{time}</div>
                <div class="prayer-name">{name}</div>
            </div>
        """, unsafe_allow_html=True)

# Divider for better visual separation
st.markdown("---")

# Special Jummah Card
st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(183, 68, 255, 0.15), rgba(183, 68, 255, 0.05));
        border: 1px solid var(--secondary);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(183, 68, 255, 0.2);
    ">
        <div style="color: var(--secondary); font-size: 1.1rem; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px;">
            🕌 Jummah (Friday) Prayer
        </div>
        <div style="font-size: 2.5rem; font-weight: 800; color: white; margin: 5px 0;">
            1:30 PM
        </div>
        <div style="color: var(--text-light); font-size: 1rem; margin-top: 5px; display: flex; align-items: center; justify-content: center; gap: 5px;">
            <span style="font-size: 1.2rem;">📍</span> St. Mary's Hall, Portlaoise
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# After the welcome messages, add the navigation buttons
col1, col2, col3, col4 = st.columns(4)

# Create session state to track active tab if it doesn't exist
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'school'

# Navigation buttons
if col1.button('School Information', width='stretch', type='primary' if st.session_state.active_tab == 'school' else 'secondary'):
    st.session_state.active_tab = 'school'
if col2.button('Activities', width='stretch', type='primary' if st.session_state.active_tab == 'activities' else 'secondary'):
    st.session_state.active_tab = 'activities'
if col3.button('Gallery', width='stretch', type='primary' if st.session_state.active_tab == 'gallery' else 'secondary'):
    st.session_state.active_tab = 'gallery'
if col4.button('Contact', width='stretch', type='primary' if st.session_state.active_tab == 'contact' else 'secondary'):
    st.session_state.active_tab = 'contact'

# Content display based on active tab
if st.session_state.active_tab == 'school':
    st.header("School Information")

elif st.session_state.active_tab == 'activities':
	display_activities()

elif st.session_state.active_tab == 'gallery':
	display_image_gallery()

elif st.session_state.active_tab == 'contact':
    display_contact_form()

# --------------------------------------------------------------------------
# SIDEBAR CONTENT
# --------------------------------------------------------------------------
with st.sidebar:
    # 1. HEADER SECTION
    st.markdown("""
        <div class="sidebar-title">Portlaoise Masjid</div>
        <div class="sidebar-subtitle">📍 Portlaoise, Ireland</div>
    """, unsafe_allow_html=True)

    # 2. STATUS CARD (Next Prayer)
    next_prayer, next_time = get_next_prayer(prayer_times)
    time_until = get_time_until(next_time)
    
    st.markdown(f"""
        <div class="status-card">
            <div class="status-label">Next Prayer</div>
            <div class="status-value">{next_prayer} at {next_time}</div>
            <div class="status-sub">{time_until}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Refresh Button
    if st.button("🔄 Refresh Time", use_container_width=True):
        handle_manual_refresh()

    # 3. DATE CARD (Moved here under Time)
    st.markdown(f"""
        <div class="sidebar-card">
            <div class="info-row">
                <span class="info-label">Gregorian</span>
                <span class="info-value">{datetime.now().strftime('%b %d, %Y')}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Hijri</span>
                <span class="info-value">{get_hijri_time()}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. SOCIALS CARD
# 4. IMAM & SOCIALS CARD (Combined)
    st.markdown("""
        <div class="sidebar-card">
            <div style="text-align: center; margin-bottom: 12px;">
                <div style="font-size: 0.8rem; color: var(--text-light); text-transform: uppercase; letter-spacing: 1px;">Imam</div>
                <div style="font-size: 1.2rem; font-weight: bold; color: var(--text); margin-top: 4px;">Ahmed Halawa</div>
            </div>
            <div style="display: flex; justify-content: center; gap: 20px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.1);">
                <a href="https://www.tiktok.com/@halawa611?_t=ZN-8tStGYmer14&_r=1" target="_blank" style="text-decoration: none; opacity: 0.8; transition: opacity 0.3s;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 448 512">
                        <path fill="#FFFFFF" d="M448,209.91a210.06,210.06,0,0,1-122.77-39.25V349.38A162.55,162.55,0,1,1,185,188.31V278.2a74.62,74.62,0,1,0,52.23,71.18V0l88,0a121.18,121.18,0,0,0,1.86,22.17h0A122.18,122.18,0,0,0,381,102.39a121.43,121.43,0,0,0,67,20.14Z"/>
                    </svg>
                </a>
                <a href="https://www.youtube.com/@AHMED_HALAWA" target="_blank" style="text-decoration: none; opacity: 0.8; transition: opacity 0.3s;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 576 512">
                        <path fill="#FF0000" d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"/>
                    </svg>
                </a>
                <a href="https://www.facebook.com/AlRahmanPortlaoise/" target="_blank" style="text-decoration: none; opacity: 0.8; transition: opacity 0.3s;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 320 512">
                        <path fill="#1877F2" d="M279.14 288l14.22-92.66h-88.91V142.41c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S256.43 0 225.36 0c-73.08 0-121.15 44.38-121.15 124.72v70.62H56v92.66h48.21V496h99.89V288z"/>
                    </svg>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Qiyam al-Layl CARD
    st.markdown(f"""
        <div class="sidebar-card">
            <div style="margin-bottom: 10px; color: var(--primary); font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">Qiyam al-Layl</div>
            <div class="info-row">
                <span class="info-label">Midnight</span>
                <span class="info-value">{prayer_times.get('Midnight', 'N/A')}</span>
            </div>
            <div class="info-row">
                <span class="info-label">First Third</span>
                <span class="info-value">{prayer_times.get('Firstthird', 'N/A')}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Last Third</span>
                <span class="info-value">{prayer_times.get('Lastthird', 'N/A')}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)