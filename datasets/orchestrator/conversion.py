# # import json

# # def convert_validation(in_file, out_file):
# #     with open(in_file, "r", encoding="utf-8") as fin, \
# #          open(out_file, "w", encoding="utf-8") as fout:

# #         for line in fin:
# #             s = json.loads(line)

# #             context = s.get("context", {})
# #             plan = s.get("orchestration_plan", [{}])[0]

# #             topic = context.get("topic", "Unknown")
# #             time_available = context.get("time_available", "Not specified")

# #             text = (
# #                 f"Goal: {s.get('goal', '')}\n"
# #                 f"Topic: {topic}\n"
# #                 f"Time available: {time_available}\n"
# #                 f"Task: Decide which agent should be invoked and with what instruction."
# #             )

# #             out = {
# #                 "text": text,
# #                 "expected_agent": plan.get("agent", ""),
# #                 "expected_instruction": plan.get("input", "")
# #             }

# #             fout.write(json.dumps(out, ensure_ascii=False) + "\n")


# # convert_validation(
# #     "D:/fy_proj/datasets/orchestrator/validation.jsonl",
# #     "D:/fy_proj/datasets/orchestrator/validation_eval.jsonl"
# # )

# # print("Validation set converted successfully.")
















# import json

# def convert_train(in_file, out_file):
#     with open(in_file, "r", encoding="utf-8") as fin, \
#          open(out_file, "w", encoding="utf-8") as fout:

#         for line in fin:
#             s = json.loads(line)

#             context = s.get("context", {})
#             plan = s.get("orchestration_plan", [{}])[0]

#             topic = context.get("topic", "Unknown")
#             time_available = context.get("time_available", "Not specified")

#             text = (
#                 f"Goal: {s.get('goal', '')}\n"
#                 f"Topic: {topic}\n"
#                 f"Time available: {time_available}\n\n"
#                 f"Orchestration decision:\n"
#                 f"Use the {plan.get('agent', '')} agent to {plan.get('input', '')}."
#             )

#             fout.write(json.dumps({"text": text}, ensure_ascii=False) + "\n")


# convert_train(
#     "D:/fy_proj/datasets/orchestrator/train.jsonl",
#     "D:/fy_proj/datasets/orchestrator/train_lm.jsonl"
# )

# print("Training dataset converted successfully.")




# import json

# INPUT_FILE = "validation.jsonl"
# OUTPUT_FILE = "validation_orchestrator.jsonl"

# with open(INPUT_FILE, "r", encoding="utf-8") as fin, \
#      open(OUTPUT_FILE, "w", encoding="utf-8") as fout:

#     for line in fin:
#         obj = json.loads(line)

#         new_text = (
#             f"{obj['text'].split('Task:')[0].strip()}\n\n"
#             "Task: Decide which agent to invoke.\n"
#             "Answer format:\n"
#             "Agent:\n"
#             "Instruction:"
#         )

#         new_obj = {
#             "text": new_text,
#             "expected_agent": obj["expected_agent"],
#             "expected_instruction": obj.get("expected_instruction", "")
#         }

#         fout.write(json.dumps(new_obj, ensure_ascii=False) + "\n")

# print("Conversion complete → validation_orchestrator.jsonl")







# import json

# INPUT = "validation.jsonl"   # or train.jsonl
# OUTPUT = "validation_orchestrator.jsonl"

# with open(INPUT, "r", encoding="utf-8") as fin, open(OUTPUT, "w", encoding="utf-8") as fout:
#     for line in fin:
#         obj = json.loads(line)

#         text = (
#             f"{obj['text']}\n\n"
#             "Answer format:\n"
#             "Agent:\n"
#             "Instruction:\n\n"
#             f"Agent: {obj['expected_agent']}\n"
#             f"Instruction: {obj.get('expected_instruction','')}"
#         )

#         fout.write(json.dumps({"text": text}, ensure_ascii=False) + "\n")

# print("Done.")



# import json

# INPUT = "train.jsonl"
# OUTPUT = "train_orchestrator.jsonl"

# with open(INPUT, "r", encoding="utf-8") as fin, open(OUTPUT, "w", encoding="utf-8") as fout:
#     for line in fin:
#         obj = json.loads(line)

#         text = (
#             f"{obj['text']}\n\n"
#             "Answer format:\n"
#             "Agent:\n"
#             "Instruction:\n\n"
#             f"{obj.get('orchestration_decision','')}"
#         )

#         fout.write(json.dumps({"text": text}, ensure_ascii=False) + "\n")

# print("Converted train.jsonl")





import json

INPUT = "validation.jsonl"        # or validation.jsonl
OUTPUT = "validation_lm.jsonl"    # or validation_lm.jsonl

with open(INPUT, "r", encoding="utf-8") as fin, open(OUTPUT, "w", encoding="utf-8") as fout:
    for line in fin:
        obj = json.loads(line)

        text = (
            f"{obj['prompt']}\n\n"
            "Task: Decide which agent to invoke.\n"
            "Answer format:\n"
            "Agent:\n"
            "Instruction:\n\n"
            "Expected:\n"
            f"{obj['target']}\n"
            f"Instruction: {obj['Instruction']}"
        )

        fout.write(json.dumps({"text": text}, ensure_ascii=False) + "\n")


