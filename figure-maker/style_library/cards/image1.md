id: image1
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, time_series, inset, legend, grid_light]

layout:
  aspect: 1268:447
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#DDE0DE, #A7B9A6, #FFFFFF]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Overlay multiple series to compare trends
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
