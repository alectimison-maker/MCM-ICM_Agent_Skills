id: image50
figure_type: scatter
use_case: Show relationship between two variables.
tags: [scatter, distribution, dense, jitter]

layout:
  aspect: 980:523
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#D6D6B9, #949B99, #F1F4F1]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
