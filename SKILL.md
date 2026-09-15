---
name: perfect-resume
description: Use when a user wants to build or update a personal experience library, narrate career experiences for structured capture, analyze a job description (JD), identify evidence-backed skill gaps, tailor a resume or CV to a specific role, or generate a DOCX resume from a supplied or built-in template.
---

# Perfect Resume

## Overview

Turn free-form career narratives into a confirmed experience library, then use traceable evidence to match a JD and generate a targeted resume. Keep personal facts separate from the skill: the skill contains workflow and blank assets; each user's data stays in their workspace.

## Route the request

| User intent | Action |
|---|---|
| Start a personal experience library | Copy `assets/personal-experience-library.md` to the user's workspace and begin the interview |
| Add or correct an experience | Cache the library path, collect in memory, then commit the record once; keep resume files unchanged unless the user explicitly asks to generate or update one |
| Analyze a JD | Produce a requirement-to-evidence matrix before writing resume content |
| Fill a skill gap | Create the shortest verifiable learning task; do not claim completion yet |
| Generate a resume | Match evidence, select a template, create DOCX, render, and verify |
| Review an existing resume | Trace claims to the library and flag unsupported or ambiguous statements |

### Experience-intake output boundary

When the user asks only to add, record, supplement, or correct an experience, complete the request by updating the experience library and returning the compact intake summary. Existing resume, CV, template, and DOCX files remain unchanged. The presence of a resume in the workspace does not expand the request.

Enter the resume workflow only when the user explicitly asks to generate, update, edit, tailor, or export a resume or CV. A candidate bullet created during intake is library content and a conversational preview; it is not authorization to write that bullet into a resume.

### Two sufficiency thresholds

Judge storage and resume use separately:

- **Record-sufficient**: the material identifies a distinct experience and can be preserved faithfully without inventing material facts. This is enough to save a record when the user asks to add, record, or save it, even if personal ownership is incomplete.
- **Resume-sufficient**: the facts support at least one accurate candidate bullet with a concrete personal action, decision, analysis, design, delivery, or coordination contribution; a meaningful object, result, output, or finding; and any necessary scope qualifiers. A metric is optional.

Information state records the source and confidence of supplied facts; resume sufficiency records whether those facts support a personal resume claim. Scope information state to fact groups when they differ, for example `项目事实：用户已确认；候选表述：AI整理-待确认`, rather than assigning one blanket state to the whole record. User-confirmed project facts can therefore coexist with `简历充分性：不足`. Do not turn project-wide scope or team results into personal actions merely to make a record resume-sufficient.

## Core workflow

### 1. Locate or create the experience library

Search the workspace once per task for a user-designated experience library and retain that path in the active context. Do not repeat discovery on later turns. If none exists, copy `assets/personal-experience-library.md`; ask where to save it only when multiple sensible locations exist.

Read `references/interview-and-evidence.md` once before collecting or changing personal facts. Do not reload it on every answer in the same task.

### 2. Collect experience conversationally

Default to `极速采集`. Let the user narrate freely. Preserve a faithful source narrative and treat facts stated in the current message as already provided. Do not re-ask them in different words.

Use the question gate in `references/interview-and-evidence.md` before every follow-up item. Zero questions is preferred when the narrative is resume-sufficient. Generic participation plus project-wide scope or a vague result such as “效果不错” is not resume-sufficient.

If the user explicitly asks to add, record, or save an experience and it is record-sufficient, commit it in the current turn even when it is not resume-sufficient. Mark `简历充分性：不足`, preserve the material gap, and omit the candidate bullet; do not convert this save request into a clarification-only turn.

If the current task requires resume-ready wording, JD matching, or a resume deliverable and the experience is not resume-sufficient, send one compact follow-up containing one to three related items that each pass the question gate. Do not show a draft, read the full library, or write files on that clarification turn. After that one reply, draft what is supportable and stop; continue turn-by-turn interviewing only when the user explicitly requests `精细模式`.

When a record is resume-sufficient or the user explicitly asks to save a record-sufficient experience, perform one commit using the compact record shape in `assets/personal-experience-library.md`: add or update the source narrative, main record, resume-sufficiency field, and directly affected index rows in a single edit. Use `AI整理-待确认` for AI-composed wording while preserving directly stated facts as user-provided evidence. Do not populate the legacy detailed schema, add a separate confirmation turn, rebuild unrelated indexes, or append more than one maintenance-log entry for the completed experience or batch.

During the same intake session, keep the working record in conversation context. For an existing record, search by its ID or heading and read only that record plus directly affected index rows. For a new record, scan headings or IDs only. For JD analysis or resume generation, read the capability/result indexes first and then only the most relevant records. Read the entire library only for an explicit full-library audit or a necessary end-of-session consolidation.

Existing libraries may contain the earlier detailed record format. Preserve those records and edit only the needed lines; do not migrate, normalize, or reformat them during ordinary intake.

Return either the compact clarification request or, after commit, a three-to-five-line change summary. For each record, include its ID and candidate bullet when resume-sufficient; otherwise state `已入库，暂不生成候选要点` and name the one material gap. Do not echo the full source narrative, schema, index table, or maintenance log unless the user asks to review it.

Capability indexes are retrieval aids, not interview queues. Derive skill-to-experience links silently from facts already supplied. If a user directly states that they know a tool or skill, store it as `用户自述`; do not ask which project used it merely to manufacture an evidence link. A self-reported skill can appear in the resume skills section with accurate scope, while unsupported project claims remain omitted. Create validation tasks only when the user explicitly asks to strengthen a gap.

