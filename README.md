# LDAP Search Script

## Description

This script connects to an LDAP server and performs a search to retrieve and display directory entries. It uses the `ldap3` library to connect to the LDAP server, perform the search, and parse the results. The script is designed to be a simple tool for querying LDAP directories and viewing results in a readable JSON format.

## Features

- **Connect to LDAP Server**: Connects to the LDAP server with anonymous bind.
- **Perform Search Query**: Searches the LDAP directory for entries based on a specified filter.
- **Display Results**: Parses and displays LDAP entries in a readable JSON format.

## Prerequisites

- Python 3.x
- `ldap3` library

To install the `ldap3` library, run:

```bash
pip install ldap3
