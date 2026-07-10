#!/usr/bin/env python3
"""
Geographic mapping utilities for the Cross-Cultural Values Alignment Analysis.

Provides:
    - ISO 3166-1 alpha-2 country code → region mapping
    - Region → Global North/South classification
    - Country name → ISO code resolution
    - WEIRD scoring helpers
"""
from __future__ import annotations

# =====================================================================
# REGION MAPPING (10 macro-regions)
# =====================================================================
# Based on UN M49 with modifications for analytical clarity.
# Countries mapped to the region most relevant for AI ethics research patterns.

COUNTRY_TO_REGION: dict[str, str] = {
    # ── East Asia ─────────────────────────────────────────────────────
    "CN": "East Asia", "JP": "East Asia", "KR": "East Asia",
    "TW": "East Asia", "HK": "East Asia", "MO": "East Asia",
    "MN": "East Asia",

    # ── South Asia ────────────────────────────────────────────────────
    "IN": "South Asia", "PK": "South Asia", "BD": "South Asia",
    "LK": "South Asia", "NP": "South Asia", "BT": "South Asia",
    "MV": "South Asia", "AF": "South Asia",

    # ── Southeast Asia ────────────────────────────────────────────────
    "ID": "Southeast Asia", "MY": "Southeast Asia", "SG": "Southeast Asia",
    "TH": "Southeast Asia", "VN": "Southeast Asia", "PH": "Southeast Asia",
    "MM": "Southeast Asia", "KH": "Southeast Asia", "LA": "Southeast Asia",
    "BN": "Southeast Asia", "TL": "Southeast Asia",

    # ── Middle East & North Africa (MENA) ─────────────────────────────
    "SA": "MENA", "AE": "MENA", "QA": "MENA", "KW": "MENA",
    "BH": "MENA", "OM": "MENA", "YE": "MENA", "IQ": "MENA",
    "IR": "MENA", "JO": "MENA", "LB": "MENA", "SY": "MENA",
    "PS": "MENA", "IL": "MENA", "TR": "MENA",
    "EG": "MENA", "LY": "MENA", "TN": "MENA", "DZ": "MENA",
    "MA": "MENA",

    # ── Sub-Saharan Africa ────────────────────────────────────────────
    "NG": "Sub-Saharan Africa", "ZA": "Sub-Saharan Africa",
    "KE": "Sub-Saharan Africa", "ET": "Sub-Saharan Africa",
    "GH": "Sub-Saharan Africa", "TZ": "Sub-Saharan Africa",
    "UG": "Sub-Saharan Africa", "RW": "Sub-Saharan Africa",
    "SN": "Sub-Saharan Africa", "CI": "Sub-Saharan Africa",
    "CM": "Sub-Saharan Africa", "CD": "Sub-Saharan Africa",
    "ZW": "Sub-Saharan Africa", "MW": "Sub-Saharan Africa",
    "MZ": "Sub-Saharan Africa", "AO": "Sub-Saharan Africa",
    "BW": "Sub-Saharan Africa", "NA": "Sub-Saharan Africa",
    "ZM": "Sub-Saharan Africa", "MG": "Sub-Saharan Africa",
    "ML": "Sub-Saharan Africa", "BF": "Sub-Saharan Africa",
    "NE": "Sub-Saharan Africa", "TD": "Sub-Saharan Africa",
    "SO": "Sub-Saharan Africa", "SS": "Sub-Saharan Africa",
    "SD": "Sub-Saharan Africa", "MU": "Sub-Saharan Africa",
    "BJ": "Sub-Saharan Africa", "TG": "Sub-Saharan Africa",
    "SL": "Sub-Saharan Africa", "LR": "Sub-Saharan Africa",
    "GN": "Sub-Saharan Africa", "GA": "Sub-Saharan Africa",
    "CG": "Sub-Saharan Africa", "ER": "Sub-Saharan Africa",
    "DJ": "Sub-Saharan Africa", "LS": "Sub-Saharan Africa",
    "SZ": "Sub-Saharan Africa", "GM": "Sub-Saharan Africa",
    "GW": "Sub-Saharan Africa", "CV": "Sub-Saharan Africa",
    "KM": "Sub-Saharan Africa", "SC": "Sub-Saharan Africa",

    # ── Latin America & Caribbean ─────────────────────────────────────
    "BR": "Latin America & Caribbean", "MX": "Latin America & Caribbean",
    "AR": "Latin America & Caribbean", "CO": "Latin America & Caribbean",
    "CL": "Latin America & Caribbean", "PE": "Latin America & Caribbean",
    "VE": "Latin America & Caribbean", "EC": "Latin America & Caribbean",
    "BO": "Latin America & Caribbean", "PY": "Latin America & Caribbean",
    "UY": "Latin America & Caribbean", "GY": "Latin America & Caribbean",
    "SR": "Latin America & Caribbean", "CR": "Latin America & Caribbean",
    "PA": "Latin America & Caribbean", "GT": "Latin America & Caribbean",
    "HN": "Latin America & Caribbean", "SV": "Latin America & Caribbean",
    "NI": "Latin America & Caribbean", "CU": "Latin America & Caribbean",
    "DO": "Latin America & Caribbean", "HT": "Latin America & Caribbean",
    "JM": "Latin America & Caribbean", "TT": "Latin America & Caribbean",
    "BB": "Latin America & Caribbean", "BS": "Latin America & Caribbean",
    "BZ": "Latin America & Caribbean",
    "PR": "Latin America & Caribbean",

    # ── Western Europe ────────────────────────────────────────────────
    "GB": "Western Europe", "DE": "Western Europe", "FR": "Western Europe",
    "IT": "Western Europe", "ES": "Western Europe", "NL": "Western Europe",
    "BE": "Western Europe", "AT": "Western Europe", "CH": "Western Europe",
    "SE": "Western Europe", "NO": "Western Europe", "DK": "Western Europe",
    "FI": "Western Europe", "IE": "Western Europe", "PT": "Western Europe",
    "GR": "Western Europe", "LU": "Western Europe", "IS": "Western Europe",
    "MT": "Western Europe", "CY": "Western Europe",

    # ── Eastern Europe & Central Asia ─────────────────────────────────
    "RU": "Eastern Europe & Central Asia", "UA": "Eastern Europe & Central Asia",
    "PL": "Eastern Europe & Central Asia", "CZ": "Eastern Europe & Central Asia",
    "SK": "Eastern Europe & Central Asia", "HU": "Eastern Europe & Central Asia",
    "RO": "Eastern Europe & Central Asia", "BG": "Eastern Europe & Central Asia",
    "RS": "Eastern Europe & Central Asia", "HR": "Eastern Europe & Central Asia",
    "SI": "Eastern Europe & Central Asia", "BA": "Eastern Europe & Central Asia",
    "ME": "Eastern Europe & Central Asia", "MK": "Eastern Europe & Central Asia",
    "AL": "Eastern Europe & Central Asia", "MD": "Eastern Europe & Central Asia",
    "BY": "Eastern Europe & Central Asia", "EE": "Eastern Europe & Central Asia",
    "LV": "Eastern Europe & Central Asia", "LT": "Eastern Europe & Central Asia",
    "GE": "Eastern Europe & Central Asia", "AM": "Eastern Europe & Central Asia",
    "AZ": "Eastern Europe & Central Asia",
    "KZ": "Eastern Europe & Central Asia", "UZ": "Eastern Europe & Central Asia",
    "TM": "Eastern Europe & Central Asia", "KG": "Eastern Europe & Central Asia",
    "TJ": "Eastern Europe & Central Asia",

    # ── North America ─────────────────────────────────────────────────
    "US": "North America", "CA": "North America",

    # ── Oceania ───────────────────────────────────────────────────────
    "AU": "Oceania", "NZ": "Oceania",
    "FJ": "Oceania", "PG": "Oceania", "WS": "Oceania",
    "TO": "Oceania", "VU": "Oceania", "SB": "Oceania",
}

