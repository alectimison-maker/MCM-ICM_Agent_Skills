id: image47
figure_type: scatter
use_case: Show relationship between two variables.
tags: [scatter, 3d, multigroup]

layout:
  aspect: 16:9
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#CFD9CF, #E0E6E0, #F1F1F1, #A3AC9C]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
