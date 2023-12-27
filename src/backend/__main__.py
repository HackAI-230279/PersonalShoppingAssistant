from uagents.setup import fund_agent_if_low

from .uagent.__main__ import price_agent

if __name__ == "__main__":
    print("Starting alert agent...")
    fund_agent_if_low(str(price_agent.wallet.address()))
    price_agent.run()
