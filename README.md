# Campus Connect

A small social app for one college: students post, follow, and see a feed.

This folder is a **starter**. Your team copies it once, then does every task in **your own team repository**. Do not push your homework to `beindustryfit/CampusConnect`. Everyone in every college shares that copy. Your work goes to the repo your mentor created for your team.

You do not need to have used Git, Docker, or Python on a project before. Follow the steps in order.

## Before you type anything

Install these three free programs. Restart the laptop after Docker finishes installing.

1. **Git** saves your code and sends it to GitHub. https://git-scm.com/downloads
2. **Docker Desktop** runs the project on your laptop the same way it runs for your teammates. https://www.docker.com/products/docker-desktop/ Open Docker Desktop once and wait until it says it is running.
3. **Python 3.12** runs the tests. https://www.python.org/downloads/ On Windows, tick "Add python.exe to PATH" during install.

Open a terminal.

- Mac: press Command+Space, type `Terminal`, press Enter.
- Windows: press the Windows key, type `PowerShell`, press Enter.

Paste these one at a time. Each one should print a version number, not "not found" or "not recognized".

```bash
git --version
docker --version
python3 --version
```

On Windows, if `python3` fails, try `python --version` instead. Use `python` in place of `python3` in the later steps.

If a command is missing, the install did not finish. Stop and message your mentor. Do not skip ahead.

## 1. Copy the starter onto your laptop

```bash
git clone https://github.com/beindustryfit/CampusConnect.git
cd CampusConnect
```

`git clone` downloads the folder. `cd` means "go into that folder". Every later command is typed **inside** this folder.

## 2. Send the code to your team repository

Your mentor will send you a link that looks like `https://github.com/beindustryfit/cloud-alpha`. That link is yours. This starter link is not.

Replace the URL below with the one your mentor sent. Keep the `.git` at the end if their link does not already have it.

```bash
git remote rename origin starter
git remote add origin PASTE-THE-TEAM-REPO-URL-HERE
git push -u origin main
```

What those lines mean:

- `origin` is the nickname of the GitHub repo you push to.
- The first line keeps the starter as a nickname called `starter`, so you can still look at it.
- The second line says "from now on, origin is our team repo".
- The third line uploads the code. `main` is the shared branch everyone starts from.

GitHub will ask you to log in. Use the GitHub account you connected on the portal.

If the push says **permission denied** or **403**, your GitHub username is not on the team repo yet. Send your username to your mentor. Do not create a different repo yourself.

## 3. Start the project

```bash
docker compose up --build
```

The first time can take several minutes. That is normal. Docker is downloading the pieces.

Open a browser and go to http://localhost:8080/. You should see a short JSON message. That means the app is running.

Leave that terminal open while you look. Stop the project later with Ctrl+C. If you used `docker compose up -d`, stop it with `docker compose down`.

## 4. Run the tests

Open a **second** terminal. Go back into the same folder (`cd` to it). Then:

```bash
python3 -m pip install -r requirements.txt
pytest -q
```

A row of dots means the tests passed. The word `FAILED` means something is wrong. Read the last 20 lines and fix that, or paste them to your mentor. Do not ignore a failure.

## 5. How to do every task after this

One task is one branch and one pull request. A branch is your private copy so you do not break `main` for the team.

1. On the portal, open the task. It names the file to edit and the command that proves you are done.
2. In the project folder:

```bash
git checkout main
git pull
git checkout -b week1-short-name
```

Use a short branch name for that task, such as `week1-health`.

3. Edit only the files the task mentions. Save.
4. Run the check command written in the task. If it fails, fix the code and run it again.
5. Upload the branch:

```bash
git add .
git commit -m "Say what you changed in one sentence"
git push -u origin HEAD
```

6. GitHub prints a link to open a pull request. Open it. In the description, paste the output of the check command.
7. Copy the pull request link (it looks like `https://github.com/.../pull/1`). On the portal task, paste it and click Submit.

Wait until the GitHub check is green before you submit. A red check means the tests failed on GitHub even if they passed on your laptop.

Do not commit directly on `main`.

## 6. Your first task

Week 1 asks you to add GET /health in `app/main.py`. The app already starts. Hit http://localhost:8080/ and you should see a JSON hint.

## If you are stuck

| What you see | What to do |
|---|---|
| `command not found` or `not recognized` | That program is not installed, or you did not reopen the terminal after installing it. |
| `permission denied` when you push | Ask your mentor to add your GitHub username to the team repo. |
| Docker will not start | Open Docker Desktop and wait until it says it is running. |
| `port is already allocated` | Something else is using that port. Quit the other project, or run `docker compose down` in this folder and start again. |
| `pytest` is not found | Run `python3 -m pip install -r requirements.txt` again from this folder. |

You are not expected to know these tools yet. The task text explains new words. If you are blocked for more than 30 minutes, post it in standup and message your mentor.
