id: image23
figure_type: scatter
use_case: Compare entities using position and size encodings.
tags: [scatter, bubble, ranking, annotation]

layout:
  aspect: 5:4
  legend: unknown # TODO
  label: annotations

style:
  font: sans
  linewidth: thin
  marker: mixed
  grid: light_major

color:
  palette: muted_qualitative [#C4C4C4, #EEEDEE, #757575, #D9D9D9]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Annotate key change points or outliers
  - Sort categories to improve comparison
  - Use transparency or jitter to reduce overplotting

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
