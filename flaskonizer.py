"""
File: flaskonizer.py
Main entry point to flaskonizer
"""
import click

@click.command()
@click.option('--count', default=1, help="Number of iterations")
@click.option('--name', prompt="Name", help="Your name please")
def hello(count, name):
    for x in range(count):
        click.echo(name)


if __name__ == '__main__':
    hello()
