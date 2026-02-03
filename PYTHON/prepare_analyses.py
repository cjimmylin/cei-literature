#!/usr/bin/env python3
"""
Analyze extracted PDF text and update paper markdown files with structured summaries.
This script processes papers ONE AT A TIME and outputs JSON for each paper.
"""

import json
from pathlib import Path

def load_extracted_text(extraction_file):
    """Load the extracted text from a PDF."""
    with open(extraction_file, 'r', encoding='utf-8') as f:
        return f.read()

def load_paper_metadata(paper_file):
    """Load the existing paper markdown file."""
    with open(paper_file, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    """Main function to process papers."""
    vault_dir = Path(__file__).parent
    extractions_dir = vault_dir / "pdf_extractions"
    papers_dir = vault_dir / "papers"
    output_dir = vault_dir / "paper_analyses"
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Get all extracted text files
    extraction_files = sorted(extractions_dir.glob("*.txt"))
    extraction_files = [f for f in extraction_files if not f.name.startswith('_')]
    
    print(f"Found {len(extraction_files)} papers to analyze")
    print("=" * 80)
    
    for idx, extraction_file in enumerate(extraction_files, 1):
        paper_name = extraction_file.stem
        print(f"\n[{idx}/{len(extraction_files)}] {paper_name}")
        
        # Load extracted text
        full_text = load_extracted_text(extraction_file)
        
        # Find matching paper file
        paper_file = papers_dir / f"{paper_name}.md"
        if not paper_file.exists():
            print(f"  Warning: Paper file not found: {paper_file.name}")
            continue
        
        # Load paper metadata
        paper_content = load_paper_metadata(paper_file)
        
        # Create output file with the text to analyze
        output_file = output_dir / f"{paper_name}.json"
        
        # Save analysis data
        analysis_data = {
            'paper_name': paper_name,
            'extraction_file': str(extraction_file),
            'paper_file': str(paper_file),
            'full_text': full_text[:5000],  # First 5000 chars as preview
            'full_text_length': len(full_text),
            'paper_metadata': paper_content[:2000],  # First 2000 chars as preview
            'status': 'ready_for_analysis'
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2)
        
        print(f"  - Text length: {len(full_text):,} characters")
        print(f"  - Analysis data saved to: {output_file.name}")
    
    print("\n" + "=" * 80)
    print(f"Prepared {len(extraction_files)} papers for analysis")
    print(f"Analysis files saved to: {output_dir}")
    print("\nNext: Process each paper individually to generate summaries")

if __name__ == "__main__":
    main()
