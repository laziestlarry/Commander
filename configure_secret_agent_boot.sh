#!/bin/bash
echo '🔐 Setting up CUA Secret Agent boot task...'

# Add to ~/.bash_profile if not already present
PROFILE=~/.bash_profile
if ! grep -q 'secret_agent_online_collector.py' $PROFILE; then
    echo 'python3 ~/Commander_Orchestrated_Online/agents/secret_agent_online_collector.py --auto >> ~/secret_agent.log 2>&1' >> $PROFILE
    echo '✅ Secret Agent added to startup in ~/.bash_profile'
else
    echo '⚠️  Secret Agent already configured in ~/.bash_profile'
fi

# Ensure script is executable and placed correctly
mkdir -p ~/Commander_Orchestrated_Online/agents
cp /mnt/data/secret_agent_online_collector.py ~/Commander_Orchestrated_Online/agents/
chmod +x ~/Commander_Orchestrated_Online/agents/secret_agent_online_collector.py

echo '🧠 Agent is now always ready under Commander control.'
