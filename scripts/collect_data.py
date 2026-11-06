
from pathlib import Path
from datasets import load_dataset
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

DATASET_NAME = "Tarakeshwaran/Hackathon_Sentiment_analysis"


def collect_data():

    print("Connecting to Hugging Face...")
    print(f"Dataset: {DATASET_NAME}")

    # Download the training split
    dataset = load_dataset(
        DATASET_NAME,
        split="train"
    )

    # Convert dataset into a Pandas DataFrame
    df = dataset.to_pandas()

    # Save original data without changing its columns
    output_path = RAW_DATA_DIR / "social_media_posts.csv"

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print("\nDataset downloaded successfully!")
    print(f"Total records: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    print(f"Saved at: {output_path}")

    print("\nAvailable columns:")
    print(df.columns.tolist())

    print("\nFirst five records:")
    print(df.head().to_string())


if __name__ == "__main__":
    collect_data()
