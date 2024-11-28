import streamlit as st
import pandas as pd
import plotly.express as px


def show_scores():
    try:
        return pd.read_csv("resources/scores.csv")
    except Exception as e:
        st.error(f"Error loading scores: {e}")
        return None


def display_scores():
    st.title(":blue[Game Stats]")

    scores_df = show_scores()

    if scores_df is not None and not scores_df.empty:
        # genaral overall statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Players", scores_df["Name"].nunique())
        with col2:
            st.metric("High Score", scores_df["Score"].max())
        with col3:
            st.metric("Average Score", f"{scores_df['Score'].mean():.1f}")

        # bar Chart
        fig = px.bar(
            scores_df.nlargest(10, "Score"), x="Name", y="Score", title="Top 10 Scores"
        )
        st.plotly_chart(fig)

        # scores table
        st.markdown("### All Scores")
        st.dataframe(
            scores_df.sort_values("Score", ascending=False),
            hide_index=True,
            use_container_width=True,
        )

    if st.button("Back to Welcome Screen"):
        st.switch_page("app.py")


display_scores()
