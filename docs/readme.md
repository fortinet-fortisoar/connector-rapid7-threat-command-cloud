## About the connector

Rapid7 Threat Command Cloud is a digital risk protection and external threat intelligence platform that helps
organizations monitor, detect, and mitigate threats originating outside their perimeters (web, deep web, dark web).
<p>This document provides information about the Rapid7 Threat Command Cloud Connector, which facilitates automated interactions, with a Rapid7 Threat Command Cloud server using FortiSOAR&trade; playbooks. Add the Rapid7 Threat Command Cloud Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Rapid7 Threat Command Cloud.</p>

### Version Information

Connector Version: 1.1.1

Authored By: Fortinet

Contributor: anonyges

Certified: No

## Release Notes for version 1.1.1

Following enhancements have been made to the Rapid7 Threat Command Cloud Connector in version 1.1.1:
<ul>
<li><code>Get Alerts List</code> action now supports the <code>Found Date From</code> and <code>Found Date To</code> parameters.</li>
</ul>

## Installing the connector

<p>Use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command to install connectors from an SSH session:</p>

```
sudo yum install cyops-connector-rapid7-threat-command-cloud
```

## Prerequisites to configuring the connector

- You must have the URL of Rapid7 Threat Command Cloud server to which you will connect and perform automated operations
  and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Rapid7 Threat Command Cloud server.

## Minimum Permissions Required

- N/A

## Configuring the connector

For the procedure to configure a connector,
click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Rapid7 Threat Command Cloud</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Rapid7 server to connect and perform automated operations.<br>
<tr><td>Account ID<br></td><td>Specify the account ID to connect to the endpoint and perform automated operations<br>
<tr><td>API Key<br></td><td>Specify the API Key to connect to the endpoint and perform automated operations<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks and you can also use the annotations to access
operations:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get IOC Sources<br></td><td>Retrieve a list of IOC sources from rapid7 threat command cloud server.<br></td><td>get_ioc_sources <br/>Investigation<br></td></tr>
<tr><td>Get IOCs by Filter<br></td><td>Retrieve a list of IOC's from the Rapid7 Threat Command cloud server based on the Last Updated From parameter you specified.<br></td><td>get_iocs_by_filter <br/>Investigation<br></td></tr>
<tr><td>Get IOC by Value<br></td><td>Retrieve a specific IOC details from rapid7 threat command cloud server based on the IOC value parameter you have specified.<br></td><td>get_ioc_by_value <br/>Investigation<br></td></tr>
<tr><td>Add IOCs to Source<br></td><td>Add IOC's to the specified source in the Rapid7 Threat Command cloud server using the provided source ID and IOC value parameters.<br></td><td>add_iocs_to_source <br/>Investigation<br></td></tr>
<tr><td>Change IOC Severity<br></td><td>Change IOC <br></td><td>change_ioc_severity <br/>Investigation<br></td></tr>
<tr><td>Get CVEs by IDs<br></td><td>Retrieve CVE details from the Rapid7 Threat Command cloud server using the CVE IDs you provided.<br></td><td>get_cves_by_ids <br/>Investigation<br></td></tr>
<tr><td>Get CVEs List from Account<br></td><td>Retrieve a list of CVEs from the Rapid7 Threat Command cloud server based on the Publish Date From parameter you specified.<br></td><td>get_cves_list_from_account <br/>Investigation<br></td></tr>
<tr><td>Get Alerts List<br></td><td>Retrieve list of alerts from the Rapid7 Threat Command cloud server based on the filter parameters you specified.<br></td><td>get_alerts_list <br/>Investigation<br></td></tr>
<tr><td>Get Alert Details<br></td><td>Retrieve alert details from the Rapid7 Threat Command cloud server using the alert ID you provided.<br></td><td>get_alert_by_id <br/>Investigation<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>generic_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get IOC Sources

#### Input parameters

None.

#### Output

The output contains a non-dictionary value.

