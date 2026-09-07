# Agent Setup Interview

> **Standing: ★ practitioner-reported. One person.** Filed 2026-09-07, run against
> [`interview-guide.md`](interview-guide.md). **Everything in this file is ★** under the evidence rule
> in [`research.md`](../research.md), *The three marks*: it is evidence about **this respondent**,
> spoken from memory about their own work, and it is not a fact about anybody else. Every number in
> it — *forty-something files*, *one in three fresh environments*, *about half of it* — is a
> recollection, not a measurement, and the respondent flags his own unreliability twice unprompted
> (*"I usually round that down"*, *"it's a story I tell myself"*).
>
> **This is one of the five the trigger names, not the five.** Q5's disposition, and the
> **provisional** label on stage 6 and stage 7, both lift on **five** conversations filed as a source
> document — five being the smallest number that can refute a primary-persona choice rather than
> merely colour it. **Four still to run**, and §2 of the guide asks that at least two of them be
> people who have never filed an issue in public, and that one be someone who does not keep this
> material at all.
>
> **The respondent is described but not identified**, and the answers are written as spoken and
> lightly cleaned up — so this cannot be re-run by a third party the way a logged query can. That is
> what separates ★ from ✓ and it is not a defect: no instrument in this repository before it could
> reach motive, cost or feeling at all.

Respondent: AI engineer, 4+ years. Mixed client work and own products.
Format: answers written as spoken, lightly cleaned up.

---

## A. Setup census

**1. Which coding agents do you currently have installed? And which one did you actually use yesterday?**

Installed: Claude Code, Cursor, Codex CLI, and Aider, which I haven't opened since maybe October. Continue is technically still in my VS Code extensions but it's dead weight.

Yesterday it was Claude Code, in the terminal, two sessions. One on a client repo doing a boring migration of an old chunking pipeline, one on my own thing where I was trying to get an eval harness to stop flaking. Cursor I open when I want to read code more than write it; the inline stuff is nicer for browsing. But the real work goes through Claude Code because it can run things and see what broke.

**2. When did you last open any of them?**

About forty minutes ago. It's open right now in another tab, sitting on a failed test I've been ignoring.

**3. Is there a file, folder or repo where you keep instructions, rules, prompts or skills for them? Where? Roughly how much is in it?**

Yes. `~/dev/kit/agents/`, which is a private GitHub repo called `agent-kit`. It gets symlinked into `~/.claude/` and a couple of other places.

Contents, roughly: 11 skills, 6 CLAUDE.md templates split by stack, an `mcp/` folder with 9 server configs, a `prompts/` folder that's honestly a separate thing that ended up living here anyway, and a `scripts/` folder with the bootstrap script that does the symlinking. Call it 40-something files. Somewhere around 6k lines total if you count the markdown, and most of that is markdown.

**4. How long has it existed? What was in it at the start?**

Fourteen months, give or take. It started as exactly one file: a CLAUDE.md I wrote for a client project that kept making the agent write raw SQL when the project had a repository layer. I copied that file to the next project, then the next, and at project four I got annoyed and made a repo.

So the origin is not "I designed a system." The origin is "I got tired of copy-pasting one file."

**5. Have you deployed it on more than one machine? What happened?**

Three, if you count containers. Work MacBook, home Linux box on Ubuntu, and devcontainers for two client projects that require an isolated environment.

What happened is it broke on Linux, and it broke in the stupidest possible way: absolute paths. The MCP configs had `/Users/me/...` hardcoded in the `command` and `args` fields because that's what the docs example looked like when I set it up and I never went back. On the Mac everything worked for months so I had no reason to look. Moved to Linux, four MCP servers just silently didn't start, and Claude Code doesn't scream about that, it just doesn't have the tools. I spent the first twenty minutes thinking the model had gotten worse.

---

## B. The last new project

**6. Walk me through the last time you started a new project or repo. What did you do in the first hour?**

Three weeks ago, a small internal tool for a client, document intake with classification on top. First hour, honestly:

Ten minutes of `mkdir`, git init, pushing an empty repo. Then Python env, pinning versions, the usual. Then I wrote the README before any code, which is a habit I picked up because if I can't write the README the scope isn't clear yet. Then about fifteen minutes arguing with myself about whether this needed Postgres or whether SQLite would carry it to the end of the engagement.

Then I wrote a fake input document and a fake expected output, because I wanted the shape of the thing pinned down before anything real existed.

**> And on the agent side?**

Right, that. I copied CLAUDE.md from a previous project of a similar shape, and that took two minutes, and then I spent maybe twenty minutes editing it, which is the part nobody counts. Then I pulled two skills across, one for the eval format and one for the commit convention I use on client repos. Then the MCP config, which I copied wholesale and then trimmed, because half the servers in it were irrelevant to this project and I didn't want the tool list bloated.

