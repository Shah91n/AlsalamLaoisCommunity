import streamlit as st
import pandas as pd

def display_activities():
    st.header("Activities Schedule")

    # Store activities data in lists
    activities = [
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A"
    ]

    days = [
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A"
    ]

    times = [
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A"
    ]

    # Create DataFrame
    df = pd.DataFrame({
        "Activity": activities,
        "Day": days,
        "Time": times
    })

    # Display the table with Streamlit
    st.dataframe(
        df,
        hide_index=True,
        width='stretch',  # Make table use full container width
        column_config={
            "Activity": st.column_config.TextColumn(
                "Activity",
                width=None,
            ),
            "Day": st.column_config.TextColumn(
                "Day",
                width=None,
            ),
            "Time": st.column_config.TextColumn(
                "Time",
                width=None,
            ),
        }
    )

if __name__ == "__main__":
    display_activities() 