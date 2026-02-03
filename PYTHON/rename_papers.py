"""
Standardizes filenames to YYYY-Author-ShortTitle.md.
See LLM_CONTEXT.md for naming convention.
"""
import os
import re
import glob

def main():
    files = glob.glob('papers/*.md')
    renamed = 0
    for f in files:
        with open(f) as fp:
            content = fp.read()
        
        year_match = re.search(r'^year: "(.*?)"', content, re.MULTILINE)
        author_match = re.search(r'^first_author: "(.*?)"', content, re.MULTILINE)
        title_match = re.search(r'^short_title: "(.*?)"', content, re.MULTILINE)
        
        if year_match and author_match and title_match:
            year = year_match.group(1)
            # Author: Take surname (split by comma or space if needed? usually "Surname, First")
            raw_author = author_match.group(1)
            if ',' in raw_author:
                author = raw_author.split(',')[0].strip()
            else:
                author = raw_author.split(';')[0].strip() # Fallback
            
            title = title_match.group(1).replace(':', '').replace('/', '-').strip()
            
            # Remove bad chars
            title = re.sub(r'[<>:"/\\|?*]', '', title)
            
            new_name = f"{year}-{author}-{title}.md"
            dir_name = os.path.dirname(f)
            new_path = os.path.join(dir_name, new_name)
            
            if os.path.abspath(f) != os.path.abspath(new_path):
                # Check if exists
                if not os.path.exists(new_path):
                    print(f"Renaming {os.path.basename(f)} -> {new_name}")
                    os.rename(f, new_path)
                    renamed += 1
                    
    print(f"Total renamed: {renamed}")

if __name__ == "__main__":
    main()
