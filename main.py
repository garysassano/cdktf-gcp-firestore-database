import cdktf
from stacks.firestore_database_stack import FirestoreDatabaseStack

app = cdktf.App()

FirestoreDatabaseStack(
    app,
    "FirestoreDatabaseStack",
)

app.synth()
