# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/firlifirrizqi/unsent-confession-makefun/rank.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/firlifirrizqi/unsent-confession-makefun/reward.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

A two-part micro-confession for the [Unsent: The Micro-Confession Sprint](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) bounty on make.fun: a `To:` line naming who the unsent message was meant for, and the unsent message itself, one line written exactly as it was typed — specific, honest, and never sent.

## Entry

```text
To: My sister
i was the one who broke your camera before your trip. i let you blame the airline for two years.
```

110 characters total. The confession is specific (a broken camera before a trip, two years of blaming the airline), the reason it stayed in drafts is felt rather than stated (guilt and fear, not a joke or a greeting), and the `To:` line and the message need each other — swap the addressee and the confession stops making sense.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (creating the directory if needed), then verifies it: gate of 1–260 characters, exactly two parts (`To:` line + one message line of at most 200 characters), and a read-back check that the file is byte-identical to the entry.

Standard library only — no network, no secrets, no input files.
