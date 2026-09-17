# Delivery and versioning

## When to use this reference

Use this reference only when a resume is actually generated or edited. Intake-only saves, JD-only analysis, and resume reviews do not create a delivery mapping unless the user requests one.

## Delivery checks

Run and record these checks separately:

1. **Fact check**: each material claim traces to an experience or capability ID; personal action, team result, status, estimate, range, and condition remain accurate.
2. **Text check**: contact details, dates, experience order, section text, bullets, and qualifiers are complete after generation.
3. **Layout check**: render the requested page count with the documents skill and inspect every page for clipping, overlap, overflow, page breaks, missing glyphs, and normal-size readability.
4. **Privacy check**: export only information approved for this application; inspect document properties, headers, footers, alt text, comments, revisions, custom XML, embedded objects, and relationship targets for unrelated data.
5. **Cleanup check**: remove unused brackets, empty bullets or headings, unused modules, and PHOTO graphics when no photo is requested.

Run the built-in-template audit before editing a built-in DOCX. It is a structural and metadata check, not an ATS test or third-party identity verification. If the DOCX library or renderer is unavailable, complete the content that can be completed, list the checks not run, and never claim visual verification. Do not substitute repeated retries for a limitation disclosure.

## Mapping file

When a resume is generated or edited, save a same-name file with the suffix .mapping.md beside the deliverable. Keep it in the user's workspace; do not place it in the public resume body or the skill assets.

Use this compact format:

    # Resume mapping
    - Generated: YYYY-MM-DD
    - Target role: [role or general resume]
    - JD source: [path, necessary user-provided snapshot, or none]
    - Language: [language]
    - Template: [user template or built-in default template]
    - Experience IDs: [IDs used]

    ## Key claims
    - Resume wording: [final wording]
      - Source ID: [ID]
      - Source excerpt: [short fact excerpt]
      - Preserved scope or qualifier: [scope/status/condition]

    ## Unresolved items
    - [unknown, omitted claim, or risk]

    ## Checks
    - Fact: [completed/not run + note]
    - Text: [completed/not run + note]
    - Layout: [rendered and inspected/not run + note]
    - Privacy: [completed/not run + note]
    - Cleanup: [completed/not run + note]

Include only the source excerpts needed to explain this version; do not copy the entire personal library or JD. A later library correction does not rewrite an existing mapping. Regenerate and replace the mapping only when the user asks for a new resume version.

## Version boundaries

- A new resume version gets a new filename or an explicit user-approved overwrite.
- Updating an experience library does not silently modify an already delivered resume or mapping.
- If a claim is corrected after delivery, note the correction and leave the previous mapping intact until regeneration is requested.
- Never use the mapping to claim universal ATS compatibility, hiring probability, or checks that were not performed.
