from subprocess import call, run
from sys import platform
from invoke import task

@task
def start(ctx):
    if platform == "win32":
        run("python3 src/index.py", check=True)
    else:
        ctx.run("python3 src/index.py")

@task
def test(ctx):
    if platform == "win32":
        ctx.run("pytest src")
    else:
        ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    if platform == "win32":
        ctx.run("coverage run --branch -m pytest src")
    else:
        ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    if platform == "win32":
        ctx.run("coverage html")
        ctx.run("start htmlcov/index.html")
    else:
        ctx.run("coverage html", pty=True)
        call(("xdg-open", "htmlcov/index.html"))

@task
def lint(ctx):
    if platform == "win32":
        ctx.run("pylint src")
    else:
        ctx.run("pylint src", pty=True)
