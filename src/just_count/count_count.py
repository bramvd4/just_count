import click

from just_count import square


@click.command()
@click.option(
    "-v",
    "--value",
    type=int,
    default=0,
    help="Value used for calculating the square",
    show_default=True,
)
def main(value):
    print(f"The square of {value} is {round(square.square(value))}")


if __name__ == "__main__":
    main()
