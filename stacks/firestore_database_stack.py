import json
import os
from cdktf import TerraformStack
from cdktf_cdktf_provider_google.firestore_database import FirestoreDatabase
from cdktf_cdktf_provider_google.firestore_document import FirestoreDocument
from cdktf_cdktf_provider_google.project_service import ProjectService
from cdktf_cdktf_provider_google.provider import GoogleProvider
from constructs import Construct


class FirestoreDatabaseStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
        GCP_REGION = os.environ.get("GCP_REGION")

        GoogleProvider(
            self,
            "GoogleProvider",
            project=GCP_PROJECT_ID,
            region=GCP_REGION,
            credentials=os.path.abspath("credentials.json"),
        )

        # Enable Cloud Firestore API for the project
        cloud_firestore_api = ProjectService(
            self,
            "CloudFirestoreAPI",
            service="firestore.googleapis.com",
            disable_on_destroy=True,
        )

        firestore_database = FirestoreDatabase(
            self,
            "FirestoreDatabase",
            name="database",
            location_id=GCP_REGION,
            type="FIRESTORE_NATIVE",
            concurrency_mode="OPTIMISTIC",
            app_engine_integration_mode="DISABLED",
            depends_on=[cloud_firestore_api],
        )

        document = FirestoreDocument(
            self,
            "FirestoreDocument_document",
            document_id="document",
            collection="collection",
            fields=json.dumps({"key-1": {"stringValue": "value-1"}}),
            depends_on=[cloud_firestore_api],
        )

        sub_document = FirestoreDocument(
            self,
            "FirestoreDocument_sub-document",
            document_id="sub-document",
            collection=f"{document.path}/sub-collection",
            fields=json.dumps({"key-2": {"stringValue": "value-2"}}),
            depends_on=[cloud_firestore_api],
        )

        sub_sub_document = FirestoreDocument(
            self,
            "FirestoreDocument_sub-sub-document",
            document_id="sub-sub-document",
            collection=f"{sub_document.path}/sub-sub-collection",
            fields=json.dumps({"key-3": {"stringValue": "value-3"}}),
            depends_on=[cloud_firestore_api],
        )
