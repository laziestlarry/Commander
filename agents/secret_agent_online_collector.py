#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path
import requests

REPO = "laziestlarry/Commander"
SECRETS = {
    "GCP_PROJECT_ID": ["env", "config.json", "credentials.json"],
    "GCP_SA_KEY": ["credentials.json", "service-account.json"],
    "SHOPIFY_API_KEY": [".env", "config/shopify.json"],
    "SHOPIFY_API_SECRET": [".env", "config/shopify.json"],
    "TELEGRAM_BOT_TOKEN": [".env", "config/telegram.json"],
    "TELEGRAM_CHAT_ID": [".env", "config/telegram.json"]
}

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
    lines = []
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            lines = f.readlines()
    found = False
    with open(ENV_FILE, "w") as f:
        for line in lines:
            if line.startswith(name + "="):
                f.write(f"{name}={value}\n")
                found = True
            else:
                f.write(line)
        if not found:
            f.write(f"{name}={value}\n")

def extract_from_file(file, key):
    import json
    try:
        if file.endswith(".json"):
            with open(file, "r") as f:
                data = json.load(f)
            return data.get(key)
        elif file.endswith(".env"):
            with open(file, "r") as f:
                for line in f:
                    if line.startswith(key + "="):
                        return line.split("=", 1)[1].strip()
    except Exception as e:
        log(f"Error parsing {file}: {e}")
    return None

def find_secret_value(secret_name, sources):
    for source in sources:
        source_path = Path(source)
        if source_path.exists():
            value = extract_from_file(str(source_path), secret_name)
            if value:
                log(f"✅ Found {secret_name} in {source}")
                return value
    return None

def try_online_secret(secret):
    log(f"🌐 Attempting to find {secret} online...")
    try:
        # Placeholder API - Replace with real agent crawler or cloud source lookup
        url = f"https://api.example.com/secret-lookup?key={secret}"
        response = requests.get(url, timeout=3)
        if response.ok:
            result = response.json()
            value = result.get("value")
            if value:
                log(f"🌍 Found {secret} online via API.")
                return value
    except Exception as e:
        log(f"⚠️  Online lookup failed for {secret}: {e}")
    return None

def main():
    if not gh_installed():
        print("❌ GitHub CLI not found. Please install it and run `gh auth login` first.")
        return

    print("🤖 CUA Agent: Autonomous Secret Collector Activated...")

    for secret, sources in SECRETS.items():
        current = os.getenv(secret)
        if current:
            log(f"{secret} already in environment. Skipping.")
            continue

        value = find_secret_value(secret, sources)
        if not value:
            value = try_online_secret(secret)

        if not value:
            log(f"⚠️  Could not find {secret} locally or online.")
            continue

        try:
            update_env_file(secret, value)
            set_github_secret(secret, value)
            log(f"🔐 {secret} synced to .env and GitHub.")
        except Exception as e:
            log(f"❌ Error syncing {secret}: {e}")

    print("✅ Secret Collection Finished. Ready for secure deployment.")

if __name__ == "__main__":
    main()
