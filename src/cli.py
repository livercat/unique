#!/usr/bin/env python3

import logging
import os
import sys

import click

from src.processing import process, render

logging.basicConfig(level=logging.INFO)


@click.command()
@click.argument('file')
def run(file: str) -> None:
    if not os.path.isfile(file):
        logging.error(f"File {file} doesn't exist. Please provide a valid path to file.")
        sys.exit(1)
    result = process(file)
    print(render(result))
