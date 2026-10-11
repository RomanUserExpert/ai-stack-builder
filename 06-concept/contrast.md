# Contrast — Mica · Lime

**Measured by `tools/contrast.py` on `tokens.css` as written** (phase 06, stage 4). AA is 4.5:1 for text,
3:1 for a control's edge or an icon shown as a state. The outline of a tag is decorative support for its text
(the text itself passes), so its row is informational.

## Dark — the product

| Text | On | Ratio | AA | Where |
|---|---|---:|:---:|---|
| `--text` #F3F4EF | `--tray` #232420 | 14.13 | pass | a row’s name |
| `--text` #F3F4EF | `--cutout` #1E1F1B | 14.99 | pass | a row’s name in its cut-out |
| `--text` #F3F4EF | `--raised` #2A2B27 | 12.89 | pass | panel and dialog text |
| `--text` #F3F4EF | `--ground` #1B1C19 | 15.49 | pass | the project’s name |
| `--text` #F3F4EF | `--bar` #181916 | 15.97 | pass | the current place |
| `--text` #F3F4EF | `--control` #2E302A | 12.08 | pass | a secondary button’s label |
| `--text` #F3F4EF | `--well-deep` #161714 | 16.28 | pass | code |
| `--text` #F3F4EF | `--problem-box` #342A28 | 12.60 | pass | a Problem’s sentence |
| `--text` #F3F4EF | `--note-box` #312E21 | 12.31 | pass | a Note’s sentence |
| `--text-2` #C5C7BE | `--cutout` #1E1F1B | 9.70 | pass | a row’s description |
| `--text-2` #C5C7BE | `--raised` #2A2B27 | 8.34 | pass | panel description |
| `--text-2` #C5C7BE | `--bar` #181916 | 10.33 | pass | a place, not current |
| `--text-2` #C5C7BE | `--ground` #1B1C19 | 10.02 | pass | the project description |
| `--text-3` #A1A49A | `--cutout` #1E1F1B | 6.54 | pass | a row’s path, metadata |
| `--text-3` #A1A49A | `--raised` #2A2B27 | 5.63 | pass | a section label in the panel |
| `--text-3` #A1A49A | `--control` #2E302A | 5.27 | pass | a disabled button’s label |
| `--text-3` #A1A49A | `--ground` #1B1C19 | 6.76 | pass | the breadcrumb |
| `--on-lime` #141A08 | `--lime` #C6EF5A | 13.46 | pass | the primary button |
| `--on-lime` #141A08 | `--lime-hover` #D3F57A | 14.49 | pass | the primary button, hovered |
| `--on-danger` #FFFFFF | `--danger` #D4363F | 4.77 | pass | the remove in a dialog |
| `--on-danger` #FFFFFF | `--danger-hover` #BE2E37 | 5.78 | pass | the remove, hovered |
| `--problem` #FF8F98 | `--cutout` #1E1F1B | 7.60 | pass | a Problem tag on a row |
| `--problem` #FF8F98 | `--raised` #2A2B27 | 6.54 | pass | a Problem in the panel |
| `--problem` #FF8F98 | `--problem-box` #342A28 | 6.39 | pass | the muted remove, and a Problem’s head |
| `--note` #F2C661 | `--cutout` #1E1F1B | 10.28 | pass | a Note tag on a row |
| `--note` #F2C661 | `--note-box` #312E21 | 8.44 | pass | a Note’s head |
| `--checked` #C5C7BE | `--cutout` #1E1F1B | 9.70 | pass | Checked, a stage verdict |
| `--skipped` #A1A49A | `--ground` #1B1C19 | 6.76 | pass | Skipped, a stage verdict |
| `--lime-mark` #C6EF5A | `--bar` #181916 | 13.36 | pass | the current place’s icon (non-text, 3:1) |
| `--lime-mark` #C6EF5A | `--raised` #2A2B27 | 10.79 | pass | the active row’s pill (non-text, 3:1) |
| `--line-strong` #4A4C44 | `--raised` #2A2B27 | 1.63 | — | a tag’s outline (non-text, 3:1) |
| `--text-3` #A1A49A | `--well-deep` #161714 | 7.11 | pass | mockups: a search field’s placeholder |
| `--text-2` #C5C7BE | `--tray` #232420 | 9.14 | pass | mockups: an empty or error state’s sentence |
| `--text` #F3F4EF | `--control` #2E302A | 12.08 | pass | mockups: inline code |
| `--text-3` #A1A49A | `--tray` #232420 | 6.17 | pass | mockups: an error code under a state |
| `--problem` #FF8F98 | `--problem-wash@cutout` #3E2F2C | 5.85 | pass | mockups: the Conflict tag and a Problem tag on a row |
| `--note` #F2C661 | `--note-wash@cutout` #3A3524 | 7.60 | pass | mockups: a Note tag on a row |
| `--problem` #FF8F98 | `--problem-wash@tray` #423331 | 5.51 | pass | mockups: an error state’s icon tile (non-text, 3:1) |
| `--lime-mark` #C6EF5A | `--cutout` #1E1F1B | 12.55 | pass | mockups: the empty state’s illustration (non-text, 3:1) |
| `--control-edge` #7C7F74 | `--raised` #2A2B27 | 3.49 | pass | mockups: a checkbox or radio’s edge in a popover (non-text, 3:1) |
| `--control-edge` #7C7F74 | `--bar` #181916 | 4.33 | pass | mockups: a checkbox or radio’s edge in the sidebar (non-text, 3:1) |
| `--on-lime` #141A08 | `--lime` #C6EF5A | 13.46 | pass | mockups: the tick in a checked checkbox |

