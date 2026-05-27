"""
Timestamp forensics on Satoshi's public communications.

Inputs (pulled by src/pull_corpus.py into /tmp/ni-site/):
  - forum_posts.json: 543 BitcoinTalk + P2PFoundation posts attributed to Satoshi
  - emails.json: 39 bitcoin-list / cryptography-list emails sent by Satoshi

All timestamps are ISO-8601 UTC in the source JSON.

Outputs:
  - results/hour-of-day-summary.json: hour-bin counts per candidate timezone
  - results/hour-of-day-by-timezone.png: side-by-side histograms
  - results/holiday-gap-summary.json: activity on each holiday compared to baseline
  - results/holiday-gap-by-tz.png: bar chart of activity-vs-baseline per holiday

Reproducibility:
  python src/pull_corpus.py     # populates /tmp/ni-site/
  python src/time_forensics.py  # writes results/*

What this test can and cannot do:
  - "Resident in UK" vs "resident in US": discriminable (sleep window + holiday gaps).
  - "Resident in EST" vs "resident in PST": only weakly discriminable. The two
    interpretations differ in *when* Satoshi went to sleep but produce the same
    UTC quiet window. We report both interpretations and let the reader judge.
  - The morning-onset gradient (rate of activity ramp at wake-up) is the most
    informative single signal for EST vs PST.
"""

import json
import os
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
NI_DATA = Path("/tmp/ni-site/server/data")
RESULTS = ROOT / "results"

TZS = {
    "UTC (GMT)": 0,
    "BST (UK summer)": 1,
    "EST (US Eastern)": -5,
    "EDT (US East summer)": -4,
    "PST (US Pacific)": -8,
    "PDT (US Pac summer)": -7,
}

# US federal holidays observed in BOTH EST and PST (cannot discriminate EST/PST).
# Source: 5 U.S.C. § 6103 — the canonical federal-holiday statute.
# We list 2008-2010 dates explicitly; "_obs" suffix marks shifted observance.
US_FEDERAL_HOLIDAYS = {
    "2008-01-01": "New Year",
    "2008-01-21": "MLK Day",
    "2008-02-18": "Presidents Day",
    "2008-05-26": "Memorial Day",
    "2008-07-04": "Independence Day",
    "2008-09-01": "Labor Day",
    "2008-10-13": "Columbus Day",
    "2008-11-11": "Veterans Day",
    "2008-11-27": "Thanksgiving",
    "2008-12-25": "Christmas",
    "2009-01-01": "New Year",
    "2009-01-19": "MLK Day",
    "2009-02-16": "Presidents Day",
    "2009-05-25": "Memorial Day",  # also UK Spring Bank Holiday — coincidence
    "2009-07-03": "Independence Day (obs)",  # Jul 4 was Saturday
    "2009-09-07": "Labor Day",
    "2009-10-12": "Columbus Day",
    "2009-11-11": "Veterans Day",
    "2009-11-26": "Thanksgiving",
    "2009-12-25": "Christmas",
    "2010-01-01": "New Year",
    "2010-01-18": "MLK Day",
    "2010-02-15": "Presidents Day",
    "2010-05-31": "Memorial Day",
    "2010-07-05": "Independence Day (obs)",  # Jul 4 was Sunday
    "2010-09-06": "Labor Day",
    "2010-10-11": "Columbus Day",
    "2010-11-11": "Veterans Day",
    "2010-11-25": "Thanksgiving",
    "2010-12-24": "Christmas Eve (de facto)",  # Christmas was Saturday
}

