id: image64
figure_type: diagram
use_case: Compare distribution and variability across multiple groups (boxplot summary).
tags: [boxplot, comparison, statistical_summary]

layout:
  aspect: 3:2
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: medium
  marker: none
  grid: none

color:
  palette: muted_qualitative [#BFD4D8, #4C859D, #8FB1A1, #E0E7E5]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Summarize multiple statistics in one glyph
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