# =====================================================================
# GLOBAL NORTH / SOUTH MAPPING
# =====================================================================
# Based on Brandt Line with modern updates.
# "Ambiguous" for countries that straddle the divide (e.g., Turkey, Israel, Singapore).

GLOBAL_NORTH_REGIONS = {"North America", "Western Europe", "Oceania"}
GLOBAL_SOUTH_REGIONS = {"Sub-Saharan Africa", "Latin America & Caribbean", "South Asia", "Southeast Asia"}
# East Asia, MENA, Eastern Europe are mixed

NORTH_SOUTH_OVERRIDES: dict[str, str] = {
    # Global North countries in otherwise mixed regions
    "JP": "Global North", "KR": "Global North",
    "IL": "Global North",
    "CZ": "Global North", "PL": "Global North", "EE": "Global North",
    "LT": "Global North", "LV": "Global North", "SI": "Global North",
    "HR": "Global North", "HU": "Global North", "SK": "Global North",

    # Global South — MENA countries (except Gulf petrostates which are Ambiguous)
    "IR": "Global South", "IQ": "Global South", "JO": "Global South",
    "LB": "Global South", "SY": "Global South", "PS": "Global South",
    "YE": "Global South", "EG": "Global South", "LY": "Global South",
    "TN": "Global South", "DZ": "Global South", "MA": "Global South",

    # Ambiguous
    "CN": "Ambiguous",   # 2nd largest economy but developing nation self-designation
    "SG": "Ambiguous",   # High income but geographically Global South
    "TR": "Ambiguous",   # Straddles Europe/Asia
    "RU": "Ambiguous",   # Post-Soviet, high HDI but sanctioned
    "SA": "Ambiguous",   # High income but Global South by geography
    "AE": "Ambiguous",   # Same as Saudi Arabia
    "QA": "Ambiguous",   # Same
    "TW": "Ambiguous",   # High income, East Asian
}


