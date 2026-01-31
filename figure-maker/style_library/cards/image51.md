id: image51
figure_type: bar
use_case: Compare composition across categories with stacked bars.
tags: [bar, stacked, horizontal, comparison]

layout:
  aspect: 1030:539
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#BCD1ED, #397AAA, #F2D376, #599DA8]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Stacked encoding to show totals and composition
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
