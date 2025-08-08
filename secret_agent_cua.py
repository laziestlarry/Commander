#!/usr/bin/env python3
import os
import subprocess
from getpass import getpass

REPO = "laziestlarry/Commander"
SECRETS = [
    "GCP_PROJECT_ID",
    "GCP_SA_KEY",
    "SHOPIFY_API_KEY",
    "SHOPIFY_API_SECRET",
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_CHAT_ID"
]

ENV_FILE = ".env"
LOG_FILE = "agent_actions.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    print("🔍", message)

def gh_installed():
    return subprocess.call(["which", "gh"], stdout=subprocess.DEVNULL) == 0

def set_github_secret(name, value):
    subprocess.run(["gh", "secret", "set", name, "-R", REPO], input=value.encode(), check=True)

def update_env_file(name, value):
    updated = False
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            lines = f.readlines()
        with open(ENV_FILE, "w") as f:
            for line in lines:
                if line.startswith(name + "="):
                    f.write(f"{name}={value}\n")
                    updated = True
                else:
                    f.write(line)
            if not updated:
                f.write(f"{name}={value}\n")
    else:
        with open(ENV_FILE, "w") as f:
            f.write(f"{name}={value}\n")

def main():
    if not gh_installed():
        print("❌ GitHub CLI not found. Please install it and run `gh auth login` first.")
        return

    print("🤖 Starting CUA Agent for Secrets Collection...")
    for secret in SECRETS:
        if os.getenv(secret):
            log(f"{secret} already present in environment.")
            continue

        print(f"🔐 Missing secret: {secret}")
        approve = input(f"Do you approve collecting {secret}? (y/n): ").strip().lower()
        if approve != "y":
            log(f"{secret} collection denied.")
            continue

        value = getpass(f"Enter value for {secret}: ")
        if not value:
            log(f"{secret} not provided.")
            continue

        try:
            log(f"Syncing {secret}...")
            update_env_file(secret, value)
            set_github_secret(secret, value)
            log(f"{secret} synced to .env and GitHub.")
        except Exception as e:
            log(f"❌ Error syncing {secret}: {e}")

    print("✅ Secret collection completed. Check .env and GitHub Secrets.")

if __name__ == "__main__":
    main()
