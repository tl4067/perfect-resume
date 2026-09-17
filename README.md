<a id="english"></a>

[English](#english) | [中文](#中文)

# Perfect Resume

Perfect Resume is a Codex skill for turning free-form career narratives into a structured, traceable experience library, matching that evidence against a job description (JD), and producing a targeted resume without inventing claims.

The skill keeps reusable instructions and blank assets in the repository. A user's personal data belongs in their own workspace and should never be committed here.

## Features

- Capture career experiences through a concise conversational workflow.
- Separate confirmed facts, AI-organized wording, optional gaps, and unresolved conflicts.
- Maintain a reusable personal experience library with stable experience and capability IDs.
- Decompose a JD into requirements and map each requirement to supporting evidence.
- Identify unsupported requirements and propose small, verifiable gap-validation tasks.
- Tailor resume content to a target role while preserving scope, qualifiers, and source traceability.
- Generate and visually verify a DOCX resume from a user-supplied template or the bundled default template.
- Audit existing resume claims against the experience library.
- Produce targeted or general job resumes, local edits, and evidence-aware reviews.
- Audit the built-in DOCX template with a read-only checker before using it.
- Create a same-name mapping file for generated or edited resumes, preserving source IDs and completed checks.

## How It Works

1. Perfect Resume routes the request as intake, JD analysis, gap planning, resume generation, local editing, or review.
2. For intake, it copies the blank experience-library template when no library exists, records confirmed facts, and asks only for details that materially affect a resume claim.
3. For a targeted JD, it builds a requirement-to-evidence matrix before drafting resume text; a general resume can be created without a JD.
4. It selects the strongest relevant evidence, preserves uncertainty and participation boundaries, and omits unsupported keywords.
5. For a DOCX deliverable, it prefers the user's template. Otherwise it audits and uses the single bundled default (`resume-template-ats.docx`), then renders and checks the result.
6. Generated or edited resumes receive a same-name mapping file containing source IDs, context, qualifiers, unresolved items, and completed checks.

The repository contains instructions, blank assets, the single resume template, a read-only DOCX audit script, and focused tests. It does not include an API service, executable installer, or background process.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tl4067/perfect-resume.git
   ```

2. Copy or clone the repository folder into a Codex skills directory. Codex normally discovers personal skills from `$CODEX_HOME/skills`; when `CODEX_HOME` is unset, use `~/.codex/skills`:

   ```text
   $CODEX_HOME/skills/perfect-resume/
   ```

   On Windows with the default location, this is typically:

   ```text
   %USERPROFILE%\.codex\skills\perfect-resume\
   ```

3. Confirm that `SKILL.md` is directly inside the `perfect-resume` folder and keep `agents/`, `assets/`, `references/`, `scripts/`, and `tests/` beside it.

4. Start a new Codex task and invoke `$perfect-resume`, or describe a matching resume task so Codex can select the skill automatically.

DOCX reading, editing, rendering, and visual verification require the `documents:documents` skill referenced by `SKILL.md`. Experience capture and JD analysis can still use the Markdown workflow, but DOCX generation depends on a compatible document-processing skill in the host environment.

## Usage

Typical requests include:

```text
Use $perfect-resume to create a blank personal experience library and help me record my first project experience.
```

```text
Use $perfect-resume to add this experience to my library. Ask only for missing facts that would materially affect an accurate resume bullet: ...
```

```text
Use $perfect-resume to analyze this JD. Show the requirement-to-evidence matrix and skill gaps before drafting anything: ...
```

```text
Use $perfect-resume to tailor my resume to this JD using my existing experience library and DOCX template. Keep every material claim traceable to a source ID.
```

```text
Use $perfect-resume to review this resume and flag claims that are unsupported or ambiguous compared with my experience library.
```

## Project Structure

```text
perfect-resume/
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── agents/
│   └── openai.yaml
├── assets/
│   ├── personal-experience-library.md
│   └── resume-template-ats.docx
├── archive/
│   └── resume-template-visual.docx
├── references/
│   ├── docx-template-map.md
│   ├── delivery-and-versioning.md
│   ├── interview-and-evidence.md
│   └── jd-matching-and-generation.md
├── scripts/
│   └── audit_docx_template.py
└── tests/
    ├── behavior-cases.md
    └── test_audit_docx_template.py
```

- `SKILL.md` defines routing, evidence boundaries, and the end-to-end workflow.
- `agents/openai.yaml` provides display metadata for compatible Codex environments.
- `assets/personal-experience-library.md` is an unfilled, reusable experience-library template.
- `assets/resume-template-ats.docx` is the only bundled one-page V4 resume template; the `ATS` filename describes the default route and does not certify compatibility with every recruiting system.
- `archive/resume-template-visual.docx` is a legacy rollback copy and is not loaded by the Skill.
- `references/` contains detailed rules loaded only for the relevant workflow stage, including delivery and versioning checks.
- `scripts/audit_docx_template.py` performs a read-only blank-template privacy and structure audit.
- `tests/` contains behavior cases and tests for the DOCX audit script.

Run the audit script on a built-in template with:

```bash
python scripts/audit_docx_template.py assets/resume-template-ats.docx --profile blank-template
```

## Privacy

Do not commit real resumes, completed experience libraries, contact details, identity documents, credentials, confidential project information, or generated resume outputs to a public fork of this repository.

Keep user-specific files outside the skill directory whenever possible. The included `.gitignore` excludes common private-data directories, root-level resume outputs, environment files, credentials, and temporary files, but it is not a substitute for reviewing `git diff --cached` before every push.

## License

Perfect Resume is released under the [MIT License](LICENSE).

---

<a id="中文"></a>

[English](#english) | [中文](#中文)

# Perfect Resume（中文）

Perfect Resume 是一个 Codex Skill，用于将自由叙述的职业经历整理为结构化、可追溯的个人经历库，将其中的证据与职位描述（JD）进行匹配，并在不虚构信息的前提下生成针对性简历。

仓库只保存可复用的指令和空白资产。用户的个人数据应保存在其自己的工作目录中，不应提交到本仓库。

## 主要功能

- 通过简洁的对话流程采集职业经历。
- 区分用户确认的事实、AI 整理的表述、可选待补充项和未解决冲突。
- 使用稳定的经历 ID 和能力 ID 维护可复用的个人经历库。
- 拆解 JD 要求，并将每项要求映射到对应证据。
- 识别缺少证据支持的要求，并设计小型、可验证的能力补齐任务。
- 在保留参与范围、限定词和来源追溯关系的前提下，针对目标岗位调整简历内容。
- 使用用户提供的模板或仓库内置的默认模板生成并可视化检查 DOCX 简历。
- 对照个人经历库审查现有简历中的表述。
- 生成针对岗位或通用求职简历，执行本地编辑，并进行基于证据的审查。
- 使用只读检查器审计内置 DOCX 模板后再使用。
- 为生成或编辑的简历创建同名映射文件，保留来源 ID 和已完成的检查。

## 工作流程

1. Perfect Resume 将请求路由为经历采集、JD 分析、能力缺口规划、简历生成、本地编辑或审查。
2. 采集经历时，如果用户工作目录中尚无经历库，Skill 会复制空白模板，记录已确认事实，只追问会实质影响简历表述的缺失信息。
3. 面向目标 JD 时，Skill 会先建立“岗位要求—经历证据”匹配矩阵，再起草简历内容；通用求职简历可以不依赖 JD。
4. Skill 选择与岗位最相关的可靠证据，保留不确定性和参与边界，并省略缺少支持的关键词。
5. 用户要求 DOCX 成果时，Skill 优先使用用户提供的模板，否则先审计并使用唯一的内置默认模板（`resume-template-ats.docx`），再渲染检查。
6. 生成或编辑的简历会获得同名映射文件，其中记录来源 ID、上下文、限定词、未解决事项和已完成的检查。

本仓库包含指令、空白资产、唯一的简历模板、只读 DOCX 审计脚本和针对性测试，不包含 API 服务、可执行安装程序或后台进程。

## 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/tl4067/perfect-resume.git
   ```

2. 将仓库复制或克隆到 Codex 的 Skills 目录。Codex 通常从 `$CODEX_HOME/skills` 查找个人 Skill；未设置 `CODEX_HOME` 时，使用 `~/.codex/skills`：

   ```text
   $CODEX_HOME/skills/perfect-resume/
   ```

   Windows 默认位置通常为：

   ```text
   %USERPROFILE%\.codex\skills\perfect-resume\
   ```

3. 确认 `SKILL.md` 直接位于 `perfect-resume` 目录下，并保留同级的 `agents/`、`assets/`、`references/`、`scripts/` 和 `tests/` 目录。

4. 新建 Codex 任务并调用 `$perfect-resume`，或者直接描述符合触发范围的简历任务，让 Codex 自动选择该 Skill。

读取、编辑、渲染和可视化检查 DOCX 文件需要 `SKILL.md` 中引用的 `documents:documents` Skill。经历采集和 JD 分析可以继续使用 Markdown 工作流，但 DOCX 生成依赖宿主环境中兼容的文档处理 Skill。

## 使用示例

```text
使用 $perfect-resume 创建一个空白个人经历库，并帮我记录第一段项目经历。
```

```text
使用 $perfect-resume 把下面的经历加入经历库。只追问会实质影响简历表述准确性的缺失事实：……
```

```text
使用 $perfect-resume 分析这份 JD。先展示岗位要求与证据的匹配矩阵和能力缺口，不要立即起草简历：……
```

```text
使用 $perfect-resume 根据我的经历库、DOCX 模板和目标 JD 定制简历。所有关键表述都必须能够追溯到来源 ID。
```

```text
使用 $perfect-resume 审查这份简历，并对照经历库标出缺少支持或含义不明确的表述。
```

## 项目结构

```text
perfect-resume/
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── agents/
│   └── openai.yaml
├── assets/
│   ├── personal-experience-library.md
│   └── resume-template-ats.docx
├── archive/
│   └── resume-template-visual.docx
├── references/
│   ├── docx-template-map.md
│   ├── delivery-and-versioning.md
│   ├── interview-and-evidence.md
│   └── jd-matching-and-generation.md
├── scripts/
│   └── audit_docx_template.py
└── tests/
    ├── behavior-cases.md
    └── test_audit_docx_template.py
```

- `SKILL.md` 定义任务路由、证据边界和完整工作流程。
- `agents/openai.yaml` 为兼容的 Codex 环境提供界面显示信息。
- `assets/personal-experience-library.md` 是未填写的通用个人经历库模板。
- `assets/resume-template-ats.docx` 是唯一的当前一页 V4 内置简历模板；文件名中的 `ATS` 表示默认入口，不代表对所有招聘系统的兼容性认证。
- `archive/resume-template-visual.docx` 仅作为历史回滚副本保留，Skill 不会加载它。
- `references/` 保存仅在对应工作阶段加载的详细规则，包括交付和版本检查。
- `scripts/audit_docx_template.py` 执行只读的空白模板隐私与结构审计。
- `tests/` 保存行为用例和 DOCX 审计脚本测试。

使用以下命令审计内置默认模板：

```bash
python scripts/audit_docx_template.py assets/resume-template-ats.docx --profile blank-template
```

## 隐私

请勿将真实简历、已填写的个人经历库、联系方式、身份证明、账号凭证、保密项目信息或生成的简历文件提交到本仓库或其公开分支。

应尽量把用户专属文件保存在 Skill 目录之外。仓库内的 `.gitignore` 会排除常见私人数据目录、根目录简历输出、环境变量文件、凭证和临时文件，但每次 push 前仍应人工检查 `git diff --cached`。

## 许可证

Perfect Resume 使用 [MIT License](LICENSE) 发布。
