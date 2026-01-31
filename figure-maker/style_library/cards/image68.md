id: image68
figure_type: line
use_case: Compare distribution curves across groups or conditions.
tags: [line, density_curve, comparison]

layout:
  aspect: 4:3
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#DAE2DF, #AAABAD, #BADACE]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Overlay multiple series to compare trends
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
