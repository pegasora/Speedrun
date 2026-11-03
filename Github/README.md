# Git and GitHub Guide

This guide covers everything you need to get this repository onto your computer, keep it up to date, and open it in VS Code. It assumes you've never used Git or GitHub before.

> **TL;DR:** Install Git, run `git clone https://github.com/pegasora/Speedrun.git`, open the folder in VS Code, and run `git pull` whenever I tell you I've added new stuff.

> 🪟 **This guide is written for Windows.** Commands are shown for **PowerShell**, the default terminal in Windows and in VS Code. They work the same in Git Bash. Wherever **Linux / WSL2** or **macOS** does something differently, there's a note. In commands, `~` means your home folder, which on Windows is `C:\Users\<you>`.

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
   ┌──────────────────────────────┐
   │  Your computer               │   ← You read, run code, and work here
   │  C:\Users\<you>\Projects\    │
   │    Speedrun\                 │
   └──────────────────────────────┘
```

For this repo, information flows **one way**: I add material and push it to GitHub, and you **pull** it down. You won't be pushing anything to this repo. (If you want a copy you *can* push your own work to and still get my updates, see [forking in section 8](#option-b-fork-this-repo).)

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
| **Fork** | Your own copy of someone else's repo *on GitHub*. Optional. See [Option B in section 8](#option-b-fork-this-repo). |
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

> This repo is public, so you don't need an account just to browse, clone, or pull it.

---

## 4. Installing Git

Pick your operating system:

### Windows (do this one)

**Option 1: Installer**

1. Download **Git for Windows** from [git-scm.com/downloads](https://git-scm.com/downloads).
2. Run the installer. **The default options are fine.** Just keep clicking Next.
   - When it asks for a default editor, you can pick **Visual Studio Code** if you have it installed.
   - Leave **Git Credential Manager** enabled. It handles signing in to GitHub for you later.

**Option 2: winget** (Windows' built-in package manager). Open PowerShell and run:

```powershell
winget install --id Git.Git -e --source winget
```

Either way, you get Git in **PowerShell** and the **VS Code terminal**, plus **Git Bash**, a Linux-style terminal. Use whichever you like. This guide uses PowerShell.

> **Opening PowerShell:** Press the **Windows key**, type `PowerShell`, and press Enter. Or, in File Explorer, right-click inside a folder and choose **Open in Terminal**. That opens PowerShell already in that folder.

### Linux and WSL2

**WSL2** (Windows Subsystem for Linux) runs a real Ubuntu install inside Windows. You'll probably want it later for things like ROS 2. You don't need it for this repo yet.

To install WSL2, open PowerShell **as Administrator** (right-click PowerShell → **Run as administrator**) and run:

```powershell
wsl --install
```

Restart when it asks, then open **Ubuntu** from the Start menu and create a Linux username and password.

Inside Ubuntu (WSL2) or any Ubuntu/Debian machine, install Git with:

```bash
sudo apt update
sudo apt install git
```

> **WSL2 has its own separate Git and files.** Git installed on Windows and Git installed inside WSL2 are two different installs. If you work inside WSL2, clone repos into your Linux home folder (`~/Projects`, which is `/home/<you>/Projects`), *not* under `/mnt/c/...`. It's much faster.
> Microsoft's guide: [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

### macOS

Open the **Terminal** app and run `git --version`. If Git isn't installed, macOS will offer to install the **Command Line Developer Tools**. Click **Install**. (Or, with [Homebrew](https://brew.sh/): `brew install git`.)

### Check that it worked

Open a **new** PowerShell window (close any that were open before installing) and run:

```powershell
git --version
```

You should see something like `git version 2.x.x`. If you get "command not found" or "not recognized," see [Troubleshooting](#12-troubleshooting).

### One-time setup (optional for now)

Git attaches your name and email to commits. You only need this if you start making commits (see [section 9](#9-bonus-your-own-repo-commit-and-push)), but it's easy to do now:

```powershell
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
| **Windows** | **`C:\Users\<you>\Projects`** (in PowerShell, that's `~/Projects`) |
| Linux / WSL2 | `~/Projects`, which is `/home/<you>/Projects` |
| macOS | `~/Projects`, which is `/Users/<you>/Projects` |

> ⚠️ **Windows: don't use Documents or Desktop.** On many Windows PCs, those folders are synced to **OneDrive**, and OneDrive and Git don't get along. It can lock files, create duplicate copies, and corrupt the repo. `C:\Users\<you>\Projects` is outside OneDrive. The same goes for iCloud and Dropbox folders.

### Step 2: Open a terminal in that folder

Open **PowerShell** and run:

```powershell
mkdir ~/Projects     # only the first time, to create the folder
cd ~/Projects
```

These exact commands also work in Git Bash, Linux / WSL2, and macOS.

### Step 3: Clone

```powershell
git clone https://github.com/pegasora/Speedrun.git
```

This creates a `Speedrun` folder containing everything in the repo. It might take a minute because of the PDFs.

```powershell
cd Speedrun
ls        # you should see Github, Python, PLCs, README.md, etc.
```

That's it. You now have the whole repo on your computer, at `C:\Users\<you>\Projects\Speedrun`. You can also open that folder in File Explorer (`explorer .` opens the current folder).

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
2. **File → Open Folder…**
3. Select the `Speedrun` folder you cloned and click **Open**.
4. If VS Code asks *"Do you trust the authors of the files in this folder?"*, click **Yes, I trust the authors**.

**Option B: from the terminal**

```powershell
cd ~/Projects/Speedrun
code .
```

The `.` means "this folder."

**Option C: from File Explorer**

Right-click the `Speedrun` folder and choose **Open with Code**. (On Windows 11, you may need to click **Show more options** first.)

> **Windows VS Code install tips:** During setup, leave **Add to PATH** checked so `code .` works, and check both **Add "Open with Code" action to Windows Explorer** boxes for Option C. If you skipped these, just re-run the installer.
>
> **WSL2:** Install the [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). Then running `code .` in the Ubuntu terminal opens VS Code on Windows, connected to your Linux files.
>
> **macOS:** If `code` isn't found, press `Cmd+Shift+P` in VS Code and run **Shell Command: Install 'code' command in PATH**.

### Getting around in VS Code

| What | Where / shortcut |
|---|---|
| **Explorer** (file tree) | Left sidebar, top icon, or `Ctrl+Shift+E` |
| **Preview a README** nicely formatted | Open the `.md` file, then `Ctrl+Shift+V` (or right-click the tab → **Open Preview**) |
| **Side-by-side preview** | `Ctrl+K V` |
| **Built-in terminal** | **Terminal → New Terminal**, or `` Ctrl+` `` |
| **Command Palette** (search every command) | `Ctrl+Shift+P` |
| **Quick open a file** by name | `Ctrl+P` |
| **Source Control** (Git) panel | Left sidebar, branch icon, or `Ctrl+Shift+G` |

*On macOS, use `Cmd` instead of `Ctrl`.*

Links in the README preview work too, so you can click around the repo the same way you would on GitHub.

### Git inside VS Code

VS Code has Git built in, so you don't have to leave the editor:

- The **bottom-left corner** of the window shows your current branch (`main`) and a **sync** button (circular arrows). Clicking it pulls new changes.
- The **Source Control** panel shows any files you've changed, plus a **…** menu with **Pull**, **Push**, **Commit**, and more.

More detail: [Source Control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).

---

## 7. Staying up to date (pulling)

I'll keep adding material, like new assignments, notes, and sections. To get the latest version:

```powershell
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
  ```powershell
  git log --oneline -10
  ```

---

## 8. Where to put your own work

You have two options. Either one works, so pick whichever makes more sense to you.

| | Option A: Separate folder | Option B: Fork this repo |
|---|---|---|
| Your work lives… | In its own folder or repo, next to Speedrun | Inside your own copy of Speedrun |
| Getting my updates | `git pull` | **Sync fork** on GitHub (or `git fetch upstream`), then `git pull` |
| Backing up your work | Optional, by making it its own repo ([section 9](#9-bonus-your-own-repo-commit-and-push)) | Built in. You push to your fork. |
| Complexity | Simplest | A little more Git, but good practice |

### Option A: Keep your work in a separate folder

**Don't edit files inside the Speedrun folder.** If you edit a file and I later change the same file, `git pull` will complain (see [Troubleshooting](#12-troubleshooting)). Treat this repo as **read-only reference material**.

Instead, keep your own exercises, assignment solutions, and experiments in a **separate folder**:

```
C:\Users\<you>\Projects\
├── Speedrun/          ← this repo (read-only; just pull)
└── my-internship/     ← YOUR work
    ├── python-crash-course/
    ├── machine-vision/
    └── plc-notes/
```

If you want to run or modify something from Speedrun, **copy it** into your own folder first.

Even better: make `my-internship` its own Git repo. See the next section.

### Option B: Fork this repo

A **fork** is your own copy of this repo on GitHub, under your account. You can add your own work to it and push to it, and you can still pull in my updates whenever I add material.

With a fork, there are **two** remotes:

| Remote name | Points to | You… |
|---|---|---|
| `origin` | **Your fork**, `github.com/<your-username>/Speedrun` | Push your work here, and pull from here |
| `upstream` | **My repo**, `github.com/pegasora/Speedrun` | Only pull from here to get my updates |

```
   ┌────────────────────────────┐
   │  pegasora/Speedrun         │   upstream (my repo)
   └─────────────┬──────────────┘
                 │  Sync fork  /  git fetch upstream
                 ▼
   ┌────────────────────────────┐
   │  <your-username>/Speedrun  │   origin (your fork)
   └──────┬─────────────▲───────┘
  git pull│             │git push
          ▼             │
   ┌────────────────────────────┐
   │  Your computer             │
   │  C:\Users\<you>\Projects\  │
   │    Speedrun\               │
   └────────────────────────────┘
```

#### Step 1: Create the fork

1. Sign in to GitHub ([section 3](#creating-a-github-account)).
2. Go to [github.com/pegasora/Speedrun](https://github.com/pegasora/Speedrun).
3. Click **Fork** (top right), leave the defaults, then click **Create fork**.

You now have `github.com/<your-username>/Speedrun`.

> Forks of public repos are public, so don't put anything private in it.

#### Step 2: Clone *your fork*

Clone **your fork**, not mine:

```powershell
cd ~/Projects
git clone https://github.com/<your-username>/Speedrun.git
cd Speedrun
```

> **Already cloned my repo?** You don't need to start over. Rename my repo to `upstream` and point `origin` at your fork:
> ```powershell
> git remote rename origin upstream
> git remote add origin https://github.com/<your-username>/Speedrun.git
> git fetch origin
> git branch --set-upstream-to=origin/main main
> ```

#### Step 3: Connect it to my repo (`upstream`)

```powershell
git remote add upstream https://github.com/pegasora/Speedrun.git
git remote -v
```

You should see both remotes:

```
origin    https://github.com/<your-username>/Speedrun.git (fetch)
origin    https://github.com/<your-username>/Speedrun.git (push)
upstream  https://github.com/pegasora/Speedrun.git (fetch)
upstream  https://github.com/pegasora/Speedrun.git (push)
```

You only do this once.

#### Step 4: Add your work in your own folder

Put **all** your work in a folder that I'll never touch, like `my-work/` at the top of the repo:

```
Speedrun/
├── my-work/            ← YOUR stuff goes here
│   ├── python-crash-course/
│   ├── machine-vision/
│   └── plc-notes/
├── Github/
├── Python/
├── PLCs/
└── ...
```

Keep my files as they are. If you want to change something of mine, copy it into `my-work/` and change the copy. As long as you only edit inside `my-work/`, syncing will never cause a conflict.

#### Step 5: Commit and push your work

```powershell
git add my-work/
git commit -m "Add chapter 3 exercises"
git push
```

This pushes to **your fork** (`origin`), not to my repo.

#### Step 6: Get my updates (sync)

**Commit your own work first**, then pick one of these.

**On GitHub (easiest):**

1. Go to your fork's page on GitHub.
2. Click **Sync fork**, then **Update branch**.
3. On your computer, run:
   ```powershell
   git pull
   ```

**From the terminal:**

```powershell
git fetch upstream          # download my new commits
git merge upstream/main     # merge them into your main branch
git push                    # update your fork on GitHub too
```

**In VS Code:** **Source Control → … → Pull, Push → Pull from…**, then choose `upstream`, then `upstream/main`. Then click **Sync Changes** to push the result to your fork.

> ⚠️ **On GitHub:** If **Sync fork** ever offers **Discard N commits**, **don't click it**. That deletes your work from the fork. It only happens when your changes conflict with mine (usually because a file outside `my-work/` was edited). Sync from the terminal instead and follow the [merge conflict steps](#conflict-content-merge-conflict-in-file), or ask me.

> **Don't open pull requests to my repo** unless I ask you to. GitHub sometimes shows a **Contribute** button on forks. You can ignore it.

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

```powershell
cd ~/Projects
git clone https://github.com/<your-username>/my-internship.git
cd my-internship
```

### Step 3: Make changes and commit

Add or edit some files, then:

```powershell
git status                      # see what changed
git add .                       # stage everything that changed
git commit -m "Add chapter 2 exercises"
```

Write commit messages that say *what* you did: `Add webcam capture script` beats `stuff` or `update`.

### Step 4: Push

```powershell
git push
```

The first time, Git will ask you to sign in to GitHub. On Windows, **Git Credential Manager** (installed with Git for Windows) opens a browser window. Sign in there once, and it remembers you after that.

> **Linux / WSL2 / macOS:** Install the [GitHub CLI](https://cli.github.com/) and run `gh auth login` once. (Inside WSL2 you can also reuse the Windows credential manager. See the [Git Credential Manager WSL docs](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/wsl.md).)

Refresh the repo page on GitHub, and your changes are there.

### Doing it in VS Code instead

1. Open the **Source Control** panel (`Ctrl+Shift+G`).
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
| `ls` | List files in the current folder |
| `cd <folder>` | Move into a folder |
| `cd ..` | Move up one folder |
| `mkdir <name>` | Make a new folder |
| `code .` | Open the current folder in VS Code |
| `explorer .` | *(Windows)* Open the current folder in File Explorer |
| `clear` | Clear the terminal screen |

These work in PowerShell, Git Bash, and Linux / WSL2. (The old Windows **Command Prompt** (`cmd`) is different. For example, it uses `dir` instead of `ls`. Stick with PowerShell.)

GitHub also has a printable [Git cheat sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf).

---

## 12. Troubleshooting

### `'git' is not recognized as the name of a cmdlet…` / `git: command not found`

Git isn't installed, or your terminal was open before you installed it. **Close and reopen PowerShell** (or restart VS Code completely). If that doesn't fix it, reinstall Git ([section 4](#4-installing-git)).

### `warning: LF will be replaced by CRLF`

This is harmless. Windows and Linux use different invisible characters for line endings, and Git converts them automatically. You can ignore it.

### `Filename too long` (Windows)

Windows has a default limit on path length. Tell Git to allow long paths:

```powershell
git config --global core.longpaths true
```

Keeping projects in a short path like `C:\Users\<you>\Projects` also helps.

### `fatal: not a git repository`

You're not inside the repo folder. `cd` into it first:

```powershell
cd ~/Projects/Speedrun
```

### `error: Your local changes to the following files would be overwritten by merge`

You edited a file that I also updated. Pick one:

- **Keep your edits somewhere else, then pull** (safe):
  ```powershell
  git stash        # set your changes aside
  git pull         # get my updates
  git stash pop    # bring your changes back (may cause a conflict)
  ```
- **Throw away your edits and pull** (⚠️ loses your changes to those files):
  ```powershell
  git restore .
  git pull
  ```

To avoid this entirely, keep your work outside the Speedrun folder ([section 8](#8-where-to-put-your-own-work)).

### `CONFLICT (content): Merge conflict in <file>`

Git couldn't combine two sets of changes. Open the file in VS Code. It highlights the conflicting sections and gives you buttons: **Accept Current Change**, **Accept Incoming Change**, or **Accept Both Changes**. Pick one, save, then:

```powershell
git add <file>
git commit
```

If you're unsure, stop and ask me. Nothing is lost.

### Authentication failed / asked for a password

GitHub doesn't accept your account password on the command line anymore. Use one of these:

- **Windows:** Let **Git Credential Manager** handle it. It comes with Git for Windows and opens a browser sign-in. If it never appears, reinstall Git with the credential manager option left on.
- Install the [GitHub CLI](https://cli.github.com/) and run `gh auth login`.
- Use [GitHub Desktop](https://desktop.github.com/).

### `Repository not found` when cloning

The URL probably has a typo. Copy it straight from the green **Code** button on the repo page and try again.

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
