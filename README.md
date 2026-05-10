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

# 3. Install
pip install -e ".[dev]"

# 4. Check it works
tally add tasks
tally show
pytest
```

## The lessons

The full course lives at [git-lessons](https://github.com/paulieb89/bouch-test/blob/main/docs/git-lessons/00-overview.md).

Each lesson adds one command or fixes one bug. By Lesson 6, an AI agent is opening PRs using the same workflow you've been practicing.