## Light — the slice

| Text | On | Ratio | AA | Where |
|---|---|---:|:---:|---|
| `--text` #181A14 | `--tray` #E9EAE2 | 14.48 | pass | a row’s name |
| `--text` #181A14 | `--cutout` #FBFBF8 | 16.93 | pass | a row’s name in its cut-out |
| `--text` #181A14 | `--raised` #FFFFFF | 17.55 | pass | panel and dialog text |
| `--text` #181A14 | `--ground` #F4F5EF | 16.01 | pass | the project’s name |
| `--text` #181A14 | `--bar` #ECEDE6 | 14.89 | pass | the current place |
| `--text` #181A14 | `--control` #FFFFFF | 17.55 | pass | a secondary button’s label |
| `--text` #181A14 | `--well-deep` #F0F1EA | 15.44 | pass | code |
| `--text` #181A14 | `--problem-box` #F6ECEA | 15.13 | pass | a Problem’s sentence |
| `--text` #181A14 | `--note-box` #F1EEE4 | 15.12 | pass | a Note’s sentence |
| `--text-2` #464A40 | `--cutout` #FBFBF8 | 8.75 | pass | a row’s description |
| `--text-2` #464A40 | `--raised` #FFFFFF | 9.08 | pass | panel description |
| `--text-2` #464A40 | `--bar` #ECEDE6 | 7.70 | pass | a place, not current |
| `--text-2` #464A40 | `--ground` #F4F5EF | 8.28 | pass | the project description |
| `--text-3` #5F6358 | `--cutout` #FBFBF8 | 5.94 | pass | a row’s path, metadata |
| `--text-3` #5F6358 | `--raised` #FFFFFF | 6.15 | pass | a section label in the panel |
| `--text-3` #5F6358 | `--control` #FFFFFF | 6.15 | pass | a disabled button’s label |
| `--text-3` #5F6358 | `--ground` #F4F5EF | 5.61 | pass | the breadcrumb |
| `--on-lime` #141A08 | `--lime` #C6EF5A | 13.46 | pass | the primary button |
| `--on-lime` #141A08 | `--lime-hover` #BCE84A | 12.51 | pass | the primary button, hovered |
| `--on-danger` #FFFFFF | `--danger` #D4363F | 4.77 | pass | the remove in a dialog |
| `--on-danger` #FFFFFF | `--danger-hover` #BE2E37 | 5.78 | pass | the remove, hovered |
| `--problem` #B4232E | `--cutout` #FBFBF8 | 6.29 | pass | a Problem tag on a row |
| `--problem` #B4232E | `--raised` #FFFFFF | 6.52 | pass | a Problem in the panel |
| `--problem` #B4232E | `--problem-box` #F6ECEA | 5.62 | pass | the muted remove, and a Problem’s head |
| `--note` #7A5600 | `--cutout` #FBFBF8 | 6.41 | pass | a Note tag on a row |
| `--note` #7A5600 | `--note-box` #F1EEE4 | 5.73 | pass | a Note’s head |
| `--checked` #464A40 | `--cutout` #FBFBF8 | 8.75 | pass | Checked, a stage verdict |
| `--skipped` #5F6358 | `--ground` #F4F5EF | 5.61 | pass | Skipped, a stage verdict |
| `--lime-mark` #55700F | `--bar` #ECEDE6 | 4.80 | pass | the current place’s icon (non-text, 3:1) |
| `--lime-mark` #55700F | `--raised` #FFFFFF | 5.66 | pass | the active row’s pill (non-text, 3:1) |
| `--line-strong` #C3C6BA | `--raised` #FFFFFF | 1.73 | — | a tag’s outline (non-text, 3:1) |
| `--text-3` #5F6358 | `--well-deep` #F0F1EA | 5.41 | pass | mockups: a search field’s placeholder |
| `--text-2` #464A40 | `--tray` #E9EAE2 | 7.49 | pass | mockups: an empty or error state’s sentence |
| `--text` #181A14 | `--control` #FFFFFF | 17.55 | pass | mockups: inline code |
| `--text-3` #5F6358 | `--tray` #E9EAE2 | 5.08 | pass | mockups: an error code under a state |
| `--problem` #B4232E | `--problem-wash@cutout` #F1DDDC | 5.00 | pass | mockups: the Conflict tag and a Problem tag on a row |
| `--note` #7A5600 | `--note-wash@cutout` #EAE6D8 | 5.32 | pass | mockups: a Note tag on a row |
| `--problem` #B4232E | `--problem-wash@tray` #E2CEC9 | 4.32 | pass | mockups: an error state’s icon tile (non-text, 3:1) |
| `--lime-mark` #55700F | `--cutout` #FBFBF8 | 5.46 | pass | mockups: the empty state’s illustration (non-text, 3:1) |
| `--control-edge` #7E8276 | `--raised` #FFFFFF | 3.93 | pass | mockups: a checkbox or radio’s edge in a popover (non-text, 3:1) |
| `--control-edge` #7E8276 | `--bar` #ECEDE6 | 3.34 | pass | mockups: a checkbox or radio’s edge in the sidebar (non-text, 3:1) |
| `--on-lime` #141A08 | `--lime` #C6EF5A | 13.46 | pass | mockups: the tick in a checked checkbox |
