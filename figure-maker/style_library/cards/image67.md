id: image67
figure_type: heatmap
use_case: Summarize pairwise correlations in a matrix view.
tags: [heatmap, correlation, matrix, colorbar]

layout:
  aspect: 774:547
  legend: outside_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: none

color:
  palette: sequential_mixed [#DEE1E1, #828492, #B3C3C8, #F0F0EF]
  note: sequential gradient with readable colorbar; print-friendly

density_tricks:
  - Encode a full matrix in a compact grid
  - Use a colorbar to map intensity to values

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
