id: image7
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, time_series, annotation, markers, legend]

layout:
  aspect: 4:3
  legend: inside_top_right
  label: annotations

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#B6BEC6, #EAE8E8, #8C95AD, #C1E3EE, #FFFFB5]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Annotate key change points or outliers
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
