# SteamAuthenticator

This repository contains a script to generate Steam Guard codes.

## Requirements

This script is compatible with Python 3 and requires the `requests` package. 

## How to Use

1. Clone the repository or download the Python file to your local machine.
2. Input the SteamGuard Files on the .maFiles folder, you can extract them files using [SDA](https://github.com/Jessecar96/SteamDesktopAuthenticator) or an root device.
3. Open the terminal and navigate to the directory containing the script `cd SteamAuthenticator`.
4. You need to install the necessary dependencies or requirements to run the script. The command: `pip install requests`.
5. Run the script using Python by typing `python SteamGuard.py` in the terminal.

## Script Information

The script works as follows:

- It initially checks the server time from the Steam API.
- Then, it generates a guard code using the shared secret.
- The guard code, username, and Steam ID are printed on the console.
- After that, it waits for 1 second before displaying a progress bar.
- To stop the script, press `Ctrl+C`.
- After the progress bar, the console is cleared and the script runs again.

## Troubleshooting

Make sure to check if your directory is not empty and it has '.maFile' files, as the script requires them to run properly.

## Contributions

Contributions, issues, and feature requests are welcome!

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

