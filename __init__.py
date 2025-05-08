import sys; sys.dont_write_bytecode=True
from ctypes import *
import struct
from enum import Enum
from typing import Literal as Lit
from datetime import *
# from getpass import getpass



# ======================================================================= #
# ================================ Types ================================ #
# ======================================================================= #
class TConnectorOrderType(Enum):
    Limit = 2
    Stop = 4
    Market = 1

class TConnectorOrderSide(Enum):
    Buy = 1
    Sell = 2

class TConnectorPositionType(Enum):
    DayTrade = 1
    Consolidated = 2

class SystemTime(Structure):
    _fields_ = [
        ("wYear", c_ushort),
        ("wMonth", c_ushort),
        ("wDayOfWeek", c_ushort),
        ("wDay", c_ushort),
        ("wHour", c_ushort),
        ("wMinute", c_ushort),
        ("wSecond", c_ushort),
        ("wMilliseconds", c_ushort)
    ]

class TConnectorAccountIdentifier(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("BrokerID", c_int),
        ("AccountID", c_wchar_p),
        ("SubAccountID", c_wchar_p),
        ("Reserved", c_int64)
    ]

class TConnectorAccountIdentifierOut(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("BrokerID", c_int),
        ("AccountID", c_wchar * 100),
        ("AccountIDLength", c_int),
        ("SubAccountID", c_wchar * 100),
        ("SubAccountIDLength", c_int),
        ("Reserved", c_int64)
    ]

class TConnectorAssetIdentifier(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("Ticker", c_wchar_p),
        ("Exchange", c_wchar_p),
        ("FeedType", c_ubyte)
    ]

class TConnectorAssetIdentifierOut(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("Ticker", c_wchar_p),
        ("TickerLength", c_int),
        ("Exchange", c_wchar_p),
        ("ExchangeLength", c_int),
        ("FeedType", c_ubyte)
    ]

class TConnectorOrderIdentifier(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("LocalOrderID", c_int64),
        ("ClOrderID", c_wchar_p)
    ]

class TConnectorSendOrder(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("AssetID", TConnectorAssetIdentifier),
        ("Password", c_wchar_p),
        ("OrderType", c_ubyte),
        ("OrderSide", c_ubyte),
        ("Price", c_double),
        ("StopPrice", c_double),
        ("Quantity", c_int64)
    ]

class TConnectorChangeOrder(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("OrderID", TConnectorOrderIdentifier),
        ("Password", c_wchar_p),
        ("Price", c_double),
        ("StopPrice", c_double),
        ("Quantity", c_int64)
    ]

class TConnectorCancelOrder(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("OrderID", TConnectorOrderIdentifier),
        ("Password", c_wchar_p)
    ]

class TConnectorCancelOrders(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("AssetID", TConnectorAssetIdentifier),
        ("Password", c_wchar_p)
    ]

class TConnectorCancelAllOrders(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("Password", c_wchar_p)
    ]

class TConnectorZeroPosition(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("AssetID", TConnectorAssetIdentifier),
        ("Password", c_wchar_p),
        ("Price", c_double),
        ("PositionType", c_ubyte)
    ]

class TConnectorTradingAccountOut(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("BrokerName", c_wchar_p),
        ("BrokerNameLength", c_int),
        ("OwnerName", c_wchar_p),
        ("OwnerNameLength", c_int),
        ("SubOwnerName", c_wchar_p),
        ("SubOwnerNameLength", c_int),
        ("AccountFlags", c_int)
    ]

class TConnectorTradingAccountPosition(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("AccountID", TConnectorAccountIdentifier),
        ("AssetID", TConnectorAssetIdentifier),
        ("OpenQuantity", c_int64),
        ("OpenAveragePrice", c_double),
        ("OpenSide", c_ubyte),
        ("DailyAverageSellPrice", c_double),
        ("DailySellQuantity", c_int64),
        ("DailyAverageBuyPrice", c_double),
        ("DailyBuyQuantity", c_int64),
        ("DailyQuantityD1", c_int64),
        ("DailyQuantityD2", c_int64),
        ("DailyQuantityD3", c_int64),
        ("DailyQuantityBlocked", c_int64),
        ("DailyQuantityPending", c_int64),
        ("DailyQuantityAlloc", c_int64),
        ("DailyQuantityProvision", c_int64),
        ("DailyQuantity", c_int64),
        ("DailyQuantityAvailable", c_int64),
        ("PositionType", c_ubyte)
    ]

class TConnectorOrder(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("OrderID", TConnectorOrderIdentifier),
        ("AccountID", TConnectorAccountIdentifier),
        ("AssetID", TConnectorAssetIdentifier),
        ("Quantity", c_int64),
        ("TradedQuantity", c_int64),
        ("LeavesQuantity", c_int64),
        ("Price", c_double),
        ("StopPrice", c_double),
        ("AveragePrice", c_double),
        ("OrderSide", c_ubyte),
        ("OrderType", c_ubyte),
        ("OrderStatus", c_ubyte),
        ("ValidityType", c_ubyte),
        ("Date", SystemTime),
        ("LastUpdate", SystemTime),
        ("CloseDate", SystemTime),
        ("ValidityDate", SystemTime),
        ("TextMessage", c_wchar_p)
    ]

class TConnectorOrderOut(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("OrderID", TConnectorOrderIdentifier),
        ("AccountID", TConnectorAccountIdentifierOut),
        ("AssetID", TConnectorAssetIdentifierOut),
        ("Quantity", c_int64),
        ("TradedQuantity", c_int64),
        ("LeavesQuantity", c_int64),
        ("Price", c_double),
        ("StopPrice", c_double),
        ("AveragePrice", c_double),
        ("OrderSide", c_ubyte),
        ("OrderType", c_ubyte),
        ("OrderStatus", c_ubyte),
        ("ValidityType", c_ubyte),
        ("Date", SystemTime),
        ("LastUpdate", SystemTime),
        ("CloseDate", SystemTime),
        ("ValidityDate", SystemTime),
        ("TextMessage", c_wchar_p),
        ("TextMessageLength", c_int)
    ]

class TConnectorTrade(Structure):
    _fields_ = [
        ("Version", c_ubyte),
        ("TradeDate", SystemTime),
        ("TradeNumber", c_uint),
        ("Price", c_double),
        ("Quantity", c_longlong),
        ("Volume", c_double),
        ("BuyAgent", c_int),
        ("SellAgent", c_int),
        ("TradeType", c_ubyte)
    ]

