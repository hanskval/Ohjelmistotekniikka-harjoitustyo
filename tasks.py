from invoke import task

@task
def start(ctx):
    ctx.run("python3 -m src.index")
@task
def build(ctx):
    ctx.run("python3 -m src.build")
@task
def coverage_report(ctx):
    ctx.run("coverage report -m")