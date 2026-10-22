---
name: howtolivelonger
description: Look up research on longevity, diet, exercise, sleep and everyday habits in the HowToLiveLonger JSON dataset.
---

# HowToLiveLonger

Download and read https://raw.githubusercontent.com/geekan/HowToLiveLonger/main/data/evidence.json.

Match the user's question to entries in `records`. Read `finding`, `action`, `grade`, `effect`, `ci`, `comparison`, `population`, `limitations` and `sources`. `originalClaim` is historical text, not the current finding.

Answer in the user's language, keeping the relevant study population and the dataset’s evidence level. Link the original studies in `sources[].url`. If the dataset does not cover the question, say so.