### 3. Analyze the JD before drafting

Read `references/jd-matching-and-generation.md`. Separate hard requirements, responsibilities, tools, domain context, and optional qualifications. Map each requirement to experience and skill IDs with one status: strong, medium, weak, or gap.

Show the matching report before generating a resume unless the user explicitly asks to skip it.

### 4. Route unsupported requirements to validation

Never convert absence into experience. For a gap, define a minimal learning goal, practical task, saved evidence, and interview self-check. Upgrade the capability only after the user reports completion and provides enough detail to create a validation record.

### 5. Select the resume template

Use the user's supplied template first. Otherwise copy `assets/resume-template-ats.docx`. The built-in template is anonymized and contains no example person's experiences.

**REQUIRED SUB-SKILL:** Use documents:documents when reading, editing, rendering, or verifying DOCX files. Preserve the chosen template's visual system while adapting section order and visibility to the JD.

Read `references/docx-template-map.md` when using the built-in template.

For a default one-page resume, target a visually balanced, substantially filled A4 page with reasonable breathing room. This is a layout preference, not a reason to add, stretch, or distort content; follow the page-balance recipe in the template map.

### 6. Generate and verify

Select the three to five strongest relevant experiences. Prefer problem or goal, personal action, result, and verification. Keep conditions and qualifiers attached to numbers.

For a sparse one-page resume, use this page-balance recipe in order: (1) include additional JD-relevant, evidence-backed material already in the library, such as a relevant project, skill, course, award, or qualification; (2) turn supported experience into concise action-and-result bullets; (3) rebalance section order and the template's normal spacing. If evidence remains sparse after those steps, retain clean white space. Do not use generic self-evaluations, unrelated entries, invented detail, or unreadably small text merely to fill the page.

Before delivery, verify:

- Every material experience claim maps to an experience ID; a skills-section claim may map to a `用户自述` capability ID without a project link.
- No common-but-unreported tool, method, domain fact, or learning status was added.
- Team results are not presented as individual results.
- `预计`, `约`, `参与`, `协助`, `申请中`, and similar qualifiers remain intact.
- Dynamic personal details and dates are current.
- The DOCX renders cleanly at the requested page count.
- For the default one-page A4 output, relevant evidence has been used to make the page visually balanced without avoidable large blank areas; truthfulness and readability take priority when the evidence is genuinely limited.
- The output file contains no unrelated person's data or document metadata.

Deliver the resume, the mapping summary, and any unresolved risks.

## Evidence boundary

Use this positive contract for every resume sentence:

`Claim = confirmed fact or clearly labeled transferable capability + source ID + preserved scope/condition`

Allowed transformations: concise rewriting, ordering, synonym normalization, and evidence-backed keyword alignment.

Do not infer routine details merely because they are common in the field. For example, a CFD project does not by itself prove conjugate heat transfer, a specific mesher, NumPy/Pandas, a particular turbulence model, or automotive production experience.

Do not challenge a user-provided number or fact based only on plausibility, domain expectations, or an AI calculation. Clarify only an explicit, material contradiction that blocks safe resume wording. Citation numbers, exhaustive component lists, parameter tables, exact configurations, and similar reconstruction details are outside default resume intake unless the target JD makes that detail directly useful or the user requests deep review.

## Conditional artifacts

- Experience intake or correction: update the user-owned Markdown experience library and return the compact intake summary.
- JD analysis: produce a matching report with requirement, match level, source ID, evidence, and action.
- Resume generation or editing: produce a user-template or built-in-template DOCX only when the user explicitly requests a resume deliverable or modification.
- Gap plan: produce only when unsupported requirements materially affect fit.

## Common mistakes

| Mistake | Correction |
|---|---|
| Asking a long questionnaire | Ask one high-value question, wait, then continue |
| Updating a resume because the user said “add an experience” | Update only the experience library unless the user explicitly asks to generate or edit a resume |
| Treating “can be saved” and “can support a resume bullet” as the same threshold | Save record-sufficient material on explicit request; assess resume sufficiency separately and omit unsupported candidate bullets |
| Asking one item per turn by habit | In `极速采集`, group up to three essential items into one follow-up round |
| Reading or writing the whole library every turn | Cache the path, use bounded reads, and commit once per experience |
| Rebuilding every index after each answer | Update affected rows once; defer full consolidation |
| Filling every field in the detailed legacy schema | Use the compact record shape; expand only in `精细模式` |
| Asking where a skill was used | Store direct skill statements as `用户自述`; derive links without interrogating |
| Asking because a field is blank | Draft once resume-sufficient; mark nonessential gaps `可选待补充` |
| Re-asking a stated fact | Treat the current narration as known information and reuse it |
| Auditing technical or academic minutiae | Stay at resume depth unless the user explicitly requests deep review |
| Questioning plausible or unusual data | Preserve user-provided data unless an explicit material conflict exists |
| Treating an old resume as confirmed truth | Mark imported facts as `资料来源-待本人复核` |
| Adding plausible technical details | Use only reported or confirmed evidence |
| Leaving a largely empty default A4 page | Apply the page-balance recipe with relevant, supported content; retain reasonable white space rather than adding filler or shrinking text |
| Writing the resume before matching | Build the JD-to-evidence matrix first |
| Listing a new tool as “currently learning” | Confirm learning has actually started and record evidence |
| Bundling personal data in the skill | Keep user data in the workspace only |
| Recreating a user's design unnecessarily | Preserve their template when supplied |