So call it thirty-five minutes of the first hour, if I'm being honest about it, and I usually round that down to "ten minutes, it's just a copy" when someone asks.

**7. Did anything carry over from earlier work? What exactly, and how?**

The CLAUDE.md, the two skills, the MCP config. All of it moved by `cp`. Not by git submodule, not by a package, not by the bootstrap script that exists specifically to do this. By `cp -r` from a sibling directory.

The bootstrap script only handles the global `~/.claude/` layer. Per-project stuff I've never automated, and I keep meaning to.

**8. Was there something you wanted to bring over and didn't? What stopped you?**

Yeah, the eval harness from the invoice project. It's the best thing I've built for this category of work and I use maybe a third of what it can do on any given project.

I didn't bring it because it's welded to that project's data model. Extracting it means either doing a proper generalization pass, which is half a day I wasn't going to bill anyone for, or copying it and mutilating it, which is how I ended up with three divergent copies of the chunking module. So I wrote a worse thing from scratch in an hour and told myself I'd fix it later. I did not fix it later.

**9. How long did the whole setup take end to end?**

Between forty minutes and an hour for the agent side alone, spread across the first day. Not one continuous block; it's more like I hit a wall, realize the agent doesn't know something, go add a paragraph to CLAUDE.md, continue. Then again two hours later.

That trickle is the actual cost and it's invisible because no single instance of it feels expensive.

**10. Has anything you copied ever gone stale or diverged from the original? What happened?**

The chunking module, and it cost me real money.

Same code in three projects. I fixed an off-by-one in the overlap logic in one of them, on a Friday, and it never got back to the other two. Six weeks later a client flagged that retrieval was returning fragments cut mid-sentence, which is exactly the bug I'd already fixed elsewhere and had zero memory of. I debugged it for three hours as if it were new before I opened the other repo and saw my own fix sitting there.

Same thing happens to CLAUDE.md, just less visibly. The version in project A says "use pytest fixtures, never module-level setup." Project B's copy predates that rule, so the agent happily writes module-level setup and I don't notice until review, and when I do notice I fix it in B and not in the template, so the next copy is wrong too. It's a loop.

---

## C. The last time it didn't work

**11. Tell me about the last time you moved your setup to another machine, a container, a new laptop, or handed it to someone, and it didn't work. How did you find out? How long to fix?**

The Linux move I mentioned, plus a devcontainer one that was worse.

The devcontainer case: the container had Node 18, one of my MCP servers needs 20+. Server exits immediately on start. The failure mode is that the agent just doesn't have those tools and carries on without them, cheerfully, improvising with bash instead. I found out because it started writing curl commands against an API it should have had a proper tool for, and I sat there for a while thinking it was being weird before I checked the logs.

Detection took the longest, maybe twenty-five minutes of being confused. The fix was two minutes once I knew. That ratio is the whole problem: broken config doesn't announce itself, it degrades quietly.

**12. One-off, or does this happen?**

It happens. Not every time, but I'd say one in three fresh environments has something silently not loading. Paths, versions, a missing env var, an auth token that expired months ago and the server starts but every call 401s.

**13. Has a tool ever done something you didn't ask for, or ignored something you did ask for, and you only found out later?**

Both, repeatedly. The one that stung: a skill of mine had a formatting rule left over from a project that used Prettier with 120-char lines. Carried it into a repo that uses Black at 88. Agent reformatted a big chunk of the codebase as a side effect of a small change, I didn't read the diff carefully because it was "just a small change," and I pushed 1,100 lines of noise into a branch a colleague was reviewing.

The ignoring is more common and less dramatic. CLAUDE.md says don't touch migrations without asking. It touches migrations. Not always, and I've never worked out the pattern. My honest suspicion is that when the file gets long, the middle of it stops mattering, but I've never actually tested that; it's a story I tell myself.

**14. How did you notice? What should have happened instead?**

Noticed in the PR diff, from someone else's comment, which is the worst way. What should have happened: the rule that got applied should have been traceable. I want to be able to ask, after the fact, which instruction produced that behaviour. Right now I can't, so I guess, and my guesses are unfalsifiable.

**15. When it happened, did you already have the collection, or were you setting up one thing?**

Already had the collection, and that's the point. When it was one file I knew what was in it. At forty files with overlapping instructions I have no working model of what's active on a given run. The collection created the problem.

---

## D. The material itself

**16. Is there anything in that folder you're not sure actually does anything?**

Maybe half of it, if you want the real answer.

Specific examples: I have a skill about error handling conventions that I wrote in one sitting nine months ago, and I've never once seen output I could attribute to it. A CLAUDE.md section about preferring composition over inheritance which reads like something I'd say in an interview rather than something that changes behaviour. Two MCP servers in the config that I'm fairly sure haven't been called this year.

