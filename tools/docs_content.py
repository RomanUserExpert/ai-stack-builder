"""Phase 09, step 2: what the docs say about each component, beside the specimens build_kit cuts from the screens.

Read by tools/build_docs.py. One entry per component of build_kit.components(), by its name. Each holds:

- files  the file in components/ that holds it, where its class names do not find it (build_docs.files_for)
- anat   which of the component's states the anatomy is drawn on (index into its states; 0 by default)
- parts  (selector, part, what it is) — the selector is looked up inside the live specimen; build_docs fails the build
         if one matches nothing, so a part named here is a part the code has
- size   its measure, from DESIGN.md (omitted where there is one size and nothing to say)
- when   the role it plays in the product, from DESIGN.md, inventory.md and the words microcopy.md gives it
- rule   where it is right
- anti   when to take another component, and which: (sentence, the other component's name)

Sources, so a sentence here can be traced: DESIGN.md *Components*, 07-ui-assembly/ui/inventory.md, CLAUDE.md §5–§8 and
the register (Q-numbers). Nothing here is a new decision; where a sentence states a rule, the rule is already signed.
"""

C = {}

# ------------------------------------------------------------------ Navigation
C["App header"] = dict(
    anat=0,
    parts=[("header.app-header", "Bar", "52 px on Top Bar, a hairline below"),
           ("span.product", "Product mark", "a 14 px lime square and the name: the one lime that is neither an action nor a place"),
           ("nav.app-nav", "Places", "My library · Public library · Projects, as text"),
           ('nav.app-nav [aria-current="page"]', "Current place", "a Raised tile with the tile shadow, in Ink"),
           ("p.account", "Account", "the signed-in person's 24 px portrait, the product's only image")],
    size="52 px high; a place is Button type, 32 px high.",
    when="The frame of every place the owner has: My library, Public library, Projects, a project and its configuring "
         "mode. It says where you are and reaches the other two places in one click (Q29). It carries three places and no "
         "more, because there are three.",
    rule="One per owner screen, the current place marked with aria-current. The places carry no icons and no counts.",
    anti=("A screen the owner does not own — the door, or anything opened from a link — takes the Shared header. A mode "
          "takes the Run bar: Run has no entry here, because it is not a place.", "Shared header"),
)
C["Shared header"] = dict(
    anat=1,
    parts=[("header.shared-header", "Bar", "the same 52 px bar as the App header"),
           ("span.product", "Product mark", "the mark and the name, with no places"),
           (".owner", "Shared by", "the sharer's name and portrait, on the receiver's surfaces only")],
    when="The frame of every surface somebody reaches without owning anything here. At the door (Sign in, Create account, "
         "Reset password) it is the mark alone. On Shared project, Shared item and their Run it says who shared it. It has "
         "no account, because the receiver has none (Q13, Q25).",
    rule="Door: the mark only. Receiver: the mark and Shared by, with the sharer's portrait.",
    anti=("An owner's place takes the App header. A sign-in link never goes into this bar: the receiver meets the door only "
          "by choosing to copy something into a library of their own (§9).", "App header"),
)
C["Run bar"] = dict(
    parts=[("header.run-bar", "Bar", "52 px on Top Bar, like the other two"),
           ("a.back", "Back", "to the place Run was entered from"),
           ("span.title", "Title", "Export, the mode's name"),
           ("label.pick", "Agent target", "a select; it chooses the paths and the reader of SETUP.md")],
    size="52 px high.",
    when="The bar of the Export mode, which takes the whole surface. Run is a mode, not a place — nothing is stored and no "
         "address returns to it — so its bar has a way back instead of places, and the agent target, because the target "
         "changes every path in the archive.",
    rule="The same in every Run state: checking, checked, exporting, exported, failed. On the receiver's Run it sits under "
         "the Shared header (Q39).",
    anti=("Never the App header with Run highlighted: an entry pointing at a mode would promise a place nobody can be "
          "sent to (§8).", "App header"),
)
C["Breadcrumb"] = dict(
    parts=[("p.meta", "Trail", "Small, Ink 3"),
           ("p.meta a", "Link up", "Projects, the one step above")],
    when="Above a project's name on Project, Configuring and Detached row: the one step back to Projects.",
    rule="One level. The project is the only place that sits inside another.",
    anti=("Not on the three places themselves: the App header already marks where you are.", "App header"),
)
C["Page head"] = dict(
    parts=[("div.page-head", "Head", "the title block, then the actions, on one line"),
           ("div.page-head h1", "Title", "Display, the one per screen"),
           ("p.head-meta", "Head meta", "Small Ink 2, facts split by dots"),
           ("div.head-actions", "Actions", "at the right, the primary last"),
           ("div.head-actions .button-primary", "Primary", "lime; one per screen, and an empty or error state's own outranks it")],
    when="The top of every place and of both shared surfaces: the name, the facts about it, and what you can do to it. "
         "Shared and Example tags follow the title, so a shared project reads as shared wherever it stands (Q37).",
    rule="One shape on every screen: a div with the title and its meta, then div.head-actions. One primary at most.",
    anti=("The configuring mode's Cancel · Export · Save is a mode's foot, drawn as Form actions; and when an empty or error "
          "state carries its own primary, the head's drops to secondary.", "Form actions"),
)
C["Tabs"] = dict(
    parts=[("nav.tabs", "Tabs", "one line; it scrolls rather than wraps"),
           ('nav.tabs [aria-current="page"]', "Current tab", "Raised, at 600"),
           ("span.count", "Count", "Ink 3: how many, before you click")],
    when="Filter a list by kind. Page tabs head the Library, with counts (GitHub's count capsule, C2). Panel tabs head the "
         "library panel — Related · All · the six kinds — and Related is first and the default, because it answers what "
         "belongs here, not what exists.",
    rule="Kind is a typology: a tab filters inside the current scope and never changes whose work it is.",
    anti=("Whose work it is — My library or Public library — is the Scope switch above the tabs, a different kind of "
          "filter.", "Scope switch"),
)
C["Scope switch"] = dict(
    parts=[("nav.scope", "Track", "recessed Deep Well with a hairline edge"),
           ('nav.scope [aria-current="page"]', "Current segment", "lifted out on Control, with the tile shadow")],
    when="In the library panel: My library · Public library. It changes whose work you are looking at and what you may do "
         "with it — the Public library is read-only.",
    rule="Two segments, both always shown. Same rows, same search, same tabs on either side: the two scopes are the same "
         "object seen in two places.",
    anti=("It is not the top bar's places, which sit on no track; and it is not Tabs, which only filter by kind.", "Tabs"),
)
C["Library panel"] = dict(
    parts=[("aside.library-sidebar", "Panel", "440 px, the left of the configuring mode"),
           ("div.panel-head", "Head", "the scope, the search and the tabs"),
           ("nav.scope", "Scope switch", "My library · Public library"),
           ("label.search", "Search", "within the scope and the tab"),
           ("nav.tabs", "Kind tabs", "Related first"),
           ("div.panel-body", "Body", "the rows that can be added"),
           ("label.check", "Add to set", "+ Add, or in this project")],
    size="440 px wide.",
    when="The configuring mode's only corpus surface. It answers what goes into this project; it reads and adds, and "
         "never edits (Q14). A zero result keeps the row that creates, which summons the Item sheet over the project.",
    rule="Only in the configuring mode. It opens on Related, or on All when the project is empty (Q33).",
    anti=("Keeping, editing and deleting items happen in My library and its Item sheet. A panel that could edit would be a "
          "second library.", "Item sheet"),
)

