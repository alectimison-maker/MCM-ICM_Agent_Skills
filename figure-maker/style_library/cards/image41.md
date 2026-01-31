id: image41
figure_type: scatter
use_case: Show clustered observations in feature space.
tags: [scatter, 3d, cluster, legend]

layout:
  aspect: 3:2
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#F0F1F0, #DFDFDE, #AA9DA4]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
