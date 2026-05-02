import yaml
from pathlib import Path

def load_yaml_config(path: str) -> dict:
    config_path = Path(path)
    if not config_path.exists():
        return {}
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            return config if config is not None else {}
    except yaml.YAMLError as e:
        print(f"Error loading YAML config from {path}: {e}")
        return {}
    except Exception as e:
        print(f"Unexpected error loading config from {path}: {e}")
        return {}
