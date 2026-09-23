from datetime import timedelta


class FeatureWindows:
    """
    Standard time windows used by feature engineering.
    """

    LAST_HOUR = timedelta(hours=1)

    LAST_24_HOURS = timedelta(hours=24)

    LAST_7_DAYS = timedelta(days=7)

    LAST_30_DAYS = timedelta(days=30)

    LAST_90_DAYS = timedelta(days=90)