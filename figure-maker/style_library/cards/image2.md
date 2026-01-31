id: image2
figure_type: scatter
use_case: Show relationship between two variables.
tags: [scatter, regression, multi_panel, grid_light, legend]

layout:
  aspect: 1170:521
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_single_hue [#D5E1CD, #BEC6B8, #E8F1E4]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