# UK bank holidays NOT observed in the US (the discriminators).
# Source: gov.uk bank-holidays archive. We list 2008-2010 dates explicitly.
UK_ONLY_HOLIDAYS = {
    "2008-03-21": "Good Friday",
    "2008-03-24": "Easter Monday",
    "2008-05-05": "Early May Bank Holiday",
    "2008-05-26": "Spring Bank Holiday",  # coincides with US Memorial Day
    "2008-08-25": "Summer Bank Holiday",
    "2008-12-26": "Boxing Day",
    "2009-04-10": "Good Friday",
    "2009-04-13": "Easter Monday",
    "2009-05-04": "Early May Bank Holiday",
    "2009-05-25": "Spring Bank Holiday",  # coincides with US Memorial Day
    "2009-08-31": "Summer Bank Holiday",
    "2009-12-28": "Boxing Day (obs)",  # Dec 26 was Saturday
    "2010-04-02": "Good Friday",
    "2010-04-05": "Easter Monday",
    "2010-05-03": "Early May Bank Holiday",
    "2010-05-31": "Spring Bank Holiday",  # coincides with US Memorial Day
    "2010-08-30": "Summer Bank Holiday",
    "2010-12-27": "Boxing Day (obs)",  # Dec 26 was Sunday
}


def load_timestamps():
    """Return a list of UTC datetimes for all 543+39 Satoshi events."""
    out = []
    with open(NI_DATA / "forum_posts.json") as f:
        posts = json.load(f)
    for p in posts:
        if p.get("satoshi_id") is None:
            continue
        out.append(datetime.fromisoformat(p["date"].replace("Z", "+00:00")))
    with open(NI_DATA / "emails.json") as f:
        emails = json.load(f)
    for e in emails:
        if e.get("sent_from") != "Satoshi Nakamoto":
            continue
        out.append(datetime.fromisoformat(e["date"].replace("Z", "+00:00")))
    return sorted(out)


def load_commit_timestamps(repo_path):
    """Return list of UTC datetimes for unique Satoshi commits in bitcoin/bitcoin.

    Satoshi appears under two attributions:
      - s_nakamoto@<SVN-UUID>: SVN-imported commits (the SourceForge SVN era)
      - satoshin@gmx.com: post-2010-Aug-28 commits after GitHub migration

    Some commits exist twice in --all (master + a release branch); we dedupe by
    commit hash. Timestamps are author dates (when Satoshi made the commit).
    """
    import subprocess
    if not os.path.isdir(repo_path):
        return []
    log = subprocess.check_output(
        ["git", "-C", repo_path, "log", "--all", "--no-merges",
         "--pretty=%H|%ae|%ad", "--date=iso-strict"],
        text=True, errors="replace",
    )
    seen_hashes = set()
    out = []
    for line in log.splitlines():
        parts = line.split("|")
        if len(parts) != 3:
            continue
        h, email, dt_str = parts
        if h in seen_hashes:
            continue
        is_satoshi = (email.startswith("s_nakamoto@")
                      or email == "satoshin@gmx.com")
        if not is_satoshi:
            continue
        seen_hashes.add(h)
        out.append(datetime.fromisoformat(dt_str))
    return sorted(out)


def hour_of_day_counts(events):
    """Return dict[tz_label] -> dict[hour] -> count."""
    out = {}
    for tz_label, offset in TZS.items():
        bins = defaultdict(int)
        for ev in events:
            local = ev + timedelta(hours=offset)
            bins[local.hour] += 1
        out[tz_label] = dict(bins)
    return out


def daily_counts_in_tz(events, offset):
    """Return dict[date_str] -> count, where date is the LOCAL date in the tz."""
    bins = defaultdict(int)
    for ev in events:
        local = ev + timedelta(hours=offset)
        bins[local.date().isoformat()] += 1
    return dict(bins)


def date_range(start_iso, end_iso):
    """All YYYY-MM-DD between start and end inclusive."""
    start = date.fromisoformat(start_iso)
    end = date.fromisoformat(end_iso)
    n = (end - start).days
    return [(start + timedelta(days=i)).isoformat() for i in range(n + 1)]


def holiday_window_activity(daily, holidays, window_days=0):
    """For each holiday, return activity on that day and on a +/- window around it.

    window_days=0 → just the holiday itself.
    """
    out = {}
    for hday, name in holidays.items():
        h_date = date.fromisoformat(hday)
        days = [hday] if window_days == 0 else [
            (h_date + timedelta(days=delta)).isoformat()
            for delta in range(-window_days, window_days + 1)
        ]
        counts = [daily.get(d, 0) for d in days]
        out[f"{hday} [{name}]"] = {
            "days_in_window": days,
            "counts": counts,
            "total": sum(counts),
        }
    return out


