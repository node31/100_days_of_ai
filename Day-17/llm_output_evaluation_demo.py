# Day 17: LLM Output Evaluation Demo
# This script demonstrates scoring LLM outputs using simple metrics

outputs = [
    "AI is transforming healthcare.",
    "AI helps doctors diagnose faster.",
    "AI in healthcare speeds up diagnosis."
]
references = [
    "AI is transforming healthcare.",
    "AI enables faster diagnosis for doctors.",
    "AI accelerates healthcare diagnosis."
]

# Simple accuracy metric (exact match)
accuracy = sum([o == r for o, r in zip(outputs, references)]) / len(outputs)
print(f"Exact Match Accuracy: {accuracy:.2f}")

# Save results to a text file
with open('Day-17/llm_output_evaluation_results.txt', 'w') as f:
    f.write(f"Exact Match Accuracy: {accuracy:.2f}\n")
    for o, r in zip(outputs, references):
        f.write(f"Output: {o}\nReference: {r}\n\n")