def get_region(country_code: str) -> str:
    """Get macro-region for an ISO 3166-1 alpha-2 country code."""
    return COUNTRY_TO_REGION.get(country_code.upper(), "Unknown")


def get_north_south(country_code: str) -> str:
    """Get Global North/South classification for a country code."""
    cc = country_code.upper()

    # Check overrides first
    if cc in NORTH_SOUTH_OVERRIDES:
        return NORTH_SOUTH_OVERRIDES[cc]

    region = get_region(cc)
    if region in GLOBAL_NORTH_REGIONS:
        return "Global North"
    elif region in GLOBAL_SOUTH_REGIONS:
        return "Global South"
    else:
        return "Ambiguous"


# =====================================================================
# COUNTRY NAME → ISO CODE RESOLUTION
# =====================================================================

COUNTRY_NAME_TO_CODE: dict[str, str] = {
    # Full names (lowercase)
    "united states": "US", "usa": "US", "u.s.": "US", "u.s.a.": "US",
    "united states of america": "US", "america": "US",
    "united kingdom": "GB", "uk": "GB", "england": "GB", "scotland": "GB",
    "great britain": "GB", "britain": "GB",
    "china": "CN", "people's republic of china": "CN", "prc": "CN",
    "japan": "JP", "south korea": "KR", "korea": "KR", "republic of korea": "KR",
    "taiwan": "TW", "hong kong": "HK",
    "india": "IN", "pakistan": "PK", "bangladesh": "BD", "sri lanka": "LK",
    "nepal": "NP",
    "singapore": "SG", "indonesia": "ID", "malaysia": "MY", "thailand": "TH",
    "vietnam": "VN", "philippines": "PH", "myanmar": "MM", "cambodia": "KH",
    "germany": "DE", "france": "FR", "italy": "IT", "spain": "ES",
    "netherlands": "NL", "belgium": "BE", "austria": "AT", "switzerland": "CH",
    "sweden": "SE", "norway": "NO", "denmark": "DK", "finland": "FI",
    "ireland": "IE", "portugal": "PT", "greece": "GR", "luxembourg": "LU",
    "iceland": "IS", "cyprus": "CY", "malta": "MT",
    "russia": "RU", "russian federation": "RU",
    "ukraine": "UA", "poland": "PL", "czech republic": "CZ", "czechia": "CZ",
    "slovakia": "SK", "hungary": "HU", "romania": "RO", "bulgaria": "BG",
    "serbia": "RS", "croatia": "HR", "slovenia": "SI",
    "estonia": "EE", "latvia": "LV", "lithuania": "LT",
    "georgia": "GE", "armenia": "AM", "azerbaijan": "AZ",
    "kazakhstan": "KZ", "uzbekistan": "UZ",
    "brazil": "BR", "mexico": "MX", "argentina": "AR", "colombia": "CO",
    "chile": "CL", "peru": "PE", "ecuador": "EC", "bolivia": "BO",
    "uruguay": "UY", "venezuela": "VE", "costa rica": "CR", "panama": "PA",
    "cuba": "CU", "puerto rico": "PR",
    "canada": "CA", "australia": "AU", "new zealand": "NZ",
    "aotearoa": "NZ",
    "saudi arabia": "SA", "united arab emirates": "AE", "uae": "AE",
    "qatar": "QA", "kuwait": "KW", "bahrain": "BH", "oman": "OM",
    "iran": "IR", "iraq": "IQ", "jordan": "JO", "lebanon": "LB",
    "syria": "SY", "palestine": "PS", "israel": "IL", "turkey": "TR",
    "egypt": "EG", "tunisia": "TN", "algeria": "DZ", "morocco": "MA",
    "libya": "LY",
    "nigeria": "NG", "south africa": "ZA", "kenya": "KE", "ethiopia": "ET",
    "ghana": "GH", "tanzania": "TZ", "uganda": "UG", "rwanda": "RW",
    "senegal": "SN", "cameroon": "CM", "zimbabwe": "ZW", "zambia": "ZM",
    "botswana": "BW", "namibia": "NA", "mozambique": "MZ", "malawi": "MW",
    "madagascar": "MG", "mauritius": "MU",
    "fiji": "FJ", "papua new guinea": "PG",
    "afghanistan": "AF",
}


