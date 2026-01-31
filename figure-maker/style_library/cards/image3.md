id: image3
figure_type: diagram
use_case: Compare distribution and variability across multiple groups (boxplot summary).
tags: [boxplot, statistical_summary, comparison]

layout:
  aspect: 5:4
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: medium
  marker: none
  grid: none

color:
  palette: muted_qualitative [#BBBBBB, #D5D4D3, #909090, #E9E8E8]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Summarize multiple statistics in one glyph
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
