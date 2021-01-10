import csv
from urllib.parse import urljoin

import requests
from django.http.response import JsonResponse
from django.views import View

from api.static import NetworkCoverage
from logger import logger
from network_coverage.settings import OPERATORS_CSV_PATH
from utils.static import API_ADDRESS_URL


class NetworkCoverageView(View):
    def get(self, request, *args, **kwargs):
        query_params = request.GET.get("q")
        try:
            cities = self.find_cities(query_params)
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Get error from search address API: {e}")
            return JsonResponse({"ERROR_CODE": "Error occurred."})
        logger.info(f"Matched cities: {cities}")
        if len(cities) != 1:
            return JsonResponse({"ERROR_CODE": "Wrong geographic match"})
        city_match = list(cities)[0]
        operator_coverage = self.find_operator_coverage(city=city_match)
        logger.info(f"Operator coverage results: {operator_coverage}")
        return JsonResponse(operator_coverage)

    def find_operator_coverage(self, city: str):
        response_data = {}
        with open(OPERATORS_CSV_PATH, mode="r", encoding="latin-1") as file:
            reader = csv.reader(file, delimiter=";")
            row_number = 0
            for row in reader:
                if row_number >= 1:
                    if row[9] == city:
                        response_data = self.calc_operator_coverage(
                            operator_coverage_results=response_data,
                            operator=row[6],
                            network_coverage=NetworkCoverage(
                                n_2G=bool(int(row[3])), n_3G=bool(int(row[4])), n_4G=bool(int(row[5]))
                            ),
                        )
                row_number += 1
        return response_data

    @staticmethod
    def calc_operator_coverage(operator_coverage_results: dict, operator: str, network_coverage: NetworkCoverage):
        if operator_coverage_results.get(operator):
            if not operator_coverage_results[operator]["2G"] and network_coverage.n_2G:
                operator_coverage_results[operator]["2G"] = True

            if not operator_coverage_results[operator]["3G"] and network_coverage.n_3G:
                operator_coverage_results[operator]["3G"] = True

            if not operator_coverage_results[operator]["4G"] and network_coverage.n_4G:
                operator_coverage_results[operator]["4G"] = True
        else:
            operator_coverage_results[operator] = {
                "2G": network_coverage.n_2G,
                "3G": network_coverage.n_3G,
                "4G": network_coverage.n_4G,
            }
        return operator_coverage_results

    @staticmethod
    def find_cities(query_params: str):
        response = requests.get(urljoin(API_ADDRESS_URL, "search"), params={"q": query_params})
        response.raise_for_status()
        logger.info(f"Response from address API: {response.json()}")
        return set([feature["properties"]["city"] for feature in response.json()["features"]])
