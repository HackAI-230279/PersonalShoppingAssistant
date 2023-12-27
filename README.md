# Personal Shopping Assistant for HackAI 2023 Final

<p align="center" width="100%"><img width="70%" src="https://graph.org/file/821fcebb56f1480d08870.jpg"></p>

## Description

<img src="https://graph.org/file/db914ce03059dca6e2e02.gif" align="right" width="150">
This project is an Agent made using Fetch.ai's UAgent that acts as a personal shopping assistant, which can be used to buy products from online stores. The agent can be used to query products from Amazon and Flipkart.

**Tech Stack:** Python, Poetry, BS4, Selenium, uAgents Library

## Deployment

To deploy this project:

1. Clone the project repository from GitHub using the following command:

   ```bash
   git clone https://github.com/HackAI-230279/PersonalShoppingAssistant.git
   ```

2. Open a terminal inside the cloned folder.
3. Install all required dependencies by running the following command:

   ```bash
   pip3 install poetry
   python3 -m poetry shell
   python3 -m poetry install
   ```

4. Rename `.sample.env` to `.env`.
5. Set the required variables, such as the server address, in the `.env` file.
6. Run the following command to start the backend:

   ```bash
   python3 -m backend
   ```

7. Then, open another terminal inside the cloned folder to interact with the backend.
8. Run the following command to start the client flow:

   ```bash
   python3 client.py
   ```

9. The client will ask for the product name, and then ask you to pick a product from the list of products returned by the agent. After you pick a product, the agent will ask you to pick a store from which you want to buy the product. After you pick a store, the agent will show you the details of the product, along with the URL.

## Credits and Contribution

<img src="https://graph.org/file/b26313d73e4d05de84a85.png" style="display: block; margin: 0 auto; width: 110px;" align="right">

This repository is tailored for the TechFest Hackathon and leverages the uAgent library. Explore more about uAgents at [Fetch.ai/uAgents](https://github.com/fetchai/uAgents/)

## Copyright and License

<img src="https://graph.org/file/b5850b957f081cfe5f0a6.png" align="right" style="display: block; margin: 0 auto; width: 110px">

- Copyright (C) 2022 by [Team HackAI-230279](https://github.com/HackAI-230279).

<img src="https://img.shields.io/badge/License-MIT-green.svg" style="display: block; margin: 0 auto">

---