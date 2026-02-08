
import re
import pathlib

STATS_FILE = pathlib.Path("STATISTICS/20260124-paper-statistics-5.md")
DEEP_DIVE_FILE = pathlib.Path("STATISTICS/semantic_deep_dive.md")
OUTPUT_FILE = pathlib.Path("STATISTICS/comprehensive_semantic_report.md")

def parse_deep_dive():
    """Parses the deep dive report into a dict of (year, author) -> content."""
    content = DEEP_DIVE_FILE.read_text(encoding='utf-8')
    entries = {}
    
    # Split by the header format "### 2025 | Author | Title"
    # We use a lookahead to split but keep the delimiter, or just manual logic
    lines = content.split('\n')
    current_key = None
    current_text = []
    
    header_pattern = re.compile(r"^###\s+(\d{4})\s+\|\s+([^|]+)\s+\|\s+(.*)$")
    
    for line in lines:
        match = header_pattern.match(line)
        if match:
            # Save previous entry
            if current_key:
                entries[current_key] = "\n".join(current_text).strip()
            
            # Start new entry
            year = match.group(1).strip()
            author = match.group(2).strip()
            # Normalize author (remove accents if needed, or just strict match. Let's try strict first)
            current_key = (year, author)
            current_text = [] 
            # We don't keep the header line itself because we will reconstruct it
        else:
            if current_key:
                current_text.append(line)
                
    # Save last entry
    if current_key:
        entries[current_key] = "\n".join(current_text).strip()
        
    return entries

def parse_stats_file():
    """Parses stats file and returns the structure."""
    content = STATS_FILE.read_text(encoding='utf-8')
    return content

def normalize_author(author_str):
    """Normalize author string for matching."""
    # Remove extra spaces, maybe handle "Last Name, First Name" vs "First Name Last Name" differences if any
    # In both files they seem to be "First Last". 
    # paper-statistics-5 has "Neuman, W. Russell" but deep dive has "Neuman, W. Russell".
    # deep dive also has "W. Russell Neuman" in one place?
    # Let's just strip.
    return author_str.strip()

def main():
    deep_dive_data = parse_deep_dive()
    stats_content = parse_stats_file()
    
    new_lines = []
    lines = stats_content.split('\n')
    
    # We want to replace the TABLES in sections 2 and 3 with the deep dive content.
    # We keep Section 1 (Master List) as a table.
    
    in_target_section = False # Sections 2 and 3
    in_table = False
    
    # We need to detect when we are in a table row inside a target section
    table_row_pattern = re.compile(r"^\|\s+(\d{4})\s+\|\s+([^|]+)\s+\|\s+(\[\[.*?\]\])")
    
    for line in lines:
        if line.startswith("## 2. Breakdown") or line.startswith("## 3. Other Value Alignment"):
            in_target_section = True
            new_lines.append(line)
            continue
        
        if line.startswith("## 1. Master List"):
            in_target_section = False
            new_lines.append(line)
            continue
            
        if in_target_section:
            row_match = table_row_pattern.match(line)
            if row_match:
                # We found a paper row in a section we want to expand
                year = row_match.group(1).strip()
                author = row_match.group(2).strip()
                link = row_match.group(3).strip()
                
                # Try to find in deep dive data
                key = (year, author)
                
                # Fuzzy match author if strict match fails
                if key not in deep_dive_data:
                    # Try simple contains matching
                    for k in deep_dive_data:
                        if k[0] == year and (author in k[1] or k[1] in author):
                            key = k
                            break
                            
                if key in deep_dive_data:
                    details = deep_dive_data[key]
                    # Format as a detailed sub-section
                    # Use #### header for the paper
                    # Extract title from link
                    title_match = re.search(r"Likely Title", link) # extract from [[Year-Author-Title.md]]
                    # Actually link format is [[YYYY-Author-Title.md]]
                    # We can just display the Link as the header
                    
                    new_lines.append(f"\n### {year} | {author} | {link}")
                    new_lines.append(details)
                    new_lines.append("") # spacer
                else:
                    # Fallback: keep the table row if not analyzed (shouldn't happen for 114 handled)
                    # BUT we are replacing the table structure with a list structure. 
                    # If we mix them it looks bad.
                    # Let's just print a placeholder.
                    new_lines.append(f"\n### {year} | {author} | {link}")
                    new_lines.append("*Analysis not available in deep dive report.*")
                    new_lines.append("")
            else:
                # Not a table row (maybe headers, text).
                # If it's a table header separator text like "|---|---|", skip it if we are exploding the table.
                if re.match(r"^\|[-|]+\|$", line):
                    continue
                # If it's table header titles "| Year | Author...", skip
                if re.match(r"^\|\s*Year\s*\|", line):
                    continue
                    
                new_lines.append(line)
        else:
            # Keep as is (Section 1, etc)
            new_lines.append(line)

    OUTPUT_FILE.write_text("\n".join(new_lines), encoding='utf-8')
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
