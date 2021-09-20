from airflow.plugins_manager import AirflowPlugin
from hubspot_plugin.hooks.hubspot_hook import HubspotHook
from hubspot_plugin.operators.hubspot_to_s3_operator import HubspotToS3Operator


class HubspotPlugin(AirflowPlugin):
    name = "hubspot_plugin"
    operators = [HubspotToS3Operator]
    hooks = [HubspotHook]
