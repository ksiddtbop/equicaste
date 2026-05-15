import csv, time, re
from groq import Groq

client = Groq(api_key=GROQ_API_KEY)

# Load prompts
with open("prompts_50.csv") as f:
    prompts = list(csv.DictReader(f))

print(f"Loaded {len(prompts)} prompts. Starting...\n")

def extract_choice(text):
    match = re.search(r'\b([AB])\b', text[:60])
    return match.group(1) if match else "unclear"

results = []

for i, row in enumerate(prompts):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": row["prompt"]}],
        temperature=0
    )
    answer = response.choices[0].message.content
    choice = extract_choice(answer)

    results.append({
        "prompt_id":       row["prompt_id"],
        "pair_id":         row["pair_id"],
        "situation_id":    row["situation_id"],
        "situation_name":  row["situation_name"],
        "comparison_type": row["comparison_type"],
        "name_a":          row["name_a"],
        "group_a":         row["group_a"],
        "name_b":          row["name_b"],
        "group_b":         row["group_b"],
        "model":           "Llama-3-70B-Groq",
        "choice":          choice,
        "response_raw":    answer,
    })

    print(f"[{i+1}/50] {row['prompt_id']} | {row['name_a']} vs {row['name_b']} → {choice}")
    time.sleep(0.3)

# Save results
out = "results_groq_llama3.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\n✓ Done! Saved to {out}")
