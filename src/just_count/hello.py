# Test for Click assignment

import time

import click


@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)
@click.option(
    "-p",
    "--pause",
    default=0,
    help="Pause in between two greetings given",
    show_default=True,
)
def hello(name, count, pause):
    for _ in range(count):
        print(f"Hello {name}!")
        time.sleep(pause)


if __name__ == "__main__":
    hello()
