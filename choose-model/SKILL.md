---
name: choose-model
description: MCM/ICM O-award oriented model selection advisor. Use when users provide task decomposition (TaskMap) and want multiple modeling routes per task with clear principles, pros/cons, difficulty, validation metrics, plus Plan A/B and a flowchart.
---

# Choose Model (MCM/ICM O-Award Advisor)

## Scope and Non-goals

- 仅做“模型路线菜单 + 评价/风险 + 推荐组合 + 流程图”
- 不做完整推导，不给最终单一模型，不写详细公式
- 原理必须讲清楚，但保持通俗、可写进论文

## Required Inputs (from user)

- TaskMap（必选：每个任务含目标/数据/输出）
- Constraints（可选）
- Preference（可选）
- FlowchartStyleExample（可选）

若缺少 TaskMap，先索要任务列表或提醒用户提供。

## Workflow

1. 任务复述
   - 将每个任务用一句话重述，确保目标/输出一致

2. 建模方向菜单
   - 每个任务至少 3 条路线：Baseline / 稳健可解释 / 冲奖创新
   - 每条路线必须包含：核心思想、适用条件、优缺点（含评委视角）、难度/风险、验证指标（>=2）

3. 推荐组合
   - 给出 Plan A 主线 + Plan B 备线
   - 解释为何在约束下稳妥或更具冲奖性

4. 流程图
   - 若提供 FlowchartStyleExample，按其风格输出
   - 否则使用 Mermaid flowchart

5. 下一步清单
   - 列出数据处理/特征工程待办（不展开建模细节）

## Output Template (strict)

严格按下列结构输出，保持中文表达：

```
# 1 任务回顾（用一句话重述每个任务）

# 2 模型方向菜单
## Task i
### 方向 1（Baseline）
- 原理解释：
- 适用条件：
- 优点/缺点：
- 难度/风险：
- 验证指标：
### 方向 2（稳健/可解释）
- 原理解释：
- 适用条件：
- 优点/缺点：
- 难度/风险：
- 验证指标：
### 方向 3（冲奖创新）
- 原理解释：
- 适用条件：
- 优点/缺点：
- 难度/风险：
- 验证指标：
- 评委视角：为什么这组方案更像 O 奖论文

# 3 推荐组合（Plan A 主线 / Plan B 备线）

# 4 总体流程图（按范例或 Mermaid）

# 5 下一步：需要准备的数据处理/特征工程清单
```

## Quality Checklist

- 每个任务 >=3 条路线（Baseline/稳健/创新）
- 每条路线含：核心思想、适用条件、优缺点、难度/风险、>=2 验证指标
- 给出 Plan A/B 并解释匹配约束/偏好原因
- 流程图符合示例风格或 Mermaid
- 原理讲清楚但不写公式
