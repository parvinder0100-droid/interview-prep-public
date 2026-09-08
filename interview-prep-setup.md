# Interview Prep in Claude Code — the setup

## Problem it solves

Every new Claude session starts cold. You re-explain what you're studying, where
you left off, what you already got wrong. That's 10 minutes of context-setting
before any actual work, every single time.

## The idea

A plain markdown directory holds your prep state. Three custom skills read and
write it. Sessions become continuous instead of independent.

```
~/InterviewPrep/     <- just markdown files, no database, no app
```

Nothing special about the files — a schedule, a log of what you've covered, a
log of what you got wrong, a spaced-repetition due list. Readable and editable
by hand. Git-trackable if you want history.

## The three skills

**resume** — starts a session. Reads the tracker, figures out what's due or
next, and begins. You don't tell it anything.

**save** — writes the session back. What you covered, what you got wrong, when
to review it again. Nothing persists until this runs, so it's the last thing you
do before closing.

**audit** — read-only checkpoint. Compares actual progress against plan.
Surfaces overdue reviews, untouched areas, repeating mistake patterns. Gives a
ranked list of what to fix. Doesn't modify anything.

That's the whole loop: `resume` → work → `save`. Run `audit` weekly.

## Why it works

- **The mistakes log is the real asset.** Reviewing what you got wrong three
  weeks ago is worth more than solving three new problems. It only works if
  something writes it down every session — hence `save`.
- **Spaced repetition needs persistence.** A due-date list in a file survives
  context loss. Your memory of "I should revisit that" doesn't.
- **Read-only audit stays honest.** Separating "check status" from "log
  progress" means the audit can't quietly rewrite the plan to make you look
  on-track.
- **Markdown is the point.** No lock-in, no tool to maintain. Read it on your
  phone, edit it in any editor, diff it in git.

## Building your own

Claude Code has a `skill-creator` skill — ask it to build a resume/save/audit
trio against a tracker directory of your choosing. Describe your tracker's file
layout and what a session looks like for you; it writes the skills.

Start with two files: a schedule and a mistakes log. Add more only when you feel
the gap. The structure should follow how you actually study, not the reverse.
