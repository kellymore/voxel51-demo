import fiftyone as fo
# dataset zoo with common datasets
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")
print("dataset contents", dataset)

# Launch app
session = fo.launch_app(dataset, port=5151)


