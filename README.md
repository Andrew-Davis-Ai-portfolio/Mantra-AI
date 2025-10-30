# Mantra-AI
AI-powered mantra generator that turns any topic into an instant motivational drop. Simple input → High-impact mantra output.
Wealth is a frequency — not a fantasy.”
Mantra-AI — Auto-Generated Mantras for Mindset, Wealth, Leadership & Focus.

Daily mental training powered by AI:
	•	Type your topic → Mantra-AI generates targeted empowerment statements
	•	Instant reframes for discipline, identity, and execution
	•	Optional audio playback & streak tracking (Phase II)

Example Mantra Prompts:
	•	“Give me a wealth mantra.”
	•	“Create a mantra for focus when energy is low.”
	•	“Leadership mantra for when doubt hits.”
	•	“I need a mantra for patience today.”

Mantra Types Included (Starter Set):
	•	🔥 Wealth Mantras — “Money flows where strategy goes.”
	•	🧠 Focus Mantras — “One task done creates the next door.”
	•	🛡️ Confidence Mantras — “Pressure reveals who’s ready.”
	•	👁️ Vision Mantras — “My future listens when I act.”

How to Use Mantra-AI
	1.	Choose a topic (or type your own).
	2.	Receive mantra variations instantly.
	3.	Save favorites to your personal vault.
	4.	Daily streak = daily strength.

Affirmation is temporary.
Mantras are identity commands. ⚡
## 🚀 Quick Start (CLI)

```bash
# From repo root
pip install -e .

# Generate mantras (Hybrid voice)
mantra "Wealth"            # default 5 lines
mantra "Focus when tired"  # any phrase
mantra "Leadership" -n 8   # more lines
mantra "Patience" --save   # saves to ~/.mantra_ai/Patience.txt
mantra "Discipline" --json # machine-readable
---

## What to do now (fastest path)
1. Create folder `mantra_ai/` and drop the three Python files inside.
2. Add `pyproject.toml` and `requirements.txt` at repo root.
3. From terminal: `pip install -e .`
4. Test: `mantra "Wealth Under Pressure" --save`

That’s it. Your **infrastructure stays perfect**, visuals are optional.  
When you want the web or desktop UI, we layer it on top of this CLI core without changing the behavior.
