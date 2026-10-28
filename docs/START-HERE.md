# Start here — ShipYard

This is a starter, not the finished project. Your team clones it, then does the work in **your own repo**. Do not push homework back to `beindustryfit/ShipYard`.

## 1. Get the code

```bash
git clone https://github.com/beindustryfit/ShipYard.git
cd ShipYard
```

Create an empty repo for your team (your mentor will share the link). Point this folder at that repo:

```bash
git remote rename origin starter
git remote add origin https://github.com/YOUR-ORG/YOUR-TEAM-REPO.git
git push -u origin main
```

## 2. Run it

You need Git, Docker Desktop, and Python 3.12.

```bash
docker compose up --build
```

## 3. How every task works

1. Read the task on the portal. It names the file and the command.
2. `git checkout -b week1-short-name`
3. Change only what the task asks. Leave a short comment if you are unsure.
4. Run the check command in the task. If it fails, fix it before you open a pull request.
5. `git push -u origin HEAD` and open a pull request. Paste the check output in the description.
6. On the portal, submit the pull request link. A mentor grades that link.

## 4. Your first task

Week 1 asks you to accept a GitHub push webhook in `app/main.py`. A sample push payload is in `fixtures/github_push.json`. The app already answers GET /.

If a word is new, the task explains it. You do not need to have used the tool before.
