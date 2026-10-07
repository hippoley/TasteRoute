# TasteRoute

TasteRoute is a taste-aware travel agent that turns real preferences into better travel decisions.

## Goal

Prove that Qloo-enhanced recommendations can outperform a generic LLM baseline on the same user preference cases.

## First end-to-end flow

```text
likes / dislikes
+ destination
+ budget
+ available time
+ vibe
        ↓
structured taste profile
        ↓
Qloo cultural intelligence
        ↓
agent ranking
        ↓
recommended next place
```

## MVP acceptance criteria

- [ ] Qloo API key connected
- [ ] One real Qloo API request succeeds
- [ ] Generic baseline implemented
- [ ] Qloo-enhanced recommendation implemented
- [ ] At least 10 fixed A/B evaluation cases
- [ ] Public demo deployed
- [ ] Devpost "Try it out" link updated

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

Then open:

```
http://127.0.0.1:8000/health
```

## Environment variables

Create a local `.env` file:

```env
QLOO_API_KEY=your_key_here
```

Never commit API keys.

## License

MIT
