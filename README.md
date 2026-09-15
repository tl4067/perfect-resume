# Perfect Resume

Perfect Resume is a Codex skill for turning free-form career narratives into a structured, traceable experience library, matching that evidence against a job description (JD), and producing a targeted resume without inventing claims.

The skill keeps reusable instructions and blank templates in the repository. A user's personal data belongs in their own workspace and should never be committed here.

## Features

- Capture career experiences through a concise conversational workflow.
- Separate confirmed facts, AI-organized wording, optional gaps, and unresolved conflicts.
- Maintain a reusable personal experience library with stable experience and capability IDs.
- Decompose a JD into requirements and map each requirement to supporting evidence.
- Identify unsupported requirements and propose small, verifiable gap-validation tasks.
- Tailor resume content to a target role while preserving scope, qualifiers, and source traceability.
- Generate and visually verify a DOCX resume from a user-supplied template or the bundled ATS-oriented template.
- Audit existing resume claims against the experience library.

## How It Works

1. Perfect Resume copies the blank experience-library template into the user's workspace when no library exists.
2. The user describes an experience in natural language. The skill records confirmed facts and asks only for missing details that materially affect a resume claim.
3. For a target JD, the skill builds a requirement-to-evidence matrix before drafting resume text.
4. It selects the strongest relevant evidence, preserves uncertainty and participation boundaries, and omits unsupported keywords.
5. When a DOCX deliverable is requested, it uses the user's template first or the bundled template, then renders and checks the result.

The repository contains instructions and templates only. It does not include an API service, executable installer, or background process.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-account>/perfect-resume.git
   ```

2. Copy or clone the repository folder into a Codex skills directory. Codex normally discovers personal skills from `$CODEX_HOME/skills`; when `CODEX_HOME` is unset, use `~/.codex/skills`:

   ```text
   $CODEX_HOME/skills/perfect-resume/
   ```

   On Windows with the default location, this is typically:

   ```text
   %USERPROFILE%\.codex\skills\perfect-resume\
   ```

3. Confirm that `SKILL.md` is directly inside the `perfect-resume` folder and keep `assets/`, `references/`, and `agents/` beside it.

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
└── references/
    ├── docx-template-map.md
    ├── interview-and-evidence.md
    └── jd-matching-and-generation.md
```

- `SKILL.md` defines routing, evidence boundaries, and the end-to-end workflow.
- `agents/openai.yaml` provides display metadata for compatible Codex environments.
- `assets/personal-experience-library.md` is an unfilled, reusable experience-library template.
- `assets/resume-template-ats.docx` is the bundled anonymized resume template.
- `references/` contains detailed rules loaded only for the relevant workflow stage.

There are currently no repository scripts or automated tests.

## Privacy

Do not commit real resumes, completed experience libraries, contact details, identity documents, credentials, confidential project information, or generated resume outputs to a public fork of this repository.

Keep user-specific files outside the skill directory whenever possible. The included `.gitignore` excludes common private-data directories, root-level resume outputs, environment files, credentials, and temporary files, but it is not a substitute for reviewing `git diff --cached` before every push.

## License

Perfect Resume is released under the [MIT License](LICENSE).
