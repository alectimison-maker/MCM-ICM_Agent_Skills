id: image65
figure_type: scatter
use_case: Show bivariate relationship with marginal distributions.
tags: [scatter, jointplot, marginal_hist, correlation]

layout:
  aspect: 1387:831
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#D5CAB6, #868E87, #EAEEF1, #FFEBCD]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use transparency or jitter to reduce overplotting
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
