# vim-course

A Neovim course that grades your keystrokes. You make real edits to Java, C, Python and ASCII art, the
course counts every key, and each exercise has a *par*: the key count of a good solution, like a golf hole.

- 11 projects, from the basic grammar (`00_grammar`) to long real-world edits (`10_advanced`)
- 150 exercises and 1,408 short drills, each with a reference solution you can read or watch typed
- A coach that replays your keys and shows shorter ways to make the same edit
- A full-screen pixel-art map in the terminal for moving between projects, levels and drills

## Start

```bash
git clone https://github.com/shdwfruit/vim-course
cd vim-course
python3 play.py
```

On the map: `h` `j` `k` `l` follow the road, `Enter` opens a level, `r` reads the lesson, `q` goes back.

## Needs

- Neovim 0.12 or newer
- Python 3.11 or newer (standard library only, nothing to install)
- macOS or Linux, in a terminal with 256 colors. Only tested on macOS with Neovim 0.12.6.

The course starts Neovim with its own config, so your own setup and plugins don't affect grading.
Your progress is saved in the course folder and is ignored by git.

[ROADMAP.md](ROADMAP.md) has the full guide: every project, every command, and how grading works.

## Licence

GPL v3. See [LICENSE](LICENSE). Copyright (C) 2026 shdwfruit.
