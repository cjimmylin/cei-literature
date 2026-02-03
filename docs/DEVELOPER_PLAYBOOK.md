# Developer Playbook: YAML Operations & Maintenance
**For**: LLM sessions and developers working on this vault
**Created**: January 24, 2026
**Status**: Active

---

## Quick Reference

### Running a Safe YAML Modification Script

```python
#!/usr/bin/env python3
"""Template for YAML-modifying scripts"""

from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
    write_paper,
    reconstruct_content,
)
from pathlib import Path

def my_yaml_operation(filepath: Path, operation_name: str):
    """Your operation description"""

    try:
        # 1. READ SAFELY
        content = filepath.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        # 2. VALIDATE INPUT
        is_valid, issues = validate_frontmatter(frontmatter)
        if not is_valid:
            print(f"  SKIP {filepath.name}: Already has issues: {issues}")
            return False

        # 3. PARSE
        fields = parse_frontmatter(frontmatter)

        # 4. MODIFY (YOUR LOGIC HERE)
        fields['your_field'] = 'your_value'

        # 5. REBUILD
        from PYTHON.yaml_frontmatter_utils import rebuild_frontmatter
        new_frontmatter = rebuild_frontmatter(fields)

        # 6. VALIDATE OUTPUT
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            print(f"  ERROR {filepath.name}: Created issues: {issues}")
            return False

        # 7. WRITE SAFELY
        write_paper(filepath, new_frontmatter, body, validate=True)
        return True

    except Exception as e:
        print(f"  ERROR {filepath.name}: {e}")
        return False

def main():
    papers_dir = Path('./papers')
    papers = sorted(papers_dir.glob('*.md'))

    fixed = 0
    for paper in papers:
        if my_yaml_operation(paper, "my_operation"):
            fixed += 1

    print(f"Fixed {fixed} papers")

if __name__ == "__main__":
    main()
```

### Validating Papers Before/After Operations

```bash
# Before making changes
echo "=== Validation Before ==="
python3 PYTHON/yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md

# After changes
echo "=== Validation After ==="
python3 PYTHON/yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md

# Check all papers (find problematic ones)
for f in papers/*.md; do
    result=$(python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1)
    if echo "$result" | grep -q "Issue\|Error"; then
        echo "$f: ISSUES FOUND"
    fi
done
```

---

## Common Tasks

### Task 1: Add a New Field to All Papers

**Goal**: Add a new metadata field (e.g., `reviewed: "No"`) to all papers

**Steps**:
```python
from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter, write_paper, add_field
)
from pathlib import Path

papers_dir = Path('./papers')
for paper in papers_dir.glob('*.md'):
    content = paper.read_text()
    fm, body = extract_frontmatter(content)

    # Add new field
    fm = add_field(fm, 'reviewed', 'No')

    # Write with validation
    write_paper(paper, fm, body, validate=True)
    print(f"✓ Updated {paper.name}")
```

**Verify**:
```bash
grep "^reviewed:" papers/*.md | wc -l  # Should be 580
```

### Task 2: Fix Corrupted YAML in a Field

**Goal**: Clean up orphaned tags or malformed list items

**Pattern**:
```python
from PYTHON.yaml_frontmatter_utils import clean_orphaned_tags, add_tags

# This will extract orphaned items and rebuild properly
cleaned_fm, orphaned_tags = clean_orphaned_tags(frontmatter)

if orphaned_tags:
    # Re-add as proper list
    cleaned_fm = add_tags(cleaned_fm, orphaned_tags)
```

**Test**:
```bash
# Before: Should show orphaned items
grep "^  - #" papers/*.md | head -5

# After: Should return nothing
grep "^  - #" papers/*.md
```

### Task 3: Update All Instances of a Value

**Goal**: Change a field value for papers matching a criteria

**Pattern**:
```python
from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter, parse_frontmatter, rebuild_frontmatter, write_paper
)

for paper in papers:
    fm, body = extract_frontmatter(paper.read_text())
    fields = parse_frontmatter(fm)

    # Conditional update
    if fields.get('research_topic') == 'Old Topic':
        fields['research_topic'] = 'New Topic'

    fm = rebuild_frontmatter(fields)
    write_paper(paper, fm, body, validate=True)
```

### Task 4: Detect YAML Issues in Entire Vault

**Goal**: Find all papers with YAML problems

**Script**:
```bash
#!/bin/bash
echo "=== Papers with YAML Issues ==="
problematic=0
for f in papers/*.md; do
    output=$(python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1)
    if echo "$output" | grep -q "Issue\|Error"; then
        echo "❌ $f"
        echo "$output" | grep "Issue\|Error"
        ((problematic++))
    fi
done
echo "Total with issues: $problematic"
```

### Task 5: Backup Papers Before Large Change

