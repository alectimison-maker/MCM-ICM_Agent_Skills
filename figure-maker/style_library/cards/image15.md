id: image15
figure_type: bar
use_case: Compare composition across categories with stacked bars.
tags: [bar, stacked, composition, categorical]

layout:
  aspect: 4:3
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#E08742, #4EAC90, #7FA5A7, #C4DAD4, #9D7354]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Stacked encoding to show totals and composition
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
