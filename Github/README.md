# Git and GitHub Guide

This guide covers everything you need to get this repository onto your computer, keep it up to date, and open it in VS Code. It assumes you've never used Git or GitHub before.

> **TL;DR:** Install Git, run `git clone https://github.com/pegasora/Speedrun.git`, open the folder in VS Code, and run `git pull` whenever I tell you I've added new stuff.

## Contents

1. [What are Git and GitHub?](#1-what-are-git-and-github)
2. [Vocabulary](#2-vocabulary)
3. [Using GitHub in the browser](#3-using-github-in-the-browser)
4. [Installing Git](#4-installing-git)
5. [Getting this repo onto your computer (cloning)](#5-getting-this-repo-onto-your-computer-cloning)
6. [Opening the repo in VS Code](#6-opening-the-repo-in-vs-code)
7. [Staying up to date (pulling)](#7-staying-up-to-date-pulling)
8. [Where to put your own work](#8-where-to-put-your-own-work)
9. [Bonus: your own repo (commit and push)](#9-bonus-your-own-repo-commit-and-push)
10. [Markdown and READMEs](#10-markdown-and-readmes)
11. [Command cheat sheet](#11-command-cheat-sheet)
12. [Troubleshooting](#12-troubleshooting)
13. [Resources](#13-resources)

---

## 1. What are Git and GitHub?

**Git** is a program on your computer that tracks changes to files over time. Every time someone saves a snapshot (a *commit*), Git remembers exactly what changed, who changed it, and when. You can look back at any point in history, see what changed, and undo mistakes. It's like "Track Changes" in Word, but for a whole folder of files, and much more powerful.

**GitHub** is a website that stores Git repositories online so people can share them. Think of it like Google Drive built for Git projects. Nearly every open-source software project lives on GitHub (or something like it), including OpenCV, ROS 2, and the Python libraries you'll be using.

| | Git | GitHub |
|---|---|---|
| What it is | A program (command-line tool) | A website / online service |
| Where it runs | Your computer | The cloud |
| What it does | Tracks file history | Hosts repos and makes them easy to share |
| Do you need it? | Yes, to clone and pull | Yes, it's where this repo lives |

**How it fits together for you:**

```
   ┌──────────────────────┐
   │   GitHub (online)    │   ← I push new material here
   │  pegasora/Speedrun   │
   └──────────┬───────────┘
              │  git clone (once)
              │  git pull  (whenever there's new stuff)
              ▼
   ┌──────────────────────┐
   │  Your computer       │   ← You read, run code, and work here
   │  ~/Projects/Speedrun │
   └──────────────────────┘
```

For this repo, information flows **one way**: I add material and push it to GitHub, and you **pull** it down. You won't be pushing anything to this repo.

---

## 2. Vocabulary

You'll hear these words a lot. Don't memorize them now. Come back here when one confuses you.

| Term | Meaning |
|---|---|
| **Repository (repo)** | A project folder tracked by Git, including its full history. This whole Speedrun project is one repo. |
| **Clone** | Download a full copy of a repo (with its history) onto your computer. You do this **once**. |
| **Commit** | A saved snapshot of changes, with a message describing what changed. |
| **Pull** | Download new commits from GitHub and update your local copy. You'll do this **often**. |
| **Push** | Upload your commits to GitHub. (You'll do this only in your *own* repos.) |
| **Remote** | The online copy of a repo. By default it's named `origin`. |
| **Branch** | A separate line of development. The main one is called `main`. You'll mostly just stay on `main`. |
| **Working directory** | The actual files in the folder on your computer. |
| **Staging (`git add`)** | Choosing which changes go into your next commit. |
| **Merge conflict** | When Git can't automatically combine two sets of changes to the same lines. See [Troubleshooting](#12-troubleshooting). |
| **Fork** | Your own copy of someone else's repo *on GitHub*. Not needed here. |
| **README** | A file (usually `README.md`) that GitHub shows automatically when you open a folder. |
| **Markdown (`.md`)** | The simple formatting language READMEs are written in. See [section 10](#10-markdown-and-readmes). |

---

## 3. Using GitHub in the browser

You can do a lot without installing anything:

- **Navigate:** Click folders and files. The README for each folder shows below the file list.
- **View files:** PDFs, images, Markdown, and code all display right in the browser. (PowerPoint files download instead.)
- **Download one file:** Open the file, then click the **Download raw file** button (the down-arrow icon at the top right of the file view).
- **Search:** Press `/` to search the repo, or `t` to jump to a file by name.
- **See what changed:** Click the **commits** link (the clock icon near the top of the file list) to see the history of every change I've made.
- **Quick web editor:** Press `.` (period) on any repo page to open it in [github.dev](https://github.dev), a VS Code editor in your browser. Good for reading code; you won't run anything there.

### Creating a GitHub account

You'll want a free account for the [bonus section](#9-bonus-your-own-repo-commit-and-push) and for most of the tools you'll use in the field.

1. Go to [github.com/signup](https://github.com/signup).
2. Pick a professional-ish username. Employers *will* look at your GitHub profile someday.
3. Send me your username.

> **If this repo is private:** I'll need to add you as a collaborator. You'll get an email invite. Accept it, and then the repo will show up for you. Git will ask you to sign in the first time you clone.

---

## 4. Installing Git

Pick your operating system:

### Windows

1. Download **Git for Windows** from [git-scm.com/downloads](https://git-scm.com/downloads).
2. Run the installer. **The default options are fine.** Just keep clicking Next.
   - When it asks for a default editor, you can pick **Visual Studio Code** if you have it installed.
3. This installs **Git Bash**, a terminal for running Git commands. You can also use Git from PowerShell or the VS Code terminal.

### macOS

Open the **Terminal** app and run:

```bash
git --version
```

If Git isn't installed, macOS will pop up a prompt to install the **Command Line Developer Tools**. Click **Install**. (Alternatively, if you use [Homebrew](https://brew.sh/): `brew install git`.)

### Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install git
```

### Check that it worked

Open a **new** terminal window and run:

```bash
git --version
```

You should see something like `git version 2.x.x`. If you get "command not found" or "not recognized," see [Troubleshooting](#12-troubleshooting).

### One-time setup (optional for now)

Git attaches your name and email to commits. You only need this if you start making commits (see [section 9](#9-bonus-your-own-repo-commit-and-push)), but it's easy to do now:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email as your GitHub account.

---

## 5. Getting this repo onto your computer (cloning)

### Step 1: Pick a home for your projects

Make a folder where all your coding projects will live. For example:

| OS | Suggested folder |
|---|---|
| Windows | `C:\Users\<you>\Projects` |
| macOS / Linux | `~/Projects` (which is `/Users/<you>/Projects` or `/home/<you>/Projects`) |

> Avoid putting projects inside OneDrive, iCloud, or Dropbox folders. Sync tools and Git don't always get along.

### Step 2: Open a terminal in that folder

- **Windows:** Open Git Bash (or PowerShell) and run `cd ~/Projects` (Git Bash) or `cd $HOME\Projects` (PowerShell).
- **macOS / Linux:** Open Terminal and run `cd ~/Projects`.

If the folder doesn't exist yet, create it first with `mkdir Projects` from your home folder.

### Step 3: Clone

```bash
git clone https://github.com/pegasora/Speedrun.git
```

This creates a `Speedrun` folder containing everything in the repo. It might take a minute because of the PDFs.

```bash
cd Speedrun
ls        # (or `dir` in PowerShell) — you should see Python, PLCs, README.md, etc.
```

That's it. You now have the whole repo on your computer.

### Alternative: GitHub Desktop

If you'd rather click than type, [GitHub Desktop](https://desktop.github.com/) is a free app that does clone and pull with buttons. Use **File → Clone repository → URL** and paste `https://github.com/pegasora/Speedrun.git`. It's a fine way to start, but I'd encourage you to learn the commands too. You'll need them on the factory floor and on Linux machines.

### Alternative: Download ZIP (not recommended)

The green **Code → Download ZIP** button works, but you'd get a frozen copy with no way to update it. You'd have to re-download every time I add something. Cloning is better.

---

## 6. Opening the repo in VS Code

If you haven't installed VS Code yet, see the [VS Code section of the Python README](../Python/README.md#vscode-ide).

### Open the folder

**Option A: from VS Code**

1. Open VS Code.
2. **File → Open Folder…** (on macOS: **File → Open…**).
3. Select the `Speedrun` folder you cloned and click **Open**.
4. If VS Code asks *"Do you trust the authors of the files in this folder?"*, click **Yes, I trust the authors**.

**Option B: from the terminal**

```bash
cd ~/Projects/Speedrun
code .
```

The `.` means "this folder."

> **macOS:** If `code` isn't found, open VS Code, press `Cmd+Shift+P`, type **Shell Command: Install 'code' command in PATH**, and press Enter. Then open a new terminal.
> **Windows:** The installer adds `code` automatically if you leave "Add to PATH" checked.

### Getting around in VS Code

| What | Where / shortcut |
|---|---|
| **Explorer** (file tree) | Left sidebar, top icon, or `Ctrl+Shift+E` / `Cmd+Shift+E` |
| **Preview a README** nicely formatted | Open the `.md` file, then `Ctrl+Shift+V` / `Cmd+Shift+V` (or right-click the tab → **Open Preview**) |
| **Side-by-side preview** | `Ctrl+K V` / `Cmd+K V` |
| **Built-in terminal** | **Terminal → New Terminal**, or `` Ctrl+` `` |
| **Command Palette** (search every command) | `Ctrl+Shift+P` / `Cmd+Shift+P` |
| **Quick open a file** by name | `Ctrl+P` / `Cmd+P` |
| **Source Control** (Git) panel | Left sidebar, branch icon, or `Ctrl+Shift+G` / `Cmd+Shift+G` |

Links in the README preview work too, so you can click around the repo the same way you would on GitHub.

### Git inside VS Code

VS Code has Git built in, so you don't have to leave the editor:

- The **bottom-left corner** of the window shows your current branch (`main`) and a **sync** button (circular arrows). Clicking it pulls new changes.
- The **Source Control** panel shows any files you've changed, plus a **…** menu with **Pull**, **Push**, **Commit**, and more.

More detail: [Source Control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).

---

## 7. Staying up to date (pulling)

I'll keep adding material, like new assignments, notes, and sections. To get the latest version:

```bash
cd ~/Projects/Speedrun
git pull
```

Or in VS Code, click the **sync** button in the bottom-left corner, or **Source Control → … → Pull**.

### What you'll see

| Output | Meaning |
|---|---|
| `Already up to date.` | Nothing new. You have the latest. |
| A list of files with `+++` / `---` and `Fast-forward` | New material came down. Check the READMEs for what's new. |
| `error: Your local changes … would be overwritten` | You edited a file I also changed. See [Troubleshooting](#12-troubleshooting). |

### Good habits

- **Pull at the start of each work session.**
- Run `git status` any time you're unsure what's going on. It tells you if you've changed anything and whether you're behind.
- To see what I've added recently:
  ```bash
  git log --oneline -10
  ```

---

## 8. Where to put your own work

**Don't edit files inside the Speedrun folder.** If you edit a file and I later change the same file, `git pull` will complain (see [Troubleshooting](#12-troubleshooting)). Treat this repo as **read-only reference material**.

Instead, keep your own exercises, assignment solutions, and experiments in a **separate folder**:

```
~/Projects/
├── Speedrun/          ← this repo (read-only; just pull)
└── my-internship/     ← YOUR work
    ├── python-crash-course/
    ├── machine-vision/
    └── plc-notes/
```

If you want to run or modify something from Speedrun, **copy it** into your own folder first.

Even better: make `my-internship` its own Git repo. See the next section.

---

## 9. Bonus: your own repo (commit and push)

You won't push to Speedrun, but you **should** put your own work in a Git repo. It backs up your code, shows your progress, and gives you real practice with Git. Here's the whole workflow.

### The basic loop

```
 edit files  →  git add  →  git commit  →  git push
  (work)       (stage)     (snapshot)     (upload to GitHub)
```

### Step 1: Create the repo on GitHub

1. Sign in at [github.com](https://github.com/).
2. Click the **+** in the top right → **New repository**.
3. Name it (e.g., `my-internship`), choose **Private** or **Public**, and check **Add a README file**.
4. Click **Create repository**.

### Step 2: Clone it

On the new repo's page, click the green **Code** button and copy the HTTPS URL. Then:

```bash
cd ~/Projects
git clone https://github.com/<your-username>/my-internship.git
cd my-internship
```

### Step 3: Make changes and commit

Add or edit some files, then:

```bash
git status                      # see what changed
git add .                       # stage everything that changed
git commit -m "Add chapter 2 exercises"
```

Write commit messages that say *what* you did: `Add webcam capture script` beats `stuff` or `update`.

### Step 4: Push

```bash
git push
```

The first time, Git will ask you to sign in to GitHub. A browser window usually opens to handle it. (Git for Windows and GitHub Desktop include a credential manager that remembers you after that. On macOS/Linux, the [GitHub CLI](https://cli.github.com/) makes this easy: run `gh auth login` once.)

Refresh the repo page on GitHub, and your changes are there.

### Doing it in VS Code instead

1. Open the **Source Control** panel (`Ctrl+Shift+G` / `Cmd+Shift+G`).
2. Click **+** next to the files you want to stage (or **+** on "Changes" to stage everything).
3. Type a message in the box at the top and click **Commit**.
4. Click **Sync Changes** (or **… → Push**).

### Ignoring files with `.gitignore`

Some files shouldn't go into Git: virtual environments, caches, big datasets, and secrets. List them in a file named `.gitignore` at the root of your repo:

```gitignore
.venv/
__pycache__/
.DS_Store
*.pyc
```

GitHub keeps a collection of [ready-made `.gitignore` templates](https://github.com/github/gitignore), including a good [Python one](https://github.com/github/gitignore/blob/main/Python.gitignore).

> ⚠️ **Never commit passwords, API keys, or other secrets.** Once something is pushed, assume it's public forever, even if you delete it later.

---

## 10. Markdown and READMEs

Every README in this repo is written in **Markdown**, a simple way to format text with plain characters. It's worth learning because you'll use it for your own notes, READMEs, GitHub issues, and more.

| You type | You get |
|---|---|
| `# Heading` | A big heading |
| `## Smaller heading` | A smaller heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `` `code` `` | `code` |
| `- item` | A bullet point |
| `1. item` | A numbered list |
| `[text](https://example.com)` | A [link](https://example.com) |
| `![alt text](image.png)` | An image |
| `> quote` | A quote block |

For a block of code, put three backticks on the line before and after it, plus the language name for syntax highlighting:

````markdown
```python
print("hello")
```
````

Full reference: [GitHub's Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

---

## 11. Command cheat sheet

### For this repo (what you'll actually use)

| Command | What it does |
|---|---|
| `git clone <url>` | Download a repo (once) |
| `git pull` | Get the latest changes |
| `git status` | Show what's changed and whether you're up to date |
| `git log --oneline` | Show the commit history, one line each (press `q` to exit) |

### For your own repos

| Command | What it does |
|---|---|
| `git init` | Turn the current folder into a new Git repo |
| `git add <file>` / `git add .` | Stage one file / everything |
| `git commit -m "message"` | Save a snapshot with a message |
| `git push` | Upload your commits to GitHub |
| `git diff` | Show unstaged changes, line by line |
| `git restore <file>` | ⚠️ Throw away your changes to a file (can't be undone) |
| `git branch` | List branches |
| `git switch -c <name>` | Create and switch to a new branch |
| `git switch main` | Go back to `main` |

### Useful terminal basics

| Command | What it does |
|---|---|
| `pwd` | Print which folder you're in |
| `ls` (`dir` on Windows CMD) | List files in the current folder |
| `cd <folder>` | Move into a folder |
| `cd ..` | Move up one folder |
| `mkdir <name>` | Make a new folder |
| `code .` | Open the current folder in VS Code |

GitHub also has a printable [Git cheat sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf).

---

## 12. Troubleshooting

### `git: command not found` / `'git' is not recognized`

Git isn't installed, or your terminal was open before you installed it. **Close and reopen the terminal** (or VS Code). If that doesn't fix it, reinstall Git ([section 4](#4-installing-git)).

### `fatal: not a git repository`

You're not inside the repo folder. `cd` into it first:

```bash
cd ~/Projects/Speedrun
```

### `error: Your local changes to the following files would be overwritten by merge`

You edited a file that I also updated. Pick one:

- **Keep your edits somewhere else, then pull** (safe):
  ```bash
  git stash        # set your changes aside
  git pull         # get my updates
  git stash pop    # bring your changes back (may cause a conflict)
  ```
- **Throw away your edits and pull** (⚠️ loses your changes to those files):
  ```bash
  git restore .
  git pull
  ```

To avoid this entirely, keep your work outside the Speedrun folder ([section 8](#8-where-to-put-your-own-work)).

### `CONFLICT (content): Merge conflict in <file>`

Git couldn't combine two sets of changes. Open the file in VS Code. It highlights the conflicting sections and gives you buttons: **Accept Current Change**, **Accept Incoming Change**, or **Accept Both Changes**. Pick one, save, then:

```bash
git add <file>
git commit
```

If you're unsure, stop and ask me. Nothing is lost.

### Authentication failed / asked for a password

GitHub doesn't accept your account password on the command line anymore. Use one of these:

- Let the **Git Credential Manager** browser sign-in handle it (comes with Git for Windows).
- Install the [GitHub CLI](https://cli.github.com/) and run `gh auth login`.
- Use [GitHub Desktop](https://desktop.github.com/).

### `Repository not found` when cloning

Either the URL has a typo, or the repo is private and you haven't accepted the collaborator invite yet. Check your email, then try again.

### I messed something up and want a fresh copy

Since you're not making changes to Speedrun, you can always just delete the `Speedrun` folder and clone it again. (Make sure none of *your* work is in there first.)

---

## 13. Resources

| Resource | What it is |
|---|---|
| [GitHub Docs: Get started](https://docs.github.com/en/get-started) | GitHub's official beginner docs |
| [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) | 10-minute walkthrough of repos, branches, and commits |
| [GitHub Skills](https://skills.github.com/) | Free interactive courses that run right in GitHub |
| [Learn Git Branching](https://learngitbranching.js.org/) | A visual, game-like way to learn how Git really works |
| [Pro Git book](https://git-scm.com/book/en/v2) | The free, complete book on Git. Chapters 1–2 are enough to start. |
| [VS Code: Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview) | Using Git inside VS Code |
| [GitHub Desktop](https://desktop.github.com/) | Point-and-click Git app |
| [Git cheat sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf) | One-page printable reference |

Back to [root](../)
