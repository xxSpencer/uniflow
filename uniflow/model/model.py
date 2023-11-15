"""Model Module."""
import copy
import json
from typing import Any, Dict, List

from uniflow.model.config import ModelConfig
from uniflow.model.server import ModelServerFactory


class Model:
    """Model Class."""

    def __init__(
        self,
        model_name: str,
        model_config: ModelConfig,
        few_shot_template: Dict[str, Any],
    ) -> None:
        """Initialize Model class.

        Args:
            model_name (str): Model name.
            model_config (ModelConfig): Model config.
            few_shot_template (Dict[str, Any]): Few shot template.
        """
        model_server_cls = ModelServerFactory.get(model_name)
        self._model_server = model_server_cls(model_config)
        self._few_shot_template = few_shot_template

    def _serialize(self, data: Dict[str, Any]) -> str:
        """Serialize data.

        Args:
            data (Dict[str, Any]): Data to serialize.

        Returns:
            str: Serialized data.
        """
        few_shot_template = copy.deepcopy(self._few_shot_template)
        few_shot_template.update(data)
        return json.dumps(few_shot_template)

    def _deserialize(self, data: List[str]) -> List[Dict[str, Any]]:
        """Deserialize data.

        Args:
            data (str): Data to deserialize.

        Returns:
            Dict[str, Any]: Deserialized data.
        """
        return [json.loads(d) for d in data]

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Run model.

        Args:
            data (Dict[str, Any]): Data to run.

        Returns:
            Dict[str, Any]: Output data.
        """
        data = self._serialize(data)
        data = self._model_server(data)
        data = self._deserialize(data)
        return data
