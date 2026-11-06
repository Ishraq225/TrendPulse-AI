
import streamlit as st
import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="TrendPulse AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 TrendPulse AI")
st.subheader("Social Media Trend Intelligence Platform")

st.markdown(
    "Discover trending topics, analyze public sentiment, "
    "and explore discussions through interactive analytics."
)

# ==========================================
# 2. LOAD DATA
# ==========================================

DATA_PATH = (
    Path(__file__).parent
    / "data"
    / "processed"
    / "social_media_posts.csv"
)

@st.cache_data
def load_data():

    if not DATA_PATH.exists():
        st.error(f"Dataset not found: {DATA_PATH}")
        st.stop()

    # Read CSV
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")

    # Clean column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
    )

    # Handle incorrect CSV delimiter
    if len(df.columns) == 1:
        df = pd.read_csv(
            DATA_PATH,
            sep=None,
            engine="python",
            encoding="utf-8-sig"
        )

        df.columns = (
            df.columns.astype(str)
            .str.strip()
            .str.lower()
        )

    # Required columns
    required_columns = [
        "post_id",
        "text",
        "platform",
        "timestamp",
        "topic"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        st.error(
            f"Missing columns: {missing_columns}"
        )

        st.write("Available columns:", df.columns.tolist())

        st.info(
            "Your CSV must contain: "
            "post_id, text, platform, timestamp, topic"
        )

        st.stop()

    # Clean text columns
    for column in ["text", "platform", "topic"]:
        df[column] = df[column].fillna("").astype(str).str.strip()

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # Remove invalid rows
    df = df.dropna(subset=["timestamp"])
    df = df[df["text"] != ""]

    # Remove duplicate posts
    df = df.drop_duplicates(subset=["post_id"])

    if df.empty:
        st.error("No valid records found in the dataset.")
        st.stop()

    return df


df = load_data()

# ==========================================
# 3. SENTIMENT ANALYSIS
# ==========================================

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):

    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    else:
        return "Neutral"


df["sentiment"] = df["text"].apply(analyze_sentiment)

# ==========================================
# 4. SIDEBAR FILTERS
# ==========================================

st.sidebar.title("⚙️ Dashboard Filters")

st.sidebar.write("Customize your analysis.")

available_topics = sorted(
    df["topic"].unique().tolist()
)

selected_topic = st.sidebar.multiselect(
    "Select Topics",
    available_topics,
    default=available_topics
)

available_platforms = sorted(
    df["platform"].unique().tolist()
)

selected_platform = st.sidebar.multiselect(
    "Select Platforms",
    available_platforms,
    default=available_platforms
)

filtered_df = df[
    df["topic"].isin(selected_topic)
    & df["platform"].isin(selected_platform)
].copy()

if filtered_df.empty:
    st.warning("No posts match your selected filters.")
    st.stop()

# ==========================================
# 5. OVERVIEW METRICS
# ==========================================

st.markdown("## 📈 Dashboard Overview")

total_posts = len(filtered_df)

positive_posts = (
    filtered_df["sentiment"] == "Positive"
).sum()

negative_posts = (
    filtered_df["sentiment"] == "Negative"
).sum()

neutral_posts = (
    filtered_df["sentiment"] == "Neutral"
).sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Posts", total_posts)
col2.metric("😊 Positive", positive_posts)
col3.metric("😞 Negative", negative_posts)
col4.metric("😐 Neutral", neutral_posts)

st.divider()

# ==========================================
# 6. SENTIMENT DISTRIBUTION
# ==========================================

st.markdown("## 🎭 Sentiment Distribution")

sentiment_counts = (
    filtered_df["sentiment"]
    .value_counts()
    .rename_axis("Sentiment")
    .reset_index(name="Posts")
)

fig1 = px.pie(
    sentiment_counts,
    names="Sentiment",
    values="Posts",
    hole=0.5,
    color="Sentiment",
    color_discrete_map={
        "Positive": "#2ecc71",
        "Negative": "#e74c3c",
        "Neutral": "#3498db"
    },
    title="Overall Audience Sentiment"
)

fig1.update_layout(
    legend_title="Sentiment",
    height=400
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# ==========================================
# 7. TOPIC POPULARITY
# ==========================================

st.markdown("## 🔥 Topic Popularity")

topic_counts = (
    filtered_df["topic"]
    .value_counts()
    .reset_index()
)

topic_counts.columns = ["Topic", "Posts"]

fig2 = px.bar(
    topic_counts,
    x="Topic",
    y="Posts",
    color="Topic",
    text="Posts",
    title="Number of Posts by Topic"
)

fig2.update_layout(
    height=400,
    xaxis_title="Topics",
    yaxis_title="Number of Posts"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# ==========================================
# 8. SENTIMENT OVER TIME
# ==========================================

st.markdown("## 📅 Sentiment Trends Over Time")

daily_sentiment = (
    filtered_df.groupby(
        ["timestamp", "sentiment"]
    )
    .size()
    .reset_index(name="Posts")
)

fig3 = px.line(
    daily_sentiment,
    x="timestamp",
    y="Posts",
    color="sentiment",
    markers=True,
    color_discrete_map={
        "Positive": "#2ecc71",
        "Negative": "#e74c3c",
        "Neutral": "#3498db"
    },
    title="Daily Sentiment Activity"
)

fig3.update_layout(
    height=450,
    xaxis_title="Date",
    yaxis_title="Number of Posts"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# 9. PLATFORM ANALYSIS
# ==========================================

st.markdown("## 🌐 Platform Analysis")

platform_counts = (
    filtered_df["platform"]
    .value_counts()
    .reset_index()
)

platform_counts.columns = ["Platform", "Posts"]

fig4 = px.bar(
    platform_counts,
    x="Platform",
    y="Posts",
    color="Platform",
    text="Posts",
    title="Posts Across Platforms"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ==========================================
# 10. ANALYZED POSTS
# ==========================================

st.markdown("## 📝 Analyzed Posts")

st.dataframe(
    filtered_df[
        [
            "post_id",
            "text",
            "platform",
            "timestamp",
            "topic",
            "sentiment"
        ]
    ],
    width="stretch",
    hide_index=True
)
# ==========================================
# 11. DOWNLOAD RESULTS
# ==========================================

st.markdown("## 📥 Export Analysis")

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Analyzed Dataset",
    data=csv_data,
    file_name="trendpulse_analysis.csv",
    mime="text/csv"
)

# ==========================================
# 12. FOOTER
# ==========================================

st.divider()

st.caption(
    "TrendPulse AI | Social Media Trend Intelligence "
    "Platform | Built with Python, Streamlit, Pandas "
    "and VADER Sentiment Analysis."
)

st.success("TrendPulse AI is running successfully! 🚀")