def resolve_country_code(name: str) -> str | None:
    """Resolve a country name or alias to ISO 3166-1 alpha-2 code."""
    if not name:
        return None

    # Already a 2-letter code?
    if len(name) == 2 and name.upper() in COUNTRY_TO_REGION:
        return name.upper()

    # Lookup by name
    key = name.strip().lower()
    return COUNTRY_NAME_TO_CODE.get(key)


# =====================================================================
# WELL-KNOWN INSTITUTION → COUNTRY MAPPING
# =====================================================================
# For fast resolution without API calls. Covers major AI/CS research institutions.

INSTITUTION_TO_COUNTRY: dict[str, str] = {
    # US
    "stanford": "US", "mit": "US", "harvard": "US", "berkeley": "US",
    "cmu": "US", "carnegie mellon": "US", "princeton": "US", "yale": "US",
    "columbia": "US", "cornell": "US", "nyu": "US", "upenn": "US",
    "uw": "US", "umass": "US", "usc": "US", "ucla": "US",
    "caltech": "US", "georgia tech": "US", "gatech": "US",
    "google": "US", "meta": "US", "openai": "US", "anthropic": "US",
    "microsoft": "US", "apple": "US", "amazon": "US", "ibm": "US",
    "nvidia": "US", "allen ai": "US", "ai2": "US",
    "johns hopkins": "US", "jhu": "US", "michigan": "US",
    "uc davis": "US", "uc san diego": "US", "ucsd": "US",
    "illinois": "US", "uiuc": "US", "maryland": "US",
    "washington": "US", "ohio state": "US", "penn state": "US",
    "virginia": "US", "duke": "US", "rice": "US", "brown": "US",

    # UK
    "oxford": "GB", "cambridge": "GB", "ucl": "GB", "imperial": "GB",
    "edinburgh": "GB", "kcl": "GB", "king's college london": "GB",
    "alan turing": "GB", "deepmind": "GB", "manchester": "GB",
    "bristol": "GB", "warwick": "GB", "southampton": "GB",
    "sheffield": "GB", "leeds": "GB", "nottingham": "GB",

    # Canada
    "toronto": "CA", "waterloo": "CA", "mcgill": "CA", "montreal": "CA",
    "ubc": "CA", "alberta": "CA", "mila": "CA", "vector institute": "CA",
    "cohere": "CA",

    # Germany
    "max planck": "DE", "tu munich": "DE", "tum": "DE",
    "tu darmstadt": "DE", "tu hamburg": "DE", "rwth aachen": "DE",
    "heidelberg": "DE", "dfki": "DE", "fraunhofer": "DE",

    # France
    "inria": "FR", "cnrs": "FR", "ecole polytechnique": "FR",
    "sorbonne": "FR", "ens": "FR", "hugging face": "FR",

    # China
    "tsinghua": "CN", "peking": "CN", "fudan": "CN", "shanghai jiao tong": "CN",
    "zhejiang": "CN", "nanjing": "CN", "ustc": "CN", "cas": "CN",
    "chinese academy": "CN", "baidu": "CN", "alibaba": "CN",
    "tencent": "CN", "bytedance": "CN", "huawei": "CN",
    "harbin": "CN", "wuhan": "CN", "beihang": "CN",

    # Japan
    "tokyo": "JP", "kyoto": "JP", "osaka": "JP", "tohoku": "JP",
    "riken": "JP", "nii": "JP", "naist": "JP", "aist": "JP",

    # South Korea
    "kaist": "KR", "snu": "KR", "seoul national": "KR",
    "yonsei": "KR", "korea university": "KR", "postech": "KR",
    "samsung": "KR", "naver": "KR", "kakao": "KR",

    # India
    "iit": "IN", "iisc": "IN", "iiit": "IN", "jnu": "IN",
    "tata": "IN", "infosys": "IN", "wipro": "IN",

    # Singapore
    "nus": "SG", "ntu": "SG", "nanyang": "SG", "sutd": "SG",
    "a*star": "SG",

    # Australia
    "melbourne": "AU", "sydney": "AU", "monash": "AU",
    "anu": "AU", "unsw": "AU", "queensland": "AU",
    "csiro": "AU",

    # New Zealand
    "auckland": "NZ", "otago": "NZ", "victoria university of wellington": "NZ",

    # Netherlands
    "amsterdam": "NL", "delft": "NL", "leiden": "NL",
    "eindhoven": "NL", "utrecht": "NL",

    # Switzerland
    "eth zurich": "CH", "ethz": "CH", "epfl": "CH",

    # Israel
    "technion": "IL", "hebrew university": "IL", "weizmann": "IL",
    "tel aviv": "IL", "ben-gurion": "IL", "bar-ilan": "IL",

    # South Africa
    "cape town": "ZA", "witwatersrand": "ZA", "wits": "ZA",
    "stellenbosch": "ZA", "pretoria": "ZA",

    # Brazil
    "usp": "BR", "unicamp": "BR", "ufrj": "BR",

    # International / multi-country
    "who": "CH", "unesco": "FR", "world bank": "US",
    "oecd": "FR",
}


