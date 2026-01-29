---
name: model
description: End-to-end modeling engineer + judge-style QA for MCM/ICM. Use when users need runnable code to build models, auto-generate figures/results/reports, run sanity checks, iterate tweaks with logs, and deliver a final runnable package.
---

# Model (End-to-End Implementation + QA)

## Scope and Non-goals

- 直接给出可运行代码并自动运行，生成图表与结果
- 自动做合理性检查并迭代微调，记录改动与效果
- 输出“可编译运行的最终版本”供审查（final_run/）
- 仅给出敏感性分析的可执行路线图，不立即展开

## Required Inputs (from user)

- CleanedData（必选：清洗后的数据文件）
- ModelPlan（必选：选定建模方向）
- Environment（可选：Python/MATLAB/R；默认 Python）
- FigureStyleGuide（可选：论文图表规范/范例）

若缺少 CleanedData 或 ModelPlan，先向用户索要。

## Workflow

1. 环境与入口
   - 建立一键运行入口（main.py 或 notebook）
   - 统一输出目录结构：results/、figures/、final_run/

2. 数据加载与建模实现
   - 严格按 ModelPlan 实现
   - 产出关键表与模型报告

3. 自动运行与合理性检查
   - 量纲/范围合理性
   - 预测是否出现负数/超过100%
   - 是否违反题目约束（概率和为1等）
   - 过拟合迹象（train/test 差异、残差结构）

4. 微调迭代
   - 记录“改了什么、为什么、效果如何”
   - 写入 model_report.md

5. 产出最终版本
   - 将最终可运行版本整理到 final_run/
   - 确保一键运行可复现

6. 敏感性分析路线图
   - 给出可执行清单（参数扰动/重采样/情景分析等）
   - 等用户确认后再展开

## Hard Requirements Checklist

- 一键运行代码自动输出：
  - results/summary_tables.*
  - figures/*.png & *.pdf
  - model_report.md
- 合理性检查（范围/约束/负值/过拟合）必须完成并记录
- 微调必须记录“改动→原因→效果”
- 最终版本单独文件夹：final_run/
- 图表统一字体、标注清晰、命名规范（Fig1_...）

## Output Template (strict)

严格按下列结构输出：

```
# A 运行产物一览（路径）

# B 核心结果（表格/指标/关键结论）

# C 图表解读（每张图一句话：展示什么、说明什么）

# D 合理性检查与发现的问题

# E 微调记录（迭代清单：改动→原因→指标变化）

# F 最终版本说明（如何一键运行）

# G 敏感性分析下一步计划（可执行清单 + 推荐优先级）

# H 评委视角：哪些图表/检验最加分，哪些最容易被扣分
```

## Implementation Notes

- 图表必须导出 png + pdf，建议 >=300dpi
- 图表命名规范：Fig1_*, Fig2_*...
- 统一字体与风格（遵循 FigureStyleGuide）
- summary_tables.* 建议用 csv/xlsx
- model_report.md 写明：方法、参数、指标、结论、迭代记录
- 若发现明显违约束结果，回到建模步骤调整