class TAssetID(Structure):
    _fields_ = [("ticker", c_wchar_p),
                ("bolsa", c_wchar_p),
                ("feed", c_int)]

class TGroupOffer(Structure):
    _fields_ = [("nPosition", c_int),
                ("nQtd", c_int),
                ("nOfferID", c_int),
                ("nAgent", c_int),
                ("sPrice", c_double),
                ("strDtOffer", c_int)]

class TGroupPrice(Structure):
    _fields_ = [("nQtd", c_int),
                ("nCount", c_int),
                ("sPrice", c_double)]

class TNewTradeCallback(Structure):
    _fields_ = [("assetId", TAssetID),
                ("date", c_wchar_p),
                ("tradeNumber", c_uint),
                ("price", c_double),
                ("vol", c_double),
                ("qtd", c_int),
                ("buyAgent", c_int),
                ("sellAgent", c_int),
                ("tradeType", c_int),
                ("bIsEdit", c_int)]

class TTheoreticalPriceCallback(Structure):
    _fields_ = [("assetId", TAssetID),
                ("dTheoreticalPrice", c_double),
                ("nTheoreticalQtd", c_uint)]

class TNewDailyCallback(Structure):
    _fields_ = [("tAssetIDRec", TAssetID),
                ("date", c_wchar_p),
                ("sOpen", c_double),
                ("sHigh", c_double),
                ("sLow", c_double),
                ("sClose", c_double),
                ("sVol", c_double),
                ("sAjuste", c_double),
                ("sMaxLimit", c_double),
                ("sMinLimit", c_double),
                ("sVolBuyer", c_double),
                ("sVolSeller", c_double),
                ("nQtd", c_int),
                ("nNegocios", c_int),
                ("nContratosOpen", c_int),
                ("nQtdBuyer", c_int),
                ("nQtdSeller", c_int),
                ("nNegBuyer", c_int),
                ("nNegSeller", c_int)]

class TNewHistoryCallback(Structure):
    _fields_ = [("assetId", TAssetID),
                ("date", c_wchar_p),
                ("tradeNumber", c_uint),
                ("price", c_double),
                ("vol", c_double),
                ("qtd", c_int),
                ("buyAgent", c_int),
                ("sellAgent", c_int),
                ("tradeType", c_int)]

class TProgressCallBack(Structure):
    _fields_ = [("assetId", TAssetID),
                ("nProgress", c_int)]

class TNewTinyBookCallBack(Structure):
    _fields_ = [("assetId", TAssetID),
                ("price", c_double),
                ("qtd", c_int),
                ("side", c_int)]

class TPriceBookCallback(Structure):
    _fields_ = [("assetId", TAssetID),
                ("nAction", c_int),
                ("nPosition", c_int),
                ("side", c_int),
                ("nQtd", c_int),
                ("ncount", c_int),
                ("sprice", c_double),
                ("pArraySell", POINTER(c_int)),
                ("pArrayBuy", POINTER(c_int))]

class TOfferBookCallback(Structure):
    _fields_ = [("assetId", TAssetID),
                ("nAction", c_int),
                ("nPosition", c_int),
                ("side", c_int),
                ("nQtd", c_int),
                ("nAgent", c_int),
                ("nOfferID", c_longlong),
                ("sPrice", c_double),
                ("bHasPrice", c_int),
                ("bHasQtd", c_int),
                ("bHasDate", c_int),
                ("bHasOfferId", c_int),
                ("bHasAgent", c_int),
                ("date", c_wchar_p),
                ("pArraySell", POINTER(c_int)),
                ("pArrayBuy", POINTER(c_int))]

class TOfferBookCallbackV2(Structure):
    _fields_ = [("assetId", TAssetID),
                ("nAction", c_int),
                ("nPosition", c_int),
                ("side", c_int),
                ("nQtd", c_int),
                ("nAgent", c_int),
                ("nOfferID", c_longlong),
                ("sPrice", c_double),
                ("bHasPrice", c_int),
                ("bHasQtd", c_int),
                ("bHasDate", c_int),
                ("bHasOfferId", c_int),
                ("bHasAgent", c_int),
                ("date", c_wchar_p),
                ("pArraySell", POINTER(c_int)),
                ("pArrayBuy", POINTER(c_int))]


TConnectorEnumerateOrdersProc = WINFUNCTYPE(
    c_bool,
    POINTER(TConnectorOrder),
    c_long
)



# ============================================================================= #
# ================================ Initializer ================================ #
# ============================================================================= #
def initializeDll(path: str) -> WinDLL:
    profit_dll = WinDLL(path)
    profit_dll.argtypes  = None

    profit_dll.SendSellOrder.restype = c_longlong
    profit_dll.SendBuyOrder.restype = c_longlong
    profit_dll.SendZeroPosition.restype = c_longlong
    profit_dll.GetAgentNameByID.restype = c_wchar_p
    profit_dll.GetAgentShortNameByID.restype = c_wchar_p
    profit_dll.GetPosition.restype = POINTER(c_int)
    profit_dll.SendMarketSellOrder.restype = c_int64
    profit_dll.SendMarketBuyOrder.restype = c_int64

    profit_dll.SendStopSellOrder.argtypes = [c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_double, c_double, c_int]
    profit_dll.SendStopSellOrder.restype = c_longlong

    profit_dll.SendStopBuyOrder.argtypes = [c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_double, c_double, c_int]
    profit_dll.SendStopBuyOrder.restype = c_longlong

    profit_dll.SendOrder.argtypes = [POINTER(TConnectorSendOrder)]
    profit_dll.SendOrder.restype = c_int64

    profit_dll.SendChangeOrderV2.argtypes = [POINTER(TConnectorChangeOrder)]
    profit_dll.SendChangeOrderV2.restype = c_int

    profit_dll.SendCancelOrderV2.argtypes = [POINTER(TConnectorCancelOrder)]
    profit_dll.SendCancelOrderV2.restype = c_int

    profit_dll.SendCancelOrdersV2.argtypes = [POINTER(TConnectorCancelOrders)]
    profit_dll.SendCancelOrdersV2.restype = c_int

    profit_dll.SendCancelAllOrdersV2.argtypes = [POINTER(TConnectorCancelAllOrders)]
    profit_dll.SendCancelAllOrdersV2.restype = c_int

    profit_dll.SendZeroPositionV2.argtypes = [POINTER(TConnectorZeroPosition)]
    profit_dll.SendZeroPositionV2.restype = c_int64

    profit_dll.GetAccountCount.argtypes = []
    profit_dll.GetAccountCount.restype = c_int

    profit_dll.GetAccounts.argtypes = [c_int, c_int, c_int, POINTER(TConnectorAccountIdentifierOut)]
    profit_dll.GetAccounts.restype = c_int

    profit_dll.GetAccountDetails.argtypes = [POINTER(TConnectorTradingAccountOut)]
    profit_dll.GetAccountDetails.restype = c_int

    profit_dll.GetSubAccountCount.argtypes = [POINTER(TConnectorAccountIdentifier)]
    profit_dll.GetSubAccountCount.restype = c_int

    profit_dll.GetSubAccounts.argtypes = [POINTER(TConnectorAccountIdentifier), c_int, c_int, c_int, POINTER(TConnectorAccountIdentifierOut)]
    profit_dll.GetSubAccounts.restype = c_int

    profit_dll.GetPositionV2.argtypes = [POINTER(TConnectorTradingAccountPosition)]
    profit_dll.GetPositionV2.restype = c_int

    profit_dll.GetOrderDetails.argtypes = [POINTER(TConnectorOrderOut)]
    profit_dll.GetOrderDetails.restype = c_int

    profit_dll.HasOrdersInInterval.argtypes = [POINTER(TConnectorAccountIdentifier), SystemTime, SystemTime]
    profit_dll.HasOrdersInInterval.restype = c_int

    profit_dll.EnumerateOrdersByInterval.argtypes = [POINTER(TConnectorAccountIdentifier), c_ubyte, SystemTime, SystemTime, c_long, TConnectorEnumerateOrdersProc]
    profit_dll.EnumerateOrdersByInterval.restype = c_int

    profit_dll.EnumerateAllOrders.argtypes = [POINTER(TConnectorAccountIdentifier), c_ubyte, c_long, TConnectorEnumerateOrdersProc]
    profit_dll.EnumerateAllOrders.restype = c_int

    profit_dll.TranslateTrade.argtypes = [c_size_t, POINTER(TConnectorTrade)]
    profit_dll.TranslateTrade.restype = c_int

    return profit_dll

