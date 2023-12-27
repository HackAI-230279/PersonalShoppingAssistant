import logging
import os
from typing import Dict, List

from dotenv import load_dotenv
from uagents import Agent, Context, Model

load_dotenv()


class Message(Model):
    message: str


class Query(Model):
    text: str


class Results(Model):
    text: str
    results: List


class Choice(Model):
    choice: int
    results: List


class Product(Model):
    text: str
    result: Dict


client_agent = Agent(
    name="Shopper",
    port=8001,
    seed="our seed for shopping assistant lol",
    endpoint=["http://127.0.0.1:8001/submit"],
)


@client_agent.on_event("startup")
async def start(ctx: Context):
    ctx.logger.info(f"Hello, my name is {ctx.name} and address is {ctx.address}")
    await ctx.send(
        os.getenv("SERVER_ADDRESS"),
        Query(text=input("\nPlease enter product name: ")),
    )


@client_agent.on_event("shutdown")
async def stop(ctx: Context):
    print("\nThanks for shopping!")


@client_agent.on_message(model=Results)
async def search(ctx: Context, sender: str, msg: Results):
    if len(msg.results) != 0:
        print("\n" + msg.text)
        await ctx.send(
            sender,
            message=Choice(
                choice=input("\nEnter choice: "),
                results=msg.results,
            ),
        )
    else:
        print("\nSorry! No products seem to be available for your selected query.")


@client_agent.on_message(model=Product)
async def search(ctx: Context, sender: str, msg: Product):
    print(msg.text)


from uagents.setup import fund_agent_if_low

if __name__ == "__main__":
    print("Starting shopping agent...")
    fund_agent_if_low(str(client_agent.wallet.address()))
    client_agent.run()
