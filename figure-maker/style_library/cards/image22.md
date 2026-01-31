id: image22
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, multi_series, convergence, legend]

layout:
  aspect: 3:2
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#B3C0BB, #89909A, #D3E0D1, #F3F3F2]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Overlay multiple series to compare trends
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
