import pandas as pd

from td.client import TDClient
from td.utils import TDUtilities

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union


class TradingBot:
    def __init__(self, client_id: str, redirect_url: str, credentials_path: str = None,
                 trading_account: str = None) -> None:
        """
    The __init__ function is called when the class is instantiated.
    It sets up the instance of the class with all of its attributes and methods.
    The __init__ function takes in a client_id, redirect_url, credentials_path, and trading account as arguments.
    These are used to create an authenticated session with TD Ameritrade's API.

    :param self: Represent the instance of the class
    :param client_id: str: Identify the application
    :param redirect_url: str: Redirect the user to a specific url after they have authenticated their account
    :param credentials_path: str: Store the credentials for the td ameritrade api
    :param trading_account: str: Specify the account you want to use
    :return: None, which is a special value in python that represents the absence of a value
    :doc-author: Trelent
    """
        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_url: str = redirect_url
        self.credentials_path: str = credentials_path
        self.session: TDClient = self._create_session()
        self.trades: Dict = {}
        self.historical_prices: Dict = {}
        self.stock_frame = None

    def _create_sesion(self) -> TDClient:
        """
    The _create_sesion function is a helper function that creates a TDClient object.
    The TDClient object is used to make requests to the TDAmeritrade API.


    :param self: Represent the instance of the class
    :return: A tdclient object
    :doc-author: Trelent
    """
        td_client = TDClient(
                client_id=self.client_id,
                redirect_uri=self.redirect_url,
                credentials_path=self.credentials_path
            )

        td_client.login()

        return td_client

    @property
    def pre_market_open(self) -> bool:
        """
    The pre_market_open function checks to see if the current time is between 12:00 and 13:30 UTC.
    If it is, then the function returns True. If not, then it returns False.

    :param self: Represent the instance of the class
    :return: True if the current time is between 12:00 and 13:30 utc
    :doc-author: Trelent
    """
        pre_market_start_time = datetime.now().replace(hour=12, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_start_time >= right_now >= pre_market_start_time:
            return True
        return False

    @property
    def post_market_open(self) -> bool:
        """
    The post_market_open function checks to see if the current time is between market close and post-market close.
        If it is, then it returns True. Otherwise, it returns False.

    :param self: Represent the instance of the class
    :return: A boolean value
    :doc-author: Trelent
    """
        post_market_end_time = datetime.now().replace(hour=22, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if post_market_end_time >= right_now >= market_end_time:
            return True
        return False

    @property
    def regural_market_open(self) -> bool:
        """
    The regural_market_open function checks to see if the current time is between 1pm and 8pm UTC.
    If it is, then it returns True. If not, then it returns False.

    :param self: Represent the instance of the class
    :return: A boolean value
    :doc-author: Trelent
    """
        market_start_time = datetime.now().replace(hour=13, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_end_time >= right_now >= market_start_time:
            return True
        return False

    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List[dict]:
        pass

    def run(self):
        pass
