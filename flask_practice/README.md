# Flask
- Generate a URL to do something
- Required packages
  - flask
  - pymysql
  ```
  pip install flask pymysql
  ```

1. Build simple web server
2. Create router (GET/POST)
3. Trigger custom function
4. Template

# Note:
- REST API
  -> URL API, trigger something via URL
- RESTful API
  -> Pretty format URL
  - Example 1: [GET] URL/api/v2/department/emp_id/<emd_id: str>
  - Example 2: [GET] URL/api/v2/department/dep_id/<dep_id: str>/emp_id/<emd_id: str>
  -> CRUD:
    - C: creat -> INSERT -> POST
    - R: read -> SELECT -> GET
    - U: update -> UPDATE -> UPDATE
    - D: delete -> DELETE -> DELETE
