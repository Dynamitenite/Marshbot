# Marshbot

A multipurpose Discord bot built with [discord.py](https://github.com/Rapptz/discord.py), featuring moderation tools, fun commands, message sniping, custom triggers, and per-server configurable prefixes.

## Features

- **Custom prefixes** — each server can set its own command prefix, stored in `prefixes.json`
- **Moderation** — kick, ban, and a mute/unmute system ("banish")
- **Message utilities** — snipe deleted messages, purge/clear messages, echo/announce messages, DM users
- **Fun & misc** — 8ball, random dog/cat pictures, jokes, quotes, polls, avatar lookup, "yo mama" jokes
- **Custom triggers** — admin and NSFW keyword-based auto-responses
- **Rotating bot status** — cycles through a set of custom "Playing" statuses
- **Custom help command** — category-organized command reference

## Project Structure

```
Marshbot/
├── bot/
│   ├── main.py              # Bot entry point, core events/commands, extension loader
│   └── cogs/
│       ├── api.py           # Dog/cat/joke/quote/mom commands (external API calls)
│       ├── commands.py      # General commands: 8ball, echo, dm, avatar, poll, role, purge
│       ├── help.py          # Custom help command
│       ├── invites.py       # Invite tracking
│       ├── logs.py          # Server logging
│       ├── moderation.py    # Kick, ban, banish/unbanish
│       ├── snipe.py         # Deleted message sniping
│       └── triggers.py      # Keyword-based auto-responses
├── channel.json              # Per-guild channel configuration (e.g. for logging)
├── prefixes.json             # Per-guild command prefix storage
└── .env                       # Bot token (not committed)
```

## Requirements

- Python 3.8+
- [discord.py](https://pypi.org/project/discord.py/) (v1.x, since the bot uses `client.load_extension` and `commands.Bot`)
- `python-dotenv`

Install dependencies:

```bash
pip install discord.py python-dotenv
```

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/Marshbot.git
   cd Marshbot
   ```

2. **Create a Discord bot application**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and add a bot user
   - Enable the **Server Members Intent** under Privileged Gateway Intents
   - Copy the bot token

3. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   TOKEN=your-bot-token-here
   ```

4. **Initialize config files**

   `prefixes.json` and `channel.json` are updated automatically as the bot joins/leaves servers, but should exist as valid JSON files (`{}`) before the first run.

5. **Invite the bot to your server**

   Use the OAuth2 URL generator in the Developer Portal with the `bot` scope and the permissions your server requires, or use the bot's built-in `invite` command once it's running.

## Running the Bot

```bash
cd bot
python main.py
```

On startup, the bot will:
- Log in and print its ready status along with the number of servers it's in
- Set a "watching you sleep 0_0" presence, then begin cycling through custom playing statuses
- Load all command extensions (cogs)

## Commands

Default prefix is `+` (configurable per-server via the `prefix` command, requires Administrator permission).

| Command | Aliases | Description |
|---|---|---|
| `ping` | `p` | Check bot latency |
| `invite` | `i` | DM yourself the bot's invite link |
| `prefix <new_prefix>` | | Change the server's command prefix (Admin only) |
| `8ball <question>` | | Ask the magic 8-ball |
| `echo <channel> <message>` | `e`, `an`, `announce` | Send a message to a channel |
| `dm <user> <message>` | | DM a user |
| `avatar [member]` | `av` | Show a user's avatar |
| `poll <message>` | | Create a poll |
| `role <member> <role>` | `r` | Assign a role to a member |
| `purge <amount>` | `c`, `clear` | Bulk delete messages |
| `snipe` | `s` | Show the last deleted message in the channel |
| `banish <member> [reason]` | `b`, `mute` | Mute a member |
| `unbanish <member>` | `ub`, `unmute` | Unmute a member |
| `kick <member> [reason]` | | Kick a member |
| `ban <member> [reason]` | | Ban a member |
| `dog` / `cat` | | Random dog/cat image |
| `joke` | | Random joke |
| `quote` | `q` | Random quote |
| `mom [text]` | | "Yo mama" joke |
| `help` | | Show the command list |

## Configuration Files

- **`prefixes.json`** — maps guild IDs to their custom command prefix. Automatically populated with the default prefix (`+`) when the bot joins a new server, and cleaned up when it leaves.
- **`channel.json`** — stores per-guild channel settings (e.g. designated logging channels).

## Notes

- The `.env` file contains your bot token and should **never** be committed to version control. Make sure it's included in `.gitignore`.
- This bot uses the legacy `discord.py` extension-loading API (`client.load_extension`); if migrating to discord.py v2.x, extension loading and intents setup will need to be updated (`await bot.load_extension(...)`, `commands.Bot(intents=...)`).

## License

Add a license of your choice (e.g. MIT) here.
