from datetime import timedelta
from typing import Optional

from lafontaine.feature_director.feature.base_feature import BaseFeature


class FeatureDirector:

    def __init__(self, genre, max_length: timedelta, all_features):
        self.genre = genre
        self.max_length = max_length
        self.all_features = all_features

    def check_for_all_features(self, frame) -> Optional[BaseFeature]:
        return self._check_for_features(frame)

    def _check_for_features(self, frame):
        for f in self.all_features:
            result = f.check_feature(frame)

            if result.result:
                return result

        return None
