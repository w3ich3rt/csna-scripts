#!/usr/bin/python3
"""
DESCRIPTION:
Get the current license state of Cisco Secure Network Analytics (CSNA) via API.

License: open source - feel free to use, fork and develop!

Created: 03.07.2023 by Ulli Weichert
State: Currently in playmode.
"""

# IMPORTS
import json
import requests


# FUNCTIONS
class CiscoSecureNetworkAnalyticsAPI:
    """
    Class to handle the CSNA API.
    """

    def __init__(self, csna_ip):
        self.csna_ip = csna_ip
        self.csna_api_url = f"https://{csna_ip}"
        self.csna_api_auth_endpoint = "/token/v2/authenticate"
        self.csna_api_license_endpoint = "/cm/licensing/status"

    def get_csna_api_token(self):
        """
        Get the CSNA API token.
        """
        # Get the token
        api_request = requests.Session()
        request_data = {
            "username": "admin",
            "password": "password"
        }
        response = api_request.request("POST",
                                       url=f"{self.csna_api_url}{self.csna_api_auth_endpoint}",
                                       data=json.dumps(request_data),
                                       verify=False,
                                       timeout=5
                                       )
        return response.cookies

    def get_license_state(self):
        """
        Get the current license state.
        """
        response = requests.get(
            url=f"{self.csna_api_url}{self.csna_api_license_endpoint}",
            cookies=self.get_csna_api_token(),
            verify=False,
            timeout=5
        )
        return response.json()


# MAIN
if __name__ == "__main__":
    CSNA_IP = "PUT.IP.ADR.HERE"
    csna_api = CiscoSecureNetworkAnalyticsAPI(CSNA_IP)
    print(csna_api.get_license_state())
