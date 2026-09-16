# Interview and evidence rules

## Contents

1. Intake and two thresholds
2. Question gate and interruption
3. Record states and evidence
4. Bounded I/O and update contract
5. Depth and skill claims

## Intake and two thresholds

Accept natural language; do not require a form. Start by extracting facts already supplied in the current message, the confirmed library, and user-provided files. Do not re-ask a fact merely because it came from an earlier sentence or a source file.

Evaluate two thresholds independently:

### Record-sufficient

The material names a distinct experience and can be saved faithfully without inventing a material fact. A project name plus stated participation and project-wide scope is enough to save a project fact, even when the user's personal action is unknown.

When the user explicitly asks to add, record, or save record-sufficient material, save it in the current turn. Mark 简历充分性：不足（原因） when personal ownership, result, or a necessary qualifier is missing. Omit the candidate bullet; do not turn a record-only request into a clarification-only turn.

### Resume-sufficient

The material supports at least one accurate candidate bullet with:

1. A concrete personal action, decision, analysis, design, delivery, or coordination contribution, with participation scope preserved.
2. A meaningful object and a result, output, deliverable, or finding. A concrete qualitative result is acceptable; a metric is optional.
3. Conditions needed to avoid presenting team scope, future work, estimates, or uncertainty as an individual completed result.

If a target role is known, the candidate wording should be relevant to it. Without a target role, professionally meaningful wording is enough for the library. Project-wide scope and team results never become personal actions by implication.

## Question gate and interruption

Ask a follow-up only when all of these are true:

1. A specific fact is missing or two supplied facts explicitly conflict.
2. The answer could change a core fact, ownership, JD match, experience selection, or likely bullet.
3. The user can answer from memory in one short reply.
4. Neutral wording, a qualifier, or omission cannot safely handle the gap.
5. The resume value justifies the user's effort.

If any condition fails, do not ask. Store a nonessential enhancement as 可选待补充 or omit it.

Choose questions in this order: contribution boundary, concrete action or decision, role-relevant result or deliverable, then a JD-critical tool, scale, or condition. In default 极速采集, send at most one clarification message for an experience, containing one to three related items only when each passes the gate. After the reply, draft what is supportable and list remaining optional gaps; do not continue interviewing unless the user explicitly requests 精细模式.

允许第二次澄清：当新答案产生实质矛盾，或关键身份、日期、贡献边界仍无法安全表达时，可以再次澄清。如果争议点可以省略而其余内容仍可交付，则省略该点并说明限制。

Do not question plausibility alone. Treat an unusual number, method, chronology, or outcome as provided unless mutually exclusive statements, incompatible labels or units, or the user's own uncertainty make the meaning unsafe.

The clarification response contains only a short reason and the requested items. Do not show a schema, full draft, index, or write the library on that turn when the task requires resume-ready wording.

## Record states and evidence

Information state:

- 用户已确认: directly stated or confirmed by the user.
- 资料来源-待本人复核: imported from an old resume, certificate, work, or other source not yet checked.
- AI整理-待确认: AI-composed wording that may add meaning and needs confirmation.
- 待补充: a material gap that blocks safe wording.
- 可选待补充: useful enhancement that does not block the current task.
- 存在冲突: incompatible statements not yet resolved.

Capability state:

- 用户自述: direct skill or proficiency statement without a required project link.
- 已验证: supported by a concrete experience, artifact, result, or validation process; this does not mean independent third-party verification.
- 可迁移: supported in an adjacent context but not directly in the target context.
- 待补齐: no sufficient evidence yet.

Scope states by fact group when they differ, for example 项目事实：用户已确认；候选表述：AI整理-待确认. Never let a record-wide label upgrade AI wording or downgrade user-confirmed facts. 忠实改写（faithful rewrite）only compresses, reorders, or normalizes terms and does not need a new confirmation round. A substantive inference adds causal meaning, contribution level, proficiency, or extrapolation and must remain pending until confirmed.

Use these eligibility rules:

| Source or action | Store as | Resume use |
|---|---|---|
| User-confirmed action or result | Confirmed fact | Yes, with scope |
| User-stated tool or skill | Self-reported capability | Skills section with stated scope; no invented project use |
| Old resume or certificate not reviewed | Source awaiting review | Draft cautiously and disclose status |
| AI-derived adjacent capability | Transferable capability | Use only with precise scope |
| Intended study or future project | Plan | Not as completed experience |
| Completed practice with saved output | Validation record | Describe as practice or personal project |

Preserve every baseline, range, condition, estimate, project status, and qualifier attached to a number or result. Do not require documentary proof during normal intake unless the user requests an audit or the claim is a regulated credential required in the final resume.

## Bounded I/O and update contract

1. Find the user's experience library once per task and retain its path.
2. For an existing record, read only the ID or heading section and directly affected index rows. For a new record, scan headings or IDs rather than the entire file.
3. Hold a clarification draft in conversation context; do not write on that turn.
4. On commit, update the source narrative, compact main record, resume-sufficiency field, and affected index rows in one edit. Append at most one maintenance-log entry per completed experience or batch.
5. Defer global index rebuilding and consistency checks until the intake session ends or a JD/resume task makes them necessary.
6. Existing libraries may use a detailed legacy schema. Preserve them in place and change only relevant lines; do not batch-migrate, normalize, reorder, or reformat during ordinary intake.

The compact record contains ID/title, type or context, fact-group states, resume sufficiency, faithful source narrative, supported personal action and result/output when known, keywords, a candidate bullet only when resume-sufficient, and optional gaps only when useful.

Apply the requested outcome:

- Explicit record-only save: save if record-sufficient, even when resume-insufficient.
- Resume-ready intake, JD matching, or generation: if not resume-sufficient, ask the compact clarification first; after the reply, commit what is supportable.
- Unrelated records and indexes remain untouched.
- A direct skill statement does not trigger a project-link question. Derive links only from existing narrative.

## Depth and skill claims

Default depth is 简历采集: ownership, relevant action, and meaningful result or output.

Use 简历增强 only for a requested optimization or a target JD that makes scale, baseline, constraint, tool, or decision materially useful. Use 深度复盘 only after an explicit request for technical reconstruction, interview preparation, portfolio work, or research audit.

Do not request citations, complete formulas, exhaustive component lists, parameter tables, serial numbers, every stakeholder, or full experiment settings merely to complete a template.
