# PlayOK Makruk Statistics Downloader

This Python script downloads game statistics from the PlayOK website (https://www.playok.com) for a specified user ID and saves them as text files in a local "txtdata" directory.

## Requirements

To run this script, you will need Python 3.x and the following libraries:

- `requests` (version 2.28.2 or newer)
- `beautifulsoup4` (version 4.12.2 or newer)

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4
```

### Usage
To run the script, simply execute it using Python:

```bash
python playok_downloader.py
```

When prompted, enter the user ID for which you want to download game statistics:
```bash
Please enter the ID (e.g., cpm1399g): <your_user_id>
```

The script will then start downloading the game statistics text files and saving them in the "txtdata" directory. It will also display progress messages as it downloads each file and increments the page number.

Once the script has searched through all the pages, it will print the total number of pages visited and the total number of files downloaded.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
PlayOK (https://www.playok.com) for providing the game statistics.
