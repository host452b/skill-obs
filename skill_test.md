# Skill 测试设计：借鉴与逻辑 / Designing Skill Tests — patterns & rationale

> 这份文档是对 cohort 21 个 repo「怎么验证 skill、怎么防回归」横向研究的**可落地提炼**——不是 survey（survey 见 [`README.md` §🧪](./README.md) 与 [`EVALUATION.md`](./EVALUATION.md)），而是**「为什么这样测」的逻辑 + 「该抄什么」的清单 + 一个最小可落地模板**。
>
> 证据来源：gstack `test/helpers/llm-judge.ts` + `test/fixtures/eval-baselines.json`、caveman `evals/llm_run.py`、last30days `skills/last30days/scripts/evaluate_search_quality.py` + 其 ADR、anthropics `skills/skill-creator/scripts/run_eval.py` + `agents/grader.md`、obra `skills/writing-skills/`、OpenSpec `test/core/{migration,profile-sync-drift}.test.ts`、Understand-Anything `tests/skill/understand/`、career-ops `test-all.mjs`。

---

## 1. 核心逻辑：skill 测试 ≠ 代码测试

普通代码测试是 `assert f(x) == y`——确定性、可断言。skill 是 **prompt**，产出要经过 LLM，所以：

- **非确定性**：同一 SKILL.md + 同一输入，两次产出不必逐字相同 → 不能只 `assert`，要么**钉确定性子集**（结构/契约），要么**用 eval 打分**（质量）。
- **被测对象有三层，别混为一谈**：

  | 层 | 被测的是 | 用什么测 | 多数 repo 的现状 |
  |---|---|---|---|
  | ① 支撑脚本 | skill 调用的 `.py`/`.ts`/`.sh` | 普通单元/集成测试（vitest/pytest） | 几乎都做了，但**只做这层就号称「测了 skill」** |
  | ② 触发 | 描述是否「该激活时激活、不该时不激活」 | 跑 naive prompt 看 skill 是否 fire + 留出集防过拟合 | 极少（anthropics / superpowers / affaan-m skill-comply） |
  | ③ 行为与产出 | 装了之后输出是否真的更好/更对 | 配对 eval + LLM-judge + golden | 极少（gstack / caveman / last30days） |

- **「regression」对 skill 有四种定义**，各有对应测法：

  | regression 类型 | 现象 | 对应测法 |
  |---|---|---|
  | a. 触发退化 | 新版描述后不再被激活 | 触发率测试（跑 N 次数 fire 率） |
  | b. 质量退化 | 输出变差/变啰嗦/漏要点 | 配对 eval（新 vs 旧 / 装 vs 不装）+ LLM-judge |
  | c. 指令失守 | SKILL.md 里的承重指令被悄悄删改 | prose 契约 grep（断言关键门短语存在） |
  | d. 契约破坏 | 支撑脚本输出 schema 漂移 | golden / 确定性 pin + 单元测试 |

> **第一性原理**：你要测的是「**这个 skill 让 agent 的行为产生了什么边际变化**」，不是「这段脚本对不对」。后者重要，但它只是 (d)。

---

## 2. 七条设计原则（逻辑）

1. **测边际，不测绝对**（control-arm）。
   单测「装了 skill 的输出好不好」会把模型本来就会的功劳算给 skill。正确做法是设一个**等价强度的对照臂**，测**差值**。caveman 三臂 `baseline`（无提示）/ `terse`（“Answer concisely.”）/ `skill`（terse + SKILL.md），诚实指标取 **skill − terse**——README 直言拿 baseline 比是「作弊」。

2. **配对对照才有「变好/变坏」信号**。
   绝对分数会随模型版本、随机种子漂移，单独看没意义。要么 **装 vs 不装**（新 skill），要么 **新版 vs 旧版快照**（迭代）。anthropics `skill-creator` 同一轮 spawn 两个 subagent 跑同样输入，只比相对优劣。

