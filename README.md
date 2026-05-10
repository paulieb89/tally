# tally

A tiny CLI for counting things. Used as the practice vehicle for a six-lesson git workflow course.

```bash
tally add tasks        # increment the 'tasks' counter
tally show             # print all counters
```

## Setup

```bash
# 1. Fork this repo on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/tally.git
cd tally

# 3. Create and activate a virtual environment

# Mac / Linux
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

# 4. Install
pip install -e ".[dev]"

# 5. Check it works
tally add tasks
tally show
pytest
```

> The venv must be active whenever you use `tally` or run tests.
> You'll know it's active when you see `(.venv)` at the start of your terminal prompt.
> To reactivate in a new terminal: run the `activate` command from step 3 again.

## The lessons

The full course lives at [git-lessons](https://github.com/paulieb89/bouch-test/blob/main/docs/git-lessons/00-overview.md).

Each lesson adds one command or fixes one bug. By Lesson 6, an AI agent is opening PRs using the same workflow you've been practicing.
