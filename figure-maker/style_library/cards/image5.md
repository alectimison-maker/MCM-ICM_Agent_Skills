id: image5
figure_type: diagram
use_case: Compare distribution and variability across multiple groups (boxplot summary).
tags: [boxplot, comparison, multi_group]

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
  palette: muted_qualitative [#BCBCBB, #D5D3D1, #929191, #EDEBE9]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Summarize multiple statistics in one glyph
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
