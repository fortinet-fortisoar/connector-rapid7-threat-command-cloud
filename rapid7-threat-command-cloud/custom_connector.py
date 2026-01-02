"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
import arrow
from connectors.core.connector import get_logger
from typing import Union, Literal, Optional
from requests.auth import HTTPBasicAuth

logger = get_logger('rapid7-threat-command-cloud')


class CustomConnector:
    def __init__(self, url: str, account_id: str, api_key: str, verify_ssl: bool = False):
        self.url = url
        self.account_id = account_id
        self.api_key = api_key
        self.verify_ssl = verify_ssl

        self._check_url(self.url)

    def _check_url(self, url: str):
        if not (url.startswith("https://") or url.startswith("http://")):
            raise Exception("config url must start with 'https://' or 'http://'")

        if url.endswith("/"):
            raise Exception("config url must not end with '/'")

    def _check_api_endpoint(self, api_endpoint: str):
        if not api_endpoint.startswith("/"):
            raise Exception("param api_endpoint must startswith '/'")

    def _delete_none_dict(self, _d: Union[dict, list, None]) -> Union[dict, list, None]:
        return {k: v for k, v in _d.items() if v is not None}

    def _convert_fsr_datetime_to_iso_8601(self, date: Union[str, None]) -> Optional[str]:
        if date == None:
            return None
        if date == "":
            return None
        return arrow.get(date).format("YYYY-MM-DDTHH:mm:ss.SSS") + "Z"

    def _convert_fsr_datetime_to_timestamp(self, date: Union[str, None]) -> Optional[float]:
        if date == None:
            return None
        if date == "":
            return None
        return arrow.get(date).timestamp() * 1000

    def _check_health(self):
        data = self.get_account_used_credits({})
        if not data:
            raise Exception("/public/v1/account/used-credits did not return any data, probably authentication error.")

    def generic_api_call(
            self,
            method: Literal["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"],
            api_endpoint: str,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            json_data: Union[dict, list, None] = None,
    ) -> dict:
        self._check_api_endpoint(api_endpoint)
        url = self.url + api_endpoint

        headers = headers or {}
        headers["content-type"] = "application/json"

        authorization = (self.account_id, self.api_key)

        params_new = self._delete_none_dict(params) if params else None
        json_data_new = self._delete_none_dict(json_data) if json_data else None

        resp = requests.request(
            method, url, headers=headers, auth=authorization, params=params_new, json=json_data_new,
            verify=self.verify_ssl
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise Exception(resp.content)

    def get_account_used_credits(self, params: dict) -> dict:
        endpoint = "/public/v1/account/used-credits"
        return self.generic_api_call("GET", endpoint)

    def get_ioc_sources(self) -> dict:
        """IOCs - Get IOC sources"""
        endpoint = "/public/v1/iocs/sources"
        return self.generic_api_call("GET", endpoint)

    def get_iocs_by_filter(self, lastUpdatedFrom: str, limit: Optional[int] = None,
                           offset: Optional[int] = None) -> dict:
        """IOCs - Get IOCs by filter"""
        endpoint = "/public/v3/iocs"
        lastUpdatedFrom_conv = self._convert_fsr_datetime_to_iso_8601(lastUpdatedFrom)
        params = {"lastUpdatedFrom": lastUpdatedFrom_conv, "limit": limit, "offset": offset}
        return self.generic_api_call("GET", endpoint, params=params)

    def get_ioc_by_value(self, iocValue: str) -> dict:
        """IOCs - Get IOC by value"""
        endpoint = "/public/v3/iocs/ioc-by-value"
        params = {"iocValue": iocValue}
        return self.generic_api_call("GET", endpoint, params=params)

    def add_iocs_to_source(self, sourceID: str, iocs: dict) -> dict:
        """IOCs - Add IOCs to source"""
        endpoint = f"/public/v1/iocs/add-iocs-to-source/{sourceID}"
        json_data = iocs
        return self.generic_api_call("POST", endpoint, json_data=json_data)

    def change_ioc_severity(self, iocValue: str, severity: str) -> dict:
        """IOCs - Change IOC severity"""
        endpoint = "/public/v2/iocs/severity"
        json_data = [{"iocValue": iocValue, "severity": severity}]
        return self.generic_api_call("POST", endpoint, json_data=json_data)

    def get_cves_by_ids(self, cveList: list) -> dict:
        """Cves - Get CVEs by IDs"""
        endpoint = "/public/v1/cves/get-cves"
        json_data = {"CveList": cveList}
        return self.generic_api_call("POST", endpoint, json_data=json_data)

    def get_cves_list_from_account(self, publishDateFrom: Optional[str] = None) -> dict:
        """Cves - Get CVEs list from account"""
        endpoint = "/public/v1/cves/get-cves-list"
        params = {
            "publishDateFrom": self._convert_fsr_datetime_to_iso_8601(publishDateFrom) if publishDateFrom else None,
        }
        return self.generic_api_call("GET", endpoint, params=params)

    def get_alerts_list(
            self,
            alertType: Optional[
                list[Literal["AttackIndication", "DataLeakage", "Phishing", "BrandSecurity", "ExploitableData", "vip"]]
            ] = None,
            severity: Optional[list[Literal["High", "Medium", "Low"]]] = None,
            sourceType: Optional[
                list[Literal[
                    "ApplicationStores", "BlackMarkets", "HackingForums", "SocialMedia", "PasteSites", "Others"]]
            ] = None,
            networkType: Optional[list[Literal["ClearWeb", "DarkWeb"]]] = None,
            matchedAssetValue: Optional[str] = None,
            tags: Optional[str] = None,
            remediationStatus: Optional[
                list[Literal[
                    "InProgress", "Pending", "CancellationInProgress", "Cancelled", "CompletedSuccessfully", "Failed"]]
            ] = None,
            sourceDateFrom: Optional[str] = None,
            sourceDateTo: Optional[str] = None,
            foundDateFrom: Optional[str] = None,
            foundDateTo: Optional[str] = None
    ) -> dict:
        """Alerts - Get alerts list"""
        endpoint = "/public/v2/data/alerts/alerts-list"
        params = {
            "alertType": ",".join(alertType) if alertType else None,
            "severity": ",".join(severity) if severity else None,
            "sourceType": ",".join(sourceType) if sourceType else None,
            "networkType": ",".join(networkType) if networkType else None,
            "matchedAssetValue": matchedAssetValue if matchedAssetValue else None,
            "tags": tags if tags else None,
            "remediationStatus": ",".join(remediationStatus) if remediationStatus else None,
            "sourceDateFrom": self._convert_fsr_datetime_to_timestamp(sourceDateFrom) if sourceDateFrom else None,
            "sourceDateTo": self._convert_fsr_datetime_to_timestamp(sourceDateTo) if sourceDateTo else None,
            "foundDateFrom": self._convert_fsr_datetime_to_timestamp(foundDateFrom) if foundDateFrom else None,
            "foundDateTo": self._convert_fsr_datetime_to_timestamp(foundDateTo) if foundDateTo else None
        }
        return self.generic_api_call("GET", endpoint, params=params)

    def get_alert_by_id(self, alertID: str) -> dict:
        """Alerts - Get alerts list"""
        endpoint = f"/public/v1/data/alerts/get-complete-alert/{alertID}"
        return self.generic_api_call("GET", endpoint)
