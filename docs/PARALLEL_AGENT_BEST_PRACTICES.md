# Parallel Agent Best Practices

*Learned from 2026-01-25 author enrichment session*

## When to Use Parallel Agents

Use parallel agents for tasks that:
1. Require processing 50+ similar items (authors, papers, files)
2. Each item can be processed independently
3. Task requires web research or external API calls
4. Manual processing would take hours

**Proven use case**: Enriching 408 author profiles in 50 minutes (~50x faster than manual)

## Critical Configuration

### 1. Always Specify Tool Permissions Upfront

❌ **Wrong** - Will fail with permission denials:
```python
Task(
    subagent_type="general-purpose",
    run_in_background=true,
    prompt="Enrich these authors..."
)
```

✅ **Correct** - Pre-approve all needed tools:
```python
Task(
    subagent_type="general-purpose",
    allowed_tools=["WebSearch", "WebFetch", "Read", "Edit", "Write", "Glob", "Grep"],
    run_in_background=true,
    prompt="Enrich these authors..."
)
```

**Why**: Background agents cannot prompt for permissions interactively.

### 2. Optimal Batch Sizes

| Batch Size | Result | Use When |
|------------|--------|----------|
| < 20 items | Too much overhead | Never recommended |
| 20-30 items | Good for complex tasks | Each item needs extensive research |
| 40-50 items | **Optimal for most tasks** | Standard enrichment work |
| 50-70 items | Acceptable | Simple, quick tasks only |
| > 70 items | Memory issues, long runtime | Avoid |

**Sweet spot**: **40-45 items per agent**

### 3. Two-Phase Approach

**Phase 1: Broad Sweep** (85-90% completion expected)
- Split all items into batches of 40-45
- Launch 10-15 parallel agents
- Use general prompts

**Phase 2: Focused Cleanup** (Final 99%+ completion)
- Identify remaining hard cases
- Split into smaller batches (10-15 each)
- Launch 3-5 focused agents
- Use more detailed prompts with context

## Effective Prompt Structure

```
Task: Enrich author profiles

Your batch:
[Clear list of 40 authors]

For EACH author:
1. WebSearch for: "[Name] researcher affiliation"
2. Find: current job, affiliation, research interests
3. Read existing file: Authors/[Name].md
4. Update if placeholder (has "University/Organization" or "Topic 1")
5. Minimum required:
   - Real affiliation
   - 2-3 research interests
   - At least one profile link

Critical: Work through ALL authors in your batch.
Report which ones you successfully enriched.
```

**Key elements**:
- Explicit list of items to process
- Step-by-step instructions
- Clear quality standards
- "Work through ALL" instruction
- Request for summary report

## Launching Agents

### Multiple Agents in Parallel

✅ **Correct** - Single message with multiple Task calls:
```python
# Launch all 10 agents at once
Task(...batch 1...)
Task(...batch 2...)
Task(...batch 3...)
...
Task(...batch 10...)
```

❌ **Wrong** - Sequential calls:
```python
# Don't wait between launches
Task(...batch 1...)
# Wait for response...
Task(...batch 2...)
# Wait for response...
```

## Monitoring Progress

### Check File Modifications
```bash
# Count files modified in last 10 minutes
find Authors -name "*.md" -mmin -10 | wc -l

# List recent updates
find Authors -name "*.md" -mmin -10
```

### Check Completion Status
```python
import os
remaining = 0
for f in os.listdir("Authors"):
    if f.endswith('.md'):
        with open(f"Authors/{f}") as file:
            content = file.read()
            if '"Topic 1"' in content or 'University/Organization' in content:
                remaining += 1
print(f"Remaining: {remaining}")
```

### Agent Activity
- Use system reminders to track agent progress
- Agents report tool usage count and token consumption
- Don't read output files until agents complete (you'll be notified)

## Performance Expectations

### Timing (from 408 author enrichment)
- Setup & batching: 10 minutes
- Phase 1 (10 agents, 356 authors): 20 minutes
- Phase 2 (4 agents, 52 authors): 10 minutes
- Cleanup & verification: 10 minutes
- **Total**: 50 minutes for 408 authors (~7.5 seconds per item)

### Completion Rates
- Phase 1: 85-90% of items
- After Phase 2: 99%+ of items
- Remaining cases: Usually institutional names or metadata errors

## Common Pitfalls

### 1. Permission Denials
**Symptom**: "Permission to use WebSearch has been auto-denied"
**Fix**: Always specify `allowed_tools` parameter

### 2. Memory Issues
**Symptom**: Agents run slowly or timeout
**Fix**: Reduce batch size to 30-40 items

### 3. Incomplete Results
**Symptom**: Agents finish but many items not processed
**Fix**: Add "Work through ALL items" to prompt, use two-phase approach

### 4. No Progress Updates
**Symptom**: Can't tell if agents are working
**Fix**: Check file modification times, agents report progress automatically

## Additional Benefits

Beyond the primary task, parallel agents often discover:
- Data quality issues
- Metadata errors
- Duplicate entries
- Naming inconsistencies

**Example**: During author enrichment, agents found:
- 1 astronomy paper misclassified as AI paper
- 1 paper with wrong first author
- 2 institutional names labeled as people

## Agent Types

### general-purpose
- **Best for**: Research-heavy tasks, web searches, file modifications
- **Has access to**: All tools (WebSearch, Read, Write, Edit, etc.)
- **Use when**: Task requires flexibility and multiple tool types

### Explore
- **Best for**: Codebase exploration, finding files, understanding structure
- **Has access to**: Read-only tools (Glob, Grep, Read)
- **Use when**: Need to search/analyze without modifications

### Bash
- **Best for**: Running shell commands, git operations
- **Has access to**: Bash command execution
- **Use when**: Need to run scripts or system commands

## Checklist for Parallel Agent Tasks

Before launching:
- [ ] Task can be parallelized (items are independent)
- [ ] Batch size determined (40-45 recommended)
- [ ] Tool permissions specified in `allowed_tools`
- [ ] Prompt includes explicit item list
- [ ] Prompt has step-by-step instructions
- [ ] Prompt requests summary report
- [ ] Using `run_in_background=true`
- [ ] Have monitoring strategy ready

## Success Metrics

From 2026-01-25 session:
- **Speed**: 50x faster than manual processing
- **Completion**: 99% of legitimate items
- **Quality**: All profiles met minimum standards
- **Bonus**: Found 2 metadata errors in papers
- **Time/item**: ~7.5 seconds average

## Related Documentation

- [docs/SESSION_2026_01_25_AUTHOR_ENRICHMENT.md](SESSION_2026_01_25_AUTHOR_ENRICHMENT.md) - Detailed session report
- [docs/WORKFLOWS.md](WORKFLOWS.md) - Updated workflows including parallel enrichment
- [docs/SESSION_HISTORY.md](SESSION_HISTORY.md) - Historical context

---

*This document captures key learnings from successfully enriching 408 author profiles using 14 parallel agents. Apply these principles to future large-scale enrichment tasks.*