# ------------------------------------------------------------------ Cards and lists
C["Row list"] = dict(
    parts=[("ol.row-list", "Tray", "14 px radius, 8 px padding, 8 px between rows"),
           ("article.row", "Cut-out", "each row's own pressed-in field, with the inward cut-out shadow"),
           ("article.row span.tag", "Kind tag", "beside the name"),
           ("article.row p.description", "Description", "Small Ink 2"),
           ("article.row p.facts", "Facts", "Micro Ink 3, mono for paths and refs"),
           ("article.row div.row-actions", "Actions", "at the right of the row")],
    size="Rows have 12 px vertical padding; the row grid is name · middle column (320) · actions (200).",
    when="Every list of items: Library rows with usage facts, set rows in a project, compact rows in the library panel. "
         "It is the signature component — every item in its own cut-out inside a tray.",
    rule="Hover moves a row half a step towards Raised. Active is a 3 px lime pill at the left and the cut-out on Raised — "
         "never a ring, and no coloured ring for a finding either.",
    anti=("A list of projects is the card grid on Projects, so a project is never mistaken for an item. A short list of "
          "facts with no state is a Plain list.", "Plain list"),
)
C["Item text block"] = dict(
    parts=[("article.row span.tag", "Kind tag", "the kind, a word on a grey pill"),
           ("article.row p.description", "Description", "Small Ink 2, held to 640 px"),
           ("article.row p.facts", "Facts", "defers to · conflicts with · needs ENV · @ ref · licence, in Micro Ink 3")],
    when="How an item introduces itself wherever it is listed: its name and kind, a sentence, then the facts that matter "
         "for a handover. An external item shows its pinned ref and its licence, and a missing licence reads as no "
         "licence stated, never as a blank (§5).",
    rule="Facts, never judgements. A licence is a term of use, drawn as text, never as a badge.",
    anti=("Whether an item is used — used in 3 projects — is the Usage facts line, whose ceiling is stated: it answers is "
          "it used, never is it good (Q22).", "Usage facts"),
)
C["Set row states (§7)"] = dict(
    parts=[("ol.sub-rows", "Sub-rows", "auto-added items, nested under what pulled them in, behind a dashed rule"),
           ("span.tag-state", "State tag", "Auto-added, Detached: the tag's type without its outline"),
           ("ol.sub-rows ol.sub-rows", "Second level", "what an auto-added item pulled in, one level deeper")],
    when="A row inside a project, in each of §7's states: selected, auto-added under its parent, conflicting, missing an "
         "env key, detached with the differing fields named. The set row is the only place an item's state is true, "
         "because the states are properties of membership.",
    rule="An auto-added row has no remove of its own: the nesting carries the refusal. Both items of a declared conflict "
         "read as Conflict, and the Problem annotates the declaring row (Q41).",
    anti=("Library rows and panel rows never show these states: an item outside a project is not auto-added, detached or "
          "conflicting.", "Row list"),
)
C["Kind tag"] = dict(
    parts=[("span.tag", "Tag", "a 20 px pill outlined in Strong Hairline, Micro, Ink 2")],
    size="20 px high, a pill.",
    when="The kind beside a name — skill, agent, prompt, mcp, script, app — and the states Shared, Example, Auto-added and "
         "Detached as the same type without its outline. Conflict is the one coloured tag: rose, on its wash, beside the "
         "name.",
    rule="Kind is a word on a grey pill, never a colour (pair 5: colour is a claim, and kind claims nothing).",
    anti=("A finding a row carries — Problem, Note — is a Finding capsule with its icon, at the row's right edge.",
          "Finding capsule"),
)
C["Usage facts"] = dict(
    parts=[("p.usage", "Usage", "used in N projects · N items require this · last exported …")],
    when="On a Library row: what it costs to touch this item. The same count expands to name the projects, because a "
         "person deciding to delete needs to know which (§5).",
    rule="Usage, never quality. Its ceiling is stated beside it: it answers is it used, never is it any good (Q22).",
    anti=("A score, a rating or a badge has no component here and never will: the product runs nothing, so it has nothing "
          "to grade with (§5). The item's own facts are the Item text block.", "Item text block"),
)
C["Item side panel"] = dict(
    parts=[("aside.drawer", "Panel", "440 px beside the set, sticky"),
           ("div.drawer-head", "Head", "the name, its tags and Close"),
           ("div.drawer-head .close", "Close", "back to the set alone"),
           ("div.callout", "Finding", "a Problem or Note about this item"),
           ("section.drawer-section", "Section", "contents, then facts"),
           ("dl.drawer-facts", "Facts", "a definition list"),
           ("div.drawer-actions", "Actions", "Detach; on a detached item Reset and Promote")],
    size="440 px wide.",
    when="An item opened from a set row, beside the set rather than over it. It is the only place Detach, Reset and Promote "
         "live (Q33), and on a detached item it names the fields that differ from the original.",
    rule="One item at a time; its row carries the lime pill while it is open. Promote is immediate, because it creates a "
         "library item.",
    anti=("Editing the library original is the Item sheet, over My library: the side panel only edits a detached copy, "
          "and only in the configuring mode (Q21).", "Item sheet"),
)
C["Check stages"] = dict(
    parts=[("section.stage-group", "Group", "Findings, Handover — a Label heading over its stages"),
           ("ol.stages > li", "Stage", "a 10 px cut-out, each a disclosure"),
           ("span.n", "Number", "mono, Ink 3"),
           ("span.name", "Name", "body 600"),
           ("span.result", "Result", "its glyph and its word"),
           ("span.time", "Duration", "mono, tabular, right-aligned: evidence that it looked"),
           ("li.is-skipped", "Skipped", "no fill, a dashed Control Edge outline")],
    size="A stage row is number (24) · name (300) · result · time (48).",
    when="Run's stack of checks: each stage with its own verdict, duration and expansion, after Vercel's deployment page "
         "(B1). A finding opens under its stage, across the row, with what can be done about it.",
    rule="A stage with nothing inside is not a disclosure: no chevron and no focus. Skipped is its own neutral mark, never a "
         "green tick it did not earn.",
    anti=("The verdict for the whole run is the Run summary; the archive is made by the Export stage, last.", "Run summary"),
)
C["Run summary"] = dict(
    parts=[("section.summary", "Summary", "the verdict line, Title size"),
           ("section.summary p.meta", "Counts", "problems · notes · skipped")],
    when="The head of Run: when it was checked and what the check found, as counts — Checked just now, 1 problem, 2 notes, "
         "1 skipped. On failure its code is in mono.",
    rule="The word is checked, never works, valid or passing; the counts are the thing you can act on.",
    anti=("A grade — Basic, Good, Great — was considered and refused: one set is checked against itself (§6). Per-stage "
          "results are Check stages.", "Check stages"),
)
C["Export stage"] = dict(
    parts=[("section.export-stage", "Card", "Raised, the last stage"),
           ("section.export-stage span.n", "Number", "mono Ink 3, continuing the stages above"),
           ("div.export-actions", "Actions", "Export and what goes with it"),
           ("div.export-actions .button-primary", "Export", "the primary; amber when it goes ahead despite a Problem")],
    when="The last stage of Run, which makes the archive: ready, ready with a Problem (Export with 1 problem), exporting, "
         "exported with what is inside, failed. Exported gets a lime pill at its left edge; our failure stays neutral.",
    rule="Export is never disabled on a project with content. An unclean set is confirmed in this stage, under the finding "
         "that caused it — never refused (§6).",
    anti=("It is not a button beside the check, and the confirmation is not a Dialog: Export is a stage, read after the "
          "handover it follows (§8).", "Dialog"),
)
C["File block"] = dict(
    files=["code.css"],
    parts=[("pre.file", "File", "Deep Well, Strong Hairline, 10 px, mono; scrolls sideways")],
    when="A file's contents or a path tree: SETUP.md, .env.example, the archive's tree, an item's content. Whatever an "
         "agent or a terminal will read.",
    rule="Mono, because a machine reads it (the Machine Reads Mono Rule). It scrolls rather than wraps.",
    anti=("A list of facts for a person to read is a Plain list.", "Plain list"),
)
C["Plain list"] = dict(
    parts=[("ul.plain-list", "List", "Small, Ink 2"),
           ("ul.plain-list li", "Item", "a dash in Ink 3 that hangs, so a wrapped line returns to the text")],
    when="A short list of facts in prose: what is inside an export, what the receiving machine still needs.",
    rule="Facts, not actions; nothing in it has a state.",
    anti=("Anything with a state, a kind or an action is a row in a Row list.", "Row list"),
)
C["Aside box"] = dict(
    parts=[("aside.aside-box", "Box", "Raised, 14 px, 20 px in"),
           ("aside.aside-box ul.plain-list", "Needs", "what your machine still needs"),
           ("aside.aside-box p.meta", "Live page", "the sentence that says the page is live and the archive a snapshot"),
           ("aside.aside-box .button-primary", "Export", "the receiver's way to take it")],
    when="The receiver's column beside a shared project or item: what their machine still needs, and the way to take the "
         "archive.",
    rule="Only on the receiver's surfaces, and only what is derived from what the owner needs: the shared surfaces get the "
         "most conservative treatment in the product (Q20).",
    anti=("The owner reads the same disclosures in Run's handover stages, before Export.", "Check stages"),
)