**17. How would you know whether it works? Have you ever checked?**

Properly, no. I've never A/B'd anything.

What I could do is obvious in principle: same task, same repo state, run it with the file and without, compare. It's not hard. I've never done it because each individual file feels too small to justify the ceremony, and it's forty small things, so the total never gets audited.

The closest I've come was accidental. I once had a run where the config didn't load, and the output was noticeably worse in a way I could point at, which told me *something* in there works. It didn't tell me which part.

**18. Is there anything in there you'd delete, honestly?**

The Aider config, gone, I don't use it. The composition-over-inheritance paragraph. Probably three of the eleven skills, and I could name two of them right now.

What stops me isn't sentiment, it's that deleting feels riskier than keeping. If I remove something and quality drops, I won't connect the two events; the feedback is too slow and too noisy. So the folder only grows, which is a bad property for a thing whose job is to be precise.

**19. When you go into that folder, what are you usually about to do?**

Three modes, in descending frequency. Most often I'm copying something out of it into a new project. Second, I'm adding a rule right after the agent did something annoying, which means most edits are written while irritated, which is probably visible in the tone of some of them. Third, and rarest, I'm looking for something I know I wrote and can't find; that's usually a prompt, and it usually takes longer than rewriting it would.

I basically never go in there to read or review. There's no reason to, nothing prompts it, so it doesn't happen.

**20. If you were picking something of your own to reuse and couldn't remember which parts were good, what would help you decide?**

Usage data, first. Just: this file was loaded in 40 sessions, this one in 2, this one never. That alone would let me delete half of it with confidence.

After that, some record of when a rule got applied and what it changed. Not full traces, I don't want to read logs. Something more like: here's where this instruction actually affected output.

And a date. Not created-date, last-actually-useful date. If a skill hasn't influenced anything in four months it's either dead or it's a rule I've internalized and no longer need written down. Either way I want to know.

---

## E. Other people

**21. Has anyone else ever opened or run your setup? Who, and how did it go?**

Once, properly. A contractor I brought onto a project last winter. I gave him the repo including the agent config, and he got roughly the same experience as my Linux move: paths broken, one server not starting, and he assumed that was normal and worked around it for two days without mentioning it. I found out during a call when he described a workflow that made no sense unless he was missing half his tools.

That was the moment I understood the config had become tribal knowledge rather than a setup.

**22. Have you ever given this material to someone, a colleague, a friend, publicly? What did you have to explain?**

Twice, both informally, both to people I know.

What I had to explain: which files are load-bearing and which are aspirational. Which rules are real constraints from the client versus my personal taste. Why there are two CLAUDE.md templates that look almost identical, where the difference is a single paragraph and the reason is a project from a year ago that no longer exists.

None of that is written down anywhere, so the explanation is me, on a call, for twenty minutes.

**23. Is any of it public? Would you want it to be?**

None of it. I'd like a slice of it public, mostly for the reason that publishing forces cleanup and I need external pressure to do that. But I can't publish as-is because client-specific rules are scattered through it, some naming conventions I shouldn't share, one file that has an internal API shape in an example. Separating that is a couple of hours of careful work and it's never the most urgent couple of hours.

**24. Have you ever filed an issue or written publicly about any of this?**

One issue, about MCP config path handling, which is the thing that burned me on Linux. Got a reasonable answer, not much came of it.

Written about it, no. I've drafted a post twice about how these config folders rot and deleted it both times because it felt like complaining without a solution.

---

## F. Closing

**25. If a genie fixed exactly one thing tomorrow, what would you assign it?**

Show me what actually loaded and what actually mattered. Per session: these files were read, this rule fired here, these six things were present and had no observable effect. That's it. I don't need it to fix anything, I need to see it, because everything else I'd fix myself in an afternoon if I could see it.

**> Have you ever gone looking for something that does that?**

Yeah, twice, both times right after being burned.

**> Did you find anything? Did you keep using it?**

Sort of and no. There are session viewers and log tools, and they tell you what happened in the conversation, which isn't the same question. I want to know which of *my* files was responsible, and nothing I found connects a behaviour back to a config line. I used one for about a week, mostly to look at token counts, then stopped, and I couldn't tell you the exact day I stopped.

**26. Anything I should have asked and didn't?**

Two things.

You didn't ask what happens when a rule and a client requirement conflict. That comes up constantly. My CLAUDE.md says one thing, the client's linter says another, and there's no precedence anywhere; it's resolved by whichever I remember at the time, which is a bad way to resolve anything.

And you didn't ask about the boundary between what lives in these files and what lives in my head. Roughly half of what makes a project go well is stuff I've never written down because writing it down felt too obvious. Then a contractor joins and none of it transfers. If you're studying why these setups fail, "the written part was never the whole thing" is probably a bigger factor than anything about the files themselves.
