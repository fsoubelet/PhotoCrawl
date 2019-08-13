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


def plot_shots_per_camera(data):
    """Creates a barplot of the number of shots for each camera."""
    plt.figure(figsize=(20, 15))
    plt.title("Number of Shots per Camera Model", fontsize=23)
    sns.countplot(
        y="Camera",
        hue="Brand",
        palette="pastel",
        data=data,
        order=data["Camera"].value_counts().index,
    )
    plt.tick_params(axis="both", which="major", labelsize=13)
    plt.xlabel("Number of Shots", fontsize="xx-large")
    plt.ylabel("Camera Model", fontsize="xx-large")
    plt.legend(loc="lower right", fontsize=18, title_fontsize=25)
    plt.savefig("shots_per_camera.png", format="png", dpi=300)


def plot_shots_per_fnumber(data):
    """Barplot of the number of shots for each F number."""
    plt.figure(figsize=(15, 10))
    plt.title("Distribution of Apertures", fontsize=23)
    sns.countplot(x="F_Number", palette="pastel", data=data)
    plt.tick_params(axis="both", which="major", labelsize=13)
    plt.xlabel("F Number", fontsize="xx-large")
    plt.ylabel("Number of Shots", fontsize="xx-large")
    plt.savefig("shots_per_aperture.png", format="png", dpi=300)


def plot_shots_per_focal_length(data):
    """Creates a barplot of the number of shots for each focal length in 35mm FF equivalent."""
    plt.figure(figsize=(15, 10))
    plt.title("Number of shots per Focal Length (FF equivalent)", fontsize=23)
    sns.countplot(
        x="Focal_Range",
        hue="Lens",
        palette="tab20",
        data=data,
        order=data["Focal_Range"].value_counts().index,
    )
    plt.tick_params(axis="both", which="major", labelsize=13)
    plt.xlabel("Focal Length", fontsize="xx-large")
    plt.ylabel("Number of Shots", fontsize="xx-large")
    plt.legend(loc="upper center", fontsize=18, title_fontsize=25)
    plt.savefig("shots_per_focal.png", format="png", dpi=300)


def plot_shots_per_lens(data):
    """Creates a barplot of the number of shots for each lens used."""
    plt.figure(figsize=(25, 13))
    plt.title("Number of Shots per Lens Model", fontsize=23)
    sns.countplot(
        y="Lens", hue="Brand", palette="pastel", data=data, order=data["Lens"].value_counts().index
    )
    plt.tick_params(axis="both", which="major", labelsize=13)
    plt.xlabel("Number of Shots", fontsize="xx-large")
    plt.ylabel("Lens Model", fontsize="xx-large")
    plt.legend(loc="lower right", fontsize=18, title_fontsize=25)
    plt.savefig("shots_per_lens.png", format="png", dpi=300)


def plot_shots_per_shutter_speed(data):
    """Creates a plot of the number of shots for each shutter speed."""
    plt.figure(figsize=(15, 10))
    plt.title("Number of Shots per Shutter Speed", fontsize=23)
    sns.countplot(x="Shutter_Speed", data=data, order=data.Shutter_Speed.value_counts().index)
    plt.xticks(rotation=70)
    plt.tick_params(axis="y", which="major", labelsize=13)
    plt.xlabel("Shutter Speed", fontsize="xx-large")
    plt.ylabel("Number of Shots", fontsize="xx-large")
    plt.savefig("shots_per_shutter_speed.png", format="png", dpi=300)


def plot_shots_per_year(data):
    """Creates a barplot of the number of shots taken each year."""
    plt.figure(figsize=(20, 15))
    plt.title("Number of Shots per Year", fontsize=23)
    sns.countplot(
        y="Year", hue="Brand", palette="pastel", data=data, order=data["Year"].value_counts().index
    )
    plt.tick_params(axis="both", which="major", labelsize=13)
    plt.xlabel("Number of Shots", fontsize="xx-large")
    plt.ylabel("Year", fontsize="xx-large")
    plt.legend(loc="lower right", fontsize=18, title_fontsize=25)
    plt.savefig("shots_per_year.png", format="png", dpi=300)
