# cdktf-gcp-firestore-databases

CDKTF app that deploys two Firestore databases in the same GCP project.

This repository showcases a recently added new feature which allows to have [multiple Firestore databases within the same GCP project](https://cloud.google.com/blog/products/databases/manage-multiple-firestore-databases-in-a-project) (also of different types). Previously you were limited to a single Firestore database per project, always named `"default"`.

## Prerequisites

- **_GCP:_**
  - Must have authenticated with [Application Default Credentials](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#running-terraform-on-your-workstation) in your local environment.
  - Must have set the `GCP_PROJECT_ID` and `GCP_REGION` variables in your local environment.
- **_Node.js + npm:_**
  - Must be [installed](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) in your system.

## Installation

```sh
npx projen install
```

## Deployment

```sh
npx projen deploy
```

## Cleanup

```sh
npx projen destroy
```

## Architecture Diagram

![Architecture Diagram](./src/assets/arch.svg)
