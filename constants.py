from collections import OrderedDict

# DATASET
MARKET_CAP_DIR = "./data/marketcap.csv"
ADJCLOSE_DIR = "./data/adjclose.csv"

# TICKER
TICKER = OrderedDict(
    {
        "KODEX 200": "069500.KS",
        "TIGER 코스닥150": "232080.KS",
        "TIGER 미국S&P500선물(H)": "143850.KS",
        "TIGER 유로스탁스50(합성 H)": "195930.KS",
        "KINDEX 일본Nikkei225(H)": "238720.KS",
        "TIGER 차이나CSI300": "192090.KS",
        "KOSEF 국고채10년": "148070.KS",
        "KBSTAR 중기우량회사채": "136340.KS",
        "TIGER 단기선진하이일드(합성 H)": "182490.KS",
        "KODEX 골드선물(H)": "132030.KS",
        "TIGER 원유선물Enhanced(H)": "130680.KS",
        "KODEX 인버스": "114800.KS",
        "KOSEF 미국달러선물": "138230.KS",
        "KOSEF 미국달러선물인버스": "139660.KS",
        "KOSEF 단기자금": "130730.KS",
        #   'KODEX 국고채3년': '114260.KS'
    }
)

WEIGHT_CONSTRAINT = OrderedDict(
    {
        "KODEX 200": (0, 40),
        "TIGER 코스닥150": (0, 20),
        "TIGER 미국S&P500선물(H)": (0, 20),
        "TIGER 유로스탁스50(합성 H)": (0, 20),
        "KINDEX 일본Nikkei225(H)": (0, 20),
        "TIGER 차이나CSI300": (0, 20),
        "KOSEF 국고채10년": (0, 50),
        "KBSTAR 중기우량회사채": (0, 40),
        "TIGER 단기선진하이일드(합성 H)": (5, 40),
        "KODEX 골드선물(H)": (0, 15),
        "TIGER 원유선물Enhanced(H)": (0, 15),
        "KODEX 인버스": (0, 20),
        "KOSEF 미국달러선물": (0, 20),
        "KOSEF 미국달러선물인버스": (0, 20),
        "KOSEF 단기자금": (0, 50),
        #      'KODEX 국고채3년': (0, 50)
    }
)

SECTOR = OrderedDict(
    {
        "KODEX 200": "local_stock",
        "TIGER 코스닥150": "local_stock",
        "TIGER 미국S&P500선물(H)": "foreign_stock",
        "TIGER 유로스탁스50(합성 H)": "foreign_stock",
        "KINDEX 일본Nikkei225(H)": "foreign_stock",
        "TIGER 차이나CSI300": "foreign_stock",
        "KOSEF 국고채10년": "bond",
        "KBSTAR 중기우량회사채": "bond",
        "TIGER 단기선진하이일드(합성 H)": "bond",
        "KODEX 골드선물(H)": "commodity",
        "TIGER 원유선물Enhanced(H)": "commodity",
        "KODEX 인버스": "inverse",
        "KOSEF 미국달러선물": "fx",
        "KOSEF 미국달러선물인버스": "fx",
        "KOSEF 단기자금": "cash",
        # 'KODEX 국고채3년': "cash"
    }
)


SECTOR_CONSTRAINT = OrderedDict(
    {
        "local_stock": (10, 40),
        "foreign_stock": (10, 40),
        "bond": (20, 60),
        "commodity": (5, 20),
        "inverse": (0, 20),
        "fx": (0, 20),
        "cash": (0, 50),  # 현금 제외
    }
)
