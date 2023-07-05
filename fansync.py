import httpx


class FanSync:
    _client = httpx.Client(http2=True)

    _sessionId = None
    _token = None

    def login(self, email, password):
        r = self._client.post('https://fanimation.apps.exosite.io/api:1/session',
                              json={"email": email, "password": password})

        if r.status_code != 200:
            print("Failed to login")

        print(r.json())
        _sessionId = r.json()["id"]
        _token = r.json()["token"]

    def fuzz(self, url, useAuth = False):

        headers = []
        if(useAuth):
            headers = self._getAuthHeader()

        methods = [
            self._client.get,
            self._client.head,
            self._client.post,
            self._client.put,
            # self._client.delete,
            self._client.options,
            self._client.patch
        ]

        ignoreCodes = set()
        ignoreCodes.add(404)
        ignoreCodes.add(415)

        for m in methods:

            r = m(url, headers=headers)
            if r.status_code in ignoreCodes:
                continue

            print("%s %s - %s" % (m.__name__.upper(), url, r.status_code))
            try:
                if r.content.strip() != "":
                    pass
                    print(r.content)
                    # print(r.headers)
            except:
                # Swallow
                pass



    def _getAuthHeader(self):
        return "Authorization: Bearer %s" % self._token