profit_dll = initializeDll("./ProfitDLL/Win64.dll")




# =============================================================================== #
# ================================ Definitions 1 ================================ #
# =============================================================================== #
NL_OK                    = 0x00000000
NL_INTERNAL_ERROR        = -2147483647                   # Internal error
NL_NOT_INITIALIZED       = NL_INTERNAL_ERROR        + 1  # Not initialized
NL_INVALID_ARGS          = NL_NOT_INITIALIZED       + 1  # Invalid arguments
NL_WAITING_SERVER        = NL_INVALID_ARGS          + 1  # Aguardando dados do servidor
NL_NO_LOGIN              = NL_WAITING_SERVER        + 1  # Nenhum login encontrado
NL_NO_LICENSE            = NL_NO_LOGIN              + 1  # Nenhuma licença encontrada
NL_PASSWORD_HASH_SHA1    = NL_NO_LICENSE            + 1  # Senha não está em SHA1
NL_PASSWORD_HASH_MD5     = NL_PASSWORD_HASH_SHA1    + 1  # Senha não está em MD5
NL_OUT_OF_RANGE          = NL_PASSWORD_HASH_MD5     + 1  # Count do parâmetro maior que o tamanho do array
NL_MARKET_ONLY           = NL_OUT_OF_RANGE          + 1  # Não possui roteamento
NL_NO_POSITION           = NL_MARKET_ONLY           + 1  # Não possui posição
NL_NOT_FOUND             = NL_NO_POSITION           + 1  # Recurso não encontrado
NL_VERSION_NOT_SUPPORTED = NL_NOT_FOUND             + 1  # Versão do recurso não suportada
NL_OCO_NO_RULES          = NL_VERSION_NOT_SUPPORTED + 1  # OCO sem nenhuma regra
NL_EXCHANGE_UNKNOWN      = NL_OCO_NO_RULES          + 1  # Bolsa desconhecida
NL_NO_OCO_DEFINED        = NL_EXCHANGE_UNKNOWN      + 1  # Nenhuma OCO encontrada para a ordem
NL_INVALID_SERIE         = NL_NO_OCO_DEFINED        + 1  # (Level + Offset + Factor) inválido
NL_LICENSE_NOT_ALLOWED   = NL_INVALID_SERIE         + 1  # Recurso não liberado na licença
NL_NOT_HARD_LOGOUT       = NL_LICENSE_NOT_ALLOWED   + 1  # Retorna que não esta em HardLogout
NL_SERIE_NO_HISTORY      = NL_NOT_HARD_LOGOUT       + 1  # Série não tem histórico no servidor
NL_ASSET_NO_DATA         = NL_SERIE_NO_HISTORY      + 1  # Asset não tem o dados carregado
NL_SERIE_NO_DATA         = NL_ASSET_NO_DATA         + 1  # Série não tem dados (count = 0)
NL_HAS_STRATEGY_RUNNING  = NL_SERIE_NO_DATA         + 1  # Existe uma estratégia rodando
NL_SERIE_NO_MORE_HISTORY = NL_HAS_STRATEGY_RUNNING  + 1  # Não tem mais dados disponiveis para a serie
NL_SERIE_MAX_COUNT       = NL_SERIE_NO_MORE_HISTORY + 1  # Série esta no limite de dados possíveis
NL_DUPLICATE_RESOURCE    = NL_SERIE_MAX_COUNT       + 1  # Recurso duplicado
NL_UNSIGNED_CONTRACT     = NL_DUPLICATE_RESOURCE    + 1
NL_NO_PASSWORD           = NL_UNSIGNED_CONTRACT     + 1  # Nenhuma senha informada
NL_NO_USER               = NL_NO_PASSWORD           + 1  # Nenhum usuário informado no login
NL_FILE_ALREADY_EXISTS   = NL_NO_USER               + 1  # Arquivo já existe
NL_INVALID_TICKER        = NL_FILE_ALREADY_EXISTS   + 1
NL_NOT_MASTER_ACCOUNT    = NL_INVALID_TICKER        + 1  # Conta não é master



# bAtivo = False
# bMarketConnected = False
# bConnectado = False
# bBrokerConnected = False