def baseline_daily_mean(daily, start_iso, end_iso, exclude=set()):
    """Mean daily count over [start, end], excluding listed dates and zero-activity days."""
    days = date_range(start_iso, end_iso)
    vals = [daily.get(d, 0) for d in days if d not in exclude]
    nonzero = [v for v in vals if v > 0]
    return {
        "n_days_total": len(days),
        "n_days_nonzero": len(nonzero),
        "mean_all_days": sum(vals) / len(days),
        "mean_active_days_only": sum(nonzero) / max(len(nonzero), 1),
    }


def activity_window_bounds(events):
    """Activity range — Satoshi's first and last public timestamps."""
    return events[0].isoformat(), events[-1].isoformat()


def render_holiday_table(label, daily, baseline, holidays, window, neighbor_radius=7):
    """Build a list of rows describing activity around each holiday.

    Local baseline: mean of the ±neighbor_radius window EXCLUDING the holiday-window
    itself. Controls for the bias that Satoshi's overall activity was rising over
    2009-2010 and so a global-baseline comparison would wrongly conflate "holiday
    silence" with "early-corpus sparseness".
    """
    rows = []
    for hday, name in holidays.items():
        h_date = date.fromisoformat(hday)
        # Skip holidays outside Satoshi's active window
        if h_date < date(2008, 10, 31) or h_date > date(2010, 12, 13):
            continue
        window_days_list = [
            (h_date + timedelta(days=delta)).isoformat()
            for delta in range(-window, window + 1)
        ]
        window_counts = [daily.get(d, 0) for d in window_days_list]

        # Local neighbor baseline: ±neighbor_radius days minus the window itself
        neighbor_days = []
        for delta in range(-neighbor_radius, neighbor_radius + 1):
            d = (h_date + timedelta(days=delta)).isoformat()
            if d not in window_days_list:
                neighbor_days.append(d)
        neighbor_counts = [daily.get(d, 0) for d in neighbor_days]
        local_baseline = sum(neighbor_counts) / max(len(neighbor_counts), 1)

        rows.append({
            "tz_label": label,
            "holiday_date": hday,
            "holiday_name": name,
            "window_days": window_days_list,
            "window_counts": window_counts,
            "window_total": sum(window_counts),
            "window_size_days": len(window_days_list),
            "window_mean_per_day": sum(window_counts) / len(window_days_list),
            "neighbor_days_n": len(neighbor_days),
            "neighbor_mean_per_day": local_baseline,
            "vs_global_baseline_ratio": (sum(window_counts) / len(window_days_list)) / max(baseline["mean_all_days"], 1e-9),
            "vs_local_neighbor_ratio": (sum(window_counts) / len(window_days_list)) / max(local_baseline, 1e-9),
            "neighbor_baseline_is_meaningful": local_baseline >= 0.5,  # need data to compare to
        })
    return rows


def day_of_week_counts(events, offset):
    """Return counts of events by local day-of-week. 0=Mon, 6=Sun."""
    bins = defaultdict(int)
    for ev in events:
        local = ev + timedelta(hours=offset)
        bins[local.weekday()] += 1
    return {i: bins.get(i, 0) for i in range(7)}


def morning_gradient(hour_counts):
    """For each tz, return the activity ramp 5am-noon to gauge wake-up time.
    A sharp ramp at hour N suggests wake-up at N-1; a flat ramp suggests no wake-up signal."""
    out = {}
    for tz_label, bins in hour_counts.items():
        ramp = [(h, bins.get(h, 0)) for h in range(4, 13)]
        out[tz_label] = ramp
    return out


