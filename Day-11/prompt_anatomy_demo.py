# Day 11: Anatomy of a Prompt – Demo
# This script demonstrates how different prompt structures affect LLM output and visualizes the results

import matplotlib.pyplot as plt
import random
import datetime

# Simulated LLM responses for demonstration (replace with OpenAI API or local LLM for real outputs)
prompts = [
    "Translate 'Hello' to French.",
    "What is the capital of France?",
    "Write a short story about a cat.",
    "Summarize the following text: Artificial intelligence is transforming the world.",
    "List three benefits of exercise."
]

# Simulate different prompt styles
prompt_styles = [
    "Direct",
    "With context",
    "With example",
    "Explicit instruction",
    "Conversational"
]

# Simulated responses (for demo purposes)
responses = [
    ["Bonjour", "Paris", "Once upon a time, there was a clever cat...", "AI is changing many industries.", "1. Health 2. Mood 3. Energy"],
    ["The French word for 'Hello' is 'Bonjour'.", "France's capital is Paris.", "A cat named Whiskers loved adventures...", "AI is revolutionizing technology and society.", "Exercise improves health, mood, and energy."],
    ["Example: 'Hello' in French is 'Bonjour'.", "E.g., Paris is the capital of France.", "E.g., Cats are curious animals...", "E.g., AI is making big changes.", "E.g., Health, mood, energy."],
    ["Translate 'Hello' to French: Bonjour", "Capital of France: Paris", "Short story: The cat chased a butterfly...", "Summary: AI is transforming the world.", "Benefits: Health, mood, energy."],
    ["Hi! 'Hello' in French is 'Bonjour'.", "Hey! Paris is the capital of France.", "Let me tell you a story about a cat...", "Sure! AI is changing the world.", "Absolutely! Health, mood, energy."]
]


# Wrap text in table cells for better readability
def wrap_text(text, width=30):
    import textwrap
    return '\n'.join(textwrap.wrap(text, width))

wrapped_table_data = [[wrap_text(responses[j][i], 30) for j in range(len(prompt_styles))] for i in range(len(prompts))]

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

table = ax.table(cellText=wrapped_table_data, rowLabels=[wrap_text(p, 30) for p in prompts], colLabels=prompt_styles, loc='center', cellLoc='left')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Adjust row heights for better readability
for (row, col), cell in table.get_celld().items():
    if row == -1 or col == -1:
        continue
    # Estimate height based on number of lines in cell text
    lines = str(cell.get_text().get_text()).count('\n') + 1
    cell.set_height(0.08 * lines)


# Add alternating row colors for readability (only data cells, skip headers)
for (row, col), cell in table.get_celld().items():
    # Skip header row and column (row == -1 or col == -1)
    if row == -1 or col == -1:
        continue
    if row % 2 == 0:
        cell.set_facecolor('#f2f2f2')
    else:
        cell.set_facecolor('#e6f7ff')

plt.title('LLM Output Comparison by Prompt Style')
plt.tight_layout()

# Save with timestamp to avoid overwriting manual edits
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'Day-11/prompt_output_comparison_{timestamp}.png'
plt.savefig(filename)
plt.show()
print(f'Prompt output comparison image saved as {filename}')
