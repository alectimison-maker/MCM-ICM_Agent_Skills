id: image46
figure_type: bar
use_case: Show the distribution of values using binned counts.
tags: [histogram, distribution, bar]

layout:
  aspect: square
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#E5E7E3, #799377, #89C088, #90D191, #F0F9E8]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use binning to summarize distribution shape
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