def resolve_institution_country(text: str) -> str | None:
    """
    Try to resolve a country code from institution mentions in text.

    Checks text against known institution keywords. Returns the first match.
    """
    if not text:
        return None

    text_lower = text.lower()
    for inst, cc in INSTITUTION_TO_COUNTRY.items():
        if inst in text_lower:
            return cc
    return None


# =====================================================================
# WEIRD SCORING COMPONENTS
# =====================================================================

# High-WEIRD countries (top quintile on all 5 dimensions)
HIGH_WEIRD_COUNTRIES = {
    "US", "GB", "CA", "AU", "NZ",  # Anglosphere
    "DE", "NL", "SE", "NO", "DK", "FI", "CH", "AT",  # Northern/Central Europe
}

# Moderate-WEIRD (3-4 of 5 dimensions)
MODERATE_WEIRD_COUNTRIES = {
    "FR", "IT", "ES", "PT", "GR", "IE", "BE", "LU",  # Southern/Western Europe
    "JP", "KR", "IL", "SG", "TW", "HK",  # High-income non-Western
    "CZ", "PL", "EE", "SI", "HR",  # EU accession states
}

# Low-WEIRD (1-2 dimensions, typically only Industrialized + Rich)
LOW_WEIRD_COUNTRIES = {
    "CN", "SA", "AE", "QA", "KW", "BH",  # High/upper-middle income but non-Western
    "RU", "TR", "MX", "BR", "AR", "CL",  # Upper-middle income
    "MY", "TH",  # Upper-middle income SE Asia
}

# Non-WEIRD remainder — Global South, low-income, non-democratic, or non-Western
# (not listed = non-WEIRD by default)


def get_weird_tier(country_code: str) -> str:
    """Classify a country into a WEIRD tier."""
    cc = country_code.upper()
    if cc in HIGH_WEIRD_COUNTRIES:
        return "High-WEIRD"
    elif cc in MODERATE_WEIRD_COUNTRIES:
        return "Moderate-WEIRD"
    elif cc in LOW_WEIRD_COUNTRIES:
        return "Low-WEIRD"
    else:
        return "Non-WEIRD"


def weird_country_score(country_code: str) -> int:
    """Return a 0-100 WEIRD score for a country (based on tier)."""
    tier = get_weird_tier(country_code)
    return {"High-WEIRD": 90, "Moderate-WEIRD": 60, "Low-WEIRD": 30, "Non-WEIRD": 10}[tier]


if __name__ == "__main__":
    # Quick self-test
    tests = [
        ("US", "North America", "Global North", "High-WEIRD"),
        ("CN", "East Asia", "Ambiguous", "Low-WEIRD"),
        ("NG", "Sub-Saharan Africa", "Global South", "Non-WEIRD"),
        ("JP", "East Asia", "Global North", "Moderate-WEIRD"),
        ("BR", "Latin America & Caribbean", "Global South", "Low-WEIRD"),
        ("IN", "South Asia", "Global South", "Non-WEIRD"),
        ("DE", "Western Europe", "Global North", "High-WEIRD"),
        ("IR", "MENA", "Global South", "Non-WEIRD"),
    ]
    print("Self-test:")
    for cc, exp_region, exp_ns, exp_weird in tests:
        region = get_region(cc)
        ns = get_north_south(cc)
        weird = get_weird_tier(cc)
        status = "✓" if (region == exp_region and ns == exp_ns and weird == exp_weird) else "✗"
        print(f"  {status} {cc}: region={region}, N/S={ns}, WEIRD={weird}")
