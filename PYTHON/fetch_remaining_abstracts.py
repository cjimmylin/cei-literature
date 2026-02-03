#!/usr/bin/env python3
"""Mark papers without abstracts as 'No abstract available' or try to find them."""

from pathlib import Path

from vault_config import PAPERS_DIR

def has_abstract(content):
    if '## Abstract' not in content:
        return False
    abstract_section = content.split('## Abstract')[1].split('##')[0].strip()
    return bool(abstract_section)

def add_no_abstract_marker(filepath):
    """Add 'No abstract available.' to papers without abstracts."""
    content = filepath.read_text(encoding='utf-8')

    marker = "*No abstract available in source.*"

    if '## Abstract' in content:
        # Replace empty abstract section
        parts = content.split('## Abstract')
        before = parts[0]
        after_parts = parts[1].split('##', 1)
        rest = '##' + after_parts[1] if len(after_parts) > 1 else ''
        new_content = before + '## Abstract\n\n' + marker + '\n\n' + rest
    elif '## Notes' in content:
        # Insert before Notes section
        new_content = content.replace('## Notes', f'## Abstract\n\n{marker}\n\n## Notes')
    else:
        # Append at the end
        new_content = content + f'\n## Abstract\n\n{marker}\n'

    filepath.write_text(new_content, encoding='utf-8')

def main():
    updated = 0

    for md_file in sorted(PAPERS_DIR.glob('*.md')):
        content = md_file.read_text(encoding='utf-8')

        if has_abstract(content):
            continue

        add_no_abstract_marker(md_file)
        print(f"Marked: {md_file.name[:60]}...")
        updated += 1

    print(f"\n{'='*50}")
    print(f"Marked {updated} papers as 'No abstract available'")

if __name__ == "__main__":
    main()
