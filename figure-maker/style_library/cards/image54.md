id: image54
figure_type: scatter
use_case: Show relationship between two variables.
tags: [scatter, small_multiples, correlation]

layout:
  aspect: 4:3
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#CDD1C9, #A79389, #E9EFD5, #FCF8EB]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Use small multiples to compare subsets side-by-side
  - Use transparency or jitter to reduce overplotting

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
