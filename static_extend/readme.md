# static_extend
Web pages, served at `/static/<name>` and opened at `/page/<app>`: one file `<app>.html` or a folder `<app>/index.html` with its assets linked absolutely (`/static/<app>/js/app.js`). Lowercase names keep URLs clean; state such as a tab goes in the query (`/page/<app>?tab=x`). See AGENTS.md (Where code goes).
