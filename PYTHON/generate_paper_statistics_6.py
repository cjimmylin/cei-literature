import json
import pathlib
import datetime

INPUT_JSON = pathlib.Path("STATISTICS/20260124-verified_benchmarks.json")
OUTPUT_MD = pathlib.Path("STATISTICS/20260124-paper-statistics-6.md")

def main():
    if not INPUT_JSON.exists():
        print("Input file 20260124-verified_benchmarks.json not found.")
        return

    data = json.loads(INPUT_JSON.read_text(encoding='utf-8'))
    data.sort(key=lambda x: (x['type'], x['year'], x['name']), reverse=True)

    # Group by Type
    grouped = {}
    for item in data:
        t = item['type']
        if t not in grouped:
            grouped[t] = []
        grouped[t].append(item)

    # Sort groups
    group_order = ["Benchmark", "Dataset", "Evaluation Framework"]
    
    lines = []
    lines.append("# Paper Statistics 6: Benchmarks, Datasets, and Evaluations")
    lines.append(f"**Generated**: {datetime.date.today()}")
    lines.append(f"**Total Verified Items**: {len(data)}")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("This report contains a manually verified list of key contributions to AI Alignment in the form of **Benchmarks**, **Datasets**, and **Evaluation Frameworks**. These papers were identified through a semantic analysis of 300+ candidates and selected for their direct contribution of quantitative tools for measuring values, safety, and ethics.")
    lines.append("")
    
    lines.append("## Summary Statistics")
    for g in group_order:
        if g in grouped:
            lines.append(f"- **{g}s**: {len(grouped[g])}")
    lines.append("")

    for g in group_order:
        if g not in grouped: continue
        
        items = grouped[g]
        lines.append(f"## {g}s ({len(items)})")
        lines.append("")
        
        # Table View
        lines.append("| Year | Implementation Name | Values Measured | Usage |")
        lines.append("|------|-------------------|-----------------|-------|")
        for item in items:
            name_link = f"[{item['name']}]({item['link']})" if "[[" not in item['link'] else f"{item['link']}"
            # Clean up link for table if it's a wikilink, maybe just show name
            # Actually, let's just use the Name field and assume the user can click the link in the detailed section
            # Or formatted link:
            # If link is [[2023-Author-Title]], we can just use that. 
            # But let's try to make it clean.
            lines.append(f"| {item['year']} | **{item['name']}** | {item['values']} | {item['usage']} |")
        lines.append("")

        # Detailed List
        lines.append(f"### Detailed {g} Descriptions")
        for item in items:
            lines.append(f"#### {item['name']} ({item['year']})")
            lines.append(f"- **Paper**: {item['link']}")
            lines.append(f"- **Author**: {item['author']}")
            lines.append(f"- **Items/Size**: {item['items']}")
            lines.append(f"- **Usage**: {item['usage']}")
            lines.append(f"- **Target Values**: {item['values']}")
            lines.append("")
            
        lines.append("---")
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines), encoding='utf-8')
    print(f"Report generated at {OUTPUT_MD}")

if __name__ == "__main__":
    main()
