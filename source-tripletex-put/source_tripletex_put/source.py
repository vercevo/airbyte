import sys
from airbyte_cdk.sources import AbstractSource
from .streams import CustomersStream


class SourceMyApi(AbstractSource):
    def check_connection(self, logger, config):
        try:
            stream = CustomersStream(config=config)
            next(stream.read_records(sync_mode=None))
            return True, None
        except Exception as e:
            return False, str(e)

    def streams(self, config):
        return [CustomersStream(config=config)]


def main():
    from airbyte_cdk.entrypoint import launch
    source = SourceMyApi()
    launch(source, sys.argv[1:])
    