# ------------------------------------------------------------------ Forms
C["Button"] = dict(
    parts=[(".button-primary", "Primary", "lime, Lime Ink at 600"),
           ("a.button:not(.button-primary):not(.button-quiet)", "Secondary", "Control fill, Strong Hairline edge, Ink"),
           (".button-quiet", "Quiet", "no fill, no edge, Ink 2"),
           (".button-primary svg.icon", "Icon", "16 px, 8 px from the label")],
    size="32 px high, 12 px side padding, 6 px radius.",
    when="Every action, its variant chosen by what the act claims. Primary: the screen's one act. Secondary: the rest. "
         "Quiet: leaving. Danger: only the confirmation of a removal. Warning: only Export with 1 problem. Disabled: only "
         "Export on an empty project, and it still takes focus and points at its reason (Q16).",
    rule="One primary per screen, settled by the build, ranked: an open dialog's, a failure box's, an empty or error "
         "state's, the page head's, the item panel's, the Export stage's.",
    anti=("A small action in a line of text is a Link button. A removal outside its confirmation is quiet danger — rose "
          "text and edge — never the red fill.", "Link button"),
)
C["Link button"] = dict(
    parts=[("button.link-button", "Link button", "underlined Ink 2 text")],
    when="A small action that sits in a header or a line: Clear filters in the popover, Remove in a file list.",
    rule="It brightens on hover and never becomes a chip.",
    anti=("An action that moves the screen on is a Button.", "Button"),
)
C["Search field"] = dict(
    parts=[("label.search", "Field", "Deep Well, Control Edge, 6 px"),
           ("label.search svg.icon", "Icon", "search, in Ink 3"),
           ("label.search input", "Input", "its placeholder in Ink 3")],
    size="32 px high.",
    when="Filter a list by name: My library, Public library, Projects, the library panel. A zero result says what matched "
         "nothing, and in the panel it keeps the row that creates.",
    rule="It filters within the current scope and tab. On focus the edge goes lime and the ring shows.",
    anti=("Filtering by a property — last check, target, sharing — is the Filters popover.", "Filters button and popover"),
)
C["Filters button and popover"] = dict(
    parts=[("form.find", "Find", "the search and the button, together"),
           ("label.search", "Search", "by name"),
           ("button.filters-button", "Filters", "one button, carrying the count of filters on")],
    size="The popover is 360 px wide.",
    when="Projects and the Library: one Filters button hangs a popover with groups under Label legends, checkboxes or "
         "radios, Clear and apply (Q30).",
    rule="One button, never a row of chips. The popover takes the dialog's sheet and acrylic edge.",
    anti=("Filtering by kind is Tabs; by name, the Search field.", "Tabs"),
)
C["Text field"] = dict(
    parts=[("label.field", "Field", "a label over an input"),
           ("label.field input", "Input", "Deep Well, Control Edge; mono when it holds a path, a name or a key")],
    size="32 px high; the label is Micro 600 Ink 2.",
    when="A short value with its label: the door's email and password, an item's name and target path, a detached field.",
    rule="No per-field error: an error arrives as a failure box over the form. A path, a name or a key is set in mono.",
    anti=("Long content is a Textarea; a choice among fixed values is a Select.", "Textarea"),
)
C["Select"] = dict(
    files=["select.css"],
    parts=[("label.pick", "Field", "its label beside or above"),
           ("label.pick select", "Select", "a secondary button's shape with a Control Edge")],
    when="A choice among fixed values: the agent target in Run, an item's kind in the Item sheet.",
    rule="Only for values the product defines. Changing the agent target voids the last check, because a path collision "
         "is a collision under a target (§6).",
    anti=("Two values the person switches between all the time are a Scope switch.", "Scope switch"),
)
C["Textarea"] = dict(
    parts=[("label.field", "Field", "a label over the area"),
           ("label.field textarea", "Textarea", "mono, Deep Well, Control Edge")],
    when="An item's content in the Item sheet, and a detached item's content in the side panel.",
    rule="Mono: it holds what an agent will read. Its words are the person's content, not the product's.",
    anti=("A one-line value is a Text field.", "Text field"),
)
C["Add to set"] = dict(
    parts=[("label.check", "Add", "+ Add; once added, in this project with a lime-mark tick, unfilled")],
    when="On a panel row: put the item into the project, or see that it is in. The native checkbox stays underneath for "
         "the keyboard and screen readers.",
    rule="An auto-added row refuses: its tick in Ink 3, no hover, its checkbox disabled, and Required by … beside it — §8's "
         "only refusal, shown rather than only stated.",
    anti=("Taking an item out is the set row's own control, Remove from set: membership is shown in the panel and owned by "
          "the row.", "Remove from set"),
)
C["Checkbox"] = dict(
    files=["checkbox.css"],
    parts=[("fieldset.popover-group", "Group", "a Label legend over its options"),
           ('input[type="checkbox"]', "Checkbox", "a 16 px Deep Well cell with a Control Edge; checked, lime with a dark tick")],
    size="16 px.",
    when="Independent filters in the Filters popover: any number at once.",
    rule="Drawn for the dark theme, never the browser's white box. In light, a checked box is Deep Lime with a white tick.",
    anti=("One choice among several is a Radio.", "Radio"),
)
C["Radio"] = dict(
    files=["checkbox.css"],
    parts=[("fieldset.popover-group", "Group", "a Label legend over its options"),
           ('input[type="radio"]', "Radio", "a 16 px Deep Well cell; selected, a lime ring with a lime dot")],
    size="16 px.",
    when="One value among several in the Filters popover: the order, one target.",
    rule="Drawn for the dark theme, never the browser's white circle.",
    anti=("Several at once are Checkboxes.", "Checkbox"),
)
C["Remove from set"] = dict(
    parts=[("button.remove", "Remove", "a 32 px square ✕, quiet on a row; its label names the item")],
    size="32 px square.",
    when="In the configuring mode, on a set row: take this item out of this project. Its accessible name is the act in "
         "full: Remove code-style from this project.",
    rule="Absent on an auto-added row — that is the refusal. It is a draft act, kept on Save and dropped on Cancel.",
    anti=("Deleting an item from the library is Delete in the Item sheet, confirmed with its blast radius; removing a "
          "Problem's item from Run is the quiet danger button in the Finding box.", "Finding box"),
)
C["Close"] = dict(
    files=["drawer.css"],
    parts=[("a.close", "Close", "a 32 px square ✕, secondary on a panel")],
    size="32 px square.",
    when="Close a panel or a sheet: the item side panel, the Item sheet, the import dialog.",
    rule="It closes what it sits on, and nothing else is lost by it.",
    anti=("Leaving a draft with its changes dropped is Cancel, in Form actions.", "Form actions"),
)
C["Form actions"] = dict(
    parts=[("div.form-actions", "Row", "a hairline above"),
           ("div.form-actions .push", "Push", "everything from here goes to the right"),
           ("div.form-actions .button-primary", "Primary", "last, at the right")],
    when="The foot of a form, a sheet or a dialog, and the configuring mode's head: Cancel … the primary pushed right.",
    rule="Cancel first, the primary last; one primary.",
    anti=("The top of a place, with its title, is the Page head.", "Page head"),
)
C["Door form"] = dict(
    parts=[("section.door", "Column", "one 400 px column, centred"),
           ("section.door p.head-meta", "Lead", "the product's one line"),
           ("form.form", "Form", "fields and the one primary"),
           ("label.field", "Field", "a Text field"),
           ("section.door .button-primary", "Primary", "Sign in, Create account, Send the link"),
           ("p.door-alt", "The other door", "under a hairline")],
    size="400 px wide.",
    when="Sign in, Create account, Reset password: the way in, built to the minimum the decision forces (Q25).",
    rule="Only what the door needs. Coming back after a session ends returns you to where you were, not into the act.",
    anti=("A profile, a settings screen or a session list is not built (§9): there is no component for it.", "Text field"),
)

