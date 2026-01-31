id: image19
figure_type: scatter
use_case: Show relationship between two variables.
tags: [scatter, pairplot, multivariate, small_multiples]

layout:
  aspect: 3:2
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_single_hue [#D9D9D9, #EFEFEF, #5F5F5F]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use transparency or jitter to reduce overplotting

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
