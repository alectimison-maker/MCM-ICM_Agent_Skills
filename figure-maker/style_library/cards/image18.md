id: image18
figure_type: line
use_case: Compare trends across multiple panels for different subsets.
tags: [line, small_multiples, comparison]

layout:
  aspect: square
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#EDE8E8, #C4BCBC, #FFFFFF]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
