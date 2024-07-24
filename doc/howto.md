# How-to Guides

## Set up Postgres for Local Development

- Install Postgres version 16: `brew install postgresql@16`
- Start the database server: `brew services start postgresql@16`
- Enter the Postgres shell: `psql postgres`
- Create an HCI user: `CREATE ROLE hci_admin WITH LOGIN PASSWORD 'whateverYouWantForLocalDevelopment';`
- Add the user's name to the `.env` file
- Add the user's password to the `.env` file
- Give the new user permission to create databases: `ALTER ROLE hci_admin CREATEDB;`
- Quit out of the shell: `\q`
- Re-enter the shell as the `hci_admin` user: `psql postgres -U hci_admin`
- Check the list of roles to make sure the `hci_admin` user was given the correct permissions: `\du`
- Create the HCI database: `CREATE DATABASE hci;`
- Add the name of the database to the `.env` file