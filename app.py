import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# ======================
# Load Dataset Function
# ======================
@st.cache_data
def load_data():
    try:
        # Adjust the path if needed
        df = pd.read_csv("metadata_5000.csv", low_memory=False, nrows=5000)
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df["year"] = df["publish_time"].dt.year
        df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))
        return df
    except Exception as e:
        st.error(f"❌ Failed to load dataset: {e}")
        return pd.DataFrame()

# ======================
# Streamlit Layout
# ======================
st.title("📊 CORD-19 Data Explorer")
st.write("An interactive app to explore COVID-19 research metadata.")

# Load data
df = load_data()

if df.empty:
    st.stop()  # stop app if data failed to load

# Show data preview
if st.checkbox("Show raw data sample"):
    st.write(df.head(20))

# ======================
# Filters
# ======================
if "year" in df.columns and df["year"].notna().any():
    year_min, year_max = int(df["year"].min()), int(df["year"].max())
    year_range = st.slider("Select year range:", year_min, year_max, (year_min, year_max))
    filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]
else:
    st.warning("⚠ No year data found in dataset.")
    filtered_df = df

# ======================
# Papers by Year
# ======================
if not filtered_df.empty:
    st.subheader("Papers Published by Year")
    papers_by_year = filtered_df["year"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=papers_by_year.index, y=papers_by_year.values, ax=ax, color="skyblue")
    ax.set_title("Papers Published by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # ======================
    # Top Journals
    # ======================
    st.subheader("Top 10 Journals Publishing COVID-19 Papers")
    top_journals = filtered_df["journal"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="viridis")
    ax.set_title("Top Journals")
    ax.set_xlabel("Number of Papers")
    ax.set_ylabel("Journal")
    st.pyplot(fig)

    # ======================
    # Word Cloud
    # ======================
    st.subheader("Word Cloud of Paper Titles")
    all_words = " ".join(filtered_df["title"].dropna().astype(str)).lower().split()

    if all_words:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(all_words))
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.info("No titles available to generate word cloud.")
else:
    st.warning("⚠ No data available for selected filters.")