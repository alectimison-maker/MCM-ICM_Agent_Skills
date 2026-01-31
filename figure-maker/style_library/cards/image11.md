id: image11
figure_type: heatmap
use_case: Summarize pairwise correlations in a matrix view.
tags: [heatmap, correlation, matrix, colorbar]

layout:
  aspect: 752:681
  legend: outside_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: none

color:
  palette: sequential_mixed [#1C397D, #2999C0, #EAF2D4, #84CDBC, #5DADB9, #FFFFDC]
  note: sequential gradient with readable colorbar; print-friendly

density_tricks:
  - Encode a full matrix in a compact grid
  - Use a colorbar to map intensity to values

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
