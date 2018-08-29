import json
import serializer

class JsonSerializer(serializer.Serializer):
    EXTENSION = '.json'

    def _load(self):
        with open(self.filename, 'rt') as f:
            return json.load(f)

    def save(self, obj):
        with open(self.filename, 'wt') as f:
            json.dump(obj, f)
