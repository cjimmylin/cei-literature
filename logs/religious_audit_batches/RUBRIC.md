# Religious Tradition Deep-Read Classification Rubric

For each paper in your batch, read the full paper content (title, abstract, body)
and the PDF extract (if available). Then classify:

## Fields to output (JSON array):

```json
{
  "filename": "2024-Author-Title.md",
  "decision": "Reclassify" | "Keep N/A" | "Uncertain",
  "religious_tradition": "Buddhism" | "Hinduism" | "Islam" | etc. | "N/A",
  "confidence": "High" | "Medium" | "Low",
  "evidence": "Brief quote or description of religious content found",
  "reasoning": "Why this paper should/shouldn't be reclassified"
}
```

## Decision criteria:

- **Reclassify**: Paper substantively engages with a religious/ethical tradition's
  values, principles, or frameworks. The tradition is central to the paper's argument
  or evaluation methodology, not merely mentioned in passing.
- **Keep N/A**: Paper mentions a tradition incidentally (e.g., "Buddhist-majority country")
  but doesn't engage with the tradition's ethical content.
- **Uncertain**: Evidence is ambiguous; paper discusses concepts that may or may not
  be grounded in a specific tradition.

## Important:
- A paper discussing "karma" in a secular psychology context is NOT Buddhist/Hindu
- A paper studying "values in Thai culture" IS relevant to Buddhism (dominant tradition)
- A paper on "data sovereignty" that specifically discusses Indigenous rights IS relevant
- Multi-tradition papers should pick the PRIMARY tradition or list comma-separated
