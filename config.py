# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'montgomeryal',
    package_name = 'montclair-montgomeryal',
    name = 'Go Montgomery, AL',
    description = 'Real Time Tracking of the Buses for Montgomery, AL',
    url = 'https://montgomeryal.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.6.0',
        revision = 1,
        title = 'Go Montgomery, AL',
        first_run_text = "Welcome to Montgomery, AL's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.4',
        revision = 1,
        app_id = 'com.gotransitapp.montgomeryal',
        app_store_id = '1494071249',
        app_store_url = 'https://apps.apple.com/us/app/go-montgomery-al/id1494071249'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.montgomeryal',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.montgomeryal'
    )
)
