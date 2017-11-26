# End-to-end Integration

For simplicity, we will run the following commands within Azure Cloud Shell. The Azure Cloud Shell is a free Bash shell that you can run directly within the Azure portal. It has the Azure CLI preinstalled and configured to use with your account.  You can also run these on your host machine with the following link: [Install Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli). If you use the Azure CLI 2.0 from your host machine, make sure that you run `az login` prior to running any commands.

The Cloud Shell looks like this within the Azure Portal:

![](https://docs.microsoft.com/en-us/azure/includes/media/cloud-shell-try-it/cloud-shell-menu.png)

The button launches an interactive shell that you can use to run all of the steps in this topic:

![](https://docs.microsoft.com/en-us/azure/includes/media/cloud-shell-try-it/cloud-shell-safari.png)

Sign in to your Azure account and select your subscription.

From here on, the main follow we will follow is `deploy.sh`


## Cleanup

To ensure you're not wasting any resources after class you can destroy all resources within the resource we created.

Run the following:

```bash
host$ ./destroy.sh
```