def NResultToString(nResult: int) -> str:
    if   nResult == NL_INTERNAL_ERROR:          return "NL_INTERNAL_ERROR"
    elif nResult == NL_NOT_INITIALIZED:         return "NL_NOT_INITIALIZED"
    elif nResult == NL_INVALID_ARGS:            return "NL_INVALID_ARGS"
    elif nResult == NL_WAITING_SERVER:          return "NL_WAITING_SERVER"
    elif nResult == NL_NO_LOGIN:                return "NL_NO_LOGIN"
    elif nResult == NL_NO_LICENSE:              return "NL_NO_LICENSE"
    elif nResult == NL_PASSWORD_HASH_SHA1:      return "NL_PASSWORD_HASH_SHA1"
    elif nResult == NL_PASSWORD_HASH_MD5:       return "NL_PASSWORD_HASH_MD5"
    elif nResult == NL_OUT_OF_RANGE:            return "NL_OUT_OF_RANGE"
    elif nResult == NL_MARKET_ONLY:             return "NL_MARKET_ONLY"
    elif nResult == NL_NO_POSITION:             return "NL_NO_POSITION"
    elif nResult == NL_NOT_FOUND:               return "NL_NOT_FOUND"
    elif nResult == NL_VERSION_NOT_SUPPORTED:   return "NL_VERSION_NOT_SUPPORTED"
    elif nResult == NL_OCO_NO_RULES:            return "NL_OCO_NO_RULES"
    elif nResult == NL_EXCHANGE_UNKNOWN:        return "NL_EXCHANGE_UNKNOWN"
    elif nResult == NL_NO_OCO_DEFINED:          return "NL_NO_OCO_DEFINED"
    elif nResult == NL_INVALID_SERIE:           return "NL_INVALID_SERIE"
    elif nResult == NL_LICENSE_NOT_ALLOWED:     return "NL_LICENSE_NOT_ALLOWED"
    elif nResult == NL_NOT_HARD_LOGOUT:         return "NL_NOT_HARD_LOGOUT"
    elif nResult == NL_SERIE_NO_HISTORY:        return "NL_SERIE_NO_HISTORY"
    elif nResult == NL_ASSET_NO_DATA:           return "NL_ASSET_NO_DATA"
    elif nResult == NL_SERIE_NO_DATA:           return "NL_SERIE_NO_DATA"
    elif nResult == NL_HAS_STRATEGY_RUNNING:    return "NL_HAS_STRATEGY_RUNNING"
    elif nResult == NL_SERIE_NO_MORE_HISTORY:   return "NL_SERIE_NO_MORE_HISTORY"
    elif nResult == NL_SERIE_MAX_COUNT:         return "NL_SERIE_MAX_COUNT"
    elif nResult == NL_DUPLICATE_RESOURCE:      return "NL_DUPLICATE_RESOURCE"
    elif nResult == NL_UNSIGNED_CONTRACT:       return "NL_UNSIGNED_CONTRACT"
    elif nResult == NL_NO_PASSWORD:             return "NL_NO_PASSWORD"
    elif nResult == NL_NO_USER:                 return "NL_NO_USER"
    elif nResult == NL_FILE_ALREADY_EXISTS:     return "NL_FILE_ALREADY_EXISTS"
    elif nResult == NL_INVALID_TICKER:          return "NL_INVALID_TICKER"
    elif nResult == NL_NOT_MASTER_ACCOUNT:      return "NL_NOT_MASTER_ACCOUNT"
    else:                                       return str(nResult)

def datetime_to_systemtime(dt):
     return SystemTime(
        wYear=dt.year,
        wMonth=dt.month,
        wDayOfWeek=dt.weekday(),
        wDay=dt.day,
        wHour=dt.hour,
        wMinute=dt.minute,
        wSecond=dt.second,
        wMilliseconds=int(dt.microsecond / 1000)
     )

def systemtime_to_datetime(st):
    return datetime(
        year=st.wYear,
        month=st.wMonth,
        day=st.wDay,
        hour=st.wHour,
        minute=st.wMinute,
        second=st.wSecond,
        microsecond=st.wMilliseconds * 1000
    )

def evalDllReturn(function: str, ret: int) -> bool:
    if ret < NL_OK:
        print("{0}: {1}".format(
            function,
            NResultToString(ret)
        ))

        return False
    else:
        return True

def printOrder(title:str, orderId: TConnectorOrderIdentifier):
    order = TConnectorOrderOut(
        Version=0,
        OrderID=orderId
    )

    ret = profit_dll.GetOrderDetails(byref(order))
    if not evalDllReturn("GetOrderDetails-1", ret):
        return

    order.AssetID.Ticker   = ' ' * order.AssetID.TickerLength
    order.AssetID.Exchange = ' ' * order.AssetID.ExchangeLength
    order.TextMessage      = ' ' * order.TextMessageLength

    ret = profit_dll.GetOrderDetails(byref(order))
    if not evalDllReturn("GetOrderDetails-2", ret):
        return

    print('{0}: {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}'.format(title,
        order.AssetID.Ticker,
        order.TradedQuantity,
        order.OrderSide,
        order.Price,
        order.AccountID.AccountID,
        order.AccountID.SubAccountID,
        order.OrderID.ClOrderID,
        order.OrderStatus,
        order.TextMessage
    ))



@WINFUNCTYPE(None, c_int32, c_int32)
def stateCallback(nType, nResult):
    global bAtivo
    global bMarketConnected
    global bConnectado

    nConnStateType = nType
    result = nResult

    if nConnStateType == 0: # notificacoes de login
        if result == 0:
            bConnectado = True
            print("Login: conectado")
        else :
            bConnectado = False
            print('Login: ' + str(result))
    elif nConnStateType == 1:
        if result == 5:
            # bBrokerConnected = True
            print("Broker: Conectado.")
        elif result > 2:
            # bBrokerConnected = False
            print("Broker: Sem conexão com corretora.")
        else:
            # bBrokerConnected = False
            print("Broker: Sem conexão com servidores (" + str(result) + ")")

    elif nConnStateType == 2:  # notificacoes de login no Market
        if result == 4:
            print("Market: Conectado" )
            bMarketConnected = True
        else:
            print("Market: " + str(result))
            bMarketConnected = False

    elif nConnStateType == 3: # notificacoes de login
        if result == 0:
            print("Ativação: OK")
            bAtivo = True
        else:
            print("Ativação: " + str(result))
            bAtivo = False

    if bMarketConnected and bAtivo and bConnectado:
        print("Serviços Conectados")

    return

@WINFUNCTYPE(None, TAssetID, c_int)
def progressCallBack(assetId, nProgress):
    print(assetId.ticker + ' | Progress | ' + str(nProgress))
    return

