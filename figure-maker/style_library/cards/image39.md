id: image39
figure_type: line
use_case: Compare trends across multiple panels for different subsets.
tags: [line, small_multiples, time_series]

layout:
  aspect: 1298:784
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#E3DFBC, #EEF1E2, #C9C2A4]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