# ------------------------------------------------------------------ Feedback
C["Finding box"] = dict(
    parts=[("div.callout", "Box", "rose at 10 % over the cut-out, a rose edge, 10 px"),
           ("div.callout span.severity", "Severity", "the word, bold, in its tone"),
           ("div.callout .button-danger-quiet", "Way out", "quiet danger: rose text and edge, washed on hover")],
    when="A finding with its sentence and what can be done: a Problem (the archive will be wrong) or a Note (correct but "
         "incomplete). The same shape, neutral, carries our failure (Our server didn't answer) and the keys reminder — "
         "neither is a finding, so neither wears rose.",
    rule="The sentence names the consequence in the present tense, in the reader's terms, before the step.",
    anti=("On a row the finding is a Finding capsule; the sentence itself is only ever in this box.", "Finding capsule"),
)
C["Finding capsule"] = dict(
    parts=[("p.marks", "Marks", "at the row's right edge"),
           ("span.mark-problem", "Problem", "circle-alert and the word, on the rose wash"),
           ("span.mark-note", "Note", "info and the word, on the amber wash")],
    size="24 px high, a pill.",
    when="The findings a set row owns, so the list shows where the Problems are before anything is opened.",
    rule="A wash, a coloured word and its icon, with no edge. A finding never draws a ring round the row.",
    anti=("The sentence and the actions belong to the Finding box; Conflict beside the name is a Kind tag in rose.",
          "Finding box"),
)
C["Severity glyph"] = dict(
    parts=[("svg.glyph-problem", "Problem", "circle-alert, rose"),
           ("svg.glyph-note", "Note", "info, amber"),
           (".glyph-checked", "Checked", "a 6 px neutral dot — never a green tick"),
           ("svg.glyph-skipped", "Skipped", "ban, Ink 3"),
           (".glyph-waiting", "Waiting", "an empty ring in Control Edge"),
           (".glyph-running", "Running", "a spinner with a lime head"),
           ("svg.glyph-stopped", "Stopped", "cloud-off, Ink 2: our server broke mid-stage")],
    when="The mark beside a result: in a stage, in a capsule, in the Run summary.",
    rule="Always beside its word; the colour is held to Problem and Note. There is no success colour anywhere (the No "
         "Success Rule).",
    anti=("A glyph alone is not a verdict: on a row the mark is a Finding capsule, which carries the word.",
          "Finding capsule"),
)
C["Empty and error state"] = dict(
    parts=[("section.state-block", "Block", "on a Tray, centred"),
           ("svg.state-icon", "Tile", "a 48 px Control tile, one icon by state: layers, search-x, cloud-off, unlink"),
           ("section.state-block h2", "Title", "Title size: what is here, or what happened"),
           ("div.state-actions", "Actions", "its own primary outranks the page head's")],
    when="A place with nothing in it, a search that matched nothing, a place our server did not load, a link that opens "
         "nothing any more. It is one element on every screen.",
    rule="Not lime and not a wash: the sentence carries what happened, and an error code is mono Ink 3.",
    anti=("Something still loading is a Skeleton; a failure inside a working screen is the neutral Finding box.",
          "Skeleton"),
)
C["Skeleton"] = dict(
    parts=[("span.skeleton", "Bar", "4 px radius, the shape of the text that will arrive")],
    when="A place loading: bars in the shape of what will arrive, so nothing jumps when it does.",
    rule="Shimmers Raised → Control Hover → Raised, and stands still under reduced motion. Its widths are on the 4 px scale.",
    anti=("An act in progress — exporting, signing in, importing — is the Busy indicator, with a word.", "Busy indicator"),
)
C["Busy indicator"] = dict(
    anat=1,
    parts=[('[aria-busy="true"]', "Busy region", "the count, announced as busy"),
           ("progress", "Progress", "a native bar, lime-mark on Control, under the count it repeats")],
    when="An act under way: exporting, signing in, importing a library — the last with a native progress bar under the "
         "count it repeats.",
    rule="The words say what the spinner shows, so it holds when the motion is off.",
    anti=("Content that has not arrived yet is a Skeleton.", "Skeleton"),
)
C["Dialog"] = dict(
    parts=[("div.scrim", "Veil", "dims the place behind, at .58"),
           ("dialog.modal", "Sheet", "520 px, Raised, opaque, an 8 px acrylic edge and the sheet shadow"),
           ("div.sheet-head", "Head", "the question, naming the thing"),
           ("dialog.modal p.meta", "Consequence", "what happens, in the present tense"),
           ("dialog.modal div.form-actions", "Actions", "Cancel … the act; red only when it removes")],
    size="520 px wide; a field inside sits 16 px below the title.",
    when="Before a step that cannot be walked back, or one that publishes: delete, remove, stop sharing (destructive), "
         "share (a disclosure), promote (neutral), import with its progress, failure and result.",
    rule="It names the consequence — which projects, what becomes visible — and never asks Are you sure?",
    anti=("An unclean export is confirmed in the Export stage, under the finding that caused it, not in a dialog.",
          "Export stage"),
)