@WINFUNCTYPE(None, c_int, c_wchar_p, c_wchar_p, c_wchar_p)
def accountCallback(nCorretora, corretoraNomeCompleto, accountID, nomeTitular):
    print("Conta | " + accountID + ' - ' + nomeTitular + ' | Corretora ' + str(nCorretora) + ' - ' + corretoraNomeCompleto)
    return

@WINFUNCTYPE(None, TAssetID, c_int, c_int, c_int, c_int, c_int, c_double, POINTER(c_int), POINTER(c_int))
def priceBookCallback(assetId, nAction, nPosition, Side, nQtd, nCount, sPrice, pArraySell, pArrayBuy):
    if pArraySell is not None:
        print("todo - priceBookCallBack")
    return

@WINFUNCTYPE(None, TConnectorAssetIdentifier, c_size_t, c_uint)
def tradeCallback(assetId, pTrade, flags):
    is_edit = bool(flags & 1)

    trade = TConnectorTrade(Version=0)

    if profit_dll.TranslateTrade(pTrade, byref(trade)):
        print(f'{assetId.Ticker} | Trade | {trade.Price} | {trade.Quantity} | Edit={is_edit}')

    pass

@WINFUNCTYPE(None, TAssetID, c_double, c_int, c_int)
def newTinyBookCallBack(assetId, price, qtd, side):
    if side == 0 :
        print(assetId.ticker + ' | TinyBook | Buy: ' + str(price) + ' ' + str(qtd))
    else :
        print(assetId.ticker + ' | TinyBook | Sell: ' + str(price) + ' ' + str(qtd))

    return

@WINFUNCTYPE(None, TAssetID, c_wchar_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double,
           c_double, c_int, c_int, c_int, c_int, c_int, c_int, c_int)
def newDailyCallback(assetID, date, sOpen, sHigh, sLow, sClose, sVol, sAjuste, sMaxLimit, sMinLimit, sVolBuyer,
                     sVolSeller, nQtd, nNegocios, nContratosOpen, nQtdBuyer, nQtdSeller, nNegBuyer, nNegSeller):
    print(assetID.ticker + ' | DailySignal | ' + date + ' Open: ' + str(sOpen) + ' High: ' + str(sHigh) + ' Low: ' + str(sLow) + ' Close: ' + str(sClose))
    return



# price_array_sell = []
# price_array_buy  = []



def descript_offer_array_v2(offer_array):
    # le o cabeçalho da lista
    header = bytearray(offer_array[0:8])
    start = 0
    
    qtd_offer, pointer_size = struct.unpack('ii', header[start : start+8])
    start += 8

    # sabendo o tamanho do array, e o tamanho do pacote, podemos ler diramente o rodapé
    trailer = bytearray(offer_array[start + (qtd_offer * 53):pointer_size])
    flags = struct.unpack('I', trailer[0:4])[0]
    
    is_last = bool(flags & 1)

    print(f"OfferBook: Qtd: {qtd_offer} | Size: {pointer_size} | Last: {is_last}")

    # tendo a quantidade, podemos ler as ofertas

    offer_list = []
    frame = bytearray(offer_array[8 : 8 + (qtd_offer * 53)])

    start = 0
    for i in range(qtd_offer):
        price, qtd, agent, offer_id, date_length = struct.unpack('=dqiqH', frame[start:start+30])
        start += 30

        date_str = struct.unpack(f'{date_length}s', frame[start:start+date_length])[0].decode('ansi')
        start += date_length

        date = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S.%f")

        offer_list.append([price, qtd, agent, offer_id, date])

    return offer_list

@WINFUNCTYPE(None, TAssetID, c_int, c_int, c_int, c_int, c_int, c_longlong, c_double, c_int, c_int, c_int, c_int, c_int, c_wchar_p, POINTER(c_ubyte), POINTER(c_ubyte))
def offerBookCallbackV2(assetId, nAction, nPosition, Side, nQtd, nAgent, nOfferID, sPrice, bHasPrice,
                      bHasQtd, bHasDate, bHasOfferID, bHasAgent, date, pArraySell, pArrayBuy):
    global price_array_buy
    global price_array_sell

    if bool(pArraySell):
        price_array_sell = descript_offer_array_v2(pArraySell)

    if bool(pArrayBuy):
        price_array_buy = descript_offer_array_v2(pArrayBuy)

    if Side == 0:
        lst_book = price_array_buy
    else:
        lst_book = price_array_sell

    if lst_book and 0 <= nPosition <= len(lst_book):
        """
        atAdd = 0
        atEdit = 1
        atDelete = 2
        atDeleteFrom = 3
        atFullBook = 4
        """
        if nAction == 0:
            group = [sPrice, nQtd, nAgent]
            idx = len(lst_book)-nPosition
            lst_book.insert(idx, group)
        elif nAction == 1:
            group = lst_book[-nPosition - 1]
            group[1] = group[1] + nQtd
            group[2] = group[2] + nAgent
        elif nAction == 2:
            del lst_book[-nPosition - 1]
        elif nAction == 3:
            del lst_book[-nPosition - 1:]
    return

@WINFUNCTYPE(None, TAssetID, c_wchar_p, c_uint, c_double)
def changeCotationCallback(assetId, date, tradeNumber, sPrice):
    print("todo - changeCotationCallback")
    return

@WINFUNCTYPE(None, TAssetID, c_wchar_p)
def assetListCallback(assetId, strName):
    print ("assetListCallback Ticker=" + str(assetId.ticker) + " Name=" + str(strName))
    return

@WINFUNCTYPE(None, TAssetID, c_double, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_uint, c_double)
def adjustHistoryCallbackV2(assetId, value, strType, strObserv, dtAjuste, dtDelib, dtPagamento, nFlags, dMult):
    print("todo - adjustHistoryCallbackV2")
    return

@WINFUNCTYPE(None, TAssetID, c_wchar_p, c_wchar_p, c_int, c_int, c_int, c_int, c_int, c_double, c_double, c_wchar_p, c_wchar_p)
def assetListInfoCallback(assetId, strName, strDescription, iMinOrdQtd, iMaxOrdQtd, iLote, iSecurityType, iSecuritySubType, dMinPriceInc, dContractMult, strValidDate, strISIN):
    print('TAssetListInfoCallback = Ticker: ' + str(assetId.ticker) +
          'Name: ' + str(strName) +
          'Descrição: ' + str(strDescription))
    return

