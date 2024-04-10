Link to the issue: https://github.com/renovatebot/renovate/discussions/28243

## Reproduction steps:


1. Run the server:
```
pip install -r example-server/requirements.txt
python example-server/app.py
```

2. Execute renovate command

3. Observe server logs


Tested on version `37.279.4`

## Current behaviour:
After executing `LOG_LEVEL=debug renovate --platform=local` I get 401 response from Databricks. My suspection is that the token may not be set correctly.


## Expected behaviour:
Token is set properly and status code 200 is receiced from Databricks.

As a working workaround I used `{
"allowedHeaders": [
"Authorization"
]
}` global config and
```
"hostRules": [{
"matchHost": "https://workspace_id.cloud.databricks.com",
"headers": {
   "Authorization": "Bearer dapifaketoken"
},
```
but there are issues with encrypting the header. It returns status code 200.

### Couple of additional notes:
- `defaultRegistryUrlTemplate` has also been anonymized and this url does not exist (`workspace_id` should be replaced)
- `token` added to hostRules is for demonstrating purposes only it won't work
- `matchHost` also includes workspace_id that should be replaced with something else.

Execute command:
`LOG_LEVEL=debug renovate --platform=local`
