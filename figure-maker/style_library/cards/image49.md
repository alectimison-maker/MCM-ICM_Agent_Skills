id: image49
figure_type: line
use_case: Compare model/classifier performance curves and tradeoffs across methods.
tags: [line, roc, comparison, legend]

layout:
  aspect: 680:609
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#F0EEED, #D3CECB, #91878F]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Overlay multiple series to compare trends
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
