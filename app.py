
import streamlit as st
import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="TrendPulse AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 TrendPulse AI")
st.subheader("Social Media Trend Intelligence Platform")

st.write(
    "Analyze public discussions, discover trending topics "
    "and understand audience sentiment."
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/sample_posts.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()

# -----------------------------
# SENTIMENT ANALYSIS
# -----------------------------
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    return "Neutral"

df["sentiment"] = df["text"].apply(analyze_sentiment)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Dashboard Filters")

topics = ["All"] + sorted(df["topic"].unique().tolist())

selected_topic = st.sidebar.selectbox(
    "Select Topic",
    topics
)

if selected_topic != "All":
    df = df[df["topic"] == selected_topic]

# -----------------------------
# METRICS
# -----------------------------
st.markdown("### Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Posts", len(df))
col2.metric("Positive", (df["sentiment"] == "Positive").sum())
col3.metric("Negative", (df["sentiment"] == "Negative").sum())
col4.metric("Neutral", (df["sentiment"] == "Neutral").sum())

st.divider()

# -----------------------------
# SENTIMENT CHART
# -----------------------------
st.markdown("### Sentiment Distribution")

sentiment_counts = (
    df["sentiment"]
    .value_counts()
    .rename_axis("Sentiment")
    .reset_index(name="Count")
)

fig1 = px.pie(
    sentiment_counts,
    names="Sentiment",
    values="Count",
    hole=0.45,
    title="Audience Sentiment"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# TOPIC ANALYSIS
# -----------------------------
st.markdown("### Topic Popularity")

topic_counts = (
    df["topic"]
    .value_counts()
    .reset_index()
)

topic_counts.columns = ["Topic", "Posts"]

fig2 = px.bar(
    topic_counts,
    x="Topic",
    y="Posts",
    color="Topic",
    title="Posts by Topic"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# SENTIMENT OVER TIME
# -----------------------------
st.markdown("### Sentiment Trends Over Time")

daily = (
    df.groupby(["timestamp", "sentiment"])
    .size()
    .reset_index(name="Posts")
)

fig3 = px.line(
    daily,
    x="timestamp",
    y="Posts",
    color="sentiment",
    markers=True,
    title="Daily Sentiment Trends"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# DATA TABLE
# -----------------------------
st.markdown("### Analyzed Posts")

st.dataframe(
    df[["post_id", "text", "platform",
        "timestamp", "topic", "sentiment"]],
    use_container_width=True
)

st.success("TrendPulse AI dashboard is running!")
