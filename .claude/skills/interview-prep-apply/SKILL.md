---
name: interview-prep-apply
description: >-
  Assist with filling out a job application form live, in the user's browser,
  for a specific role — auto-fills known/standard fields from the candidate's
  profile, leaves company-specific screening questions for the user, and always
  stops before the final Submit/Apply click for the user's explicit confirmation.
  Use when the user says "apply to <company>", "help me apply to this role",
  "fill out this application", or picks a role from the nightly Job Search
  Monitor routine or from ~/InterviewPrep/Applications/tracker.md's Target List.
  Never submits an application unattended — this is a live, human-in-the-loop
  flow, not a scheduled/background task.
---

# Interview Prep — Application Assist

Fills a specific job application form using Claude in Chrome, live, with the user
watching. The user always clicks the final Submit — this skill never does.

## Hard rule

**Never click Submit, Apply-confirm, or any equivalent final-action button.**
This applies even if every field looks complete and correct. The moment the form
is filled and ready, stop and show the user — they click it themselves. This is
non-negotiable: automated career-site submissions risk ToS violations and
account/application blacklisting, and screening-question answers need human
judgment. See `~/InterviewPrep/README.md` and prior session precedent — this
constraint was set deliberately, not a default to relax.

## Step 1: Confirm the target

Get the exact job posting URL from the user, or from the latest nightly Job
Search Monitor routine report (`https://claude.ai/code/routines/trig_01MveF1LTSDrczn9MLFNx7jK`)
if they just named a company/role from it. If ambiguous, ask which specific
posting before opening a browser tab.

## Step 2: Load browser tools

If `mcp__claude-in-chrome__*` tools are deferred, load the core set in one
`ToolSearch` call: `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__find`.
Call `tabs_context_mcp` first, then open the job posting in a **new tab** — don't
reuse an existing tab unless the user asks.

## Step 3: Read the candidate's standard answers

Read `~/InterviewPrep/Applications/standard_answers.md` for the fields to
auto-fill (name, email, phone, LinkedIn, resume file, years of experience, work
authorization, etc.). If that file doesn't exist yet, tell the user and offer to
create it from their resume before continuing — don't guess or fabricate any
field.

## Step 4: Fill the form

Click "Apply" if needed, then read the form fields (`read_page` / `find`).
Fill only fields with a direct, confident match in `standard_answers.md`:
name, email, phone, LinkedIn URL, resume upload, years of experience, work
authorization (if stated), location.

**Leave blank, and flag to the user, anything that needs judgment or isn't in
standard_answers.md**: compensation expectations, notice period (unless stated),
"why this company," free-text screening questions, referral source, cover
letter, diversity/EEO questions. Never invent an answer to these.

If the resume field requires a specific file, use the latest resume PDF (check
`~/InterviewPrep/Applications/standard_answers.md` for the current file
location/Drive link — don't assume a stale path).

## Step 5: Stop before Submit

Once the known fields are filled and the remaining ones are flagged, stop.
Tell the user plainly what's filled, what's still blank and needs them, and
that the form is ready for their review. Do not proceed further. If a CAPTCHA,
bot-check, or login wall blocks the flow, stop immediately and report it —
don't retry blindly or try to work around it (per the browser-automation
guidance: no more than 2-3 attempts before checking in).

## Step 6: After the user submits

Ask the user to confirm once they've actually clicked submit. Then log it in
`~/InterviewPrep/Applications/tracker.md`: move the company from the **Target
List** section to **Active**, using the entry format already in that file
(Applied date, Stage: applied, Notes on anything relevant from the application
— e.g. screening questions asked, comp range entered).