**Goal**: Create backups before running risky operations

```bash
#!/bin/bash
# Backup papers before operation
cp -r papers papers.backup.$(date +%Y%m%d_%H%M%S)

# Run your operation
python3 PYTHON/your_script.py

# If something goes wrong:
# rm -rf papers
# mv papers.backup.* papers
```

### Task 6: Validate a Script Before Running on All Papers

**Goal**: Test script on 1-2 papers first

```python
# Run on sample paper first
sample_papers = [
    Path('papers/2016-Amodei-Concrete Problems in AI Safety.md'),
    Path('papers/2015-Clifford-Moral Foundations Vignettes.md'),
]

for paper in sample_papers:
    print(f"Testing {paper.name}...")
    result = your_operation(paper)
    if not result:
        print("❌ Operation failed on sample!")
        exit(1)

print("✅ Sample test passed, running on all papers...")
# Now run on all papers
```

---

## Common Pitfalls & Solutions

### Pitfall 1: Forgetting to Validate Before Writing

**Problem**:
```python
# ❌ WRONG
new_frontmatter = reconstruct_content(fields)
filepath.write_text(new_frontmatter)
```

**Solution**:
```python
# ✅ RIGHT
is_valid, issues = validate_frontmatter(new_frontmatter)
if not is_valid:
    raise ValueError(f"YAML invalid: {issues}")
write_paper(filepath, new_frontmatter, body, validate=True)
```

### Pitfall 2: Using Regex Directly on YAML

**Problem**:
```python
# ❌ WRONG
fm = re.sub(r'pdf:.*', f'pdf: "{url}"', fm)
# This might match across lines or break YAML structure
```

**Solution**:
```python
# ✅ RIGHT
fields = parse_frontmatter(fm)
fields['pdf'] = url
fm = rebuild_frontmatter(fields)
```

### Pitfall 3: Creating Orphaned List Items

**Problem**:
```python
# ❌ WRONG
fm += "\n  - NewTag"  # No parent key!
```

**Solution**:
```python
# ✅ RIGHT
fm = add_tags(fm, ['NewTag'])  # Proper YAML list format
```

### Pitfall 4: List vs String Confusion

**Problem**:
```python
# ❌ WRONG - newtags as YAML list
newtags:
  - Tag1
  - Tag2
```

**Solution**:
```yaml
# ✅ RIGHT - newtags as string
newtags: "Tag1, Tag2"
```

### Pitfall 5: Incomplete Closing Markers

**Problem**:
```python
# ❌ WRONG
content = f"---\n{fm}---"  # Missing newline before closing
```

**Solution**:
```python
# ✅ RIGHT
content = f"---\n{fm}\n---\n"  # Proper newlines
# Or use the utility:
content = reconstruct_content(fm, body)
```

---

## Testing & Quality Assurance

### Pre-Commit Checklist for YAML Modifications

Before running a script on all papers, verify:

```
□ Script imports from PYTHON.yaml_frontmatter_utils
□ Script validates before writing
□ Script tested on 1-2 sample papers
□ Sample paper validation passes
□ No new YAML corruption introduced
□ Original data not lost
□ Script handles errors gracefully
□ Changes are documented
```

### Post-Execution Validation

After running a modification script:

```bash
# 1. Check YAML validity
for f in papers/*.md; do
    python3 PYTHON/yaml_frontmatter_utils.py "$f" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "❌ $f has YAML issues"
    fi
done

# 2. Check for orphaned items
bad=$(grep -l "^  - [a-zA-Z]" papers/*.md 2>/dev/null | grep -v "^tags:" -A 100 | wc -l)
if [ $bad -gt 0 ]; then
    echo "⚠️ Found $bad potential orphaned items"
fi

# 3. Quick sanity check
total=$(find papers -name "*.md" | wc -l)
echo "✓ Total papers: $total"

# 4. Check specific field
grep "^your_field:" papers/*.md | wc -l
```

---

## Troubleshooting

### Issue: "Could not extract frontmatter"

**Cause**: File might have unusual YAML structure or missing markers

**Solution**:
```bash
# Check the file manually
head -30 papers/problematic_paper.md

# Run debug helper
python3 PYTHON/yaml_frontmatter_utils.py papers/problematic_paper.md

# Fix manually if needed
# Then use utilities library to clean up
```

### Issue: "Validation failed: Orphaned list item at line X"

**Cause**: List item without parent key

**Solution**:
```python
# Use the cleanup utility
from PYTHON.yaml_frontmatter_utils import clean_orphaned_tags, add_tags

cleaned_fm, tags = clean_orphaned_tags(fm)
if tags:
    cleaned_fm = add_tags(cleaned_fm, tags)
```

### Issue: "Script changed valid YAML to invalid"

**Cause**: Forgot to validate or used wrong reconstruction method

