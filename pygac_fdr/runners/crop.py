#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 pygac-fdr developers
#
# This file is part of pygac-fdr.
#
# pygac-fdr is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pygac-fdr is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pygac-fdr. If not, see <http://www.gnu.org/licenses/>.
"""Crop pygac-fdr output file to account for overlap."""

import argparse

from dateutil.parser import isoparse

from pygac_fdr.crop import CROP_OVERLAP_BEGINNING, CROP_OVERLAP_END, crop


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename", type=str, help="pygac-fdr output file")
    parser.add_argument(
        "--date",
        type=lambda s: isoparse(s).date(),
        help="Only include observations of the given date (YYYYmmdd)",
    )
    parser.add_argument(
        "--where",
        choices=(CROP_OVERLAP_BEGINNING, CROP_OVERLAP_END),
        default="end",
        help="Specifies where to crop overlap. In the beginning (removes overlap "
        "with preceding file) or end (removes overlap with subsequent file).",
    )
    args = parser.parse_args()

    start_line, end_line = crop(args.filename, args.where, args.date)
    print(start_line, end_line)
