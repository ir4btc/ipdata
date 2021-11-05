# IPDATA
IPDATA - SCAN ALL IP With Python `IPData`

This is a Python client and command line interface (CLI) for the ipdata.co IP Geolocation API. ipdata offers a fast, highly-available API to enrich IP Addresses with Location, Company, Threat Intelligence and numerous other data attributes.
Note that you need an API Key to use this package. You can get a free one with a 1,500 daily request limit by [Signing up here](https://dashboard.ipdata.co/sign-up.html).

## Installation
Install the latest version of the cli with pip.
`pip install ipdata`

 =============
## Basic Usage
    # Initialize the CLI
    ipdata init <API Key>

    # Look up your own IP address
    ipdata

    # or 
    ipdata me

    # Look up an arbitrary IP address
    ipdata 8.8.8.8

    # Get specific fields with jq
    ipdata 8.8.8.8 | jq .country_name
