import fiftyone as fo
# dataset zoo with common datasets
import fiftyone.zoo as foz

video = foz.load_zoo_dataset("quickstart-video")
print("dataset contents", video)

# Launch app
session = fo.launch_app(video, port=5152)