def evening_tail(hour_counts):
    """Activity 9pm-3am — late-night working signal."""
    out = {}
    for tz_label, bins in hour_counts.items():
        tail = [(h, bins.get(h % 24, 0)) for h in [21, 22, 23, 24, 25, 26, 27]]
        # Convert 24-27 to 0-3
        tail = [(h if h < 24 else h - 24, c) for h, c in tail]
        out[tz_label] = tail
    return out


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    events = load_timestamps()
    print(f"Loaded {len(events)} Satoshi forum-post + email timestamps.")
    print(f"First: {events[0]}, last: {events[-1]}")

    commits = load_commit_timestamps("/tmp/bitcoin-shallow")
    print(f"Loaded {len(commits)} Satoshi commit timestamps from bitcoin/bitcoin git log.")
    if commits:
        print(f"First commit: {commits[0]}, last commit: {commits[-1]}")

    # --- Hour-of-day (forum+email corpus) ---
    h_counts = hour_of_day_counts(events)
    hod_path = RESULTS / "hour-of-day-summary.json"
    hod_payload = {
        "n_events": len(events),
        "first_event_utc": events[0].isoformat(),
        "last_event_utc": events[-1].isoformat(),
        "tz_offsets": TZS,
        "hour_counts": h_counts,
        "morning_gradient_5am_to_noon": morning_gradient(h_counts),
        "evening_tail_9pm_to_3am": evening_tail(h_counts),
    }
    hod_path.write_text(json.dumps(hod_payload, indent=2))
    print(f"Wrote {hod_path}")

    # --- Hour-of-day (commit corpus, independent replication) ---
    if commits:
        c_counts = hour_of_day_counts(commits)
        commit_path = RESULTS / "commit-hour-of-day-summary.json"
        commit_payload = {
            "n_commits": len(commits),
            "first_commit_utc": commits[0].isoformat(),
            "last_commit_utc": commits[-1].isoformat(),
            "tz_offsets": TZS,
            "hour_counts": c_counts,
            "morning_gradient_5am_to_noon": morning_gradient(c_counts),
            "evening_tail_9pm_to_3am": evening_tail(c_counts),
            "source": "bitcoin/bitcoin git log, authors s_nakamoto@<SVN-UUID> and satoshin@gmx.com, deduped by commit hash",
        }
        commit_path.write_text(json.dumps(commit_payload, indent=2))
        print(f"Wrote {commit_path}")

    # --- Holiday-gap (per-timezone reading) ---
    holiday_out = {
        "n_events": len(events),
        "activity_window_utc": list(activity_window_bounds(events)),
        "windows_days": 1,  # ±1 day around each holiday
        "neighbor_baseline_radius_days": 7,
        "us_federal_holidays": {},
        "uk_only_holidays": {},
        "summary_per_tz": {},
    }
    for tz_label, offset in TZS.items():
        daily = daily_counts_in_tz(events, offset)
        baseline = baseline_daily_mean(
            daily, "2008-11-01", "2010-12-13",
            exclude=set(US_FEDERAL_HOLIDAYS.keys()) | set(UK_ONLY_HOLIDAYS.keys()),
        )
        us_rows = render_holiday_table(tz_label, daily, baseline, US_FEDERAL_HOLIDAYS, window=1, neighbor_radius=7)
        uk_rows = render_holiday_table(tz_label, daily, baseline, UK_ONLY_HOLIDAYS, window=1, neighbor_radius=7)
        # Filter to rows where neighbor baseline is meaningful (≥0.5/day around the holiday)
        # — controls for "holiday is in low-activity early-corpus phase" bias
        us_meaningful = [r for r in us_rows if r["neighbor_baseline_is_meaningful"]]
        uk_meaningful = [r for r in uk_rows if r["neighbor_baseline_is_meaningful"]]
        us_local_ratios = [r["vs_local_neighbor_ratio"] for r in us_meaningful]
        uk_local_ratios = [r["vs_local_neighbor_ratio"] for r in uk_meaningful]
        # Day-of-week
        dow = day_of_week_counts(events, offset)
        holiday_out["summary_per_tz"][tz_label] = {
            "baseline": baseline,
            "day_of_week_local": dow,
            "n_us_holidays_in_window": len(us_rows),
            "n_us_holidays_with_meaningful_neighbor_baseline": len(us_meaningful),
            "n_uk_only_holidays_in_window": len(uk_rows),
            "n_uk_only_holidays_with_meaningful_neighbor_baseline": len(uk_meaningful),
            "mean_us_local_neighbor_ratio": (sum(us_local_ratios) / len(us_local_ratios)) if us_local_ratios else None,
            "mean_uk_local_neighbor_ratio": (sum(uk_local_ratios) / len(uk_local_ratios)) if uk_local_ratios else None,
            "us_holiday_rows": us_rows,
            "uk_only_holiday_rows": uk_rows,
        }
    hol_path = RESULTS / "holiday-gap-summary.json"
    hol_path.write_text(json.dumps(holiday_out, indent=2))
    print(f"Wrote {hol_path}")

    # --- Concise console report ---
    print("\n=== Sleep-window arithmetic (00:00-06:00 local) ===")
    for tz_label, bins in h_counts.items():
        sleep = sum(bins.get(h, 0) for h in range(0, 6))
        total = sum(bins.values())
        print(f"  {tz_label:25s}: {sleep:3d} / {total} ({100*sleep/total:5.1f}%)")

    print("\n=== Morning gradient 5am-noon local (wake-up tell) ===")
    for tz_label, ramp in hod_payload["morning_gradient_5am_to_noon"].items():
        bar = " ".join(f"{h}:{c}" for h, c in ramp)
        print(f"  {tz_label:25s}: {bar}")

    print("\n=== Holiday-vs-local-neighbor ratios (lower = bigger silence) ===")
    print("Filtered to holidays with meaningful ±7-day neighbor baseline (≥0.5 events/day)")
    print(f"{'Timezone':25s} {'US fed (n)':>14s} {'UK only (n)':>14s}")
    for tz_label, summary in holiday_out["summary_per_tz"].items():
        us_str = f"{summary['mean_us_local_neighbor_ratio']:.3f} (n={summary['n_us_holidays_with_meaningful_neighbor_baseline']})" if summary['mean_us_local_neighbor_ratio'] is not None else f"n/a (n=0)"
        uk_str = f"{summary['mean_uk_local_neighbor_ratio']:.3f} (n={summary['n_uk_only_holidays_with_meaningful_neighbor_baseline']})" if summary['mean_uk_local_neighbor_ratio'] is not None else f"n/a (n=0)"
        print(f"  {tz_label:23s} {us_str:>14s} {uk_str:>14s}")

    print("\n=== Day-of-week distribution (UTC offset applied) ===")
    print(f"{'Timezone':25s} {'Mon':>5s} {'Tue':>5s} {'Wed':>5s} {'Thu':>5s} {'Fri':>5s} {'Sat':>5s} {'Sun':>5s}")
    for tz_label, summary in holiday_out["summary_per_tz"].items():
        dow = summary["day_of_week_local"]
        row = " ".join(f"{dow.get(i, 0):>5d}" for i in range(7))
        print(f"  {tz_label:23s} {row}")

    if commits:
        print("\n=== Commit-corpus replication: sleep-window arithmetic ===")
        c_counts = hour_of_day_counts(commits)
        for tz_label, bins in c_counts.items():
            sleep = sum(bins.get(h, 0) for h in range(0, 6))
            total = sum(bins.values())
            print(f"  {tz_label:25s}: {sleep:3d} / {total} ({100*sleep/total:5.1f}%)")
        print("\n=== Commit-corpus morning gradient 5am-noon ===")
        for tz_label, ramp in morning_gradient(c_counts).items():
            bar = " ".join(f"{h}:{c}" for h, c in ramp)
            print(f"  {tz_label:25s}: {bar}")

    print("\nDone. PNGs to be regenerated via the existing plotting code path.")


if __name__ == "__main__":
    main()
