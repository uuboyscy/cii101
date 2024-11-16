1. Prepare data
   - URL?para=123
   - Headers
   - Cookies
   - Form data
2. Request
    - GET -> requests.get(url, headers, cookies)
    - POST -> requests.post(url, headers, cookies, form_data)
3. Response
    - HTML string -> BeautifulSoup
    - JSON
      - requests.post().json() -> Dist | List
      - json.loads(requests.post().text) -> Dist | List
4. Selenium
