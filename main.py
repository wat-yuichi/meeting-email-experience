from pathlib import Path


joke = "I listed 'survived meetings that could've been emails' on my résumé; HR counted it as five years' experience."
Path("/output/entry.txt").write_text(joke, encoding="utf-8")
