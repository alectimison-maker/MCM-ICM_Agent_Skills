id: image44
figure_type: bar
use_case: Compare composition across categories with stacked bars.
tags: [bar, stacked, categorical, composition]

layout:
  aspect: 1073:673
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#C6894D, #E8DAB1, #C9BF7F, #F6F1E4]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Stacked encoding to show totals and composition
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