@WINFUNCTYPE(None, TAssetID, c_wchar_p, c_wchar_p, c_int, c_int, c_int, c_int, c_int, c_double, c_double, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p)
def assetListInfoCallbackV2(assetId, strName, strDescription, iMinOrdQtd, iMaxOrdQtd, iLote, iSecurityType, iSecuritySubType, dMinPriceInc, dContractMult, strValidDate, strISIN, strSetor, strSubSetor, strSegmento):
    print('TAssetListInfoCallbackV2 = Ticker: ' + str(assetId.ticker) +
          'Name: ' + str(strName) +
          'Descrição: ' + str(strDescription) +
          'Setor: ' + str(strSetor))
    return

@WINFUNCTYPE(None, TConnectorOrderIdentifier)
def orderCallback(orderId : TConnectorOrderIdentifier):
    printOrder("OrderCallback", orderId)

@WINFUNCTYPE(c_bool, POINTER(TConnectorOrder), c_long)
def PrintEnumOrders(order_ptr, param):
    order = order_ptr.contents

    print('OrderHistoryCallback: {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8}'.format(
        order.AssetID.Ticker,
        order.TradedQuantity,
        order.OrderSide,
        order.Price,
        order.AccountID.AccountID,
        order.AccountID.SubAccountID,
        order.OrderID.ClOrderID,
        order.OrderStatus,
        order.TextMessage
    ))

    return True

@WINFUNCTYPE(None, TConnectorAccountIdentifier)
def orderHistoryCallback(accountId : TConnectorAccountIdentifier):
    profit_dll.EnumerateAllOrders(byref(accountId), 0, 0, TConnectorEnumerateOrdersProc(PrintEnumOrders))

@WINFUNCTYPE(None, TConnectorAssetIdentifier)
def invalidAssetCallback(assetID : TConnectorAssetIdentifier):
    print("invalidAssetCallback: " + assetID.Ticker)





# =============================================================================== #
# ================================ Definitions 2 ================================ #
# =============================================================================== #
def dllStart(key:str, user:str, password:str):
    try:
        # key         = input('Chave de acesso: ')
        # user        = input('Usuário: ') # preencher com usuário da conta (email ou documento)
        # password    = getpass('Senha: ') # preencher com senha da conta

        bRoteamento = True

        if bRoteamento: res = profit_dll.DLLInitializeLogin(c_wchar_p(key), c_wchar_p(user), c_wchar_p(password), stateCallback, None, None, accountCallback, None, newDailyCallback, priceBookCallback, None, None, progressCallBack, newTinyBookCallBack)
        else :          res = profit_dll.DLLInitializeMarketLogin(c_wchar_p(key), c_wchar_p(user), c_wchar_p(password), stateCallback, None, newDailyCallback, priceBookCallback, None, None, progressCallBack, newTinyBookCallBack)

        profit_dll.SetAssetListCallback(assetListCallback)
        profit_dll.SetAdjustHistoryCallbackV2(adjustHistoryCallbackV2)
        profit_dll.SetAssetListInfoCallback(assetListInfoCallback)
        profit_dll.SetAssetListInfoCallbackV2(assetListInfoCallbackV2)
        profit_dll.SetOfferBookCallbackV2(offerBookCallbackV2)
        profit_dll.SetOrderCallback(orderCallback)
        profit_dll.SetOrderHistoryCallback(orderHistoryCallback)
        profit_dll.SetInvalidTickerCallback(invalidAssetCallback)
        profit_dll.SetTradeCallbackV2(tradeCallback)

        print('DLLInitialize: ', str(res))
        wait_login()

    except Exception as E:
        print(E)

def dllEnd():
    res = profit_dll.DLLFinalize()
    print('DLLFinalize:', str(res))



def wait_login():
    global bMarketConnected
    global bAtivo
    bWaiting = True
    while bWaiting:
        if bMarketConnected:
            print('DLL_CONNECTED')
            bWaiting = False
    print('STOP_WAITING')

def getAccount():
    count       = profit_dll.GetAccountCount()
    accountIDs  = (TConnectorAccountIdentifierOut * count)()
    count       = profit_dll.GetAccounts(0, 0, count, accountIDs)

    for i in range(count):
        accountID = TConnectorAccountIdentifier(
            Version=0,
            BrokerID=accountIDs[i].BrokerID,
            AccountID=accountIDs[i].AccountID
        )

        account = getAccountDetails(accountID)

        if account: 
            print(
                'BrokerID:', accountID.BrokerID,
                'AccountID:', accountID.AccountID,
                'OwnerName:', account.OwnerName
            )

            subCount = profit_dll.GetSubAccountCount(accountID)
            if subCount > 0:
                subAccountIDs = (TConnectorAccountIdentifierOut * subCount)()
                subCount = profit_dll.GetSubAccounts(accountID, 0, 0, subCount, subAccountIDs)

                for j in range(subCount):
                    subAccountID = TConnectorAccountIdentifier(
                        Version=0,
                        BrokerID=subAccountIDs[j].BrokerID,
                        AccountID=subAccountIDs[j].AccountID,
                        SubAccountID=subAccountIDs[j].SubAccountID
                    )

                    subAccount = getAccountDetails(subAccountID)

                    if account: print(
                            'BrokerID:',     subAccountID.BrokerID,
                            'AccountID:',    subAccountID.AccountID,
                            'SubAccountID:', subAccountID.SubAccountID,
                            'SubOwnerName:', subAccount.SubOwnerName
                        )

def getAccountDetails(accountId: TConnectorAccountIdentifier) -> TConnectorTradingAccountOut:
    account = TConnectorTradingAccountOut(
        Version=0,
        AccountID=accountId
    )

    if (profit_dll.GetAccountDetails(byref(account)) != NL_OK):
        return None

    account.BrokerName = ' ' * account.BrokerNameLength
    account.OwnerName = ' ' * account.OwnerNameLength
    account.SubOwnerName = ' ' * account.SubOwnerNameLength

    if (profit_dll.GetAccountDetails(byref(account)) != NL_OK):
        return None

    return account



def subscribeOffer(asset:str, bolsa:str):
    # print('subscribe offer book')
    # asset  = input('Asset: ')
    # bolsa  = input('Bolsa: ')
    res = profit_dll.SubscribeOfferBook(c_wchar_p(asset), c_wchar_p(bolsa))
    print('SubscribeOfferBook:', str(res))
    return res
    
def subscribeTicker(asset:str, bolsa:str):
    # asset = input('Asset: ')
    # bolsa = input('Bolsa: ')
    res = profit_dll.SubscribeTicker(c_wchar_p(asset), c_wchar_p(bolsa))
    print('SubscribeTicker:', str(res))
    return res

