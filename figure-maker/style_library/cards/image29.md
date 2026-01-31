id: image29
figure_type: line
use_case: Diagnose time-series autocorrelation structure across lags.
tags: [line, small_multiples, acf, diagnostic]

layout:
  aspect: 1314:397
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#D5DBDE, #E8ECED, #90AEC0]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
