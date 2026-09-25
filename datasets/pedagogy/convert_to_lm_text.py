import json

def convert(in_file, out_file):
    with open(in_file, "r", encoding="utf-8") as fin, \
         open(out_file, "w", encoding="utf-8") as fout:
        for line in fin:
            sample = json.loads(line)

            text = (
                f"Topic: {sample.get('topic', '')}\n"
                f"Level: {sample.get('level', '')}\n"
                f"Style: {sample.get('style', '')}\n"
                f"Explanation: {sample.get('explanation', '')}"
            )

            fout.write(json.dumps({"text": text}, ensure_ascii=False) + "\n")


# paths — change only if needed
convert(
    "D:/fy_proj/datasets/pedagogy/train.jsonl",
    "D:/fy_proj/datasets/pedagogy/train_lm.jsonl"
)

convert(
    "D:/fy_proj/datasets/pedagogy/validation.jsonl",
    "D:/fy_proj/datasets/pedagogy/validation_lm.jsonl"
)

print("Conversion complete.")
