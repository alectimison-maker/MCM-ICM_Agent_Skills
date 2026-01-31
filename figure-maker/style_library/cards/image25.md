id: image25
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, time_series, noise, comparison]

layout:
  aspect: 1065:638
  legend: inside_top_right
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#C5C9CA, #E9EAEA, #849CAA]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Overlay multiple series to compare trends
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
