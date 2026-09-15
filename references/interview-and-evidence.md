# Interview and evidence rules

## Contents

1. Conversational intake
2. Two sufficiency thresholds
3. Question gate
4. Resume-sufficiency stop
5. Detail depth
6. Skill claims
7. Token-efficient I/O
8. Record states
9. Evidence and inference
10. Update contract

## Conversational intake

Accept an incomplete narrative without demanding a form. First extract a known-facts list from the current message, the user's confirmed library, and supplied source files. Normalize wording without turning an already stated fact into a question.

The goal is a useful, supportable experience record, not a complete technical history. When the narrative is resume-sufficient, return the structured draft and candidate resume wording without appending a question. When an explicit save request is only record-sufficient, save the faithful record without manufacturing a candidate bullet.

## Two sufficiency thresholds

Evaluate these thresholds independently:

### Record-sufficient

Material is record-sufficient when it identifies a distinct experience and its source narrative can be saved faithfully without inventing material facts. A project name plus the user's stated participation and project-wide scope can be record-sufficient even when it does not show what the user personally did.

When the user explicitly asks to add, record, or save record-sufficient material, save it in the current turn. If personal ownership is missing, preserve the confirmed project facts, set `简历充分性：不足`, record the blocking gap, and omit the candidate resume bullet. Do not use resume insufficiency to block an explicit record-only save request.

### Resume-sufficient

Material is resume-sufficient when it supports at least one accurate candidate bullet containing:

1. A concrete personal action, decision, analysis, design, delivery, or coordination contribution, with ownership or participation scope preserved.
2. A meaningful object plus a result, output, deliverable, or finding. The result can be qualitative when concrete; a metric is optional.
3. Any condition or qualifier needed to avoid presenting team scope, future work, or uncertainty as an individual completed result.

When a target role is known, the bullet must also be relevant to that role. Without a target role, professionally meaningful wording is sufficient for the library.

Information state and resume sufficiency are separate. Directly supplied project facts remain `用户已确认` even when the record is not resume-sufficient. When source states differ inside one record, label them by fact group, for example `项目事实：用户已确认；候选表述：AI整理-待确认`; never let a record-wide label upgrade AI wording or downgrade user-confirmed facts.

## Question gate

For a task that requires resume-sufficient wording, ask a follow-up only when every condition below is true:

1. A specific fact is missing or two supplied facts are explicitly inconsistent.
2. The answer could materially change resume truth, personal ownership, experience selection, JD match level, or the wording of a likely bullet.
3. The user can probably answer from memory in one short reply; the question does not require research, document lookup, calculation, or reconstruction.
4. Accurate neutral wording or a preserved qualifier cannot safely handle the gap.
5. The expected resume value is worth the user's effort.

If any condition fails, do not ask. Record a nonessential gap as `可选待补充`, or omit it entirely.

For an explicit record-only save request, use this gate only to decide whether a gap should be reported after saving; it must not convert the turn into a no-write clarification turn. Ask before writing only when the material is not record-sufficient because the experience itself cannot be identified or preserved faithfully.

Plausibility is not a conflict. An unusual number, method, chronology, or result is not grounds for rechecking. A material conflict requires observable evidence such as mutually exclusive statements about the same event, incompatible labels or units that make the sentence unintelligible, or the user explicitly expressing uncertainty. Ask only if that conflict blocks safe wording.

When a question passes the gate, choose in this order:

1. Personal contribution boundary
2. Concrete actions and decisions
3. Result or deliverable needed for the target role
4. A tool, method, scale, or condition explicitly important to the target JD

In default `极速采集`, send at most one clarification message for an experience. Prefer one item; include up to three related items only when every item independently passes the gate and combining them avoids another round. After the user's reply, draft what is supportable and list any remaining optional gaps without continuing the interview.

The clarification response contains only a short reason and the requested items. Do not repeat the narrative, show a schema, preview indexes, or write to the library on that turn.

## Resume-sufficiency stop

Stop questioning as soon as the available facts support at least one accurate candidate bullet that meets the resume-sufficient threshold. A role label or generic verb such as `参与`, `负责`, or `协助` without a specific action is not sufficient; project-wide research scope and team results do not substitute for personal action; neither does a vague result such as `效果不错` or `表现良好`.

A metric is helpful but not mandatory when the action and output are concrete. If the narrative contains only generic participation and a vague outcome, ask first what the user personally did—not for company name, exact dates, technical minutiae, or proof.

Company name, exact dates, team size, exhaustive methods, and evidence identifiers may improve a record but do not block the first draft unless the user is assembling the final resume and that field must appear there.

When sufficient, prepare internally:

1. Faithful source narrative or known facts
2. Structured experience draft
3. One or more candidate resume bullets
4. Optional gaps as non-blocking notes, only when useful

Save them in one commit when authorized. For a resume-sufficient record, the user-facing response contains the record ID, one candidate bullet, and a compact change summary. For a record saved below that threshold, report the ID, `已入库，暂不生成候选要点`, and the one material gap. Show the full record only on request. Do not end with a question just to keep the interview moving.

## Detail depth

Default to `简历采集` depth.

