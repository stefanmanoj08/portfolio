# webweb

Personal portfolio site — product & analytics workflow landing page.

## Run locally

```bash
open index.html
# or
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Structure

| Path | What |
|------|------|
| `index.html` | Landing + Domain / Approach / Selected work |
| `about.html` | About — portrait, work rail, education, talks |
| `index.html#contact` | Contact (final landing section) + link to About |
| `assets/Stefan_Manojlovic_CV.pdf` | Downloadable CV |
| `projects.html` | Full projects list (all 9) |
| `projects/*.html` | Individual case-study pages (STAR+M) |
| `projects/images/` | Drop case images here (see README inside) |
| `archive/` | Earlier iterations (v1–v4) |
| `refs/` | Visual reference frames |
| `portrait.png` | Clay character portrait on About (transparent) |

Drop a `portrait.jpg` next to `index.html` if you want the photo to show. Case images go in `projects/images/` using the filenames shown on each page placeholder.
