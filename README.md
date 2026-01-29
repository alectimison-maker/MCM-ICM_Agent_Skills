# MCM-ICM_Agent_Skills

Core agent skills for MCM/ICM workflows.

## Skills

- article-maker
  - When to use: Review MCM/ICM paper format and generate LaTeX structure.
  - Inputs: style files or template/specs, text blocks; optional outline/figure table list.
  - Outputs: compliance checklist, academic rewrites, LaTeX skeleton, figure/table templates.

- problem-analysis
  - When to use: Decompose a contest prompt into tasks and early execution plan.
  - Inputs: problem statement (EN required, CN optional), datasets/constraints optional.
  - Outputs: task list (hard/soft), light modeling directions, 0-6 hour team plan, judge-view notes.

- choose-model
  - When to use: Select modeling routes after you already have a TaskMap.
  - Inputs: TaskMap, constraints, preferences; optional flowchart style example.
  - Outputs: multiple routes per task with pros/cons, difficulty, validation metrics, Plan A/B, flowchart.

- data-cleaner
  - When to use: Produce reproducible data cleaning artifacts for papers/competition submissions.
  - Inputs: raw data files plus optional data description/cleaning goals.
  - Outputs: cleaned data, cleaning log, post-clean audit report, paper-ready figures.

- figure-maker
  - When to use: Recreate a paper figure style from an example and given data.
  - Inputs: data, style example, figure type; optional tool preference/output format.
  - Outputs: paper-ready figures (png/pdf), dual versions, captions, figure README.

- model
  - When to use: End-to-end modeling implementation and QA.
  - Inputs: cleaned data and selected model plan.
  - Outputs: runnable code, results tables, figures, model_report, final_run package, sanity checks.