### operation: Get IOCs by Filter

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Last Updated From<br></td><td>Select a date and time to retrieve results that include only items last updated after the specified timestamp.<br>
</td></tr><tr><td>Offset<br></td><td>Specify the number of records to skip when retrieving records from rapid7 threat command cloud server.<br>
</td></tr><tr><td>Page Size<br></td><td>Specify the maximum number of results this operation should return, per page, in the response.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Get IOC by Value

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IOC<br></td><td>Specify the IOC value based on which you want to retrieve details from rapid7 threat command cloud server.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Add IOCs to Source

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Source ID<br></td><td>Specify the ID of the source based on which you want to add IOC's.<br>
</td></tr><tr><td>IOCs<br></td><td>Specify a comma-separated list of IOC's to add to the source in the Rapid7 Threat Command cloud server.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Change IOC Severity

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IOC<br></td><td>Specify the IOC value for which you want to update the severity in the Rapid7 Threat Command cloud server.<br>
</td></tr><tr><td>Severity<br></td><td>Select the severity level you want to assign to the IOC. Available options are: High, Medium, or Low.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Get CVEs by IDs

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>CVE IDs<br></td><td>Specify the list of CVE IDs for which you want to retrieve details from the Rapid7 Threat Command cloud server.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Get CVEs List from Account

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Publish Date From<br></td><td>Select a date and time to retrieve results that include only items published after the specified timestamp.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Get Alerts List

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Alert Type<br></td><td>Select one or more alert type from the following options to filter alerts: "AttackIndication", "DataLeakage", "Phishing", "BrandSecurity", "ExploitableData", "vip"<br>
</td></tr><tr><td>Severity<br></td><td>Select one or more severity from the following options to filter alerts: "High", "Medium", and "Low"<br>
</td></tr><tr><td>Source Type<br></td><td>Select one or more source type from the following options to filter alerts: "ApplicationStores", "BlackMarkets", "HackingForums", "SocialMedia", "PasteSites", and "Others"<br>
</td></tr><tr><td>Network Type<br></td><td>Select one or more network type from the following options to filter alerts: "ClearWeb", and "DarkWeb"<br>
</td></tr><tr><td>Matched Asset Value<br></td><td>Specify the matched asset value to use when filtering alerts.<br>
</td></tr><tr><td>Tags<br></td><td>Specify the tags based on which you want to filter alerts.<br>
</td></tr><tr><td>Remediation Status<br></td><td>Select one or more remediation status from the following options to filter alert: "InProgress", "Pending", "CancellationInProgress", "Cancelled", "CompletedSuccessfully", and "Failed"<br>
</td></tr><tr><td>Source Date From<br></td><td>Select a date and time to retrieve results that include only items with a source date after the specified timestamp.<br>
</td></tr><tr><td>Source Date To<br></td><td>Select a date and time to retrieve results that include only items with a source date before the specified timestamp.<br>
</td></tr><tr><td>Found Date From<br></td><td>Select a date and time to retrieve results that include only items with a found date after the specified timestamp.<br>
</td></tr><tr><td>Found Date To<br></td><td>Select a date and time to retrieve results that include only items with a found date before the specified timestamp.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Get Alert Details

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Alert ID<br></td><td>Specify the alert ID for which you want to retrieve details from the Rapid7 Threat Command cloud server.<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

### operation: Execute an API Request

#### Input parameters

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options: 

GET

PUT

POST

DELETE

PATCH

HEAD

OPTIONS

TRACE<br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be /images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

## Included playbooks

The `Sample - Rapid7 Threat Command Cloud - 1.1.1` playbook collection comes bundled with the Rapid7 Threat Command
Cloud connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled
playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Rapid7 Threat Command
Cloud connector.

- Add IOCs to Source
- Change IOC Severity
- Execute an API Request
- Get Alerts List
- Get CVEs List from Account
- Get CVEs by IDs
- Get IOC Sources
- Get IOC by Value
- Get IOCs by Filter
- Get Alert Details

---
**Note**:

If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and
move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and
delete.

---