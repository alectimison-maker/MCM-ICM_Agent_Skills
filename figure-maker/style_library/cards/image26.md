id: image26
figure_type: line
use_case: Compare trends across multiple panels for different subsets.
tags: [line, acf_pacf, diagnostic, small_multiples]

layout:
  aspect: 1095:417
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#CCDAE5, #E5E7E8, #9BAFBE]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
