id: image21
figure_type: bar
use_case: Show the distribution of values using binned counts.
tags: [histogram, distribution, bar, ci_band]

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
  palette: muted_qualitative [#3BA08E, #E3E4E4, #3C8187, #74C19B]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Add uncertainty bands to convey variance
  - Use binning to summarize distribution shape

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
