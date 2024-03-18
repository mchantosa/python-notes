# Environment Variables
[home](readme.md)

```python
    import os
    #This will error of the STAGE env variable is empty
    #stage = os.environ["STAGE"].upper()

    stage = os.getenv("STAGE", "dev").upper()   #set dev as a default
    output = f"We're running in {stage}"

    if stage.startswith("PROD"):
        output = "DANGER! " + output
```
```shell
    STAGE=staging python ./code/env_vars.py 
    #   Output: We're running in STAGING

    STAGE=production python ./code/env_vars.py 
    #   Output: DANGER! We're running in PRODUCTION

    python ./code/env_vars.py   
    #   We're running in DEV
```