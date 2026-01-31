id: image56
figure_type: bar
use_case: Show the distribution of values using binned counts.
tags: [bar, distribution, symmetric, histogram]

layout:
  aspect: 16:9
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#045A8D, #5293B5, #CDD5DA, #3F6D88]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use binning to summarize distribution shape
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
