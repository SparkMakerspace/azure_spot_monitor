# Import the needed credential and management objects from the libraries.
import os
from dotenv import load_dotenv
from time import sleep

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import requests

load_dotenv()

# Acquire a credential object using CLI-based authentication.
credential = DefaultAzureCredential()

# Make sure to set AZURE_SUBSCRIPTION_ID, AZURE_TENANT_ID, AZURE_CLIENT_ID, and AZURE_CLIENT_SECRET environment variables for authentication

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

while(True):
    # do this forever...
    timeout = False
    # check if VM is up
    URL = os.environ["URL"]
    try:
        r = requests.get(url = URL,timeout=3)
    except:
        timeout = True

    if (timeout or r.status_code != 200):

        # Obtain the management object for virtual machines
        compute_client = ComputeManagementClient(credential, subscription_id)

        VM_NAME = os.environ["VM_NAME"]
        RESOURCE_GROUP_NAME = os.environ["RESOURCE_GROUP_NAME"]

        poller = compute_client.virtual_machines.begin_start(
            RESOURCE_GROUP_NAME,
            VM_NAME
        )

        vm_result = poller.result()
    else:
        print("The server is up.")
    sleep(10)