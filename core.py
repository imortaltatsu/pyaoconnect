"""
Core AOConnect functionality - streamlined interface, delegates to aopy_connect
"""

import os
import json
from typing import Dict, List, Optional, Any
from aopy_connect import AOConnectWrapper

class AOConnect:
    """
    Streamlined Python wrapper for AO Connect, using aopy_connect.AOConnectWrapper
    """
    def __init__(self, wallet_path: Optional[str] = None):
        self._wrapper = AOConnectWrapper(wallet_path)

    def create_wallet(self) -> Dict[str, Any]:
        return self._wrapper.create_wallet()

    def spawn(self, source: str, tags: Optional[List[Dict[str, str]]] = None, 
              scheduler: Optional[str] = None, data: Optional[str] = None) -> Dict[str, Any]:
        return self._wrapper.spawn_process(source, tags=tags, scheduler=scheduler, data=data)

    def send(self, process_id: str, data: str, tags: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
        return self._wrapper.send_message(process_id, data, tags=tags)

    def results(self, process_id: str, options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._wrapper.get_results(process_id, options=options)

    def dryrun(self, process_id: str, data: str, tags: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
        return self._wrapper.dryrun(process_id, data, tags=tags) 