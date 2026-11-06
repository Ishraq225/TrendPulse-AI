
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "social_media_posts.csv"
)

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = PROCESSED_DIR / "social_media_posts.csv"


def prepare_data():

    print("Loading raw dataset...")

    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_FILE}\n"
            "Run python scripts/collect_data.py first."
        )

    df = pd.read_csv(RAW_FILE, encoding="utf-8")

    # Standardize column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
    )

    print(f"Original records: {len(df)}")

    # Check essential source columns
    required = ["text", "timestamp", "platform"]

    missing = [
        column for column in required
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Required columns are missing: {missing}"
        )

    # Create our standard post ID
    # This is an internal row ID, not the original platform ID.
    df["post_id"] = range(1, len(df) + 1)

    # Clean text
    df["text"] = (
        df["text"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Clean platform
    df["platform"] = (
        df["platform"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
    )

    # Convert timestamps
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # Use hashtags as a topic proxy
    # These are not independently verified topic labels.
    if "hashtags" in df.columns:
        df["topic"] = (
            df["hashtags"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        df["topic"] = df["topic"].replace(
            "", "Uncategorized"
        )
    else:
        df["topic"] = "Uncategorized"

    # Preserve original dataset sentiment labels
    if "sentiment" in df.columns:
        df["source_sentiment"] = df["sentiment"]

    # Remove records with missing timestamps or text
    df = df.dropna(subset=["timestamp"])
    df = df[df["text"] != ""]

    # Remove duplicate posts
    df = df.drop_duplicates(
        subset=["text", "timestamp"]
    )

    # Keep useful columns
    useful_columns = [
        "post_id",
        "text",
        "platform",
        "timestamp",
        "topic"
    ]

    optional_columns = [
        "likes",
        "retweets",
        "country",
        "source_sentiment"
    ]

    final_columns = useful_columns + [
        column for column in optional_columns
        if column in df.columns
    ]

    df = df[final_columns].copy()

    # Save cleaned dataset
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )

    print("\nData preparation completed!")

    print(f"Clean records: {len(df)}")
    print(f"Removed records: {len(pd.read_csv(RAW_FILE)) - len(df)}")

    print(f"\nSaved processed data to:\n{OUTPUT_FILE}")

    print("\nFinal columns:")
    print(df.columns.tolist())

    print("\nFirst five cleaned records:")
    print(df.head().to_string())

    print("\nMissing values:")
    print(df.isnull().sum())


if __name__ == "__main__":
    prepare_data()
