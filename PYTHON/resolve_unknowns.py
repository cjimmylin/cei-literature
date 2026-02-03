"""
Fixes specific "Unknown" authors/years using hardcoded mappings.
See LLM_CONTEXT.md for learnings.

Note: This script uses simple regex for targeted field updates rather than
full YAML parsing because it makes minimal, targeted changes.
For new scripts that modify YAML, use yaml_frontmatter_utils.py.
"""
import os
import re

updates = {
    'papers/2024-Unknown-AEGIS.md': 'Ghosh',
    'papers/2024-Unknown-AI-Face.md': 'Lin',
    'papers/2024-Unknown-CHiSafetyBench.md': 'Zhang',
    'papers/2024-Unknown-Definitive Answer Dataset for LLMs Hallucination.md': 'Rahman',
    'papers/2024-Unknown-JBB-Behaviours.md': 'Chao',
    'papers/2024-Unknown-JBBQ.md': 'Yanaka',
    'papers/2024-Unknown-PSN.md': 'Saffari',
    'papers/2024-Unknown-R-Judge.md': 'Yuan',
    'papers/2024-Unknown-SG-Bench.md': 'Mou',
    'papers/2024-Unknown-StrongREJECT.md': 'Souly',
    'papers/2024-Unknown-tSMC.md': 'Zhou',
    'papers/2024-Unknown-Briefing.md': 'Techne',
    'papers/2025-Unknown-MoCoP.md': 'Jamshidi'
}

def main():
    count_updated = 0
    for fpath, author in updates.items():
        if not os.path.exists(fpath):
            dirname, basename = os.path.split(fpath)
            new_basename = basename.replace('Unknown-', f'{author}-')
            new_path = os.path.join(dirname, new_basename)
            if os.path.exists(new_path):
                continue
            # print(f"File not found: {fpath}")
            continue
            
        with open(fpath, 'r') as f:
            content = f.read()
            
        # Update metadata logic
        changed = False
        if re.search(r'^first_author:', content, re.MULTILINE):
            new_content = re.sub(r'^first_author:.*$', f'first_author: "{author}"', content, flags=re.MULTILINE)
            if new_content != content:
                content = new_content
                changed = True
        else:
            content = re.sub(r'(short_title:.*\n)', f'\\1first_author: "{author}"\n', content)
            changed = True
            
        if re.search(r'^authors: ""', content, re.MULTILINE):
            content = re.sub(r'^authors: ""', f'authors: "{author}"', content, flags=re.MULTILINE)
            changed = True

        if changed:
            with open(fpath, 'w') as f:
                f.write(content)
            
        # Rename
        dirname, basename = os.path.split(fpath)
        new_basename = basename.replace('Unknown-', f'{author}-')
        new_path = os.path.join(dirname, new_basename)
        
        os.rename(fpath, new_path)
        print(f"Resolved {fpath} -> {new_path}")
        count_updated += 1
        
    print(f"Total resolved: {count_updated}")

if __name__ == "__main__":
    main()
