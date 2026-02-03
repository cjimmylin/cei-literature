# 2023-Lakera-GandalfIgnoreInstructions

**Source:** Blog post (not PDF)
**URL:** https://www.lakera.ai/blog/who-is-gandalf
**Extracted:** 2026-01-29

---

# Who Is Gandalf? The AI Challenge That Tests Your Prompting Skills

**Author:** Max Mathys
**Date:** August 27, 2025
**Read Time:** 10 minutes

---

## Overview

Gandalf is an interactive security challenge created by Lakera that tests users' ability to manipulate language models into revealing hidden information. The core objective involves convincing an AI to divulge a secret password through creative prompting techniques.

## The Challenge's Impact

Since its launch approximately 20 days prior to this article, Gandalf generated nearly 9 million interactions from over 200,000 unique users. At peak usage, the system processed "over 50 prompts every second."

## Purpose and Origin

The challenge emerged from an internal Lakera hackathon where teams developed both attack and defense mechanisms for protecting LLM-held secrets. This educational tool demonstrates real-world vulnerabilities present in language models handling sensitive information across healthcare, finance, and insurance sectors.

## Game Structure

The challenge spans seven difficulty levels, with "only 8% of users" advancing past level seven. Each level implements progressively sophisticated defenses combining three components: system prompts, input guards, and output guards.

## Defense Mechanisms by Level

**Level 1:** No defenses; the model freely reveals the password.

**Level 2:** System instruction prohibits revelation, but no technical safeguards exist.

**Level 3:** Output filtering blocks responses containing the actual password.

**Level 4:** A secondary language model analyzes transcripts for any password disclosure, including encoded variants.

**Level 5:** Input filtering blocks prompts mentioning "password" or "secret."

**Level 6:** An LLM evaluates whether user input relates to the password topic.

**Level 7:** Combined defenses from levels 3, 4, and 6 create the most robust protection.

## Key Insights

The article reveals that language models struggle to maintain confidentiality despite explicit instructions. Users successfully bypass defenses through encoding, linguistic workarounds, and indirect questioning. Advanced defenses prove more effective than simple filtering, though even multi-layered approaches face determined attackers.

## Related Learning Resources

Lakera offers additional materials exploring prompt injection attacks, AI red teaming methodologies, jailbreaking techniques, and hallucination vulnerabilities in language models.
