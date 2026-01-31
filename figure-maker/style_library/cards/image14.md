id: image14
figure_type: line
use_case: Show temporal or continuous-axis trend and compare series.
tags: [line, time_series, event_markers, annotation]

layout:
  aspect: 3:2
  legend: unknown # TODO
  label: annotations

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#FFD3D3, #FFF2F1, #D2A5A2, #DBD1CF]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Annotate key change points or outliers
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
