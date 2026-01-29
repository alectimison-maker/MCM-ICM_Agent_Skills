---
name: data-cleaner
description: Expert workflow for MCM/ICM data cleaning with reproducible logs, pre-clean risk checklist, concrete anomaly examples, independent post-clean audit, and paper-ready figures + cleaned data outputs. Use when users need rigorous cleaning documentation and outputs for modeling/competition papers.
---

# Data Cleaner (MCM/ICM)

## Scope and Non-goals

- 产出可复现的数据清洗过程与论文可用材料（说明、对比图、清洗后数据）
- 不做模型训练与最终建模结论
- 遵守“清洗前列风险、清洗中记实例、清洗后独立审计”的刚性要求

## Required Inputs (from user)

- RawDataFiles（必选：csv/xlsx/json/txt等）
- DataDescription（可选：字段解释/附件说明）
- CleaningGoal（可选：默认“可建模、可复现、可写论文”）
- OutputDir（可选：默认当前工作目录或用户指定路径）

若缺少 RawDataFiles，先索要文件与字段信息；其余信息缺失时要在输出中明确假设。

## Workflow (A-F)

严格按顺序执行，必要时补充简短澄清问题：

1. Step A 读入与字段体检
   - dtype、唯一键、时间字段、类别字段、数值范围、缺失率、重复率

2. Step B 脏点假设清单
   - 缺失/重复/类型错/单位错/异常值/逻辑约束违反/舍入导致和不为100/日期不连续/编码问题等
   - 必须不少于 10 条，并结合字段与业务逻辑

3. Step C 清洗规则设计
   - 每条规则写成“检测 → 处理 → 记录”
   - 记录影响行数与典型实例

4. Step D 执行清洗并落盘
   - 输出 cleaned_data.* 与 cleaning_log.md
   - 清洗中必须记录 >=5 个典型具体实例（可匿名的行号/键值）

5. Step E 二次审计脚本
   - 用独立脚本复查 cleaned_data（不得复用清洗函数）
   - 产出 data_audit_report.md（缺失、重复、范围、约束校验、关键统计量）

6. Step F 可视化
   - 至少 4 类图：趋势线、分布（直方/箱线）、缺失热图/柱状、异常点标记图
   - 图要有标题、坐标轴、单位/百分号，高分辨率（png/pdf）

## Hard Requirements Checklist

- 清洗前：风险点清单 >=10 条（结合字段与业务逻辑）
- 清洗中：典型实例 >=5 条（原值→处理→理由）
- 清洗产物：
  - cleaned_data.*
  - cleaning_log.md
  - data_audit_report.md
  - figures/ 下若干图（png/pdf，高分辨率）
- 清洗后：独立脚本二次审计（不能复用同一段函数）
- 任何修正可追踪：说明“为什么改、怎么改、改了多少”

## Output Template (strict)

严格按下列结构输出，保持中文表达：

```
# A 脏数据风险点清单（结合本题字段）

# B 清洗规则与实现概览（表格：规则/字段/检测方式/处理方式/影响行数）

# C 典型实例记录（>=5条：原值→处理→理由）

# D 清洗后审计结果（缺失/重复/范围/约束/关键统计量）

# E 输出文件清单（含路径）

# F 图表说明（每张图说明“看什么、说明什么”）

# G 评委视角：清洗写进论文怎么写更加分（可复现/不造假/有理据）
```

## Logging Guidance

- cleaning_log.md 至少包含：规则编号、字段、检测逻辑、处理方式、影响行数、典型实例引用
- data_audit_report.md 至少包含：缺失率、重复率、范围检查、逻辑约束校验、关键统计量摘要
- 每一次修正都给出“原因 + 方法 + 数量/比例”

## Implementation Notes

- 输出文件命名统一：cleaned_data.*、cleaning_log.md、data_audit_report.md、figures/...
- 图表输出高分辨率（建议 >=300dpi），并保留可重复生成的脚本
- 若字段说明缺失，先做假设并在报告中标注
- 若发现关键异常未被规则覆盖，返回 Step C 迭代
