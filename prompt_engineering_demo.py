# Day 12: Prompt Engineering Basics – Demo
# This script demonstrates how prompt templates, temperature, and few-shot examples affect LLM output and visualizes the results

import matplotlib.pyplot as plt
import random
import datetime

# Simulated LLM responses for demonstration (replace with OpenAI API or local LLM for real outputs)
prompts = [
    "Translate 'Hello' to French.",
    "What is the capital of France?",
    "Write a short story about a cat."
]

# Simulate different prompt engineering techniques
techniques = [
    "Basic Prompt",
    "Prompt Template",
    "Few-Shot Example",
    "Temperature: Low",
    "Temperature: High"
]

# Simulated responses (for demo purposes)
responses = [
    ["Bonjour", "Paris", "Once upon a time, there was a clever cat..."],
    ["Translate: 'Hello' -> 'Bonjour'", "Capital: France -> Paris", "Story: Cat -> Whiskers loved adventures..."],
    ["Example: 'Hello' in French is 'Bonjour'.", "E.g., Paris is the capital of France.", "E.g., Cats are curious animals..."],
    ["Bonjour", "Paris", "A cat sat quietly by the window."],
    ["Bonjouuuur!", "Paaariis!", "The cat danced on the moon and sang a song."]
]

# Wrap text for better readability
def wrap_text(text, width=30):
    import textwrap
    return '\n'.join(textwrap.wrap(text, width))

wrapped_table_data = [[wrap_text(responses[j][i], 30) for j in range(len(techniques))] for i in range(len(prompts))]

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
table = ax.table(cellText=wrapped_table_data, rowLabels=[wrap_text(p, 30) for p in prompts], colLabels=techniques, loc='center', cellLoc='left')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Adjust row heights for better readability
for (row, col), cell in table.get_celld().items():
    if row == -1 or col == -1:
        continue
    lines = str(cell.get_text().get_text()).count('\n') + 1
    cell.set_height(0.08 * lines)
    # Add alternating row colors
    if row % 2 == 0:
        cell.set_facecolor('#f2f2f2')
    else:
        cell.set_facecolor('#e6f7ff')

plt.title('LLM Output Comparison by Prompt Engineering Technique')
plt.tight_layout()
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'Day-12/prompt_engineering_comparison_{timestamp}.png'
plt.savefig(filename)
plt.show()
print(f'Prompt engineering comparison image saved as {filename}')
