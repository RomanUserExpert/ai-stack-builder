# `terraform plan`: the reference for our validation pass

Collected 2026-08-31 with Terraform v1.16.0 (downloaded to a scratch directory, nothing installed
system-wide) on a throwaway config. The config deliberately produces the two artifacts our own
export produces — a `SETUP.md` and an `.env.example` — so the shape is directly comparable.

## Output

```
Terraform will perform the following actions:

  # local_file.env_example will be created
  + resource "local_file" "env_example" {
      + content              = <<-EOT
            OPENAI_API_KEY=
            ANTHROPIC_API_KEY=
        EOT
      + content_base64sha256 = (known after apply)
      + content_md5          = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "./out/.env.example"
      + id                   = (known after apply)
    }

  # local_file.manifest will be created
  + resource "local_file" "manifest" {
      + content              = <<-EOT
            # Setup

            Assembled by the stack builder.
        EOT
      + filename             = "./out/SETUP.md"
      + id                   = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

─────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't
guarantee to take exactly these actions if you run "terraform apply" now.
```

## What makes it trustworthy — five mechanics worth stealing

1. **A one-line verdict, and it is a count.** `Plan: 2 to add, 0 to change, 0 to destroy.` You can
   act on that line alone. Our validation pass needs its own single summary line — resolved,
   conflicts, missing keys — that means something without opening anything.

2. **Every item is addressed by name before it is described.** `# local_file.manifest will be
   created` comes before the detail, so the list is skimmable at one level and readable at two.

3. **A symbol per operation, in the left margin.** `+` create, `~` change, `-` destroy. Colour is
   redundant reinforcement, never the only channel. Ours: added manually, pulled in as a
   dependency, conflicting, blocked.

4. **It admits what it does not know.** `(known after apply)` appears on every value that cannot be
   computed yet. It never guesses and never hides the gap. We have the same class of unknown — an
   env variable whose value we cannot see, an external repo we cannot inspect.

5. **The closing note undercuts its own authority, on purpose.** It tells you the plan is not a
   guarantee unless you saved it. That sentence is why people trust the rest.

## What it does not do

No animation, no progress theatre, no spinner. The whole thing is text that appears when it is
ready. Our brief calls the validation pass "an animated sweep" — this output is the argument for
keeping any animation subordinate to a result that reads correctly when frozen.
