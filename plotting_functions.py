"""
Created on 2019.08.13
:author: Felix Soubelet

A collection of functions that turn useful for
plotting insight on my use of equipment and
settings in my practice of photography.
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def plot_shots_per_camera(subplot, data):
    """Barplot of the number of shots per camera, on the provided subplot."""
    sns.countplot(
        y="Camera",
        hue="Brand",
        palette="pastel",
        data=data,
        ax=subplot,
        order=data.Camera.value_counts().index,
    )
    subplot.set_title("Number of Shots per Camera Model", fontsize=25)
    subplot.tick_params(axis="both", which="major", labelsize=13)
    subplot.set_xlabel("Number of Shots", fontsize=20)
    subplot.set_ylabel("Camera Model", fontsize=20)
    subplot.legend(loc="lower right", fontsize=18, title_fontsize=22)


def plot_shots_per_fnumber(subplot, data):
    """Barplot of the number of shots per F number, on the provided subplot."""
    sns.countplot(x="F_Number", palette="pastel", data=data, ax=subplot)
    subplot.set_title("Distribution of Apertures", fontsize=25)
    subplot.tick_params(axis="both", which="major", labelsize=13)
    subplot.tick_params(axis="x", rotation=70)
    subplot.set_xlabel("F Number", fontsize=20)
    subplot.set_ylabel("Number of Shots", fontsize=20)


def plot_shots_per_focal_length(subplot, data):
    """Barplot of the number of shots per focal length (FF equivalent), on the provided subplot."""
    sns.countplot(
        x="Focal_Range",
        hue="Lens",
        palette="pastel",
        data=data,
        ax=subplot,
        order=data.Focal_Range.value_counts().index,
    )
    subplot.set_title("Number of shots per Focal Length (FF equivalent)", fontsize=25)
    subplot.tick_params(axis="both", which="major", labelsize=13)
    subplot.set_xlabel("Focal Length", fontsize=20)
    subplot.set_ylabel("Number of Shots", fontsize=20)
    subplot.legend(loc="upper center", fontsize=15, title_fontsize=21)


def plot_shots_per_lens(subplot, data):
    """Barplot of the number of shots per lens used, on the provided subplot."""
    sns.countplot(
        y="Lens",
        hue="Brand",
        palette="pastel",
        data=data,
        ax=subplot,
        order=data.Lens.value_counts().index,
    )
    subplot.set_title("Number of Shots per Lens Model", fontsize=25)
    subplot.tick_params(axis="both", which="major", labelsize=13)
    subplot.set_xlabel("Number of Shots", fontsize=20)
    subplot.set_ylabel("Lens Model", fontsize=20)
    subplot.legend(loc="lower right", fontsize=18, title_fontsize=25)


def plot_shots_per_shutter_speed(subplot, data):
    """Barplot of the number of shots per shutter speed, on the provided subplot."""
    sns.countplot(
        x="Shutter_Speed", data=data, ax=subplot, order=data.Shutter_Speed.value_counts().index
    )
    subplot.set_title("Number of Shots per Shutter Speed", fontsize=25)
    subplot.tick_params(axis="x", which="major", rotation=70)
    subplot.set_xlabel("Shutter Speed", fontsize=20)
    subplot.set_ylabel("Number of Shots", fontsize=20)


def plot_shots_per_year(subplot, data):
    """Barplot of the number of shots taken each year, on the provided subplot."""
    sns.countplot(
        y="Year",
        hue="Brand",
        palette="pastel",
        data=data,
        ax=subplot,
        order=data.Year.value_counts().index,
    )
    subplot.set_title("Number of Shots per Year", fontsize=25)
    subplot.tick_params(axis="both", which="major", labelsize=13)
    subplot.set_xlabel("Number of Shots", fontsize=20)
    subplot.set_ylabel("Year", fontsize=20)
    subplot.legend(loc="lower right", fontsize=18, title_fontsize=22)


def plot_insight(data):
    """Combines all the different plots into subplots on the same figure."""
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(20, 22))
    fig.suptitle("Your Photography Habits", fontsize=35)
    plot_shots_per_year(axes[0, 0], data)
    plot_shots_per_camera(axes[0, 1], data)
    plot_shots_per_lens(axes[1, 0], data)
    plot_shots_per_focal_length(axes[1, 1], data)
    plot_shots_per_fnumber(axes[2, 0], data)
    plot_shots_per_shutter_speed(axes[2, 1], data)
    fig.tight_layout()
    fig.subplots_adjust(top=0.93)
    plt.savefig("insight.jpg", format="jpg", dpi=300)
