"""{{cookiecutter.project_name}} DataFlow Process."""

from __future__ import absolute_import

import operator
import argparse
import logging
import re

import apache_beam as beam

def run(argv=None):

    """ Main entry point; defines and runs the pipeline."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',
                        dest='output',
                        required=True,
                        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    p = beam.Pipeline(argv=pipeline_args)

    (p
     | 'add_text' >> beam.Create(['Hello World!'])
     | 'save' >> beam.io.WriteToText(known_args.output))

    return p.run()
