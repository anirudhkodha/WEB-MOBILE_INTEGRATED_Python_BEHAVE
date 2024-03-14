import os
import yaml

current_dir = os.path.dirname(os.path.abspath(__file__))
test_settings_path = os.path.join(current_dir, 'test_settings.yml')

with open(test_settings_path) as f:
    script_settings = yaml.safe_load(f)
