from django.test import TestCase


class TestNetworkCoverageView(TestCase):
    def test_success(self):
        response = self.client.get("/api", {"q": "42+rue+papernest+75011+Paris"}, follow=True)
        print(f"RESPONSE: {response.json()}\n")
        assert not response.json()["Free mobile"]["2G"]

    def test_wrong_geographic_match(self):
        response = self.client.get("/api", {"q": "test"}, follow=True)
        print(f"RESPONSE: {response.json()}\n")
        assert response.json() == {"ERROR_CODE": "Wrong geographic match"}
