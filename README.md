# dm-alerts

dm-alerts is a Discord bot created by the [<Q/S> team](https://qs-e.space/community) and [Quadrat Ik (Space)](https://qs-e.space/bio) for sending notifications to all members of a server.

## Features

- Send notifications to all server members.
- Rate limiting to prevent spam.
- Archive sent messages.
- Easy configuration with `config.json`.

## Requirements

- Python 3.6+
- Required libraries listed in `req.txt`.

## Installation for Windows Users
1. Clone the repository:

   ```shell
   git clone https://github.com/Quadrat-Space/dm-alerts.git
   ```

2. Navigate to the project directory:

   ```shell
   cd dm-alerts/
   ```

3. Create a virtual environment:

    ```shell
    python -m venv myenv
    ```

4. Activate the virtual environment:

    ```shell
    myenv\Scripts\Activate.bat
    ```

5. Install the dependencies:

   ```shell
   pip install -r req.txt
   ```

6. In `config.json`, insert your parameters. Standard content:

   ```json
   {
       "token": "YOUR_BOT_TOKEN",
       "prefix": "?",
       "success_notification_user_id": "YOUR_NOTIFY_USER_ID",
       "allowed_user_id": "YOUR_ALLOWED_USER_ID",
       "message_limit": 15,
       "message_period_minutes": 1,
       "archive_folder": "archive",
       "default_guild_id": "YOUR_DEFAULT_GUILD_ID"
   }
   ```

7. Run the bot:

   ```shell
   python main.py
   ```

## Usage

1. Add the bot to your Discord server.

2. Use the following command to send notifications to all members:

   ```
   /send_everyone [guild_id] [message]
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](https://mit-license.org) file for details.

## Credits

- [Quadrat Ik (Space)](https://qs-e.space/bio)
- [<Q/S> team](https://qs-e.space/community)

## GitHub Repository

Find the project on GitHub: [quadratnew/dm-alerts](https://github.com/Quadrat-Space/dm-alerts)

## Libraries Used

- [disnake](https://pypi.org/project/disnake/)
- [shutil](https://docs.python.org/3/library/shutil.html)
- [ratelimit](https://pypi.org/project/ratelimit/)
- [tqdm](https://pypi.org/project/tqdm/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [os](https://docs.python.org/3/library/os.html)
- [json](https://docs.python.org/3/library/json.html)
- [random](https://docs.python.org/3/library/random.html)

## Commands

- `/send_everyone [guild_id] [message]`: Send a notification to all server members.

## How to Contribute

```lua
We welcome contributions to improve and enhance dm-alerts. If you would like to contribute, feel free to open issues or pull requests on the GitHub repository. Your contributions are highly appreciated!
```

Feel free to contribute to this project or report issues on the GitHub repository.
