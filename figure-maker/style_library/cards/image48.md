id: image48
figure_type: heatmap
use_case: Summarize classification performance using a confusion matrix.
tags: [heatmap, confusion_matrix, classification, colorbar]

layout:
  aspect: square
  legend: outside_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: none

color:
  palette: sequential_mixed [#CFECC9, #F3FAF0, #0B4E24, #76B781]
  note: sequential gradient with readable colorbar; print-friendly

density_tricks:
  - Encode a full matrix in a compact grid
  - Use a colorbar to map intensity to values

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
