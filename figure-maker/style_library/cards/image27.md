id: image27
figure_type: line
use_case: Show time-series trend with forecast and uncertainty interval.
tags: [line, forecast, ci_band, time_series]

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
  palette: muted_qualitative [#EFEFEE, #ACB6BA, #CBCFD1, #E1E0DE]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Add uncertainty bands to convey variance
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
