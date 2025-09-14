# Day 16: Prompt Chaining Demo
# This script demonstrates chaining prompts for multi-step reasoning

prompts = [
    "Extract the main topic from: 'AI is transforming healthcare by enabling faster diagnosis.'",
    "Summarize the topic in one sentence.",
    "Generate a headline for a news article about this topic."
]

outputs = []
for i, prompt in enumerate(prompts):
    # Simulate LLM output (replace with actual LLM call in production)
    if i == 0:
        outputs.append("Main topic: AI in healthcare")
    elif i == 1:
        outputs.append("AI is making healthcare diagnosis faster and more efficient.")
    elif i == 2:
        outputs.append("AI Revolutionizes Healthcare Diagnostics")

for i, (prompt, output) in enumerate(zip(prompts, outputs)):
    print(f"Step {i+1}: {prompt}\nOutput: {output}\n")

# Save outputs to a text file for review
with open('Day-16/prompt_chaining_results.txt', 'w') as f:
    for i, (prompt, output) in enumerate(zip(prompts, outputs)):
        f.write(f"Step {i+1}: {prompt}\nOutput: {output}\n\n")
