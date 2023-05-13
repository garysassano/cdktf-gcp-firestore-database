# cdktf-gcp-firestore-database

CDKTF app that deploys a Firestore database along with some nested documents.

## Prerequisites

For this project you need a GCP account.

## Installation

Install CDKTF:

```sh
npm install -g cdktf
```

Install Poetry + dotenv plugin:

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry self add poetry-plugin-dotenv
```

Configure Poetry to create the virtualenv inside the project's root directory:

```sh
poetry config virtualenvs.in-project true
```

Create the virtualenv and install all the dependencies inside it:

```sh
poetry install
```

## Configuration

In order to deploy to GCP, you need to [create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) in JSON format. After you created a key, download it, rename the file to `credentials.json` and put it in the project's root directory.

As a last step, rename `.env.example` to `.env` and add your variables like in the following example:

```dotenv
GCP_PROJECT_ID=project-123456
GCP_REGION=europe-west3
```

## Deployment

Synthesize the Terraform stack and deploy it:

```sh
cdktf deploy
```

## Cleanup

Destroy the Terraform stack:

```sh
cdktf destroy
```
