---
name: perfect-resume
description: Use when a user wants to record or correct career experiences, analyze a job description, identify evidence-backed gaps, review or tailor a job-seeking resume, or create or edit a DOCX resume from a supplied or built-in template.
---

# Perfect Resume

## Purpose and scope

Use this skill for a job-seeking experience library, JD analysis, resume review, and targeted or general job resume deliverables. It preserves source facts, personal contribution boundaries, and lightweight traceability. It does not claim a dedicated workflow for a complete academic CV; when that is requested, identify the scope difference and handle only the applicable requested parts.

Keep user data in the user's workspace. The skill directory contains workflow rules, blank assets, templates, and checks. Never upload a resume or personal profile to a third-party ATS or testing service.

## Route by current intent

Choose the shortest applicable route. An experience library is not a prerequisite for a local edit, review, or first resume draft.

| Current request | Read | Write | Default result |
|---|---|---|---|
| Add or correct an experience | Relevant record and affected index rows; read references/interview-and-evidence.md once | Only the affected library record and index rows | Compact save summary |
| Analyze a JD only | JD and relevant indexes/records; read references/jd-matching-and-generation.md | No personal-library write by default | Matching report, unknowns, and impact |
| Plan a gap | Target requirement and current evidence | Save only when the user asks | Verifiable task with capability limits |
| Generate a targeted resume | JD, relevant evidence, chosen template, and delivery reference | New DOCX plus same-name mapping | Matching report, resume, delivery notes |
| Generate a general resume | Existing evidence and stated direction; no JD required | New DOCX plus same-name mapping | Clearly marked as not JD-tailored |
| Edit an existing resume locally | Supplied file and only the evidence needed for the requested change | New revision or in-place edit only when explicitly requested | Changed result and unresolved items |
| Review an existing resume | Resume and supplied evidence | No file change by default | Traceability issues, edits, and unverifiable claims |
| Complete academic CV request | Requested scope and supplied material | Only the requested applicable artifact | Explain that this skill has no dedicated full academic-CV pipeline |

If a JD, template, language, or page requirement is already supplied, reuse it instead of asking again. A matching report is an output-order step, not an approval gate; continue to generation when the user asked for the deliverable.

## Global evidence contract

Every material resume claim must be:

confirmed fact or clearly labeled transferable capability + source ID + preserved scope and condition.

Keep these distinct:

- User-provided fact: directly stated in the current message or confirmed library.
- Source awaiting review: imported from an old resume, certificate, or other file and not yet checked.
- Faithful rewrite: compression, ordering, or terminology normalization that adds no meaning.
- Substantive inference: a new causal link, contribution level, proficiency, or extrapolation; confirm or label it before a final resume.
- Conflict: mutually incompatible statements; clarify or omit the affected claim.

A faithful rewrite does not need an extra confirmation round. A substantive inference cannot become a fact merely because the sentence sounds polished. Do not infer tools, methods, scope, production status, metrics, credentials, or learning status from a JD or common practice. Preserve '约', '预计', '参与', '协助', '申请中', and similar qualifiers.

Read references/interview-and-evidence.md for the intake question gate, two sufficiency thresholds, states, bounded reads, and update contract. Do not migrate or globally reformat an existing detailed library during ordinary work.

## Evidence and gap routing

- Save an explicitly requested record once it is record-sufficient, even when it is not resume-sufficient. Mark the gap and omit a candidate bullet rather than blocking the save.
- For a resume request, ask at most one compact clarification round by default, with one to three related questions only when the question gate passes. Allow a second clarification for a material contradiction or an unsafe identity, time, or contribution boundary.
- A direct skill statement may be stored as 用户自述 without forcing a project link.
- JD analysis reports missing evidence by default. Create a practice plan only when the user explicitly asks to learn, fill, or strengthen a gap. Practice supports the described practice or personal project; it does not replace formal work years, degree, credential, management scale, or production experience.

## Resume workflow

1. Identify whether the request is targeted, general, local edit, review, intake, or gap planning.
2. For intake, read the interview reference once; for JD or resume work, read the JD reference and then load only relevant records from capability/result indexes.
3. For a targeted resume, decompose the JD and produce the matching report before drafting. Use statuses 已满足, 部分满足, 未知, and 明确不满足; keep source, relevance, depth, and recency as separate internal judgments.
4. Select the template: a user-supplied template wins. For an unspecified channel, use the machine-parsing-priority template; use the visual template when the user asks to retain the visual system or explicitly wants a photo. Read references/docx-template-map.md.
5. Select evidence by role value and density rather than a fixed number of experiences. Edit bullets so each focuses on one main action or result; the experience as a whole should cover goal, personal action, and result or deliverable when supported.
6. Use the documents:documents skill for DOCX reading, editing, rendering, and verification. Run the read-only template audit before using a built-in template:
   python scripts/audit_docx_template.py <docx> --profile blank-template
7. Before delivery, follow references/delivery-and-versioning.md: separate fact, text, layout, privacy, and cleanup checks. Render and inspect every requested page; if a dependency is unavailable, disclose the specific checks not run.
8. When a resume is actually generated or edited, write a same-name .mapping.md beside it. The mapping stores the date, target/JD context, template and language, source IDs, key source excerpts, preserved qualifiers, unresolved items, and checks completed. It never becomes resume body text and is not overwritten when the library later changes unless the user requests regeneration.

## Output boundaries

- Intake/correction: update only the library and return a three-to-five-line summary.
- JD-only analysis: do not alter the library or resume by default.
- General resume: state that no JD was used.
- Local edit/review: do not turn the task into a full-library migration.
- Final resume: provide the file, concise source mapping summary, and unresolved risks. Never claim universal ATS compatibility, hiring probability, or checks that were not run.
