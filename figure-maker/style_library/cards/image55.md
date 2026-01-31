id: image55
figure_type: line
use_case: Show time-series trend with forecast and uncertainty interval.
tags: [line, time_series, ci_band, inset]

layout:
  aspect: 16:9
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#DCE8F0, #C5D4D8, #839698]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Add uncertainty bands to convey variance
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
