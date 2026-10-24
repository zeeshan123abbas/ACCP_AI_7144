# UTM Link Recipes

UTM parameters are small labels added to a link so Google Analytics knows **where** a visitor came from.

| Parameter | Meaning | Example |
|-----------|---------|---------|
| `utm_source` | The website or app | `facebook`, `instagram`, `whatsapp`, `google` |
| `utm_medium` | The type of channel | `social`, `email`, `organic`, `cpc` |
| `utm_campaign` | Your campaign name | `admissions_oct26` |
| `utm_content` (optional) | Which link/button | `bio_link`, `story_swipe` |

Rules: use lowercase, underscores instead of spaces, and the same spelling every time.

## Ready-made examples

Facebook post:
```
https://www.example.com/courses/web-design?utm_source=facebook&utm_medium=social&utm_campaign=admissions_oct26
```

Instagram bio link:
```
https://www.example.com/?utm_source=instagram&utm_medium=social&utm_campaign=always_on&utm_content=bio_link
```

WhatsApp broadcast:
```
https://www.example.com/free/html-cheat-sheet?utm_source=whatsapp&utm_medium=social&utm_campaign=cheat_sheet
```

Google Business Profile website button:
```
https://www.example.com/?utm_source=google&utm_medium=organic&utm_campaign=gbp
```

## Where to see the results

GA4 → **Reports → Acquisition → Traffic acquisition** → change the dimension to *Session source / medium* or *Session campaign*.

> Never add UTM tags to your own internal links (menu, buttons inside your site). They would reset the visitor's source.

Official builder: <https://ga-dev-tools.google/campaign-url-builder/>
