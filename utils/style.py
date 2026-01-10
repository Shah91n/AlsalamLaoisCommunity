import streamlit as st

def load_custom_css():
    st.markdown("""
        <style>
        /* ---------------------------------------------------------------------
           1. VARIABLE DEFINITIONS
           --------------------------------------------------------------------- */
        :root {
            --primary: #00d4ff;
            --secondary: #b744ff;
            --dark: #0a0a0f;
            --darker: #050508;
            --card: #1a1a2e;
            --text: #e0e0e0;
            --text-light: #a0a0a0;
            --success: #00ff88;
        }

        /* ---------------------------------------------------------------------
           2. GLOBAL STREAMLIT OVERRIDES
           --------------------------------------------------------------------- */
        
        /* Force the dark background color */
        .stApp {
            background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 100%);
            color: var(--text);
            font-family: 'Inter', sans-serif;
        }

        /* Hide the default Streamlit top decoration (the colorful line) */
        header[data-testid="stHeader"] {
            background: rgba(10, 10, 15, 0.95);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* ---------------------------------------------------------------------
           3. TEXT & HEADINGS
           --------------------------------------------------------------------- */
        h1, h2, h3 {
            color: var(--text) !important;
            font-weight: bold;
        }

        /* The Gradient Text Effect for Main Titles (Like your CV Name) */
        h1 {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 10px; /* Space for descenders */
        }

        /* ---------------------------------------------------------------------
           4. CUSTOM CARD COMPONENT (For Prayer Times)
           --------------------------------------------------------------------- */
        .prayer-card {
            background: linear-gradient(135deg, rgba(26, 26, 46, 0.9), rgba(26, 26, 46, 0.7));
            border-radius: 15px;
            padding: 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            transition: all 0.3s;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        .prayer-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.2);
            border-color: var(--primary);
        }

        .prayer-time {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }

        .prayer-name {
            font-size: 1.1rem;
            color: var(--text-light);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* ---------------------------------------------------------------------
           5. BUTTONS (Navigation)
           --------------------------------------------------------------------- */
        /* Primary Buttons */
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .stButton button[kind="primary"]:hover {
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
            transform: translateY(-2px);
        }

        /* Secondary Buttons */
        .stButton button[kind="secondary"] {
            background: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
            border-radius: 50px;
        }
        
        .stButton button[kind="secondary"]:hover {
            border-color: var(--secondary);
            color: var(--secondary);
        }

        /* ---------------------------------------------------------------------
           6. SIDEBAR SPECIFIC STYLES
        --------------------------------------------------------------------- */
        
        /* Make the sidebar background blend with the dark theme */
        section[data-testid="stSidebar"] {
            background-color: var(--darker);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Title Styling */
        .sidebar-title {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        
        .sidebar-subtitle {
            font-size: 0.85rem;
            color: var(--text-light);
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Glassmorphism Card for Sidebar Info */
        .sidebar-card {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        /* The "Next Prayer" Highlight Box */
        .status-card {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 212, 255, 0.05));
            border-left: 3px solid var(--primary);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .status-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--primary);
            margin-bottom: 0.3rem;
        }

        .status-value {
            font-size: 1.1rem;
            font-weight: bold;
            color: white;
            margin-bottom: 0.3rem;
        }

        .status-sub {
            font-size: 0.85rem;
            font-style: italic;
            color: var(--success);
            opacity: 0.9;
        }

        /* Clean Info Rows (Label ..... Value) */
        .info-row {
            display: flex;
            justify-content: space-between;
            padding: 0.4rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.9rem;
        }
        
        .info-row:last-child {
            border-bottom: none;
        }

        .info-label {
            color: var(--text-light);
        }

        .info-value {
            color: var(--text);
            font-weight: 500;
        }
                
        </style>
    """, unsafe_allow_html=True)