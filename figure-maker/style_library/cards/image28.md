id: image28
figure_type: bar
use_case: Rank categories/features by magnitude for comparison.
tags: [bar, horizontal, ranking, feature_importance]

layout:
  aspect: 3:2
  legend: unknown # TODO
  label: axis_labels

style:
  font: sans
  linewidth: thin
  marker: none
  grid: light_major

color:
  palette: muted_single_hue [#F1F2F3, #DDE4E9, #8AA8BD]
  note: print-friendly; muted palette with clear contrast

density_tricks:
  - Sort categories to improve comparison
  - Use consistent scales and labels to aid comparison

caption_style:
  - State what is plotted and the key takeaway (largest/smallest trend or difference).
  - Briefly describe how the values are computed, including data scope and settings.
