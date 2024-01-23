"""All Uniflow Clients"""

from dataclasses import asdict
from typing import Any, List, Mapping, Optional

from uniflow.flow.config import ExtractConfig, RaterConfig, TransformConfig
from uniflow.flow.server import ExtractServer, RaterServer, TransformServer, ExpandReduceServer

class ExpandReduceClient:
    def __init__(self, config: Optional[dict] = {"test_key":"test_value"}) -> None:
        self.__config = config
        # print(self.__config)
        self._server=ExpandReduceServer((self.__config))
    def run(self, input_list: List[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
        output = self._server.run(input_list)
        return output

class ExtractClient:
    """Uniflow Extract Client"""

    def __init__(self, config: ExtractConfig) -> None:
        """Client constructor

        Args:
            config (Config): Config for the flow

        """
        self._config = config
        self._server = ExtractServer(asdict(self._config))

    def run(self, input_list: List[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
        """
        Run the flow

        Args:
            input_list (List[Mapping[str, Any]]): List of inputs to the flow

        Returns:
            List[Mapping[str, Any]]: List of outputs from the flow
        """
        # convert config to dict for future remote calls
        output = self._server.run(input_list)
        return output

    def async_run(self) -> None:
        """Run the flow asynchronously"""
        # TODO: Implement async client
        print("Client running async")


class TransformClient:
    """Uniflow Transform Client"""

    def __init__(self, config: TransformConfig) -> None:
        """Client constructor

        Args:
            config (Config): Config for the flow

        """
        self._config = config
        self._server = TransformServer(asdict(self._config))

    def run(self, input_list: List[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
        """
        Run the flow

        Args:
            input_list (List[Mapping[str, Any]]): List of inputs to the flow

        Returns:
            List[Mapping[str, Any]]: List of outputs from the flow
        """
        # convert config to dict for future remote calls
        output = self._server.run(input_list)
        return output

    def async_run(self) -> None:
        """Run the flow asynchronously"""
        # TODO: Implement async client
        print("Client running async")


class RaterClient:
    """Uniflow Rater Client"""

    def __init__(self, config: RaterConfig) -> None:
        """Client constructor

        Args:
            config (Config): Config for the flow

        """
        self._config = config
        self._server = RaterServer(asdict(self._config))

    def run(self, input_list: List[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
        """
        Run the flow

        Args:
            input_list (List[Mapping[str, Any]]): List of inputs to the flow

        Returns:
            List[Mapping[str, Any]]: List of outputs from the flow
        """
        # convert config to dict for future remote calls
        output = self._server.run(input_list)
        return output

    def async_run(self) -> None:
        """Run the flow asynchronously"""
        # TODO: Implement async client
        print("Client running async")
