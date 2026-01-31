id: image60
figure_type: heatmap
use_case: Show calendar-style intensity patterns over time.
tags: [heatmap, calendar, matrix, categorical]

layout:
  aspect: 1301:413
  legend: outside_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: none

color:
  palette: sequential_mixed [#9BB899, #D58481, #C4D9CA, #F3E3E5]
  note: sequential gradient with readable colorbar; print-friendly

density_tricks:
  - Encode a full matrix in a compact grid
  - Use a colorbar to map intensity to values

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
