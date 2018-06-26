import logging
try:
    from lib.VaultClient import VaultClient
except ImportError:
    from vaultmanager.lib.VaultClient import VaultClient


class VaultManagerModule:
    logger = None
    base_logger = None
    subparser = None
    parsed_args = None
    arg_parser = None
    module_name = None

    def __init__(self, base_logger, subparsers):
        """
        :param base_logger: main class name
        :type base_logger: string
        :param subparsers: list of all subparsers
        :type subparsers: argparse.ArgumentParser.add_subparsers()
        """
        self.base_logger = base_logger
        self.logger = logging.getLogger(base_logger + "." + self.__class__.__name__)
        self.logger.debug("Initializing VaultManagerLDAP")
        self.initialize_subparser(subparsers)

    def initialize_subparser(self, subparsers):
        """
        Add the subparser of this specific module to the list of all subparsers

        :param subparsers: list of all subparsers
        :type subparsers: argparse.ArgumentParser.add_subparsers()
        :return:
        """
        self.logger.debug("Initializing subparser")
        self.module_name = self.__class__.__name__.replace("VaultManager", "").lower()
        self.subparser = subparsers.add_parser(self.module_name, help=self.module_name + ' management')
        #self.subparser.add_argument("--pull", help="Pull local policies to Vault", nargs=1)
        self.subparser.set_defaults(module_name=self.module_name)

    def run(self, arg_parser, parsed_args):
        """
        Module entry point

        :param parsed_args: Arguments parsed fir this module
        :type parsed_args: argparse.ArgumentParser.parse_args()
        """
        self.parsed_args = parsed_args
        self.arg_parser = arg_parser
        self.logger.debug("Module " + self.module_name + " started")
        print(self.parsed_args)
