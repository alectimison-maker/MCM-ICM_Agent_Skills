id: image16
figure_type: scatter
use_case: Show clustered observations in feature space.
tags: [scatter, cluster, legend, multigroup]

layout:
  aspect: square
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#CFC8C3, #928B82, #E8EBE9, #AABBB9]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
