id: image43
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, multi_series, time_series, legend]

layout:
  aspect: 1270:603
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#CDD1A9, #E5ECDE, #9DA29E, #FCF2C7]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Overlay multiple series to compare trends
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
