# Copilot Instructions — dictionary-and-loops-practice

This repository is a small teaching repository of standalone Python exercises (day-based mini-projects). The goal of these instructions is to help an AI coding agent be immediately productive working on small script-style exercises and sample datasets.

Quick overview
- Project layout: small numbered scripts grouped by day under `day_1_activities/`, `day_2_challenge/`, and `day_3_uber_eats_challenge/`.
- Data files are plain Python modules that expose lists (e.g. `students`, `orders`) used as in-memory datasets.

Key files (examples)
- `day_1_activities/student_data.py` — contains `students` list of dicts; keys: `CPSID`, `Combo,Name`, `LName`, `FName`, `MName`, `HR`, `GL`, `Email` (Email is a list of two addresses).
- `day_1_activities/3_mini_challenge_day1.py` — a CLI-style interactive exercise that imports `student_data2` and expects the agent to add search/add functionality.
- `day_3_uber_eats_challenge/orders.py` — contains `orders` list used by `5_uber__eats_challenge.py` to exercise creating/updating/filtering orders.

Architecture & patterns to follow
- These scripts are single-file, synchronous CLI programs. Avoid introducing frameworks or long-lived services.
- Data is held in plain Python modules (mutable globals). Changes should be in-memory and reflected by printing; persistent storage is out-of-scope unless explicitly requested.
- Naming: files are intentionally prefixed with numbers (e.g., `1_pre_lesson.py`) — preserve those names when editing unless user requests renames.

Conventions and idioms observed
- Use simple imperative functions or top-level guards (`if __name__ == "__main__":`) when adding runnable behavior.
- When reading or mutating datasets, use the existing keys exactly (e.g. `student['CPSID']`, `student['Combo,Name']`).
- Email values are lists: treat primary email as `Email[0]` and secondary as `Email[1]`.

Running & debugging
- Scripts are run directly with Python from the repository root. Example:

```bash
python day_1_activities/3_mini_challenge_day1.py
python day_3_uber_eats_challenge/5_uber__eats_challenge.py
```

- Because modules import sibling files (e.g. `import student_data2`), run from the repo root so Python finds packages by path.
- There are no test runners or build steps in this repo. Use simple prints and small examples to validate changes.

Safe change rules for AI agents
- Prefer minimal, focused edits that preserve the script structure and intent (do not refactor across many files).
- Do not change file names unless the user asks. Many exercises refer to named datasets by filename.
- When adding functionality, include a short, non-interactive test harness or `if __name__ == "__main__"` block so maintainers can run your change easily.

What to look for (helpful examples)
- Implement search/add/update functionality by iterating over the dataset lists and comparing keys such as `CPSID` or `order_id`.
- When preventing duplicates, check the unique id field first and print a clear message on collision.
- Keep user-facing messages simple and instructional — these are student exercises.

When to ask the user
- If a requested change would move toward persistence (file writes, databases) ask for explicit approval.
- Ask before renaming/moving files or changing the module import layout.

If you modify code
- Run the edited script locally (see Running & debugging) and include the minimal run output or a short usage example in your PR or message.

Feedback
- If any of the key dataset shapes or file references above are incorrect or incomplete, tell me which file(s) you'd like me to re-inspect.
