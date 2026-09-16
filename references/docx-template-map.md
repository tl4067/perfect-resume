# DOCX template map

## Template choice

1. A user-supplied template always wins.
2. If the user asks to retain an existing design, preserve its visual system and disclose any parsing risk.
3. If no template is supplied and the channel is a recruiting upload, use the machine-parsing-priority template.
4. If the user explicitly wants the original visual layout or a photo, use the visual template.
5. If the channel is unknown and asking would interrupt a straightforward task, use the machine-parsing-priority template and state that assumption.

Do not turn template choice into a fixed extra question. Do not export every profile field. Include photo, age, political affiliation, or other sensitive fields only when the user asks or a clear application requirement calls for them.

## Built-in files

| Use | File | Structure | Default image rule |
|---|---|---|---|
| Machine parsing priority | assets/resume-template-ats.docx | Single-column ordinary paragraphs with clear headings and contact text at the top | No photo |
| Visual preservation | assets/resume-template-visual.docx | Original three-column header and deep-blue hierarchy | Use a user-provided photo only when requested; remove the placeholder when none is supplied |

The filename ATS describes the intended structure, not compatibility certification. Successful local text extraction does not prove every recruiting system will parse a file correctly.

Before using a built-in template, run:

python scripts/audit_docx_template.py <docx> --profile blank-template

The audit is read-only and returns JSON. Exit 0 means no automatically detected blocking issue or review item; exit 1 means a blocking issue or manual review item was found; exit 2 means the file could not be checked. A pass is not a universal anonymity, accessibility, render, or ATS guarantee.

## Machine parsing priority template

- A4 portrait, one section, ordinary body paragraphs, and conventional headings.
- Contact details appear as consecutive text near the beginning, not inside a table or text box.
- Use clear section labels such as Summary, Education, Skills, Experience, Projects, and Awards; adapt language to the user's request.
- Use normal bullets and right-aligned dates only when the structure remains extractable.
- Do not add a photo, decorative text box, hidden text, or multi-column body layout.
- Keep the default body around 10 to 10.5 pt with readable spacing; do not shrink type to fill a page.

## Visual template

- Preserve the original three-column header, deep-blue hierarchy, margins, fonts, indentation, date tabs, and bullet style where practical.
- The visual system may be reordered for a JD, but placeholder text is never a required field.
- The photo cell contains only a generic PHOTO placeholder in the blank asset. Replace it with a user-approved image at the same size or remove the placeholder and rebalance the header.
- Inspect the reading order of contact details, dates, experience text, headers, footers, alt text, comments, revisions, custom XML, and document properties.

## Content mapping

| Resume area | Evidence source |
|---|---|
| Header and direction | Basic profile plus stated target |
| Summary | Two or three strongest evidence-backed capabilities and role value |
| Education | EDU records |
| Skills | Capability index entries whose state and scope allow use |
| Work or internship | WORK and EXP records |
| Projects or research | PROJ and RES records selected for the target |
| Portfolio, papers, or patents | PORT records when requested and in scope |
| Awards and credentials | ACH records with approved personal data |

For a one-page resume, use this balancing order: add relevant evidence-backed material already in the library; compress supported experience into action-and-result bullets; rebalance section order and normal spacing. If evidence remains sparse, retain clean white space. Do not add filler, generic self-evaluations, unrelated entries, or unreadably small text.

When content exceeds the requested page count, compress by relevance and information density. Do not mechanically delete a second project, enforce a three-to-five experience quota, or force a two-page senior resume into one page.

## Placeholder and layout cleanup

Before delivery, remove unused brackets, PHOTO graphics when no photo is requested, empty bullets, empty section labels, and unused modules. Keep contact text, dates, experience order, and qualifiers complete. Render the requested page count and inspect every page for clipping, overlap, overflow, missing glyphs, and readability.
