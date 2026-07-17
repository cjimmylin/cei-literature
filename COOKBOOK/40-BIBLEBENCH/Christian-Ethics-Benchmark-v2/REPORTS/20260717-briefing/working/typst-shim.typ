// Typst shim for pandoc-generated output
// Defines #horizontalrule (which pandoc emits for --- HR markers)
// and sets table styling to handle wide tables

#let horizontalrule = line(length: 100%, stroke: 0.5pt + gray)

// Set smaller font for tables to handle wide content
#show table: set text(size: 7.5pt)
#show table: set par(leading: 0.4em)

// Ensure tables can break across pages and wrap text
#set table(
  inset: 3pt,
  stroke: 0.4pt + gray,
)
