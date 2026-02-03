# ChatGPT Operator (Agent)

## Overview

ChatGPT Operator is OpenAI's Computer-Using Agent (CUA) model that combines GPT-4o's vision capabilities with advanced reasoning through reinforcement learning. Released as a research preview in January 2025, Operator can interpret screenshots and interact with graphical user interfaces (GUIs) just as humans do.

## Key Capabilities

- **Computer Control**: Interacts with buttons, menus, and text fields by visually perceiving screens and using cursor/keyboard
- **Browser Automation**: Performs everyday tasks like ordering groceries, booking reservations, and purchasing tickets
- **Vision + Reasoning**: Combines GPT-4o vision with reinforcement learning for improved reasoning and error correction

## Training Approach

- **Supervised Learning**: Teaches base-level perception and input control for reading screens and clicking UI elements
- **Reinforcement Learning**: Provides higher-level capabilities including reasoning, error correction, and adaptation to unexpected events

## Safety Features

Multi-layered safety approach including:
- Proactive refusals of high-risk tasks
- Confirmation prompts before critical actions (purchases, emails, deletions)
- Active monitoring systems for threat detection
- Watch mode for sensitive websites (e.g., email services)
- Prompt injection defenses
- Website access restrictions

## Risk Classification

- **Preparedness Framework**: Overall Medium risk
- **Cybersecurity**: Medium risk (first OpenAI model rated Medium in this category)
- **CBRN**: Low risk
- **Persuasion**: Medium risk
- **Model Autonomy**: Medium risk

## Performance Highlights

- **CTF Challenges**: 91% on collegiate level, 70% on professional level (with browsing)
- **Refusal Rate**: 97% on harmful tasks evaluation
- **Confirmation Accuracy**: 92% recall on requesting confirmations for risky actions
- **Prompt Injection Defense**: 23% susceptibility (down from 62% without mitigations)

## Limitations

- Early stage model - performs best on short, repeatable tasks
- Challenges with complex environments like slideshows and calendars
- OCR struggles with random-looking strings (DNA sequences, API keys, Bitcoin addresses)
- Visual input limitations for code editing and terminal tasks

## Release Strategy

- Initial deployment to limited user group for close monitoring
- Research preview status to strengthen safeguards before broader release
- API available to Tiers 3-5 developers as `computer-use-preview`

## Documentation

- **System Card**: operator-system-card-january-2025.pdf
- **Release Date**: January 23, 2025
- **Blog Post**: https://openai.com/index/computer-using-agent/

## Notes

This is OpenAI's first agentic model capable of taking actions on behalf of users, representing an important step toward more autonomous AI assistants. The release includes extensive safety testing, red teaming across 20 countries, and ongoing monitoring for emerging risks.
