id: image37
figure_type: line
use_case: Show time-series trend with forecast and uncertainty interval.
tags: [line, time_series, inset, ci_band]

layout:
  aspect: 1278:631
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#D1D0EA, #E3E3E8, #9DA5D4]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Add uncertainty bands to convey variance
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