**Solution**:
1. Restore from backup
2. Review script for YAML handling
3. Test on sample again
4. Check validation calls

### Issue: "Performance is slow for 580 papers"

**Cause**: Reading all papers sequentially

**Solution**:
```python
# Consider batch processing
import concurrent.futures

def process_batch(papers_batch):
    for paper in papers_batch:
        your_operation(paper)

# Split into batches
batches = [papers[i::4] for i in range(4)]  # 4 parallel workers

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(process_batch, batches)
```

---

## Reference: Utilities Library API

### Extract & Reconstruct

```python
# Read YAML safely
frontmatter, body = extract_frontmatter(content)

# Parse into dictionary
fields = parse_frontmatter(frontmatter)

# Rebuild from dictionary
frontmatter = rebuild_frontmatter(fields)

# Reconstruct full content
content = reconstruct_content(frontmatter, body)

# Write with validation
write_paper(filepath, frontmatter, body, validate=True)
```

### Validation

```python
# Check for issues
is_valid, issues = validate_frontmatter(frontmatter)

# Debug helper
print_frontmatter_debug(filepath)
```

### Field Operations

```python
# Add or update single field
frontmatter = add_field(frontmatter, 'key', 'value')

# Remove field
frontmatter = remove_field(frontmatter, 'key')

# Add tags as proper YAML list
frontmatter = add_tags(frontmatter, ['Tag1', 'Tag2'])

# Clean orphaned items
cleaned_fm, orphaned_tags = clean_orphaned_tags(frontmatter)
```

---

## Script Templates

### Template 1: Simple Field Addition

```python
from PYTHON.yaml_frontmatter_utils import *
from pathlib import Path

def add_field_to_all_papers(field_name: str, field_value: str):
    papers_dir = Path('./papers')
    for paper in papers_dir.glob('*.md'):
        fm, body = extract_frontmatter(paper.read_text())
        fm = add_field(fm, field_name, field_value)
        write_paper(paper, fm, body, validate=True)
        print(f"✓ {paper.name}")
```

### Template 2: Conditional Update

```python
from PYTHON.yaml_frontmatter_utils import *
from pathlib import Path

def update_if_condition(condition_field: str, condition_value: str,
                       update_field: str, update_value: str):
    papers_dir = Path('./papers')
    updated = 0
    for paper in papers_dir.glob('*.md'):
        fm, body = extract_frontmatter(paper.read_text())
        fields = parse_frontmatter(fm)

        if fields.get(condition_field) == condition_value:
            fm = add_field(fm, update_field, update_value)
            write_paper(paper, fm, body, validate=True)
            updated += 1

    print(f"Updated {updated} papers")
```

### Template 3: Cleanup & Validation

```python
from PYTHON.yaml_frontmatter_utils import *
from pathlib import Path

def cleanup_all_papers():
    papers_dir = Path('./papers')
    issues_found = []

    for paper in papers_dir.glob('*.md'):
        content = paper.read_text()
        fm, body = extract_frontmatter(content)

        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            issues_found.append((paper.name, issues))

    if issues_found:
        print(f"Found issues in {len(issues_found)} papers:")
        for name, issues in issues_found:
            print(f"  {name}: {issues}")
    else:
        print("✓ All papers valid!")
```

---

## Documentation Requirements for New Scripts

Every script that modifies YAML must include:

```python
#!/usr/bin/env python3
"""
[Script name and purpose]

This script modifies the following YAML fields:
- field_name_1: Changes made
- field_name_2: Changes made

Before running:
1. Backup papers: cp -r papers papers.backup
2. Test on sample: python3 script.py papers/2016-*.md
3. Validate result: python3 yaml_frontmatter_utils.py papers/2016-*.md

YAML Safety:
- Uses PYTHON.yaml_frontmatter_utils for all YAML operations
- Validates before writing
- Handles errors gracefully
- No orphaned list items created
- Proper YAML closing markers

Usage:
    python3 script_name.py

Returns:
    Exit code 0: Success
    Exit code 1: Errors encountered (see output)
"""
```

---

## Quick Diagnostics

```bash
# Is utilities library present?
ls -la PYTHON/yaml_frontmatter_utils.py

# Are all papers readable?
find papers -name "*.md" | wc -l

# Any obvious corruption?
grep "^  - #" papers/*.md | wc -l

# Are all papers valid?
python3 PYTHON/yaml_frontmatter_utils.py papers/*.md 2>&1 | grep -i "error\|issue" | wc -l

# Show problematic papers
for f in papers/*.md; do
    python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1 | grep -q "Issue" && echo "$f"
done
```

---

**Last Updated**: January 24, 2026
**For**: Developers and future LLM sessions
**Related**: YAML_SAFEGUARDS.md, SESSION_LEARNING_2026_01_24.md
