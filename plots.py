import matplotlib.pyplot as plt

plt.style.use("default")


def plot_daily_cases(df):
    fig, ax = plt.subplots(figsize=(11, 4))

    ax.bar(
        df.index,
        df["daily_cases"],
        color="#1f77b4",
        alpha=0.6,
        label="Daily Cases"
    )

    ax.plot(
        df.index,
        df["cases_7day_avg"],
        color="#ff7f0e",
        linewidth=2.5,
        label="7-Day Avg"
    )

    ax.set_title("Daily New Cases & 7-Day Average", fontsize=13, weight="bold")
    ax.set_ylabel("Cases")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4)

    return fig


def plot_deaths(df):
    fig, ax = plt.subplots(figsize=(5, 3))

    ax.bar(
        df.index,
        df["daily_deaths"],
        color="#d62728",
        alpha=0.75
    )

    ax.set_title("Daily Deaths", fontsize=12, weight="bold")
    ax.set_ylabel("Deaths")
    ax.grid(True, linestyle="--", alpha=0.4)

    return fig


def plot_recovery(df):
    fig, ax = plt.subplots(figsize=(5, 3))

    ax.fill_between(
        df.index,
        df["daily_recovered"],
        color="#2ca02c",
        alpha=0.5
    )

    ax.plot(
        df.index,
        df["daily_recovered"],
        color="#2ca02c",
        linewidth=2
    )

    ax.set_title("Daily Recoveries", fontsize=12, weight="bold")
    ax.set_ylabel("Recovered")
    ax.grid(True, linestyle="--", alpha=0.4)

    return fig


def plot_growth_rate(df):
    fig, ax = plt.subplots(figsize=(11, 3))

    ax.plot(
        df.index,
        df["growth_rate"],
        color="#9467bd",
        linewidth=2.5
    )

    ax.fill_between(
        df.index,
        df["growth_rate"],
        color="#9467bd",
        alpha=0.25
    )

    ax.set_title("Growth Rate Trend (%)", fontsize=12, weight="bold")
    ax.set_ylabel("Growth %")
    ax.grid(True, linestyle="--", alpha=0.4)

    return fig
