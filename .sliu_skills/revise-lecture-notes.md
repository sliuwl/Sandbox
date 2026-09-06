---
name: revise-lecture-notes
description: 当用户说"修订讲义"或"revise lecture notes"时，用于修订和优化课堂讲义，检查格式一致性、修复错误、改进内容
trigger: 修订讲义
trigger: revise lecture
out_of_scope: 不处理作业批改、考试成绩等非讲义内容
---

# Revise Lecture Notes Skill

当用户要求修订讲义时，按照以下流程进行：

## 1. 确定目标文件

首先确认要修订的文件：
- 查找 `2026Teaching/Book/` 目录下的 `.md` 文件
- 常见文件：`01FundamentalConcepts-A.md`, `02VariationalCalculus.md`, `Chapter*.md` 等

## 2. 检查格式一致性

讲义应遵循以下格式规范（参考 01FundamentalConcepts-B.md 和 02VariationalCalculus.md）：

### 2.1 文档结构
- 标题：`# 章节标题`
- 阅读材料：`**Reading material:** Chapter X of *Classical Mechanics* by John R. Taylor`
- 目录：使用 `## Table of Contents` 并链接到各节
- 分隔线：`------` 或 `---`

### 2.2 章节编号
- 一级标题：`## N. Section Title`（如 `## 1. Single-Variable Functions`）
- 二级标题：`### N.M Subsection Title`（如 `### 1.1 Position Vector`）
- 三级标题：`#### N.M.K Title`（如 `#### Stability of Equilibrium`）
- **注意**：编号必须连续，不能跳过数字

### 2.3 数学公式
- LaTeX 格式：使用 `$$ ... $$` 或 `\[ ... \]` 或 `\( ... \)`
- 重要公式使用 `\boxed{...}` 框起
- 公式编号：`\tag{X.X}`
- 行内公式：使用单个 `$...$`

### 2.4 图片
- 路径：`![](images/xxx.jpg)` 或 `<img src="plot2DPolar.png">`
- 图片说明：`**Figure N**: 描述文字`
- 图注放在图片下方

### 2.5 列表
- 使用 `-` 或 `1.` 编号
- 保持缩进一致

## 3. 常见错误检查

### 3.1 格式错误
- [ ] 章节编号是否连续（无跳过、无重复）
- [ ] 目录链接是否与实际标题匹配（检查 anchor）
- [ ] 标题层级是否正确（`#` vs `##` vs `###`）

### 3.2 拼写和语法
- [ ] 英文人名、术语拼写
- [ ] 中文标点使用（：`:`，`。`）
- [ ] 公式中的变量是否一致（如 $y$ vs $y(x)$）

### 3.3 内容错误
- [ ] 公式推导是否正确
- [ ] 物理概念描述是否准确
- [ ] 边界条件是否清晰

## 4. 修订流程

### 步骤 1：读取文件
```
Read /Users/sliutheory/Sandbox/2026Teaching/Book/XXX.md
```

### 步骤 2：检查TOC与正文一致性
- 运行：`grep -n "^## " filename.md` 检查实际章节
- 对照 Table of Contents

### 步骤 3：修复问题
使用 Edit 工具逐个修复：
- 格式问题：修改标题层级和编号
- 拼写错误：修正 typo
- 内容错误：修改描述或公式

### 步骤 4：推送到 GitHub
```
cd /Users/sliutheory/Sandbox
git add 2026Teaching/Book/XXX.md
git commit -m "Revise XXX.md: 修订内容描述"
git push origin master
```

## 5. 参考风格

现有讲义风格特点：
- **简洁明了**：避免冗长的解释
- **公式驱动**：重要结论用公式呈现
- **物理直观**：配合图片解释物理图像
- **层层递进**：从简单到复杂，从特殊到一般
- **应用导向**：每个概念配合具体例子

## 6. 常见文件问题

| 问题 | 修复方法 |
|------|----------|
| 章节编号跳号 | 重编号所有章节 |
| TOC 链接失效 | 更新 anchor 为 `#[数字]` 格式 |
| 图片路径错误 | 检查 images/ 目录下是否有对应文件 |
| 公式显示异常 | 检查 LaTeX 语法（特别是下划线 `_`） |

## 7. 示例：修复章节编号

```bash
# 找到所有章节
grep -n "^## [0-9]" file.md

# 如果发现 6. 重复出现
# 将第二个 "## 6. Derivation" 改为 "## 6.1 Derivation"
# 后续章节顺延：7→6.2, 8→7, 9→8...
```