| Depth | Include | Follow-up behavior |
|---|---|---|
| 简历采集 | Ownership, relevant action, meaningful result or output | Apply the question gate; stop when resume-sufficient |
| 简历增强 | High-value scale, baseline, constraint, tool, or decision | Ask only when tied to a target JD or requested optimization |
| 深度复盘 | Technical reconstruction, interview preparation, portfolio or research audit | Enter only after explicit user request |

At default depth, do not request citation or document numbers, exhaustive constituent lists, complete formulas, parameter tables, full experimental settings, serial numbers, campaign-by-campaign details, every stakeholder, or implementation minutiae. These are examples of a general rule: if the answer will not materially alter a likely resume sentence, do not ask.

## Skill claims

A direct statement such as “I use AutoCAD” is a self-reported skill fact, not a missing-project prompt. Record it as `用户自述` with the user's stated proficiency or scope. Do not ask which project used the skill, what artifact proves it, or which detailed operations were performed during normal resume intake.

Derive skill-to-experience links only from narratives already available. If no natural link exists, leave it unlinked. In the final resume, an unlinked self-reported skill may appear in the skills section but must not be rewritten as project experience. When a target JD makes stronger evidence desirable, report the evidence gap or offer a validation task; do not convert the gap report into an interview unless the user asks to strengthen it.

Pending-question lists, capability indexes, gap tables, and legacy `本轮唯一问题` fields are not queues. Filter them through the current user goal and question gate; ignore entries whose only purpose is to complete a template or prove a skill-to-project relationship.

## Token-efficient I/O

Use one intake transaction per experience or user-supplied batch:

1. Discover the library path once and retain it for the task.
2. Hold the working draft in conversation context during clarification; perform no file write.
3. Find an existing record by ID or heading and read only the bounded section plus directly affected index rows. For a new record, scan headings or IDs instead of loading the whole library.
4. Commit the source narrative, compact main record, and affected index rows together once. The compact record contains: ID/title, type/context, information state, resume sufficiency, faithful source, supported personal action and result/output when known, keywords, a candidate bullet only when resume-sufficient, and optional gaps only when useful.
5. Append one compact maintenance entry for the completed experience or batch, never one per answer.
6. Defer full capability/result index rebuilding and global consistency checks until the intake session ends or the user requests an audit. For JD analysis or resume generation, inspect indexes first and load only shortlisted records unless stale indexes make a full consolidation necessary.

Do not fill a long form merely because fields exist in an older template. Preserve legacy detailed records in place and change only relevant lines; never migrate the library during ordinary intake.

On clarification turns, output only the compact request. On commit turns, output three to five lines: saved file, record ID, candidate bullet when available, or the material gap when resume sufficiency is不足.

## Record states

Use information state separately from capability state.

Information state:

- `用户已确认`
- `资料来源-待本人复核`
- `AI整理-待确认`
- `待补充`: a material gap that blocks safe resume wording
- `可选待补充`: an enhancement that does not block drafting and should not trigger a question by default
- `存在冲突`

Information state describes the reliability or completeness of facts; it is not the resume-sufficiency field. Scope mixed states to their fact groups. Use `简历充分性：足够` or `简历充分性：不足（原因）` separately so confirmed project facts are not mislabeled merely because personal ownership is missing.

Capability state:

- `用户自述`: directly reported proficiency without a required project link
- `已验证`: linked to an experience, artifact, result, or validation process
- `可迁移`: supported by adjacent evidence but not directly used in the target context
- `待补齐`: unsupported until a learning or practice task is completed

## Evidence and inference

Preserve the difference between fact, inference, and plan.

| Input | Store as | Resume eligibility |
|---|---|---|
| User-confirmed action or result | Confirmed fact | Yes |
| User-stated tool or skill | Self-reported capability | Yes in the skills section with preserved scope; no invented project use |
| Old resume or certificate not yet reviewed | Source fact awaiting review | Use cautiously and disclose status during review |
| AI-derived adjacent capability | Transferable capability | Only with precise scope |
| Intended study or future project | Plan | No |
| Completed practice with saved output | Validation record | Yes, described as practice or personal project |

Never manufacture a number or remove its baseline, condition, range, uncertainty, or project-status qualifier.

Treat facts directly stated by the user as provided evidence. `AI整理-待确认` applies to the AI's composed wording, not to whether the user must repeat every underlying fact. Do not require proof, source identifiers, or documentary verification during default intake unless the user asks for an audit or the claim is a regulated credential that must appear in the final resume.

## Update contract

Apply the update path that matches the user's requested outcome:

1. **Explicit record-only save**: if the material is record-sufficient, perform one edit covering the source narrative, main record, resume-sufficiency field, and directly affected index rows. Save resume-insufficient records with the material gap and no candidate bullet.
2. **Resume-ready intake, JD matching, or resume generation**: if the material is not resume-sufficient, ask the compact clarification first and perform no file write on that clarification turn. After the reply, commit what is supportable.
3. Leave unrelated indexes untouched; schedule full consolidation only at a defined boundary.
4. Keep nonessential gaps as `可选待补充` without reopening the interview.
5. Append at most one maintenance-log entry for the completed experience or batch.
6. Report the change compactly without reprinting the record.