def unsubscribeTicker(asset:str, bolsa:str):
    # asset = input('Asset: ')
    # bolsa = input('Bolsa: ')
    res = profit_dll.UnsubscribeTicker(c_wchar_p(asset), c_wchar_p(bolsa))
    print('UnsubscribeTicker:', str(res))
    return res



def sendBuyMarketOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, amount:int):
    # brokerId        = int(input('Corretora: '))
    # accountId       = input('Conta: ')
    # subAccountId    = input('SubConta: ')
    # password        = getpass('Senha de Roteamento: ')

    # ticker      = input('Ativo: ')
    # exchange    = input('Bolsa: ')
    # amount      = int(input('Quantidade: '))

    send_order = TConnectorSendOrder(
        Version = 0,
        Password = password,
        OrderType = TConnectorOrderType.Market.value,
        OrderSide = TConnectorOrderSide.Buy.value,
        Price = -1,
        StopPrice = -1,
        Quantity = amount
    )
    send_order.AccountID = TConnectorAccountIdentifier(
        Version=0,
        BrokerID=brokerId,
        AccountID=accountId,
        SubAccountID=subAccountId,
        Reserved=0
    )
    send_order.AssetID = TConnectorAssetIdentifier(
        Version=0,
        Ticker=ticker,
        Exchange=exchange,
        FeedType=0
    )

    profitID = profit_dll.SendOrder(byref(send_order))

    if evalDllReturn('SendOrder', profitID):
        print('ProfitID:', str(profitID))
        return profitID

def sendSellMarketOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, amount:int):
    # brokerId        = int(input('Corretora: '))
    # accountId       = input('Conta: ')
    # subAccountId    = input('SubConta: ')
    # password        = getpass('Senha de Roteamento: ')

    # ticker          = input('Ativo: ')
    # exchange        = input('Bolsa: ')
    # amount          = int(input('Quantidade: '))

    send_order = TConnectorSendOrder(
        Version = 0,
        Password = password,
        OrderType = TConnectorOrderType.Market.value,
        OrderSide = TConnectorOrderSide.Sell.value,
        Price = -1,
        StopPrice = -1,
        Quantity = amount
    )
    send_order.AccountID = TConnectorAccountIdentifier(
        Version=0,
        BrokerID=brokerId,
        AccountID=accountId,
        SubAccountID=subAccountId,
        Reserved=0
    )
    send_order.AssetID = TConnectorAssetIdentifier(
        Version=0,
        Ticker=ticker,
        Exchange=exchange,
        FeedType=0
    )

    profitID = profit_dll.SendOrder(byref(send_order))

    if evalDllReturn('SendOrder', profitID):
        print('ProfitID:', str(profitID))

def buyStopOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, price:float, stopPrice:float, amount:int):
    # brokerId        = int(input('Corretora: '))
    # accountId       = input('Conta: ')
    # subAccountId    = input('SubConta: ')
    # password        = getpass('Senha de Roteamento: ')

    # ticker      = input('Ativo: ')
    # exchange    = input('Bolsa: ')
    # price       = float(input('Preço: '))
    # stopPrice   = float(input('Preço Stop: '))
    # amount      = int(input('Quantidade: '))

    order           = TConnectorSendOrder(Version=1, Password=password, OrderType=TConnectorOrderType.Stop.value, OrderSide=TConnectorOrderSide.Buy.value, Price=price, StopPrice=stopPrice, Quantity=amount)
    order.AccountID = TConnectorAccountIdentifier(Version=0, BrokerID=brokerId, AccountID=accountId, SubAccountID=subAccountId, Reserved=0)
    order.AssetID   = TConnectorAssetIdentifier(Version=0, Ticker=ticker, Exchange=exchange, FeedType=0)
    profitID        = profit_dll.SendOrder(byref(order))

    if evalDllReturn('SendOrder', profitID):
        print('ProfitID:', str(profitID))
        return profitID

def sellStopOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, price:float, stopPrice:float, amount:int):
    # brokerId     = int(input('Corretora: '))
    # accountId    = input('Conta: ')
    # subAccountId = input('SubConta: ')
    # password  = getpass('Senha de Roteamento: ')

    # ticker       = input('Ativo: ')
    # exchange     = input('Bolsa: ')
    # price        = float(input('Preço: '))
    # stopPrice    = float(input('Preço Stop: '))
    # amount       = int(input('Quantidade: '))

    order           = TConnectorSendOrder(Version=0, Password=password, OrderType=TConnectorOrderType.Stop.value, OrderSide=TConnectorOrderSide.Sell.value, Price=price, StopPrice=stopPrice, Quantity=amount)
    order.AccountID = TConnectorAccountIdentifier(Version=0, BrokerID=brokerId, AccountID=accountId, SubAccountID=subAccountId, Reserved=0)
    order.AssetID   = TConnectorAssetIdentifier(Version=0, Ticker=ticker, Exchange=exchange, FeedType=0)
    profitID = profit_dll.SendOrder(byref(order))

    if evalDllReturn('SendOrder', profitID):
        print('ProfitID:', str(profitID))
        return profitID

def sendSellOrder(qnt:int, price:float) :
    # qnt         = int(1)
    # price       = float(100000)
    # priceStop   = float(100000)
    nProfitID = profit_dll.SendSellOrder(c_wchar_p('CONTA'), c_wchar_p('BROKER'), c_wchar_p('PASS'), c_wchar_p('ATIVO'), c_wchar_p('BOLSA'), c_double(price), c_int(qnt))
    print('nProfitID:', str(nProfitID))
    return nProfitID



def getOrders(brokerId:str, accountId:str):
    # brokerId  = input('Corretora: ')
    # accountId = input('Conta: ')

    now = datetime.now()
    tomorrow = datetime.now() + timedelta(days=1)

    # retorno em historyCallback
    profit_dll.GetOrders(
        c_wchar_p(accountId),
        c_wchar_p(brokerId),
        c_wchar_p(now.strftime('%d/%m/%Y')),
        c_wchar_p(tomorrow.strftime('%d/%m/%Y')))

def getOrder(cl_ord_id:str, profit_id:int):
    # cl_ord_id = input('ClOrdID: ')
    # profit_id = int(input('ProfitID: '))

    order_id = TConnectorOrderIdentifier(
        Version=0,
        LocalOrderID=profit_id,
        ClOrderID=cl_ord_id
    )

    printOrder('GetOrder', order_id)
    return order_id

