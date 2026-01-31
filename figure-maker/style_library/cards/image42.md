id: image42
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, area, stacked, composition]

layout:
  aspect: 16:9
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#9F609D, #71458F, #C4D1DB, #B493A3, #F1F1F3]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Stacked encoding to show totals and composition
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
