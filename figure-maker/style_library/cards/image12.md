id: image12
figure_type: bar
use_case: Show the distribution of values using binned counts.
tags: [histogram, distribution, small_multiples, bar]

layout:
  aspect: 765:387
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_qualitative [#385ED7, #CECFD2, #F1F1F0, #6A84D5]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use binning to summarize distribution shape

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