def cancelOrder(brokerId:int, accountId:str, subAccountId:str, password:str, cl_ord_id:str):
    # brokerId     = int(input('Corretora: '))
    # accountId    = input('Conta: ')
    # subAccountId = input('SubConta: ')
    # password  = getpass('Senha de Roteamento: ')
    # cl_ord_id    = input('ClOrdID: ')

    cancel_order = TConnectorCancelOrder(
        Version=0,
        Password=password
    )
    cancel_order.OrderID = TConnectorOrderIdentifier(
        Version=0,
        LocalOrderID=-1,
        ClOrderID=cl_ord_id
    )
    cancel_order.AccountID = TConnectorAccountIdentifier(
        Version=0,
        BrokerID=brokerId,
        AccountID=accountId,
        SubAccountID=subAccountId,
        Reserved=0
    )

    ret = profit_dll.SendCancelOrderV2(byref(cancel_order))
    evalDllReturn('SendCancelOrderV2', ret)
    return ret

def cancelAllOrders(brokerId:int, accountId:str, subAccountId:str, password:str):
    # brokerId     = int(input('Corretora: '))
    # accountId    = input('Conta: ')
    # subAccountId = input('SubConta: ')
    # password  = getpass('Senha de Roteamento: ')

    cancel_order = TConnectorCancelAllOrders(
        Version=0,
        Password=password
    )
    cancel_order.AccountID = TConnectorAccountIdentifier(
        Version=0,
        BrokerID=brokerId,
        AccountID=accountId,
        SubAccountID=subAccountId,
        Reserved=0
    )

    ret = profit_dll.SendCancelAllOrdersV2(byref(cancel_order))
    evalDllReturn('SendCancelAllOrdersV2', ret)
    return ret

def changeOrder(brokerId:int, accountId:str, subAccountId:str, cl_ord_id:str, password:str, price:float, amount:int):
    # brokerId        = int(input('Corretora: '))
    # accountId       = input('Conta: ')
    # subAccountId    = input('SubConta: ')
    # cl_ord_id       = input('ClOrdID: ')
    # password        = getpass('Senha de Roteamento: ')
    # price           = float(input('Preço: '))
    # amount          = int(input('Quantidade: '))

    change_order = TConnectorChangeOrder(
        Version   = 0,
        Password  = password,
        Price     = price,
        StopPrice = -1,
        Quantity  = amount
    )
    change_order.AccountID = TConnectorAccountIdentifier(
        Version=0,
        BrokerID=brokerId,
        AccountID=accountId,
        SubAccountID=subAccountId,
        Reserved=0
    )
    change_order.OrderID = TConnectorOrderIdentifier(
        Version=0,
        LocalOrderID=-1,
        ClOrderID=cl_ord_id
    )

    profitID = profit_dll.SendChangeOrderV2(byref(change_order))
    evalDllReturn('SendChangeOrderV2', profitID)

def doHasOrdersInInterval(brokerId:int, accountId:str):
    # brokerId  = int(input('Corretora: '))
    # accountId = input('Conta: ')

    accountId = TConnectorAccountIdentifier(
        Version=0,
        BrokerID=brokerId,
        AccountID=accountId,
        SubAccountID='',
        Reserved=0
    )

    today       = datetime_to_systemtime(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) )
    yesterday   = datetime_to_systemtime(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1))

    res = profit_dll.HasOrdersInInterval(byref(accountId), yesterday, today)
    evalDllReturn('HasOrdersInInterval', res)
    return res



def printLastAdjusted(ticker:str, tick:Lit['A','B']):
    close = c_double()
    res = profit_dll.GetLastDailyClose(c_wchar_p(ticker), c_wchar_p(tick), byref(close), 1)
    print('Last session close:', close, 'result:', str(res))
    return close, res

def printPosition(ticker:str, exchange:str, brokerId:int, accountId:str, subAccountId:str, positionType:int):
    # ticker       = input('Asset: ')
    # exchange     = input('Bolsa: ')
    # brokerId     = int(input('Corretora: '))
    # accountId    = input('Conta: ')
    # subAccountId = input('SubConta: ')
    # positionType = int(input('Tipo da Posisão (1 - DayTrade, 2 - Consolidado): '))

    Pos             = TConnectorTradingAccountPosition(Version=1, PositionType=positionType)
    Pos.AccountID   = TConnectorAccountIdentifier(Version=0, BrokerID=brokerId, AccountID=accountId, SubAccountID=subAccountId)
    Pos.AssetID     = TConnectorAssetIdentifier(Version=0, Ticker=ticker, Exchange=exchange, FeedType=0)
    ret             = profit_dll.GetPositionV2(byref(Pos))

    if evalDllReturn('GetPositionV2', ret): 

        print(
            'OpenAveragePrice:',        Pos.OpenAveragePrice,
            'DailyAverageSellPrice:',   Pos.DailyAverageSellPrice,
            'DailyAverageBuyPrice:',    Pos.DailyAverageBuyPrice,
            'DailySellQuantity:',       Pos.DailySellQuantity,
            'DailyBuyQuantity:',        Pos.DailyBuyQuantity
        )

        return Pos.OpenAveragePrice, Pos.DailyAverageSellPrice, Pos.DailyAverageBuyPrice, Pos.DailySellQuantity, Pos.DailyBuyQuantity

def doZeroPosition(ticker:str, exchange:str, brokerId:int, accountId:int, subAccountId:str, password:str, positionType:int):
    # ticker          = input('Asset: ')
    # exchange        = input('Bolsa: ')
    # brokerId        = int(input('Corretora: '))
    # accountId       = input('Conta: ')
    # subAccountId    = input('SubConta: ')
    # password        = getpass('Senha de Roteamento: ')
    # positionType    = int(input('Tipo da Posisão (1 - DayTrade, 2 - Consolidado): '))

    zeroRec             = TConnectorZeroPosition(Version=1, PositionType=positionType, Password=password, Price=(-1.0))
    zeroRec.AccountID   = TConnectorAccountIdentifier(Version=0, BrokerID=brokerId, AccountID=accountId, SubAccountID=subAccountId)
    zeroRec.AssetID     = TConnectorAssetIdentifier(Version=0, Ticker=ticker, Exchange=exchange, FeedType=0)
    ret                 = profit_dll.SendZeroPositionV2(byref(zeroRec))

    if not evalDllReturn('SendZeroPositionV2', ret):
        print('ZeroOrderID: {0}'.format(ret))
        return ret
