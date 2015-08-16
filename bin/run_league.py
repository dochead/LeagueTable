#!/usr/bin/env python
# -*- coding: utf-8 -*-.
import optparse

from leaguetable import app


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('--filename', '-f', action="store", help="Include optional feature")

    options, args = parser.parse_args()

    if getattr(options, 'filename'):
        app_settings = {
            'input_type': 'file',
            'filename': options.filename
        }
    else:
        app_settings = {
            'input_type': 'raw'
        }

    main_app = app.LeagueApp(**app_settings)
    print(main_app.run())
