from invoke import task

@task
def start(ctx):
    ctx.run("python3 -m src.index")

def build(ctx):
    ctx.run("python3 -m src.build")