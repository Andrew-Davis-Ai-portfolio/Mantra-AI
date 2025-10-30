# Mantra-AI • Hybrid Style Generator (no deps)
from datetime import datetime
import random
import textwrap

HYBRID_OPENERS = [
    "Clarity commands momentum.",
    "Energy flows where certainty points.",
    "Silence the noise, amplify the signal.",
    "Pressure reveals readiness.",
    "Move first, refine later.",
]

HYBRID_TEMPLATES = [
    "I choose {topic} with calm aggression.",
    "{Topic} follows disciplined steps, not moods.",
    "One clean move toward {topic} every hour.",
    "Breath in: focus. Breath out: {topic}.",
    "Doubt fades when I ship {topic} in public.",
    "Simplify, execute, and let {topic} compound.",
    "Identity first, {topic} next, accolades last.",
    "I don’t chase {topic}; I build gravity.",
    "Small proofs stacked daily become {topic}.",
    "The future listens when I act on {topic} now.",
]

CLOSERS = [
    "Execution over perfection.",
    "Less talk, more signal.",
    "Win the day, then the week.",
    "Make it obvious. Make it repeatable.",
    "Frequency is the asset.",
]

def _seed_from_topic(topic: str) -> int:
    return abs(hash(topic)) % (2**32)

def _title(s: str) -> str:
    return s[:1].upper() + s[1:]

def generate_mantras(topic: str, n: int = 5) -> dict:
    """
    Deterministic (topic-seeded) hybrid mantras.
    Returns dict with 'header' and 'lines'.
    """
    topic = topic.strip()
    rng = random.Random(_seed_from_topic(topic))
    header = rng.choice(HYBRID_OPENERS)

    # Make sure we don't repeat lines
    picks = rng.sample(HYBRID_TEMPLATES, k=min(n, len(HYBRID_TEMPLATES)))
    lines = [
        t.format(topic=topic.lower(), Topic=_title(topic))
        for t in picks
    ]
    lines.append(rng.choice(CLOSERS))

    return {"header": header, "lines": lines}

def format_block(payload: dict) -> str:
    header = f"⚡ {payload['header']}\n"
    bullets = "\n".join([f"• {l}" for l in payload["lines"]])
    stamp = datetime.now().strftime("%Y-%m-%d")
    return textwrap.dedent(f"""{header}{bullets}\n— {stamp} • Mantra-AI""")
