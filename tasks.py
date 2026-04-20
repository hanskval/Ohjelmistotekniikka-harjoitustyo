from invoke import task

@task
def start(ctx):
    ctx.run("python3 -m src.index")
@task
def build(ctx):
    ctx.run("python3 -m src.build")

@task
def coverage(ctx):
    ctx.run("coverage run -m --branch -m pytest src")
    
@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report")
    
@task
def lint(ctx):
    ctx.run("pylint src")