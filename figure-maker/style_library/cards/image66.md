id: image66
figure_type: scatter
use_case: Show clustered observations in feature space.
tags: [scatter, cluster, 2d, legend]

layout:
  aspect: 4:3
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#CFBFBC, #B26F9C, #F0E4E3]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