# ------------------------------------------------------------------ One-off, styled in the kit
C["Item sheet"] = dict(
    parts=[("dialog.sheet", "Sheet", "640 px, the viewport's height, Raised, over a veil"),
           ("dialog.sheet div.sheet-head", "Head", "the item's name and Close"),
           (".callout-reminder", "Keys reminder", "a reminder, worded as one: nothing was scanned"),
           ("div.form-section", "Section", "a Label heading over its fields"),
           ("dialog.sheet div.form-actions", "Actions", "Cancel … Save")],
    size="640 px wide.",
    when="Add or edit a library item. It has three doors — a Library row, the Library's add, and the panel's zero-result "
         "row — and carries the keys reminder, the blast radius and defers to.",
    rule="One screen only (the Item overlay); its body scrolls, and a dialog over it brings its own veil.",
    anti=("A detached copy inside a project is edited in the Item side panel, never here.", "Item side panel"),
)
C["Two fields in a row"] = dict(
    parts=[("div.field-row", "Row", "two fields side by side"),
           ("label.field-mono", "Field", "mono, because it holds item names")],
    when="Two short fields that belong together in the Item sheet: Requires · Conflicts with.",
    rule="Only short values; two at most.",
    anti=("Anything long stands alone as a Text field.", "Text field"),
)
C["File list"] = dict(
    parts=[("ul.file-list", "List", "files in rows split by hairlines"),
           ("ul.file-list span.meta", "Size", "Ink 3"),
           ("ul.file-list .link-button", "Remove", "a Link button")],
    when="The files an item is made of, in the Item sheet (Q31, Q32).",
    rule="Names in mono; each file removable on its own.",
    anti=("Bringing files in is the Drop zone, under the list.", "Drop zone"),
)
C["Drop zone"] = dict(
    anat=0,
    parts=[("label.dropzone", "Zone", "Deep Well, a dashed Control Edge"),
           ("label.dropzone span.meta", "Sentence", "Ink 2")],
    when="Bring files or a folder into an item; the small one sits under a file list. Attach a repo is its neighbour, a "
         "secondary button with a link icon.",
    rule="The keys reminder is stated before the material is accepted (§11), not after.",
    anti=("Files already in are the File list.", "File list"),
)
C["Small heading"] = dict(
    files=["heading.css"],
    parts=[("h2.heading-small", "Heading", "Body 600")],
    when="A content title inside a page: Content, Lands at, on the shared item.",
    rule="Inside a page's content only.",
    anti=("A place's own title is the Page head's Display title.", "Page head"),
)
