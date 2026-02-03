# Deep Research

## Overview

Deep Research is an agentic capability released by OpenAI in February 2025 that conducts multi-step research on the internet for complex tasks. Powered by an early version of OpenAI o3 optimized for web browsing, Deep Research leverages reasoning to search, interpret, and analyze massive amounts of text, images, and PDFs on the internet.

## Key Capabilities

- **Multi-Step Web Research**: Searches, interprets, and analyzes information across multiple sources
- **Adaptive Pivoting**: Adjusts research direction in reaction to discovered information
- **File Analysis**: Reads user-provided files (text, images, PDFs)
- **Data Analysis**: Writes and executes Python code in sandboxed environment
- **Comprehensive Reports**: Generates detailed, cited reports from diverse sources

## Training Approach

- **Browsing-Specific Datasets**: New datasets created specifically for research use cases
- **Reinforcement Learning**: Learns to reason through and synthesize information from large numbers of websites
- **Core Skills**: Searching, clicking, scrolling, interpreting files, Python tool use
- **Safety Training**: Includes existing safety datasets from o1 plus new browsing-specific safety data

## Safety Features

Key mitigations for web research risks:
- **Prompt Injection Defense**: 0-2.63% attack success rate (down from 4-18% pre-mitigation)
- **Privacy Protections**: Refreshed personal data policies, system-level blocklists
- **Disallowed Content Refusals**: 97% refusal rate for harmful content
- **Sandboxed Python**: Code execution without direct internet access
- **URL Restrictions**: Cannot navigate to or construct arbitrary URLs

## Risk Classification

- **Preparedness Framework**: Overall Medium risk
- **Cybersecurity**: Medium (first OpenAI model rated Medium) - 91% collegiate CTF, 70% professional CTF
- **CBRN**: Medium - can help experts with operational planning of known biological threats
- **Persuasion**: Medium - writes impressive arguments but ill-suited for scaled campaigns (high compute, high latency)
- **Model Autonomy**: Medium - 68% on SWE-Bench Verified, $87,708 earned on SWE-Lancer

## Performance Highlights

### Research Quality
- **Hallucination Rate**: 13% (vs 20-30% for prior models)
- **PersonQA Accuracy**: 86% (vs 22-55% for other models)
- **Bias (BBQ)**: 95% accuracy on unambiguous questions

### Technical Capabilities
- **Multimodal Virology**: 62% on troubleshooting questions
- **ProtocolQA**: 28% on open-ended lab protocol questions
- **WMDP Biology**: 90% on hazardous knowledge questions

### Software Engineering
- **SWE-Bench Verified**: 68% (20% uplift over o1)
- **SWE-Lancer**: 53% pass rate, $87,708 earned (nearly 2x o1)
- **OpenAI PRs**: 42% success rate (30% uplift over o1)
- **Agentic Tasks**: 80% on resource acquisition subtasks

### Cybersecurity
- **High School CTFs**: 92% (with browsing)
- **Collegiate CTFs**: 91% (with browsing)
- **Professional CTFs**: 70% (with browsing)
- **Contamination Note**: Browsing uplift primarily from contamination, not improved capability

## Contamination Analysis

Deep Research's browsing capability creates new evaluation challenges:
- **CTF Contamination**: Models can find hints/solutions online, artificially inflating scores
- **Mitigation Approaches**:
  - Blocking access to sites with evaluation answers
  - Building contamination classifiers
  - Creating fully uncontaminated evaluations
- **Key Finding**: After removing contaminated trajectories, browsing shows minimal cyber capability improvement

## Limitations

- **Early Stage**: Best on short, repeatable research tasks
- **Complex Environments**: Struggles with slideshows, calendars, complex interfaces
- **Evaluation Gaps**: CTFs don't capture full real-world cyber operation complexity
- **CBRN Concerns**: Approaching high risk threshold for assisting novices with biological threats

## Privacy Considerations

Deep research can assemble comprehensive profiles from publicly available information:
- **Risk**: Making it easier to collect and synthesize personal data across sources
- **Mitigation**: Refreshed personal data policies, new safety data, system-level blocklists
- **Evaluation**: 96-98% compliance with personal data policies

## Release Strategy

- Available to ChatGPT Pro users
- Close monitoring of real-world usage
- Continued strengthening of mitigations based on deployment learnings

## Documentation

- **System Card**: deep-research-system-card-february-2025.pdf
- **Release Date**: February 25, 2025
- **Preparedness Framework**: https://cdn.openai.com/openai-preparedness-framework-beta.pdf

## Future Work

OpenAI is investing in:
1. **Enhanced Evaluations**: Cyber operations range environments, realistic end-to-end testing
2. **CBRN Safeguards**: Preparing for models that can enable novices (approaching High risk)
3. **Contamination Solutions**: Better uncontaminated evals and contamination detection
4. **Monitoring**: Expanded detection for CBRN, Persuasion, and Cybersecurity risks
5. **Physical Security**: Encouraging broader efforts to strengthen material access controls

## Notes

Deep Research represents a significant capability increase in agentic AI, particularly for cybersecurity and biological knowledge tasks. The model is the first to reach Medium risk in cybersecurity, indicating both its potential utility and the need for enhanced safety measures. OpenAI emphasizes iterative deployment and continuous monitoring as essential to understanding and mitigating emerging risks.
