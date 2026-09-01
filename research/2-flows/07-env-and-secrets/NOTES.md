# Env variables and secrets — Vercel, captured 2026-08-31

From the owner's signed-in Vercel (`portfolio-react`). Read-only: the add-variable drawer was
opened and closed with the X. Nothing was saved, nothing deployed.

## The add-variable drawer

`vercel-add-env-variable-drawer.jpg`

The best single reference we have for `needsEnv`. What it does, in order:

**1. It asks for the type before the value, and explains both.** Two radio cards at the top:

- **Secret** *(default)* — "You can't reveal this value after saving. Use for passwords, API keys,
  and tokens."
- **Config** — "Readable after saving for members with access. Use for non-sensitive values."

The irreversible option is the default, and each card states the consequence rather than the
category. We have the same split coming: a key that must never land in the archive versus a
value that can sit in `.env.example`.

**2. The Note placeholder teaches what the note is for.** `Note (Optional)` with the placeholder
*"Where to rotate, or who to contact"*. It does not say "add a description". It names the two
questions someone will actually have at 3am. This is the cheapest good idea on the screen and we
should copy the technique everywhere our forms have an optional field.

**3. Value has a reveal toggle**, so the field is masked by default but checkable before saving.

**4. Bulk entry is a first-class path, twice.** A `+ Add Another Variable` row, and in the footer
an **Import .env** button beside the sentence *"or paste .env contents in Key input"* — pasting a
whole `.env` into the Key field is parsed into rows. Our import story is the mirror image: we
*produce* `.env.example`. Their paste-to-parse is what we should offer when a user brings an
existing project in.

**5. Scope last.** An `Environments` dropdown (Production) sits at the bottom, above Save.

## The empty state

`vercel-env-vars-empty-state.jpg` — also filed under flow 08.

*"No Environment Variables Added — Add Environment Variables to Production, Preview, and
Development environments, including branches in Preview."* One heading, one sentence that names
where variables can go, and no illustration.

Worth noting as a **flaw to avoid**: the full toolbar stays on screen over the emptiness — search
plus four filter dropdowns (All Types, All Environments, All Editors, All Variables) plus a sort
control, all filtering nothing. Our Library empty state should suppress controls that cannot do
anything yet.

## Still open in this flow

Doppler and Infisical are captured as marketing pages only. Neither is needed now: Vercel's drawer
covers the design question, and the secret-versus-config distinction is the part we were missing.
