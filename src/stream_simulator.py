import json, time, argparse
import pandas as pd
from ucimlrepo import fetch_ucirepo

def rows():
    ds = fetch_ucirepo(id=374)
    df = pd.concat([ds.data.features.copy(), ds.data.targets.copy()], axis=1)
    df["date"] = pd.to_datetime(df["date"])
    for _, r in df.tail(1000).iterrows():
        yield {
            "date": str(r["date"]),
            "lights": float(r["lights"]),
            "T1": float(r["T1"]),
            "RH_1": float(r["RH_1"]),
            "T2": float(r["T2"]),
            "RH_2": float(r["RH_2"]),
            "T3": float(r["T3"]),
            "RH_3": float(r["RH_3"]),
            "T4": float(r["T4"]),
            "RH_4": float(r["RH_4"]),
            "T5": float(r["T5"]),
            "RH_5": float(r["RH_5"]),
            "T6": float(r["T6"]),
            "RH_6": float(r["RH_6"]),
            "T7": float(r["T7"]),
            "RH_7": float(r["RH_7"]),
            "T8": float(r["T8"]),
            "RH_8": float(r["RH_8"]),
            "T9": float(r["T9"]),
            "RH_9": float(r["RH_9"]),
            "T_out": float(r["T_out"]),
            "Press_mm_hg": float(r["Press_mm_hg"]),
            "RH_out": float(r["RH_out"]),
            "Windspeed": float(r["Windspeed"]),
            "Visibility": float(r["Visibility"]),
            "Tdewpoint": float(r["Tdewpoint"]),
            "Appliances": float(r["Appliances"])
        }

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--seconds", type=float, default=1.0)
    args = p.parse_args()
    for item in rows():
        print(json.dumps(item), flush=True)
        time.sleep(args.seconds)
