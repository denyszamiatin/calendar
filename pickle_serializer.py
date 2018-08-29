import pickle
import serializer


class PickleSerializer(serializer.Serializer):
    EXTENSION = '.pickle'

    def _load(self):
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

    def save(self, obj):
        with open(self.filename, 'wb') as f:
            pickle.dump(obj, f)