3. **确定性的进阻断门，贵且不确定的留手动**（two-tier）。
   LLM-judge 慢、要花钱、判官本身不确定 → 放进每次 PR 的阻断 CI 会变 flaky。last30days 专门写了一份 ADR（`docs/solutions/architecture/search-quality-eval-manual-by-default-*.md`）论证：**确定性契约入阻断门，LLM-judge eval 留 `workflow_dispatch` 手动**，并写明何时重审这个决定。

4. **承重 prose 当契约 grep**。
   SKILL.md 里有些指令是「承重墙」（如门控短语 “Do not continue until …”、必经步骤、安全 gate）。它们被误删不会报错，但 skill 就废了。career-ops `test-all.mjs` 直接 grep mode 文件断言这些短语存在；gstack `skill-validation.test.ts` 解析 SKILL.md 里写的每条 `$B <command>` 断言它在 CLI registry 真实存在——**prose 不能和真实能力漂移**。

5. **同输入同输出**（determinism pin）。
   只要 skill 的某一步产出是结构化的（JSON/计划/图），就把它**钉成 golden**：同输入必须字节级一致。Understand-Anything 有一条 `JSON.stringify(r1) === JSON.stringify(r2)` 的确定性断言——改逻辑立刻现 diff，是最便宜的回归网。

6. **防过拟合：在留出集上选优**。
   调描述/调 prompt 很容易过拟合到你手上那几个例子。anthropics `improve_description` 用 **60/40 train/test split**，每条查询跑 3 次取稳定触发率，**按留出集（test）选最佳描述，不按 train**。

7. **把结果 commit 成 baseline**。
   eval 结果（分数/快照）写进 git，新版与基线做 diff——这样回归是一次**可 review 的 diff**，不需要每次实时调 API。caveman 提交 `evals/snapshots/results.json` 并用 `skill_md_sha256` 把每个数钉到具体 SKILL.md 版本；gstack 用 `eval-baselines.json` 做「regression vs baseline」判官。

---

## 3. 借鉴清单：模式 → 实现 → 防哪种 regression

| 模式 | 一句话实现 | 出处 | 防 regression |
|---|---|---|---|
| **Control-arm eval** | 设 `terse` 对照臂，测 `skill − terse` 边际差 | caveman | b |
| **配对对照（装/不装、新/旧）** | 同轮跑两个 subagent，比相对优劣 | anthropics, gstack | b |
| **LLM-as-judge + rubric** | 第二次 LLM 调用读 rubric 判 pass/fail + 给证据 | gstack, anthropics, last30days | b |
| **IR 指标判官** | 判官产出可排序判断 → Precision@k / nDCG | last30days | b |
| **Golden / 确定性 pin** | 结构化产出钉字节级一致 | UA, last30days(mock-json) | d |
| **Prose 契约 grep** | 断言承重门短语 / 命令存在 | career-ops, gstack | c |
| **Migration + drift 测试** | 模拟升级，断言落盘的 skill 文件仍正确 | OpenSpec | d（升级路径） |
| **触发率测试** | naive prompt 跑 N 次数 fire 率 + 留出集 | anthropics, affaan-m(skill-comply) | a |
| **对抗式行为 TDD** | 无 skill 的 subagent 在压力场景失败→记狡辩→堵→重跑 | obra/superpowers | b（鲁棒性） |
| **Two-tier CI** | 确定性套件阻断；judge eval 手动 dispatch | last30days, gstack | 全部（分流） |
| **Baseline 快照入库** | eval 结果 commit + sha 钉版本 | caveman, gstack | b/d（diff 可见） |

---

## 4. LLM-as-judge 的实现骨架（四步）

所有真测行为的 repo 都是这个骨架，只是语言/判官不同：

