from datasets import load_dataset
def main():
    dataset = load_dataset(
        "json",
        data_files={
            "train": "D:/fy_proj/datasets/mor_train/train.jsonl",
            "validation": "D:/fy_proj/datasets/mor_train/valid.jsonl"
        }
    )

    dataset.save_to_disk("D:/fy_proj/datasets/mor_hf")

if __name__ == "__main__":
    main()
