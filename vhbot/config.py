import logging
import os


def parse_variable(variable, vartype, default=None, required=False):
    value = os.getenv(variable, None)
    if not value:
        if required:
            logging.fatal(f"Missing required environment variable: {variable}")
            exit(1)
        return default

    if vartype == str:
        return value
    elif vartype == bool:
        return True if value.lower() in ["true", "1", "t", "y", "yes"] else False
    elif vartype == int:
        return int(value) if value.isdigit() else default


class Config:
    def __init__(self):
        # Required
        self.bot_token = parse_variable("BOT_TOKEN", str, required=True)
        self.guild_id = parse_variable("GUILD_ID", int, required=True)

        # IDs
        self.mod_role = parse_variable("MOD_ROLE", int, required=True)


config = Config()