```
①构造  system = SKILL.md (+ 一条 task/query)
②执行  headless 跑 agent —— claude -p / Agent SDK / 直接调 Anthropic|Gemini API
③打分  确定性(token 数 / Precision@k / 埋雷检出 / grep 断言)  或  第二次 LLM 调用读 rubric 判 pass-fail + 证据
④回归  结果 commit 成 baseline，新版 diff 比基线；成本靠 diff-selection + 把贵的留手动
```

示意（Python，伪代码，仅说明结构）：

```python
# eval.py — 对一个 skill 跑配对 eval 并与 baseline 比对
import json, subprocess, statistics

def run(skill_md: str | None, task: str) -> str:
    sys_prompt = (skill_md + "\n\n" if skill_md else "") + task
    # headless 执行：等价于各 repo 的 `claude -p`
    return subprocess.run(["claude", "-p", sys_prompt],
                          capture_output=True, text=True).stdout

def judge(task: str, output: str, rubric: str) -> dict:
    # 第二次 LLM 调用：判官读 rubric，对每条 assertion 给 pass/fail + 证据
    verdict = run(None, f"{rubric}\n\nTASK:\n{task}\n\nOUTPUT:\n{output}\n"
                        "对每条 assertion 输出 JSON: {id, pass, evidence}")
    return json.loads(verdict)

def evaluate(skill_md, cases, rubric, n=3):
    rows = []
    for c in cases:
        # 原则1/2：配对——skill 臂 vs terse 对照臂，跑 n 次取中位
        skill_scores = [score(judge(c["task"], run(skill_md, c["task"]), rubric)) for _ in range(n)]
        terse_scores = [score(judge(c["task"], run("Answer concisely.", c["task"]), rubric)) for _ in range(n)]
        rows.append({"id": c["id"],
                     "skill": statistics.median(skill_scores),
                     "terse": statistics.median(terse_scores),
                     "delta": statistics.median(skill_scores) - statistics.median(terse_scores)})
    return rows

# 原则7：与 baseline 做可 review 的 diff
def regress(rows, baseline_path, tol=0.0):
    base = {r["id"]: r for r in json.load(open(baseline_path))}
    return [r["id"] for r in rows if r["delta"] < base[r["id"]]["delta"] - tol]  # 变差的用例
```

---

## 5. 最小可落地模板（适合「产出结构化文档/计划」类 skill）

适用场景：一个 skill 吃输入、产出**有固定结构**的产物（如测试计划、报告、设计稿）。三道防线，由便宜到贵：

```
your-skill/
├── SKILL.md
├── tests/
│   ├── contract/                 # 防线1（确定性·进阻断 CI）
│   │   ├── test_structure.py     #   产出必含的章节/字段/gate 都在？(原则5)
│   │   └── test_prose_gates.py   #   SKILL.md 承重门短语仍在？(原则4)
│   ├── fixtures/
│   │   ├── inputs/               #   代表性输入
│   │   ├── golden/               #   钉死的结构化子集
│   │   └── rubric.md             #   judge 评分标准 + Good/Bad 示例
│   └── eval/                     # 防线3（LLM-judge·手动 dispatch）
│       ├── eval.py               #   §4 的骨架
│       └── baselines.json        #   commit 入库 (原则7)
```

**防线 1 — 结构 + prose 契约（每次 PR 阻断）**
- `test_structure.py`：跑 skill（或解析其产出 schema），断言「必含章节 / 必经 gate / 字段类型」都在。对应你已有的 FIXED format schema、workflow gate（如 P9–P12）——把它们变成断言。
- `test_prose_gates.py`：grep SKILL.md，断言关键门控短语逐字存在（防 (c) 指令失守）。

**防线 2 — golden 确定性（每次 PR 阻断）**
- 对 skill 里**确定性的那一步**（如把输入归一化成中间 JSON），钉 `golden/`，断言同输入字节级一致（防 (d)）。

