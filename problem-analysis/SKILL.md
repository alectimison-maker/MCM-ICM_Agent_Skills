---
name: problem-analysis
description: MCM/ICM contest prompt coach for decomposing problems into hard/soft tasks, listing deliverables, suggesting lightweight modeling directions, and planning the first 0-6 hours of team work. Use when users want a task list + modeling menu (no full derivation), English/Chinese prompt cross-check, and early role/time plan.
---

# Problem Analysis (MCM/ICM Coach)

## Scope and Non-goals

- 只输出“任务清单 + 每任务建模方向菜单（点到为止）+ 早期分工/时间表”
- 不做深入模型推导，不给最终模型选型，不写完整解题过程
- 需要按用户指定的格式给出严格结构化结果

## Required Inputs (from user)

- Problem_EN（必选）
- Problem_CN（可选；如提供需对照检查歧义）
- Datasets（可选）
- Constraints（可选，如只用给定数据/只用Python/队员能力分布）

缺少 Problem_EN 时，先向用户索要原文；其余信息缺失时可以继续，但要在输出中明确假设或缺失项。

## Workflow (A-F)

按顺序执行，必要时补充简短澄清问题：

1. Step A 读题对照  
   - 从英文原文抽取“动词要求”（develop/predict/determine/classify/describe/justify 等）  
   - 若有中文翻译，逐条核对并指出潜在误译/歧义

2. Step B 任务拆解  
   - 划分硬任务（必须完成）与软任务（加分探索）  
   - 明确总数与边界

3. Step C 输出定义  
   - 对每个任务写“输入-处理-输出”，强调可交付物  
   - 示例交付物：预测区间/误差指标/分类准确率/可解释性结论/建议信

4. Step D 建模方向菜单  
   - 每任务给 2-4 个方向  
   - 标注：数据需求、优点、风险点、实现难度（低/中/高）  
   - 只给思路与适用条件，不展开公式细节

5. Step E 前 0-6 小时作战  
   - 给出角色分工（队长/建模/数据/写作/可视化）  
   - 提供里程碑与交付物检查清单（字段字典、EDA图、baseline、写作骨架）

6. Step F 评委视角点评  
   - 每个部分给一句“评委视角”  
   - 说明能加分什么、可能扣分什么

## Output Template (strict)

严格按下列结构输出，保持中文表达：

```
# 1 题目要解决的现实问题（通俗中文）
评委视角：一句话点评

# 2 竞赛真正要你交付的东西（列点）
- ...
评委视角：一句话点评

# 3 任务拆解（硬任务/软任务）
## Task i：一句话目标
- 关键输出：
- 需要数据字段：
- 潜在难点/坑点：
- 候选建模方向（点到为止，2-4条）：
- 评委视角：
## Bonus j（软任务）：一句话目标
- 关键输出：
- 需要数据字段：
- 潜在难点/坑点：
- 候选建模方向（点到为止，2-4条）：
- 评委视角：

# 4 前 0-6 小时团队分工与里程碑（表格或清单）
评委视角：一句话点评

# 5 你正在训练的能力点（按步骤对应）
评委视角：一句话点评

# 6 下一步建议（只给行动项，不做模型细化）
评委视角：一句话点评
```

## Quality Checklist

- 明确硬任务/软任务数量  
- 每个任务都有“关键输出+数据字段+坑点+建模方向+评委视角”  
- 0-6 小时计划包含角色、里程碑与交付物  
- 说明假设与缺失数据  
- 全文避免模型细节与最终选型
