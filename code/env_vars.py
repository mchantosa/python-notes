import os
#This will error of the STAGE env variable is empty
#stage = os.environ["STAGE"].upper()

stage = os.getenv("STAGE", "dev").upper()   #set dev as a default
output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER! " + output

print(output)