**防线 3 — LLM-judge 质量 eval（手动 / 定时，不阻断）**
- `eval.py` 跑配对 + judge + 与 `baselines.json` diff（原则 1/2/7）。
- 放 `workflow_dispatch` 或 nightly，不进 PR 阻断门（原则 3）。

CI 两层（示意）：

```yaml
# .github/workflows
jobs:
  contract:           # 防线1+2：每次 PR/push 阻断
    steps: [{run: "pytest tests/contract"}]
  quality-eval:       # 防线3：手动触发，回归比 baseline
    on: {workflow_dispatch: {}}
    steps: [{run: "python tests/eval/eval.py --against tests/eval/baselines.json"}]
```

---

## 6. 决策表：该用哪种测试

| 想防的 | 选哪个 | 成本 | 进阻断门? |
|---|---|---|---|
| 支撑脚本 schema 漂移 | 单元测试 + golden | 低 | ✅ |
| 产出结构缺章节/gate | 结构契约测试 | 低 | ✅ |
| SKILL.md 承重指令被删 | prose 契约 grep | 极低 | ✅ |
| 确定性中间产物漂移 | 字节级 determinism pin | 低 | ✅ |
| 升级破坏已装 skill | migration + drift 测试 | 中 | ✅ |
| 该触发时不触发 | 触发率测试 + 留出集 | 中 | ◑ 可定时 |
| 输出质量变差 | 配对 eval + LLM-judge | 高 | ✖ 手动/定时 |
| 压力下不遵守 | 对抗式行为 TDD | 高 | ✖ 作者期 |

---

## 7. 反模式（cohort 里真实踩到的坑）

- **「测了脚本」≠「测了 skill」**：affaan-m / nexu-io 有几百个测试和多 OS CI，但都打在支撑代码/引擎/app UI 上，skill 行为本身**没测**。别用 (d) 冒充 (b)。
- **拿 baseline 当对照**：不设 terse 对照臂，会把模型固有能力算成 skill 的功劳（caveman 明确反对）。
- **把 LLM-judge 塞进阻断 CI**：慢+贵+判官不确定 → flaky gate，最后大家 `--no-verify`。该手动就手动。
- **声称覆盖，实际只 lint frontmatter**：coreyhaines 设计了 197 条 eval 却没接进 CI，CI 只验 frontmatter——容易让人误以为「质量有守」。要诚实写明哪层进了门。
- **不 commit baseline**：eval 只在本地跑、结果不入库，回归就无法 review、无法追溯到哪次改动变差。
- **silent truncation**：只测 top-N 用例却不说，读起来像「全覆盖」。被裁掉的要 `log` 出来。

---

## 8. 出处映射（想深挖时看哪个 repo）

| 想学 | 看 |
|---|---|
| 全闭环 E2E + 阻断 CI + 成本控制 | **gstack** `test/skill-e2e-*.test.ts`, `test/helpers/llm-judge.ts`, `.github/workflows/evals.yml` |
| 控制臂 + 效果度量 + 快照钉版本 | **caveman** `evals/{llm_run,measure}.py`, `evals/snapshots/results.json` |
| LLM-judge + IR 指标 + 两层 ADR 纪律 | **last30days** `skills/last30days/scripts/evaluate_search_quality.py` + `docs/solutions/architecture/*eval-manual*` |
| 统计化配对 + 防过拟合 split | **anthropics** `skills/skill-creator/scripts/{run_eval,run_loop,aggregate_benchmark}.py`, `agents/grader.md` |
| 对抗式 TDD-for-skills | **obra/superpowers** `skills/writing-skills/` |
| migration + drift（升级安全） | **OpenSpec** `test/core/{migration,profile-sync-drift}.test.ts` |
| 确定性 golden pin | **Understand-Anything** `tests/skill/understand/test_scan_project.test.mjs` |
| prose 契约 grep | **career-ops** `test-all.mjs` · **gstack** `test/skill-validation.test.ts` |
